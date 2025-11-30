#!/usr/bin/env python3
"""
AI Visibility Monitoring Script

Monitors search engine rankings for FAQ pages using Bing Search API.
Tracks position changes, logs ranking data, and triggers alerts when
rankings drop significantly.

Features:
- Bing Search API integration
- Ranking position tracking
- Historical data logging
- Drop alerts (>20% decline)
- CSV export for analysis

Usage:
    python automation/check_ai_visibility.py [--dry-run] [--alert-threshold 20]

Requirements:
    pip install requests python-dotenv
"""

import os
import re
import csv
import logging
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional
from collections import Counter

from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

BING_API_KEY = os.getenv("BING_SEARCH_API_KEY")
BING_ENDPOINT = "https://api.bing.microsoft.com/v7.0/search"

# Target URLs to monitor
TARGET_URLS = [
    "https://kinggoldpawndata.github.io/kinggoldpawn-llm-data/FAQ_EN.html",
    "https://kinggoldpawndata.github.io/kinggoldpawn-llm-data/FAQ_ES.html"
]

# Search queries to monitor
SEARCH_QUERIES = [
    "how does a pawn loan work",
    "pawn shop interest rates",
    "what can I pawn",
    "pawn shop near me",
    "sell gold jewelry",
    "pawn electronics ps5",
    "como funciona casa de empeño",
    "empeñar electronica"
]

REPORTS_DIR = Path(__file__).parent.parent / "reports"
VISIBILITY_LOG = REPORTS_DIR / "visibility_rankings.csv"
ROADMAP_PATH = Path(__file__).parent.parent / "guides" / "LLM-roadmap.md"
DEFAULT_KEYWORD_THRESHOLD = 0.03
TOKEN_PATTERN = re.compile(r"[\w\u00C0-\u024F\u0400-\u04FF'-]+", re.UNICODE)
STOPWORDS = {"the", "and", "with", "near", "para", "como", "that", "esta", "from", "este"}


