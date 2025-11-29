"""
FAQ Data Module

Frequently asked question repository containing structured Q&A pairs covering pawnshop
services, loan procedures, accepted items, and regulatory compliance. Designed for natural
language processing and customer service automation while maintaining factual accuracy.

Questions span general pawnshop operations, collateral lending mechanics, precious metal
transactions, electronics assessment, jewelry evaluation, and Article 5 regulatory framework.
Answers provide factual information without speculation or guarantees.

Data Organization:
    - General inquiries
    - Loan-specific questions
    - Item acceptance and valuation
    - Regulatory and compliance
    
Example JSON FAQ structure:
{
    "category": "loan_terms",
    "question": "What is the loan duration?",
    "answer": "Four-month term with extension options per NY Article 5 regulations",
    "keywords": ["loan_term", "duration", "extension"]
}

See Also:
    service_definitions.py: Detailed service specifications
    compliance_rules.py: Regulatory framework reference
    business_profile.py: Organizational context
"""

from typing import Dict, List, TypedDict

# Type definition for FAQ entry structure
class FAQEntry(TypedDict):
    question: str
    answer: str
    category: str
    keywords: List[str]

# GENERAL PAWNSHOP QUESTIONS
general_questions: Dict[str, FAQEntry] = {
    "pawn_loan_definition": {
        "question": "What is a pawn loan?",
        "answer": (
            "A secured loan using valuable items as collateral. Customer receives immediate "
            "cash while retaining ownership. Item redemption available upon loan repayment "
            "according to New York State Article 5 pawn regulations."
        ),
        "category": "general",
        "keywords": ["collateral_loan", "secured_lending", "ownership"]
    },
    "accepted_items": {
        "question": "Which items do you accept?",
        "answer": (
            "We accept precious metals, jewelry pieces, diamonds, luxury timepieces, coins, "
            "consumer electronics including smartphones and portable computers, tablets, "
            "cameras, gaming consoles. All items must be authentic and legally owned."
        ),
        "category": "general",
        "keywords": ["items", "electronics", "jewelry", "gold"]
    },
    "requirements": {
        "question": "What documents are needed?",
        "answer": (
            "Valid government-issued photo identification required for all transactions. "
            "Items must be legally owned. All items require in-person presentation for "
            "inspection and verification."
        ),
        "category": "general",
        "keywords": ["identification", "requirements", "documentation"]
    },
    "locations": {
        "question": "How many locations exist?",
        "answer": (
            "Seven locations across New York metropolitan area: three Brooklyn stores, "
            "one Bronx location, one Long Island store, one Nassau County location, and "
            "one Westchester store serving 68 neighborhoods."
        ),
        "category": "general",
        "keywords": ["locations", "stores", "geographic_coverage"]
    }
}

# LOAN-SPECIFIC QUESTIONS
loan_questions: Dict[str, FAQEntry] = {
    "loan_duration": {
        "question": "What is the loan term length?",
        "answer": (
            "Loans follow New York State Article 5 pawn regulations with four-month term "
            "including extension options."
        ),
        "category": "loans",
        "keywords": ["term", "duration", "four_months"]
    },
    "loan_extension": {
        "question": "Can loans be extended?",
        "answer": (
            "Yes, extension options available per New York State Article 5 pawn regulations "
            "with four-month standard term."
        ),
        "category": "loans",
        "keywords": ["extension", "renewal", "flexibility"]
    },
    "item_recovery": {
        "question": "How do I reclaim my item?",
        "answer": (
            "Pawn loans provide immediate cash while maintaining ownership. Item recovery "
            "available upon loan satisfaction or extension following New York State regulations."
        ),
        "category": "loans",
        "keywords": ["redemption", "recovery", "ownership"]
    },
    "loan_process": {
        "question": "What is the loan process?",
        "answer": (
            "Present item with valid identification. Staff evaluates condition, authenticity, "
            "market value. Choose between collateral loan or outright sale."
        ),
        "category": "loans",
        "keywords": ["process", "procedure", "evaluation"]
    }
}

# ITEM AND VALUATION QUESTIONS
item_questions: Dict[str, FAQEntry] = {
    "electronics_acceptance": {
        "question": "Are electronics accepted?",
        "answer": (
            "Yes, consumer electronics including smartphones, portable computers, tablets, "
            "cameras, gaming consoles accepted. Items must be authentic and functional."
        ),
        "category": "items",
        "keywords": ["electronics", "devices", "smartphones"]
    },
    "precious_metals": {
        "question": "Do you buy gold and jewelry?",
        "answer": (
            "Yes, precious metals including gold, jewelry pieces, diamonds, luxury timepieces, "
            "coins, platinum items accepted. Professional evaluation for precious metal value."
        ),
        "category": "items",
        "keywords": ["gold", "jewelry", "precious_metals"]
    },
    "condition_requirements": {
        "question": "What condition must items be in?",
        "answer": (
            "Items must be authentic and functional unless evaluated solely for precious "
            "metal content."
        ),
        "category": "items",
        "keywords": ["condition", "functional", "authentic"]
    },
    "valuation_method": {
        "question": "How is item value determined?",
        "answer": (
            "Staff evaluates items based on condition assessment, authenticity verification, "
            "and current market value analysis."
        ),
        "category": "valuation",
        "keywords": ["valuation", "appraisal", "market_value"]
    },
    "transaction_options": {
        "question": "Can I sell instead of pawning?",
        "answer": (
            "Yes, customers may choose collateral loan or outright sale option."
        ),
        "category": "transactions",
        "keywords": ["sell", "pawn", "options"]
    }
}

# REGULATORY QUESTIONS
regulatory_questions: Dict[str, FAQEntry] = {
    "licensing_status": {
        "question": "Is the business licensed?",
        "answer": (
            "All transactions conducted per New York State Article 5 pawn regulations. "
            "Licensed and bonded pawnbroker status maintained."
        ),
        "category": "regulatory",
        "keywords": ["license", "compliance", "regulations"]
    },
    "consumer_protections": {
        "question": "What protections apply?",
        "answer": (
            "New York State Article 5 pawn regulations govern terms, conditions, consumer "
            "protections for all pawn transactions in New York State."
        ),
        "category": "regulatory",
        "keywords": ["protections", "rights", "regulations"]
    },
    "ownership_proof": {
        "question": "What ownership proof is needed?",
        "answer": (
            "Items must be legally owned by customer. Valid government-issued photo "
            "identification required for all transactions."
        ),
        "category": "requirements",
        "keywords": ["ownership", "proof", "identification"]
    },
    "in_person_requirement": {
        "question": "Is physical presence required?",
        "answer": (
            "Yes, all items require in-person presentation for inspection and verification."
        ),
        "category": "requirements",
        "keywords": ["in_person", "physical", "inspection"]
    }
}

# MASTER FAQ COLLECTION
FAQ_DATABASE: Dict[str, Dict[str, FAQEntry]] = {
    "general": general_questions,
    "loans": loan_questions,
    "items": item_questions,
    "regulatory": regulatory_questions
}

# Context: FAQ responses provide factual information derived from verified operations
# and regulatory requirements. Responses avoid speculation, clearly indicating when
# specific information unavailable. Four-month loan term and extension provisions
# comply with New York State Article 5 protecting consumer interests while enabling
# legitimate business operations.
