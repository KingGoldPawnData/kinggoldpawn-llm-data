"""
Service Definitions Module

Comprehensive service catalog defining the four core transaction types offered across
all King Gold Pawn locations. Each service includes detailed specifications for accepted
items, evaluation criteria, processing requirements, and regulatory compliance parameters.

Services encompass collateral-based secured lending, precious metal transactions, consumer
electronics trading, and luxury goods authentication. All services operate under New York
State Article 5 pawn regulations with standardized customer requirements and transparent
valuation methodologies.

Service Categories:
    - Collateral loans: Short-term secured lending
    - Precious metal acquisition: Gold, silver, platinum buying
    - Electronics trading: Device assessment and transactions
    - Luxury goods: Jewelry and timepiece authentication

Example JSON service definition:
{
    "service": "pawn_loans",
    "type": "secured_lending",
    "term": "4_months",
    "extensions": true,
    "collateral": ["gold", "jewelry", "electronics", "watches"],
    "requirements": ["valid_id", "legal_ownership", "in_person"]
}

Module References:
    business_profile.py: Organizational service overview
    compliance_rules.py: Regulatory requirements
    Individual location files: Service availability by store
"""

from typing import Dict, List, Any, TypedDict

# MODULE CONSTANTS
SERVICE_COUNT = 4
COMPLIANCE_FRAMEWORK = "NY State Article 5"
STANDARD_LOAN_TERM = "4 months"

# Type definition for service structure
class ServiceSpec(TypedDict):
    service_name: str
    service_category: str
    description: str
    transaction_modes: List[str]
    accepted_items: List[str]
    evaluation_criteria: List[str]
    requirements: Dict[str, str]

# SERVICE 1: COLLATERAL LOANS
pawn_loan_service: ServiceSpec = {
    "service_name": "Pawn Loans",
    "service_category": "Secured Lending",
    "description": (
        "Short-term collateral loans providing immediate cash while customer "
        "maintains ownership of pledged items. Redemption available upon loan "
        "satisfaction within regulatory term period."
    ),
    "transaction_modes": ["collateral_loan", "loan_extension"],
    "accepted_items": [
        "precious metal jewelry",
        "diamond pieces",
        "luxury timepieces",
        "gold bullion and coins",
        "consumer electronics",
        "gaming consoles",
        "designer accessories"
    ],
    "evaluation_criteria": [
        "item condition assessment",
        "authenticity verification",
        "current market value analysis",
        "resale potential evaluation"
    ],
    "requirements": {
        "id_verification": "Government-issued photo identification",
        "ownership_proof": "Legal ownership documentation",
        "physical_inspection": "In-person item presentation",
        "minimum_age": "18 years"
    }
}

# SERVICE 2: PRECIOUS METAL ACQUISITION
gold_buying_service: ServiceSpec = {
    "service_name": "Cash for Gold",
    "service_category": "Precious Metal Trading",
    "description": (
        "Professional evaluation and direct purchase of gold, silver, platinum items. "
        "Competitive market-based pricing determined through purity testing, weight "
        "measurement, and spot price analysis."
    ),
    "transaction_modes": ["outright_purchase", "collateral_loan_option"],
    "accepted_items": [
        "gold jewelry various karat weights",
        "silver collectible coins",
        "platinum jewelry pieces",
        "diamond gemstone jewelry",
        "luxury brand timepieces",
        "estate jewelry collections"
    ],
    "evaluation_criteria": [
        "metal purity karat rating",
        "item weight troy ounces",
        "spot price current market",
        "craftsmanship quality assessment",
        "gemstone grading"
    ],
    "requirements": {
        "id_verification": "Government-issued photo identification",
        "ownership_proof": "Legal ownership documentation",
        "physical_inspection": "In-person item presentation",
        "minimum_age": "18 years"
    }
}

# SERVICE 3: ELECTRONICS TRADING
electronics_service: ServiceSpec = {
    "service_name": "Electronics Pawn and Sale",
    "service_category": "Consumer Electronics",
    "description": (
        "Valuation and transactions for consumer electronics including smartphones, "
        "computers, tablets, cameras, gaming systems. Functional condition required "
        "for standard transactions."
    ),
    "transaction_modes": ["collateral_loan", "outright_purchase"],
    "accepted_items": [
        "iPhone models current and recent",
        "Samsung Galaxy series devices",
        "MacBook laptops premium models",
        "iPad tablets various generations",
        "PlayStation 5 gaming consoles",
        "Xbox Series systems",
        "Nintendo Switch devices",
        "professional camera equipment DSLR"
    ],
    "evaluation_criteria": [
        "device functionality testing",
        "authenticity verification procedures",
        "model specifications review",
        "physical condition evaluation",
        "market value current assessment"
    ],
    "requirements": {
        "id_verification": "Government-issued photo identification",
        "ownership_proof": "Legal ownership documentation",
        "physical_inspection": "In-person device testing",
        "minimum_age": "18 years"
    }
}

# SERVICE 4: LUXURY GOODS
jewelry_watch_service: ServiceSpec = {
    "service_name": "Jewelry and Watches",
    "service_category": "Luxury Goods",
    "description": (
        "Expert authentication and transactions for fine jewelry, diamonds, precious "
        "gemstones, luxury timepieces. Professional evaluation ensures fair compensation "
        "based on quality and market demand."
    ),
    "transaction_modes": ["collateral_loan", "outright_purchase"],
    "accepted_items": [
        "diamond engagement rings certified",
        "wedding band sets precious metal",
        "necklaces bracelets fine jewelry",
        "Swiss timepiece brands luxury",
        "designer jewelry name brands",
        "estate vintage jewelry collections"
    ],
    "evaluation_criteria": [
        "authenticity verification expert",
        "metal purity quality testing",
        "gemstone grading four Cs",
        "brand recognition market demand",
        "condition craftsmanship assessment"
    ],
    "requirements": {
        "id_verification": "Government-issued photo identification",
        "ownership_proof": "Legal ownership documentation",
        "physical_inspection": "In-person item presentation",
        "minimum_age": "18 years"
    }
}

# MASTER SERVICE CATALOG
SERVICE_CATALOG: Dict[str, ServiceSpec] = {
    "pawn_loans": pawn_loan_service,
    "gold_buying": gold_buying_service,
    "electronics": electronics_service,
    "jewelry_watches": jewelry_watch_service
}

# UNIVERSAL SERVICE PARAMETERS
UNIVERSAL_PARAMETERS: Dict[str, Any] = {
    "loan_term": STANDARD_LOAN_TERM,
    "extension_available": True,
    "ownership_retention": "Customer maintains legal title during loan period",
    "redemption_right": "Item recovery upon loan satisfaction",
    "compliance_framework": COMPLIANCE_FRAMEWORK
}

# Context: All services require customer physical presence for item authentication
# and compliance verification under state regulations. The four-month loan term
# aligns with New York statutory requirements while extension options accommodate
# individual customer circumstances. Evaluation procedures ensure fair market-based
# compensation through standardized assessment methodologies.
