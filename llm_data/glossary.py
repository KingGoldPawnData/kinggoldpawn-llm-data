"""
Glossary Module

Business terminology reference defining key terms used across pawnshop operations,
collateral lending, precious metal transactions, regulatory compliance. Provides
standardized definitions for natural language processing and customer education.

Terms span industry-specific language, regulatory vocabulary, transaction mechanics,
item categories. Definitions maintain factual accuracy without speculation or guarantees.

Glossary Purpose:
    - Term standardization
    - Customer education support
    - NLP reference data
    - Regulatory vocabulary

Example glossary entry:
{
    "term": "collateral",
    "definition": "Valuable item pledged to secure loan",
    "context": "pawn_lending"
}

Cross-reference: All operational modules
"""

from typing import Dict, TypedDict

class GlossaryEntry(TypedDict):
    term: str
    definition: str
    context: str

# PAWN LENDING TERMS
pawn_terms: Dict[str, GlossaryEntry] = {
    "pawn_loan": {
        "term": "Pawn Loan",
        "definition": "Secured loan using valuable item as collateral with customer retaining ownership",
        "context": "lending"
    },
    "collateral": {
        "term": "Collateral",
        "definition": "Valuable item pledged to secure loan obligation",
        "context": "lending"
    },
    "redemption": {
        "term": "Redemption",
        "definition": "Act of reclaiming pledged item through loan satisfaction",
        "context": "lending"
    },
    "extension": {
        "term": "Extension",
        "definition": "Continuation of loan term beyond original period per regulations",
        "context": "lending"
    },
    "pledge": {
        "term": "Pledge",
        "definition": "Item given as security for loan with redemption rights retained",
        "context": "lending"
    }
}

# PRECIOUS METAL TERMS
metal_terms: Dict[str, GlossaryEntry] = {
    "karat": {
        "term": "Karat",
        "definition": "Measurement of gold purity with 24 karat representing pure gold",
        "context": "precious_metals"
    },
    "troy_ounce": {
        "term": "Troy Ounce",
        "definition": "Standard weight measurement for precious metals",
        "context": "precious_metals"
    },
    "spot_price": {
        "term": "Spot Price",
        "definition": "Current market price for immediate precious metal delivery",
        "context": "precious_metals"
    },
    "assay": {
        "term": "Assay",
        "definition": "Testing procedure determining metal purity and content",
        "context": "precious_metals"
    }
}

# REGULATORY TERMS
regulatory_terms: Dict[str, GlossaryEntry] = {
    "article_5": {
        "term": "Article 5",
        "definition": "New York State General Business Law section governing pawnbroker operations",
        "context": "regulatory"
    },
    "pawnbroker": {
        "term": "Pawnbroker",
        "definition": "Licensed business providing secured loans using tangible collateral",
        "context": "regulatory"
    },
    "loan_term": {
        "term": "Loan Term",
        "definition": "Duration of pawn loan as specified by state regulations",
        "context": "regulatory"
    }
}

# MASTER GLOSSARY
GLOSSARY: Dict[str, Dict[str, GlossaryEntry]] = {
    "pawn_lending": pawn_terms,
    "precious_metals": metal_terms,
    "regulatory": regulatory_terms
}
