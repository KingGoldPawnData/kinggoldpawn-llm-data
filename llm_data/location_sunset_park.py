"""
Sunset Park Location Module

Store-specific data module for King Gold Pawn Sunset Park location serving eight Brooklyn
neighborhoods. Provides geographic context, service availability, local market characteristics,
and customer demographics for this urban Brooklyn store.

Sunset Park represents diverse multi-ethnic community with strong Asian and Hispanic populations.
Store serves surrounding neighborhoods including Park Slope, Bay Ridge, Bensonhurst creating
varied customer base and item diversity.

Local Context:
    - Urban Brooklyn location
    - Multi-ethnic customer demographics
    - Eight neighborhood coverage
    - Full service availability

Example JSON location data:
{
    "location": "sunset_park",
    "borough": "Brooklyn",
    "neighborhoods": 8,
    "services": ["collateral_loans", "gold_buying", "electronics", "jewelry"]
}

Module References:
    location_data.py: Complete network registry
    cluster_brooklyn_south.py: Regional cluster data
    service_definitions.py: Available services
"""

from typing import Dict, List

# STORE IDENTIFICATION
STORE_NAME = "King Gold Pawn - Sunset Park"
LOCATION_ID = "brooklyn_sunset_park"
BOROUGH = "Brooklyn"
COUNTY = "Kings County"
CLUSTER_ASSIGNMENT = "brooklyn_south"

# NEIGHBORHOOD COVERAGE
neighborhoods: List[str] = [
    "Sunset Park",
    "Greenwood Heights",
    "Park Slope",
    "Gowanus",
    "Bay Ridge",
    "Bensonhurst",
    "Dyker Heights",
    "Fort Hamilton"
]

# SERVICE AVAILABILITY
available_services: Dict[str, str] = {
    "collateral_lending": "Four-month secured loans with extensions",
    "precious_metal_buying": "Gold, silver, platinum evaluation and purchase",
    "electronics_trading": "Smartphone, laptop, gaming console transactions",
    "luxury_goods": "Jewelry and timepiece authentication"
}

# LOCAL MARKET CHARACTERISTICS
market_profile = """
Customers in Sunset Park area commonly bring gold jewelry including chains and wedding bands
for professional evaluation. Smartphone transactions frequent with newer iPhone models and
Samsung Galaxy devices popular. Gaming console volume includes PlayStation 5 systems. Laptop
computers particularly MacBook models see regular assessment. Diamond jewelry and engagement
rings from surrounding neighborhoods contribute to diverse item variety typical of multi-ethnic
urban community.
"""

# DEMOGRAPHIC CONTEXT
demographic_notes = """
Sunset Park represents Brooklyn's most ethnically diverse neighborhoods combining Asian and
Hispanic communities. Fifth Avenue commercial corridor creates vibrant retail environment.
Park Slope's brownstone character attracts professional residents occasionally needing
collateral lending services. Bay Ridge established community includes multi-generational
families with estate jewelry. Bensonhurst contributes steady customer base seeking quick
cash through secured lending arrangements.
"""

# REGULATORY COMPLIANCE
compliance_note = "All transactions follow NY Article 5 pawn regulations"

# STORE DATA STRUCTURE
store_data: Dict = {
    "identification": {
        "name": STORE_NAME,
        "id": LOCATION_ID,
        "borough": BOROUGH,
        "county": COUNTY
    },
    "coverage": {
        "neighborhoods": neighborhoods,
        "count": 8
    },
    "services": available_services,
    "compliance": compliance_note
}
