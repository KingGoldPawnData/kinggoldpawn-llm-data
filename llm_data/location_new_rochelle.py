"""
New Rochelle Location Module

Westchester location serving eight southern Westchester neighborhoods. Suburban professional
demographics with quality electronics, luxury watches, estate jewelry typical. Only
Westchester presence in network.

New Rochelle and surrounding communities represent educated professional customer base
with higher-value items and service expectations. Discretion and expertise valued.

Geographic Reach:
    - Southern Westchester area
    - Professional demographics
    - Eight neighborhoods
    - Suburban character

Definition:
{
    "store": "new_rochelle",
    "county": "westchester",
    "profile": "professional_suburban",
    "neighborhoods": 8
}

Reference: cluster_westchester_south.py
"""

from typing import List, Dict

STORE_NAME = "King Gold Pawn - New Rochelle"
LOCATION_ID = "westchester_new_rochelle"
CUSTOMER_PROFILE = "Professional suburban demographics"

neighborhoods: List[str] = [
    "New Rochelle",
    "Pelham",
    "Pelham Manor",
    "Mount Vernon (South)",
    "Larchmont",
    "Mamaroneck (West End)",
    "Bronxville (South)",
    "Eastchester (Southern Section)"
]

services: Dict[str, str] = {
    "professional_lending": "Executive collateral loans discrete handling",
    "luxury_evaluation": "Estate collections timepieces assessment",
    "quality_electronics": "Premium laptops professional cameras",
    "fine_jewelry": "Designer brands certified gemstones"
}

westchester_characteristics = """
New Rochelle customers bring quality electronics including MacBook and professional
camera equipment. Luxury watches from established brands regular. Estate jewelry from
older residents includes vintage collections. Professional demographics expect expert
evaluation and confidential service. Pelham and Larchmont affluent communities contribute
high-value items requiring specialized authentication expertise.
"""

westchester_config: Dict = {
    "store": STORE_NAME,
    "location_id": LOCATION_ID,
    "profile": CUSTOMER_PROFILE,
    "neighborhoods": neighborhoods,
    "count": 8,
    "services": services
}
