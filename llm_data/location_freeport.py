"""
Freeport Location Module

Long Island suburban store serving nine South Shore neighborhoods with middle to upper-middle
class demographics. Higher-value items including premium electronics, luxury timepieces,
designer goods more prevalent than urban locations.

Professional discretion valued with suburban customer service expectations. Latest iPhone
models, MacBook laptops, Swiss timepieces appear frequently. Higher average transaction
values reflect affluent community character.

Market Profile:
    - Suburban Long Island location
    - Affluent community demographics
    - Nine neighborhood service
    - Premium item emphasis

Configuration:
{
    "store": "freeport",
    "type": "suburban",
    "value_profile": "premium",
    "neighborhoods": 9
}

See: cluster_long_island_south_shore.py
"""

from typing import List, Dict

STORE_NAME = "King Gold Pawn - Freeport"
LOCATION_ID = "long_island_freeport"
MARKET_TYPE = "Suburban middle to upper-middle class"

neighborhoods: List[str] = [
    "Freeport",
    "Baldwin",
    "Baldwin Harbor",
    "Merrick",
    "Roosevelt",
    "Uniondale",
    "Hempstead",
    "Oceanside",
    "Rockville Centre"
]

services: Dict[str, str] = {
    "discrete_lending": "Professional suburban lending privacy emphasis",
    "precious_metals": "Estate jewelry luxury piece evaluation",
    "premium_electronics": "Latest smartphones premium laptops professional equipment",
    "luxury_authentication": "Designer brands luxury watches high-value gemstones"
}

item_profile = """
Premium electronics including MacBook Pro laptops and iPhone Pro models frequent. Luxury
timepieces from Rolex, Omega, TAG Heuer brands regular. Designer jewelry with certification
common. PlayStation 5 from suburban families provide volume. Professional camera equipment
DSLR bodies and premium lenses occasional. Estate jewelry from older residents includes
vintage pieces and precious gemstone collections.
"""

suburban_config: Dict = {
    "store": STORE_NAME,
    "location_id": LOCATION_ID,
    "neighborhoods": neighborhoods,
    "count": 9,
    "market_type": MARKET_TYPE,
    "services": services
}
