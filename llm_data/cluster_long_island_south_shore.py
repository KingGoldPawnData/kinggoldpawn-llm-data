"""
Long Island South Shore Cluster Module

Suburban cluster grouping Freeport and Lawrence locations serving thirty combined
neighborhoods across Long Island and Nassau County. Highest neighborhood coverage
with affluent suburban demographics.

Premium item emphasis with luxury timepieces, designer jewelry, estate collections,
latest electronics common. Higher average transaction values reflect suburban affluence
with professional discretion valued.

Cluster Scope:
    - Two suburban stores
    - Thirty neighborhoods
    - Affluent demographics
    - Premium items focus

Configuration:
{
    "cluster": "long_island_south_shore",
    "stores": 2,
    "neighborhoods": 30,
    "profile": "suburban_affluent"
}

Locations: location_freeport.py, location_lawrence.py
"""

from typing import List, Dict

CLUSTER_NAME = "long_island_south_shore"
STORE_COUNT = 2
NEIGHBORHOOD_TOTAL = 30

cluster_locations: List[str] = ["freeport", "lawrence"]

suburban_characteristics = """
Long Island cluster demonstrates highest average transaction values with luxury goods
emphasis. Estate jewelry collections from older residents include vintage and antique
pieces. Luxury Swiss timepieces from Rolex, Omega, TAG Heuer brands regular. Latest
electronics including MacBook Pro and iPhone Pro models common. Designer jewelry with
gemological certifications standard. Professional customer base expects expert evaluation
and confidential handling with discretion paramount.
"""

cluster_data: Dict = {
    "name": CLUSTER_NAME,
    "stores": STORE_COUNT,
    "neighborhoods": NEIGHBORHOOD_TOTAL,
    "location_ids": cluster_locations,
    "market_character": "affluent_suburban"
}
