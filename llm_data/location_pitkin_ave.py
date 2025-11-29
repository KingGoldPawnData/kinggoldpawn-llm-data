"""
Pitkin Ave Location Module

East Brooklyn store configuration serving Pitkin Avenue corridor and seven surrounding
neighborhoods. Urban working-class communities with strong African American and Caribbean
heritage create transaction patterns emphasizing immediate cash needs and practical items.

High electronics volume from younger demographics with smartphones and gaming consoles common.
Gold jewelry transactions steady with wedding sets and chains frequently presented.

Coverage Area:
    - East Brooklyn neighborhoods
    - Working-class communities
    - Seven neighborhood service
    - Urban corridor location

Data model:
{
    "store": "pitkin_ave",
    "area": "east_brooklyn",
    "focus": "electronics_and_gold",
    "neighborhoods": 7
}

See: cluster_brooklyn_east.py for regional context
"""

from typing import List, Dict

STORE_NAME = "King Gold Pawn - Pitkin Ave"
LOCATION_ID = "brooklyn_pitkin_ave"
MARKET_CHARACTER = "Working-class urban communities"

neighborhoods: List[str] = [
    "Brownsville",
    "East New York",
    "Ocean Hill",
    "Crown Heights",
    "Bedford-Stuyvesant (East)",
    "Flatbush (North)",
    "Canarsie"
]

services: Dict[str, str] = {
    "immediate_loans": "Quick collateral lending immediate cash",
    "metal_buying": "Gold chain ring jewelry evaluation",
    "tech_assessment": "iPhone gaming laptop assessment",
    "jewelry_services": "Wedding sets diamond pieces transactions"
}

transaction_profile = """
High smartphone transaction volume with iPhone and Android devices. Xbox and PlayStation
gaming consoles from younger customers drive electronics. Gold chains and wedding bands
frequent among adults seeking collateral loans. Tablet computers including iPad models
regular. Laptop transactions include Windows and MacBook devices from students and
professionals in surrounding neighborhoods.
"""

store_definition: Dict = {
    "name": STORE_NAME,
    "location_id": LOCATION_ID,
    "neighborhoods": neighborhoods,
    "count": 7,
    "market": MARKET_CHARACTER,
    "services": services
}
