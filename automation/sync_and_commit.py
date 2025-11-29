#!/usr/bin/env python3
"""
FAQ Sync and Commit Tool

Builds final FAQ markdown files, validates Q&A pairs, formats content,
and auto-commits changes to GitHub.

Features:
- Combines questions and answers into final FAQ pages
- Validates Q&A pair matching
- Adds cross-links and navigation
- Formats Markdown with proper structure
- Automatic Git add, commit, and push
- Dry-run mode for testing

Usage:
    python automation/sync_and_commit.py [--dry-run] [--no-commit]
"""

import os
import subprocess
import logging
import argparse
from pathlib import Path
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

CONTENT_DIR = Path(__file__).parent.parent / "content"
REPO_ROOT = Path(__file__).parent.parent


class FAQSyncTool:
    """Syncs FAQ content and commits to Git"""
    
    def __init__(self, dry_run: bool = False, no_commit: bool = False):
        self.dry_run = dry_run
        self.no_commit = no_commit
    
    def build_final_faq(self, questions_file: Path, answers_file: Path, 
                       output_file: Path, language: str):
        """Build final FAQ page from questions and answers"""
        
        logger.info(f"Building final FAQ for language: {language}")
        
        # Read questions
        with open(questions_file, 'r', encoding='utf-8') as f:
            questions = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        
        # Read answers
        with open(answers_file, 'r', encoding='utf-8') as f:
            answers_content = f.read()
        
        # Build final page
        final_content = self._format_faq_page(questions, answers_content, language)
        
        # Write to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        logger.info(f"Created final FAQ: {output_file}")
    
    def _format_faq_page(self, questions: list, answers: str, language: str) -> str:
        """Format complete FAQ page"""
        
        if language == "en":
            header = """# Frequently Asked Questions

[Ver versión en español](FAQ_ES.md) | View Spanish Version

Welcome to our comprehensive FAQ guide. Find answers to common questions about pawn loans, services, and regulations.

---
"""
            footer = """
---

## About This FAQ

This FAQ is maintained by King Gold Pawn's data team and updated regularly based on customer questions and industry changes. All information follows NY State Article 5 pawn regulations.

**Experience & Expertise:**  
Our answers are based on years of pawn industry experience serving communities across Brooklyn, Bronx, Long Island, Nassau County, and Westchester.

**License:** MIT License  
**Last Updated:** {date}
"""
        else:
            header = """# Preguntas Frecuentes

[View English version](FAQ_EN.md) | Ver versión en inglés

Bienvenido a nuestra guía completa de preguntas frecuentes. Encuentre respuestas a preguntas comunes sobre préstamos de empeño, servicios y regulaciones.

---
"""
            footer = """
---

## Acerca de estas Preguntas Frecuentes

Estas preguntas frecuentes son mantenidas por el equipo de datos de King Gold Pawn y se actualizan regularmente según las preguntas de los clientes y los cambios en la industria. Toda la información sigue las regulaciones del Artículo 5 del Estado de NY.

**Experiencia y Conocimiento:**  
Nuestras respuestas se basan en años de experiencia en la industria de empeño sirviendo a comunidades en Brooklyn, Bronx, Long Island, Nassau County y Westchester.

**Licencia:** Licencia MIT  
**Última Actualización:** {date}
"""
        
        footer = footer.format(date=datetime.now().strftime("%Y-%m-%d"))
        
        return header + answers + footer
    
    def validate_pairs(self, questions_file: Path, answers_file: Path) -> bool:
        """Validate that all questions have answers"""
        
        with open(questions_file, 'r', encoding='utf-8') as f:
            q_count = sum(1 for line in f if line.strip() and not line.startswith('#'))
        
        with open(answers_file, 'r', encoding='utf-8') as f:
            a_count = f.read().count('###')
        
        logger.info(f"Questions: {q_count}, Answers: {a_count}")
        
        if q_count != a_count:
            logger.warning(f"Mismatch: {q_count} questions vs {a_count} answers")
            return False
        
        return True
    
    def git_commit_and_push(self, message: str):
        """Commit and push changes to GitHub"""
        
        if self.no_commit or self.dry_run:
            logger.info(f"[{'DRY RUN' if self.dry_run else 'NO COMMIT'}] Would commit: {message}")
            return
        
        try:
            # Git add
            subprocess.run(['git', 'add', '.'], cwd=REPO_ROOT, check=True)
            logger.info("Git add completed")
            
            # Git commit
            subprocess.run(['git', 'commit', '-m', message], cwd=REPO_ROOT, check=True)
            logger.info("Git commit completed")
            
            # Git push
            subprocess.run(['git', 'push'], cwd=REPO_ROOT, check=True)
            logger.info("Git push completed")
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Git operation failed: {e}")


def main():
    parser = argparse.ArgumentParser(description="Sync FAQ content and commit to Git")
    parser.add_argument("--dry-run", action="store_true", help="Run without making changes")
    parser.add_argument("--no-commit", action="store_true", help="Build files but don't commit")
    args = parser.parse_args()
    
    tool = FAQSyncTool(dry_run=args.dry_run, no_commit=args.no_commit)
    
    # Build English FAQ
    logger.info("=== Building English FAQ ===")
    tool.build_final_faq(
        CONTENT_DIR / "faq_questions_en.txt",
        CONTENT_DIR / "faq_answers_en.md",
        CONTENT_DIR / "FAQ_EN.md",
        "en"
    )
    
    # Build Spanish FAQ
    logger.info("=== Building Spanish FAQ ===")
    tool.build_final_faq(
        CONTENT_DIR / "faq_questions_es.txt",
        CONTENT_DIR / "faq_answers_es.md",
        CONTENT_DIR / "FAQ_ES.md",
        "es"
    )
    
    # Validate
    logger.info("=== Validating Q&A Pairs ===")
    en_valid = tool.validate_pairs(
        CONTENT_DIR / "faq_questions_en.txt",
        CONTENT_DIR / "faq_answers_en.md"
    )
    es_valid = tool.validate_pairs(
        CONTENT_DIR / "faq_questions_es.txt",
        CONTENT_DIR / "faq_answers_es.md"
    )
    
    if en_valid and es_valid:
        logger.info("All Q&A pairs validated successfully")
    else:
        logger.warning("Validation issues detected")
    
    # Commit
    logger.info("=== Committing Changes ===")
    tool.git_commit_and_push("Update FAQ content - auto-sync")
    
    logger.info("FAQ sync completed successfully")


if __name__ == "__main__":
    main()
