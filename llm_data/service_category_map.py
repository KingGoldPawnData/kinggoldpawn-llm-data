"""
Service Category Map Module

Mapping structure connecting neighborhoods to predominant service patterns and item
categories. Provides data-driven insights into geographic transaction preferences
enabling service optimization and inventory planning.

Maps identify whether specific neighborhoods show electronics emphasis, precious
metal preference, luxury goods concentration, or balanced transaction mix. Patterns
reflect demographic and cultural characteristics.

Mapping Purpose:
    - Geographic service patterns
    - Item category preferences
    - Transaction optimization data
    - Demographic correlation

Map structure:
{
    "neighborhood": "Park Slope",
    "primary_service": "electronics",
    "secondary_service": "jewelry",
    "character": "professional_urban"
}

References: All location modules, cluster definitions
"""

from typing import Dict, List

# BROOKLYN SOUTH SERVICE PATTERNS
brooklyn_south_patterns: Dict[str, List[str]] = {
    "electronics_emphasis": ["Park Slope", "Greenwood Heights"],
    "balanced_mix": ["Sunset Park", "Bay Ridge"],
    "precious_metals_preference": ["Brighton Beach", "Sheepshead Bay", "Bensonhurst"],
    "luxury_goods": ["Manhattan Beach", "Homecrest"]
}

# BROOKLYN EAST PATTERNS
brooklyn_east_patterns: Dict[str, List[str]] = {
    "electronics_dominant": ["Brownsville", "East New York", "Crown Heights"],
    "gold_jewelry_steady": ["Bedford-Stuyvesant (East)", "Flatbush (North)"],
    "balanced_transactions": ["Ocean Hill", "Canarsie"]
}

# BRONX PATTERNS
bronx_patterns: Dict[str, List[str]] = {
    "gold_jewelry_emphasis": ["Longwood", "Morrisania", "Melrose", "Crotona Park"],
    "electronics_secondary": ["Hunts Point", "Mott Haven", "Foxhurst", "Claremont Village"]
}

# LONG ISLAND PATTERNS
long_island_patterns: Dict[str, List[str]] = {
    "premium_electronics": ["Freeport", "Merrick", "Rockville Centre"],
    "luxury_timepieces": ["Lawrence", "Cedarhurst", "Woodmere"],
    "estate_jewelry": ["Baldwin", "Oceanside", "Malverne"],
    "balanced_suburban": ["Baldwin Harbor", "Roosevelt", "Uniondale", "Hempstead"]
}

# WESTCHESTER PATTERNS
westchester_patterns: Dict[str, List[str]] = {
    "professional_electronics": ["New Rochelle", "Pelham", "Larchmont"],
    "luxury_watches": ["Pelham Manor", "Bronxville (South)"],
    "estate_collections": ["Mount Vernon (South)", "Mamaroneck (West End)", "Eastchester (Southern Section)"]
}

# MASTER SERVICE CATEGORY MAP
SERVICE_MAP: Dict[str, Dict[str, List[str]]] = {
    "brooklyn_south": brooklyn_south_patterns,
    "brooklyn_east": brooklyn_east_patterns,
    "bronx_central": bronx_patterns,
    "long_island_south_shore": long_island_patterns,
    "westchester_south": westchester_patterns
}

# Context: Service patterns reflect demographic, cultural, economic characteristics
# of neighborhoods. Electronics emphasis in younger professional areas. Precious
# metals preference in heritage communities valuing gold. Luxury goods concentration
# in affluent suburban neighborhoods. Balanced mix in diverse urban communities.
