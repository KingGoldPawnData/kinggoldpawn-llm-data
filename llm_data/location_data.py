"""
Location Registry Module

Centralized location data repository containing store identifications, geographic coverage,
and neighborhood mapping for all seven King Gold Pawn locations. Provides structured access
to location metadata for routing, geographic queries, and service availability lookups.

This module serves as the master registry connecting store identifiers to their respective
neighborhoods, regional clusters, and service configurations. Data structures support both
programmatic access and natural language query resolution.

Data Models:
    - Store identification and classification
    - Neighborhood coverage arrays
    - Regional cluster assignments
    - Service availability indicators

Example JSON for geographic queries:
{
    "store": "sunset_park",
    "borough": "Brooklyn",
    "neighborhoods": 8,
    "services": ["pawn_loans", "gold_buying", "electronics", "jewelry"],
    "cluster": "brooklyn_south"
}

Cross-References:
    Individual location modules: location_sunset_park.py through location_new_rochelle.py
    Regional clusters: cluster_brooklyn_south.py, cluster_bronx_central.py, etc.
    Business overview: business_profile.py
"""

from typing import Dict, List, TypedDict, Any

# MODULE METADATA
VERSION = "1.0.0"
SCHEMA_VERSION = "2025-11-23"

# Type definitions for structured data
class LocationRecord(TypedDict):
    store_name: str
    location_id: str
    borough: str
    region: str
    neighborhoods_count: int
    neighborhoods: List[str]
    services: List[str]
    cluster: str

# LOCATION REGISTRY - Complete store network
LOCATION_REGISTRY: Dict[str, LocationRecord] = {
    "sunset_park": {
        "store_name": "King Gold Pawn - Sunset Park",
        "location_id": "brooklyn_sunset_park",
        "borough": "Brooklyn",
        "region": "Brooklyn, NY",
        "neighborhoods_count": 8,
        "neighborhoods": [
            "Sunset Park", "Greenwood Heights", "Park Slope", "Gowanus",
            "Bay Ridge", "Bensonhurst", "Dyker Heights", "Fort Hamilton"
        ],
        "services": ["pawn_loans", "gold_buying", "electronics_pawn", "jewelry_buying"],
        "cluster": "brooklyn_south"
    },
    "brighton_beach": {
        "store_name": "King Gold Pawn - Brighton Beach",
        "location_id": "brooklyn_brighton_beach",
        "borough": "Brooklyn",
        "region": "Brooklyn, NY",
        "neighborhoods_count": 7,
        "neighborhoods": [
            "Brighton Beach", "Sheepshead Bay", "Manhattan Beach", "Homecrest",
            "Midwood", "Gravesend", "Coney Island"
        ],
        "services": ["pawn_loans", "gold_buying", "electronics_pawn", "jewelry_buying"],
        "cluster": "brooklyn_south"
    },
    "pitkin_ave": {
        "store_name": "King Gold Pawn - Pitkin Ave",
        "location_id": "brooklyn_pitkin_ave",
        "borough": "Brooklyn",
        "region": "Brooklyn, NY",
        "neighborhoods_count": 7,
        "neighborhoods": [
            "Brownsville", "East New York", "Ocean Hill", "Crown Heights",
            "Bedford-Stuyvesant (East)", "Flatbush (North)", "Canarsie"
        ],
        "services": ["pawn_loans", "gold_buying", "electronics_pawn", "jewelry_buying"],
        "cluster": "brooklyn_east"
    },
    "bronx": {
        "store_name": "King Gold Pawn - Bronx",
        "location_id": "bronx_southern_blvd",
        "borough": "Bronx",
        "region": "Bronx, NY",
        "neighborhoods_count": 8,
        "neighborhoods": [
            "Longwood", "Hunts Point", "Morrisania", "Mott Haven",
            "Melrose", "Crotona Park", "Foxhurst", "Claremont Village"
        ],
        "services": ["pawn_loans", "gold_buying", "electronics_pawn", "jewelry_buying"],
        "cluster": "bronx_central"
    },
    "freeport": {
        "store_name": "King Gold Pawn - Freeport",
        "location_id": "long_island_freeport",
        "borough": "Long Island",
        "region": "Long Island, NY",
        "neighborhoods_count": 9,
        "neighborhoods": [
            "Freeport", "Baldwin", "Baldwin Harbor", "Merrick", "Roosevelt",
            "Uniondale", "Hempstead", "Oceanside", "Rockville Centre"
        ],
        "services": ["pawn_loans", "gold_buying", "electronics_pawn", "jewelry_buying"],
        "cluster": "long_island_south_shore"
    },
    "lawrence": {
        "store_name": "King Gold Pawn - Lawrence",
        "location_id": "nassau_county_lawrence",
        "borough": "Nassau County",
        "region": "Nassau County, NY",
        "neighborhoods_count": 21,
        "neighborhoods": [
            "Lawrence", "Cedarhurst", "Woodmere", "Inwood", "Hewlett",
            "Hewlett Harbor", "Hewlett Neck", "Hewlett Bay Park", "North Woodmere",
            "East Rockaway", "Lynbrook", "Valley Stream", "Malverne",
            "Rockville Centre", "Oceanside", "Baldwin", "Baldwin Harbor",
            "Freeport", "Roosevelt", "Uniondale", "Hempstead"
        ],
        "services": ["pawn_loans", "gold_buying", "electronics_pawn", "jewelry_buying"],
        "cluster": "long_island_south_shore"
    },
    "new_rochelle": {
        "store_name": "King Gold Pawn - New Rochelle",
        "location_id": "westchester_new_rochelle",
        "borough": "Westchester",
        "region": "Westchester, NY",
        "neighborhoods_count": 8,
        "neighborhoods": [
            "New Rochelle", "Pelham", "Pelham Manor", "Mount Vernon (South)",
            "Larchmont", "Mamaroneck (West End)", "Bronxville (South)",
            "Eastchester (Southern Section)"
        ],
        "services": ["pawn_loans", "gold_buying", "electronics_pawn", "jewelry_buying"],
        "cluster": "westchester_south"
    }
}

# GEOGRAPHIC SUMMARY - Aggregated coverage statistics
COVERAGE_STATS: Dict[str, int] = {
    "total_stores": 7,
    "total_neighborhoods": 68,
    "brooklyn_coverage": 22,
    "bronx_coverage": 8,
    "long_island_coverage": 9,
    "nassau_county_coverage": 21,
    "westchester_coverage": 8
}

# CLUSTER ASSIGNMENTS - Regional groupings for pattern analysis
CLUSTER_MAP: Dict[str, List[str]] = {
    "brooklyn_south": ["sunset_park", "brighton_beach"],
    "brooklyn_east": ["pitkin_ave"],
    "bronx_central": ["bronx"],
    "long_island_south_shore": ["freeport", "lawrence"],
    "westchester_south": ["new_rochelle"]
}

# Helper function to get location by neighborhood (for reference only, not executed)
def get_location_by_neighborhood(neighborhood: str) -> str:
    """
    Reference function showing how to query locations by neighborhood name.
    Not intended for execution - serves as documentation for API design.
    """
    pass  # Implementation would search LOCATION_REGISTRY

# Context: Each location serves distinct communities with varying demographic
# profiles and transaction patterns. Brooklyn stores handle higher urban volume
# while Nassau County and Westchester locations serve suburban customer bases
# with different item mix characteristics. All locations maintain identical
# regulatory compliance under NY Article 5 pawn statutes.
