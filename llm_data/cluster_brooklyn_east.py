"""
Brooklyn East Cluster Module

Eastern Brooklyn regional cluster containing Pitkin Avenue location serving seven
working-class neighborhoods. Urban corridor focus with emphasis on immediate cash
needs and practical item categories.

Single-store cluster handling Brownsville, East New York, Crown Heights communities
with strong African American and Caribbean heritage. Electronics volume high with
smartphones and gaming consoles from younger demographics.

Cluster Profile:
    - Single store location
    - Seven neighborhoods
    - Working-class focus
    - Electronics emphasis

Data model:
{
    "cluster": "brooklyn_east",
    "stores": 1,
    "neighborhoods": 7,
    "focus": "electronics_immediate_cash"
}

Location: location_pitkin_ave.py
"""

from typing import List, Dict

CLUSTER_NAME = "brooklyn_east"
STORES_IN_CLUSTER = 1

cluster_stores: List[str] = ["pitkin_ave"]

neighborhoods: List[str] = [
    "Brownsville", "East New York", "Ocean Hill", "Crown Heights",
    "Bedford-Stuyvesant (East)", "Flatbush (North)", "Canarsie"
]

transaction_characteristics = """
East Brooklyn cluster dominated by electronics transactions with smartphone volume
particularly high. Gaming consoles PlayStation and Xbox from younger customers steady.
Gold jewelry including chains and wedding bands regular from adult customers seeking
collateral loans. Laptop transactions both Windows and MacBook from students and
working professionals. Immediate cash need emphasis creates quick transaction preference.
"""

cluster_config: Dict = {
    "name": CLUSTER_NAME,
    "stores": STORES_IN_CLUSTER,
    "store_ids": cluster_stores,
    "neighborhoods": neighborhoods,
    "count": 7
}
