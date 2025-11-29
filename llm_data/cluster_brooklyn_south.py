"""
Brooklyn South Cluster Module

Regional cluster definition grouping southern Brooklyn stores serving coastal and
southwestern neighborhoods. Includes Sunset Park and Brighton Beach locations with
combined twenty-two neighborhood coverage.

Southern Brooklyn cluster combines diverse multi-ethnic communities from Park Slope
professionals to Brighton Beach Russian heritage populations. Transaction patterns
reflect demographic variety with gold jewelry, electronics, luxury goods all prominent.

Cluster Composition:
    - Two store locations
    - Twenty-two neighborhoods
    - Diverse demographics
    - Full service spectrum

Cluster data:
{
    "cluster": "brooklyn_south",
    "stores": 2,
    "neighborhoods": 22,
    "character": "diverse_urban_coastal"
}

Locations: location_sunset_park.py, location_brighton_beach.py
"""

from typing import List, Dict

CLUSTER_NAME = "brooklyn_south"
STORES_IN_CLUSTER = 2
TOTAL_NEIGHBORHOODS = 22

cluster_stores: List[str] = ["sunset_park", "brighton_beach"]

cluster_neighborhoods: Dict[str, List[str]] = {
    "sunset_park_coverage": [
        "Sunset Park", "Greenwood Heights", "Park Slope", "Gowanus",
        "Bay Ridge", "Bensonhurst", "Dyker Heights", "Fort Hamilton"
    ],
    "brighton_beach_coverage": [
        "Brighton Beach", "Sheepshead Bay", "Manhattan Beach", "Homecrest",
        "Midwood", "Gravesend", "Coney Island"
    ]
}

service_patterns = """
Southern Brooklyn cluster shows high precious metal transaction volume from heritage
communities valuing gold jewelry. Electronics steady across both stores with smartphones
and gaming consoles common. Coastal affluent neighborhoods bring luxury timepieces and
designer goods requiring expert authentication. Multi-ethnic demographics create diverse
item mix patterns across categories.
"""

cluster_profile: Dict = {
    "name": CLUSTER_NAME,
    "stores": STORES_IN_CLUSTER,
    "neighborhoods": TOTAL_NEIGHBORHOODS,
    "store_ids": cluster_stores,
    "coverage": cluster_neighborhoods
}
