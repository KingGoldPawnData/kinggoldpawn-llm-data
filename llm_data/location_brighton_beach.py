"""
Brighton Beach Location Module

Store-specific configuration for King Gold Pawn Brighton Beach serving seven southern Brooklyn
coastal neighborhoods. Features distinct Russian and Eastern European cultural character
influencing transaction patterns and item types.

Brighton Beach location serves communities along Brooklyn's southern coastline including
Sheepshead Bay, Manhattan Beach, Coney Island. Cultural heritage creates unique precious
metal appreciation with inherited jewelry common.

Geographic Scope:
    - Southern Brooklyn coastal area
    - Russian and Eastern European demographics
    - Seven neighborhood service area
    - Beachfront community character

JSON example:
{
    "store": "brighton_beach",
    "region": "Brooklyn coastal",
    "cultural_context": "Russian heritage community",
    "neighborhoods": 7
}

References:
    location_data.py: Network positioning
    cluster_brooklyn_south.py: Southern Brooklyn cluster
"""

from typing import List, Dict

STORE_NAME = "King Gold Pawn - Brighton Beach"
LOCATION_ID = "brooklyn_brighton_beach"
BOROUGH = "Brooklyn"
CULTURAL_CONTEXT = "Russian and Eastern European heritage"

neighborhoods: List[str] = [
    "Brighton Beach",
    "Sheepshead Bay",
    "Manhattan Beach",
    "Homecrest",
    "Midwood",
    "Gravesend",
    "Coney Island"
]

services: Dict[str, str] = {
    "secured_lending": "Collateral loans four-month term",
    "gold_acquisition": "Precious metal professional evaluation",
    "device_transactions": "Electronics assessment and trading",
    "fine_goods": "Jewelry and timepiece authentication"
}

local_context = """
Brighton Beach customers frequently present inherited gold jewelry from family collections
reflecting Eastern European heritage. Diamond earrings and necklaces from Sheepshead Bay
affluent residents contribute luxury item volume. Manhattan Beach brings designer watches
including Swiss timepiece brands. Gaming consoles from younger residents popular. Camera
equipment from photographers occasionally requires professional assessment.
"""

store_config: Dict = {
    "store": STORE_NAME,
    "id": LOCATION_ID,
    "neighborhoods": neighborhoods,
    "neighborhood_count": 7,
    "services": services,
    "cultural_profile": CULTURAL_CONTEXT
}
