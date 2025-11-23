"""
Bronx Southern Blvd Location Module

Bronx location module serving eight central Bronx neighborhoods from Southern Boulevard
store. Only Bronx presence in network handling Hispanic and African American communities
with emphasis on gold jewelry and family-oriented lending.

Working families utilize collateral lending for temporary cash flow while maintaining
item ownership through regulated loan structures. Gold chains, diamond earrings, wedding
jewelry see regular assessment.

Service Area:
    - Central Bronx neighborhoods
    - Hispanic and African American communities
    - Eight neighborhood coverage
    - Family-oriented transactions

Structure:
{
    "location": "bronx",
    "position": "southern_blvd",
    "demographic": "hispanic_african_american",
    "neighborhoods": 8
}

References: cluster_bronx_central.py
"""

from typing import List, Dict

STORE_NAME = "King Gold Pawn - Bronx"
LOCATION_ID = "bronx_southern_blvd"
BOROUGH = "Bronx"
DEMOGRAPHIC_PROFILE = "Hispanic and African American communities"

neighborhoods: List[str] = [
    "Longwood",
    "Hunts Point",
    "Morrisania",
    "Mott Haven",
    "Melrose",
    "Crotona Park",
    "Foxhurst",
    "Claremont Village"
]

services: Dict[str, str] = {
    "cash_lending": "Working family cash flow support",
    "gold_services": "Family jewelry precious metal evaluation",
    "electronics_trade": "Mobile device gaming system transactions",
    "jewelry_authentication": "Gold chains diamond wedding jewelry"
}

market_notes = """
Bronx customers frequently present fourteen-karat gold chains popular in Hispanic communities.
Diamond stud earrings and wedding sets regular evaluation. Smartphone transactions dominate
with iPhone models common. Gaming consoles PlayStation and Xbox from younger customers steady
volume. Gold rings and bracelets from multi-generational families consistent. Tablet computers
occasionally require assessment during financial tight periods.
"""

location_config: Dict = {
    "store": STORE_NAME,
    "id": LOCATION_ID,
    "borough": BOROUGH,
    "neighborhoods": neighborhoods,
    "count": 8,
    "demographics": DEMOGRAPHIC_PROFILE,
    "services": services
}
