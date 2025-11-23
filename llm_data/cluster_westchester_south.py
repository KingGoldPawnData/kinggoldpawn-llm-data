"""
Westchester South Cluster Module

Southern Westchester cluster containing single New Rochelle store serving eight
neighborhoods. Professional suburban demographics with quality electronics, luxury
watches, estate jewelry typical.

Only Westchester network presence handling educated professional customer base
expecting expert evaluation and discrete service. Higher-value items common with
MacBook laptops, professional cameras, Swiss timepieces frequent.

Cluster Definition:
    - Single Westchester store
    - Eight neighborhoods
    - Professional demographics
    - Quality emphasis

Model:
{
    "cluster": "westchester_south",
    "stores": 1,
    "neighborhoods": 8,
    "customer_profile": "professional"
}

Location: location_new_rochelle.py
"""

from typing import List, Dict

CLUSTER_NAME = "westchester_south"
LOCATION_COUNT = 1

stores: List[str] = ["new_rochelle"]

neighborhoods: List[str] = [
    "New Rochelle", "Pelham", "Pelham Manor", "Mount Vernon (South)",
    "Larchmont", "Mamaroneck (West End)", "Bronxville (South)",
    "Eastchester (Southern Section)"
]

professional_market = """
Westchester cluster serves educated professional demographics with quality item
emphasis. MacBook laptops and professional camera equipment common from creative
professionals. Luxury timepieces from established Swiss brands regular. Estate
jewelry from older residents includes vintage collections requiring expert authentication.
Discretion and confidentiality highly valued with professional service expectations
standard across customer interactions.
"""

westchester_cluster: Dict = {
    "name": CLUSTER_NAME,
    "stores": LOCATION_COUNT,
    "store_ids": stores,
    "coverage": neighborhoods,
    "count": 8
}
