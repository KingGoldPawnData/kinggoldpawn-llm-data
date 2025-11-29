#!/usr/bin/env python3
"""Upload the entire King Gold & Pawn dataset repo to Hugging Face.

Usage:
  1. Install requirements:  pip install --upgrade huggingface_hub
  2. Authenticate:          huggingface-cli login    # or set HF_TOKEN env var
  3. Run upload:
         python huggingface/push_to_hf.py \
           --repo-id <your_username>/king-gold-and-pawn-operations-bible \
           --branch main
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import List

from huggingface_hub import HfApi, upload_folder
from huggingface_hub.utils import HfHubHTTPError


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Push repo contents to Hugging Face dataset")
    parser.add_argument(
        "--repo-id",
        default=os.getenv("HF_REPO_ID", "<your_username>/king-gold-and-pawn-operations-bible"),
        help="Target Hugging Face dataset repo in the form username/dataset-name.",
    )
    parser.add_argument(
        "--branch",
        default=os.getenv("HF_BRANCH", "main"),
        help="Branch on the Hugging Face Hub (default: main).",
    )
    parser.add_argument(
        "--token",
        default=os.getenv("HF_TOKEN"),
        help="Hugging Face access token. Falls back to HF_TOKEN env var or cached CLI login.",
    )
    parser.add_argument(
        "--path",
        default=str(Path(__file__).resolve().parents[1]),
        help="Local folder to upload (defaults to repository root).",
    )
    parser.add_argument(
        "--ignore-patterns",
        nargs="*",
        default=[".git", "**/.git", "**/__pycache__", "**/.pytest_cache", "**/.mypy_cache"],
        help="Glob patterns to exclude from the upload.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    repo_root = Path(args.path).resolve()
    if not repo_root.exists():
        raise SystemExit(f"Path does not exist: {repo_root}")

    print(f"Uploading {repo_root} to https://huggingface.co/datasets/{args.repo_id} ({args.branch})")

    api = HfApi(token=args.token)
    try:
        api.create_repo(repo_id=args.repo_id, repo_type="dataset", exist_ok=True)
    except HfHubHTTPError as err:
        status = getattr(getattr(err, "response", None), "status_code", None)
        if status == 403:
            print("Warning: lacking permission to create repo; assuming it already exists and continuing...")
        else:
            raise

    upload_folder(
        repo_id=args.repo_id,
        folder_path=str(repo_root),
        repo_type="dataset",
        token=args.token,
        revision=args.branch,
        path_in_repo=".",
        ignore_patterns=args.ignore_patterns,
        commit_message="Sync King Gold & Pawn dataset",
    )

    print("Upload complete.")


if __name__ == "__main__":
    main()
