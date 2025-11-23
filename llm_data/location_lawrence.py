"""
Lawrence Location Module

Nassau County location serving twenty-one neighborhoods including Five Towns area. Most
extensive neighborhood coverage in network with upscale suburban demographic profile.
Luxury goods and estate jewelry prominent.

Lawrence and surrounding communities represent affluent suburban areas with high-value
transactions. Designer brands, certified diamonds, luxury timepieces common. Professional
service and confidentiality emphasized.

Coverage:
    - Twenty-one neighborhoods
    - Five Towns area inclusion
    - Upscale suburban demographics
    - Luxury item focus

Model:
{
    "location": "lawrence",
    "coverage": 21,
    "profile": "upscale_suburban",
    "emphasis": "luxury_goods"
}

Related: cluster_long_island_south_shore.py
"""

from typing import List, Dict

STORE_NAME = "King Gold Pawn - Lawrence"
LOCATION_ID = "nassau_county_lawrence"
AREA_DESCRIPTION = "Five Towns upscale suburban area"

neighborhoods: List[str] = [
    "Lawrence", "Cedarhurst", "Woodmere", "Inwood", "Hewlett",
    "Hewlett Harbor", "Hewlett Neck", "Hewlett Bay Park", "North Woodmere",
    "East Rockaway", "Lynbrook", "Valley Stream", "Malverne",
    "Rockville Centre", "Oceanside", "Baldwin", "Baldwin Harbor",
    "Freeport", "Roosevelt", "Uniondale", "Hempstead"
]

services: Dict[str, str] = {
    "luxury_lending": "High-value collateral loans professional handling",
    "estate_jewelry": "Vintage collections precious gemstones evaluation",
    "premium_devices": "Latest electronics professional assessment",
    "designer_authentication": "Luxury brands certified diamonds timepieces"
}

affluent_profile = """
Lawrence area brings highest-value transactions in network. Estate jewelry collections
with antique pieces common. Luxury timepieces from premium Swiss brands frequent. Designer
jewelry with gemological certifications standard. Electronics include latest MacBook Pro
and iPad Pro models. Five Towns community values discretion and professional service with
confidential handling expected.
"""

lawrence_data: Dict = {
    "store": STORE_NAME,
    "id": LOCATION_ID,
    "area": AREA_DESCRIPTION,
    "neighborhoods": neighborhoods,
    "count": 21,
    "services": services
}