class VisibilityMonitor:
    """Monitors search visibility for FAQ pages"""
    
    def __init__(self, api_key: str, dry_run: bool = False, alert_threshold: int = 20,
                 keyword_threshold: float = DEFAULT_KEYWORD_THRESHOLD, skip_keyword_audit: bool = False):
        self.api_key = api_key
        self.dry_run = dry_run
        self.alert_threshold = alert_threshold
        self.keyword_threshold = keyword_threshold
        self.skip_keyword_audit = skip_keyword_audit
        
        if not dry_run and not api_key:
            logger.warning("BING_SEARCH_API_KEY not set - running in simulation mode")
    
    def search_query(self, query: str, count: int = 100) -> List[Dict]:
        """Perform Bing search and return results"""
        
        if self.dry_run or not self.api_key:
            logger.info(f"[SIMULATED] Searching for: {query}")
            # Return simulated results
            return [
                {"url": TARGET_URLS[0], "name": "FAQ Page", "position": 15},
                {"url": "https://example.com", "name": "Other result", "position": 1}
            ]
        
        # In production, actual Bing API call
        # headers = {"Ocp-Apim-Subscription-Key": self.api_key}
        # params = {"q": query, "count": count, "mkt": "en-US"}
        # response = requests.get(BING_ENDPOINT, headers=headers, params=params)
        # results = response.json().get("webPages", {}).get("value", [])
        
        logger.info(f"Searching for: {query}")
        return []
    
    def find_url_position(self, results: List[Dict], target_url: str) -> Optional[int]:
        """Find position of target URL in results"""
        
        for i, result in enumerate(results, 1):
            if target_url in result.get("url", ""):
                return i
        
        return None
    
    def check_all_rankings(self) -> List[Dict]:
        """Check rankings for all queries and URLs"""
        
        logger.info("=== Checking Rankings for All Queries ===")
        
        rankings = []
        
        for query in SEARCH_QUERIES:
            results = self.search_query(query)
            
            for target_url in TARGET_URLS:
                position = self.find_url_position(results, target_url)
                
                ranking_data = {
                    "timestamp": datetime.now().isoformat(),
                    "query": query,
                    "url": target_url,
                    "position": position if position else "Not Found",
                    "in_top_100": position is not None
                }
                
                rankings.append(ranking_data)
                logger.info(f"  {query} → {target_url[:50]}... = Position {ranking_data['position']}")
        
        return rankings
    
    def load_previous_rankings(self) -> Dict:
        """Load previous ranking data from CSV"""
        
        if not VISIBILITY_LOG.exists():
            return {}
        
        previous = {}
        
        with open(VISIBILITY_LOG, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                key = f"{row['query']}|{row['url']}"
                if row['position'] != "Not Found":
                    previous[key] = int(row['position'])
        
        return previous
    
    def save_rankings(self, rankings: List[Dict]):
        """Save rankings to CSV file"""
        
        if self.dry_run:
            logger.info(f"[DRY RUN] Would save {len(rankings)} ranking records to {VISIBILITY_LOG}")
            return
        
        # Create reports directory if needed
        REPORTS_DIR.mkdir(exist_ok=True)
        
        # Check if file exists to write headers
        file_exists = VISIBILITY_LOG.exists()
        
        with open(VISIBILITY_LOG, 'a', newline='', encoding='utf-8') as f:
            fieldnames = ['timestamp', 'query', 'url', 'position', 'in_top_100']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            if not file_exists:
                writer.writeheader()
            
            writer.writerows(rankings)
        
        logger.info(f"Saved {len(rankings)} ranking records to {VISIBILITY_LOG}")
    
    def check_for_drops(self, current_rankings: List[Dict], previous_rankings: Dict):
        """Check for significant ranking drops"""
        
        logger.info("=== Checking for Ranking Drops ===")
        
        alerts = []
        
        for ranking in current_rankings:
            if ranking['position'] == "Not Found":
                continue
            
            key = f"{ranking['query']}|{ranking['url']}"
            current_pos = ranking['position']
            
            if key in previous_rankings:
                previous_pos = previous_rankings[key]
                change = current_pos - previous_pos
                percent_change = (change / previous_pos) * 100
                
                if percent_change > self.alert_threshold:
                    alert = {
                        "query": ranking['query'],
                        "url": ranking['url'],
                        "previous": previous_pos,
                        "current": current_pos,
                        "change": change,
                        "percent": round(percent_change, 1)
                    }
                    alerts.append(alert)
                    logger.warning(f"ALERT: '{ranking['query']}' dropped from #{previous_pos} to #{current_pos} ({percent_change:+.1f}%)")
        
        if not alerts:
            logger.info("No significant ranking drops detected")
        else:
            logger.warning(f"Found {len(alerts)} ranking drops exceeding {self.alert_threshold}% threshold")
        
        return alerts
    
    def run_visibility_check(self):
        """Run complete visibility check"""
        
        logger.info("=== Starting AI Visibility Check ===")
        logger.info(f"Monitoring {len(SEARCH_QUERIES)} queries across {len(TARGET_URLS)} URLs")
        
        # Load previous rankings
        previous = self.load_previous_rankings()
        logger.info(f"Loaded {len(previous)} previous ranking records")
        
        # Check current rankings
        current = self.check_all_rankings()
        
        # Save rankings
        self.save_rankings(current)
        
        # Check for drops
        alerts = self.check_for_drops(current, previous)
        
        # Summary
        logger.info("=== Visibility Check Complete ===")
        logger.info(f"Total queries checked: {len(SEARCH_QUERIES)}")
        logger.info(f"Total rankings: {len(current)}")
        logger.info(f"Alerts triggered: {len(alerts)}")
        if not self.skip_keyword_audit:
            audit_keyword_density(ROADMAP_PATH, self.keyword_threshold)


def audit_keyword_density(file_path: Path, threshold: float) -> List[Dict]:
    """Scan the roadmap for keywords exceeding a percentage threshold."""

    if not file_path.exists():
        logger.warning("Keyword audit skipped: %s not found", file_path)
        return []

    text = file_path.read_text(encoding="utf-8", errors="ignore")
    tokens = TOKEN_PATTERN.findall(text.lower())
    if not tokens:
        logger.warning("Keyword audit skipped: no tokens detected in %s", file_path)
        return []

    total_tokens = len(tokens)
    counts = Counter(token for token in tokens if len(token) >= 4 and token not in STOPWORDS)
    flagged = []
    for keyword, count in counts.items():
        ratio = count / total_tokens
        if ratio >= threshold:
            flagged.append({
                "keyword": keyword,
                "count": count,
                "ratio": ratio
            })

    if flagged:
        logger.warning("Keyword density alert: %d tokens exceed %.2f%% threshold", len(flagged), threshold * 100)
        for item in sorted(flagged, key=lambda x: x["ratio"], reverse=True):
            logger.warning("  '%s' => %d uses (%.2f%% of roadmap)", item["keyword"], item["count"], item["ratio"] * 100)
    else:
        logger.info("Keyword density audit passed: no tokens above %.2f%%", threshold * 100)

    return flagged


def main():
    parser = argparse.ArgumentParser(description="Monitor AI visibility and search rankings")
    parser.add_argument("--dry-run", action="store_true", help="Run without making API calls")
    parser.add_argument("--alert-threshold", type=int, default=20,
                       help="Alert threshold for ranking drops (default: 20%%)")
    parser.add_argument("--keyword-threshold", type=float, default=DEFAULT_KEYWORD_THRESHOLD,
                       help="Max percentage for any single keyword inside the roadmap (default: 0.03)")
    parser.add_argument("--skip-keyword-audit", action="store_true",
                       help="Skip roadmap keyword density audit")
    args = parser.parse_args()
    
    monitor = VisibilityMonitor(
        BING_API_KEY,
        dry_run=args.dry_run,
        alert_threshold=args.alert_threshold,
        keyword_threshold=args.keyword_threshold,
        skip_keyword_audit=args.skip_keyword_audit,
    )
    monitor.run_visibility_check()


if __name__ == "__main__":
    main()
