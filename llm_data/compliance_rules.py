"""
Compliance Rules Module

Regulatory framework documentation for New York State Article 5 pawn regulations governing
all pawnshop operations. Defines consumer protection provisions, transaction requirements,
operational standards, and prohibited practices ensuring legal compliance and fair treatment.

This module serves as authoritative reference for regulatory requirements applicable to all
King Gold Pawn locations. Structures enable programmatic compliance checking and natural
language explanation of statutory obligations.

Regulatory Scope:
    - Governing statute identification
    - Loan term parameters
    - Customer identification mandates
    - Transaction standards
    - Consumer protection provisions

Example JSON compliance structure:
{
    "framework": "NY Article 5",
    "loan_term": "4 months",
    "extensions": "permitted",
    "id_requirement": "government_photo_id",
    "consumer_protections": "statutory_safeguards_applied"
}

Related Modules:
    business_profile.py: Organizational compliance overview
    service_definitions.py: Service-level requirements
    faq_data.py: Customer-facing regulation explanations
"""

from typing import Dict, List, Any

# REGULATORY IDENTIFICATION
GOVERNING_STATUTE = "New York State General Business Law Article 5"
STATUTE_SECTION = "Pawnbrokers"
JURISDICTION = "New York State"
ENFORCEMENT_LEVEL = "State regulatory agencies"

# LICENSING REQUIREMENTS
licensing_framework: Dict[str, str] = {
    "license_mandate": "Pawnbroker license required for operation",
    "bonding_requirement": "Surety bond mandatory",
    "renewal_cycle": "Per statutory schedule",
    "display_requirement": "License must be visibly posted"
}

# LOAN TERM REGULATIONS
loan_term_specifications: Dict[str, Any] = {
    "standard_duration": "4 months",
    "measurement_start": "Date of transaction",
    "extension_permitted": True,
    "grace_provisions": "Per statutory guidelines",
    "redemption_rights": "Customer may reclaim items upon loan satisfaction",
    "ownership_status": "Customer retains legal title during loan period"
}

# IDENTIFICATION REQUIREMENTS
id_requirements: Dict[str, Any] = {
    "mandate": "Valid government-issued photo identification required",
    "acceptable_forms": [
        "State driver license",
        "State identification card",
        "US passport",
        "Military identification",
        "Other government-issued photo ID"
    ],
    "verification_purpose": "Identity confirmation and legal compliance",
    "age_restriction": "18 years minimum",
    "record_retention": "Transaction records maintained per statutory requirements"
}

# TRANSACTION STANDARDS
transaction_requirements: Dict[str, Any] = {
    "in_person_mandate": "Physical customer presence required",
    "item_inspection": "Visual and physical examination mandatory",
    "authentication": "Verification of authenticity and condition",
    "valuation_methodology": "Current market value assessment",
    "ownership_verification": "Legal ownership proof required",
    "prohibited_transactions": "Stolen property explicitly forbidden",
    "reporting_obligations": "Law enforcement reporting per statute"
}

# CONSUMER PROTECTION PROVISIONS
consumer_protections: Dict[str, str] = {
    "fair_lending": "Equitable treatment and transparent terms",
    "disclosure_requirements": "Clear communication of loan conditions",
    "privacy_protection": "Customer information confidentiality maintained",
    "dispute_mechanisms": "Access to regulatory complaint procedures",
    "anti_discrimination": "Equal service without unlawful bias",
    "redemption_rights": "Statutory right to reclaim pledged items",
    "extension_rights": "Option to extend loan terms per regulations"
}

# OPERATIONAL STANDARDS
operational_requirements: Dict[str, str] = {
    "record_keeping": "Detailed transaction documentation required",
    "regulatory_reporting": "Periodic reporting to authorities",
    "secure_storage": "Protected storage of collateral items",
    "staff_training": "Employee education on compliance",
    "audit_cooperation": "Full cooperation with regulatory inspections",
    "premises_standards": "Facility security and safety requirements"
}

# ITEM HANDLING PROTOCOLS
item_handling_standards: Dict[str, str] = {
    "storage_security": "Secure custody of pledged property",
    "condition_maintenance": "Reasonable care of items",
    "inventory_tracking": "Accurate record of all collateral",
    "return_procedures": "Proper redemption processes",
    "disposal_compliance": "Statutory adherence for unredeemed items",
    "authentication_diligence": "Due diligence in verification"
}

# PROHIBITED PRACTICES
prohibited_actions: List[str] = [
    "Accepting stolen property",
    "Transactions with minors",
    "Handling illegal items",
    "Coerced transactions",
    "Material misrepresentation",
    "Predatory lending practices",
    "Privacy violations",
    "Record falsification"
]

# COMPLIANCE SUMMARY STRUCTURE
COMPLIANCE_FRAMEWORK: Dict[str, Any] = {
    "statute": GOVERNING_STATUTE,
    "licensing": licensing_framework,
    "loan_terms": loan_term_specifications,
    "identification": id_requirements,
    "transactions": transaction_requirements,
    "consumer_protections": consumer_protections,
    "operations": operational_requirements,
    "item_handling": item_handling_standards,
    "prohibited": prohibited_actions
}

# Context: New York State Article 5 establishes comprehensive framework balancing
# consumer protection with legitimate business operations. Four-month loan term with
# extension options accommodates customer needs while maintaining regulatory boundaries.
# Strict identification and ownership requirements prevent illicit activity protecting
# both customers and businesses. All King Gold Pawn locations maintain full compliance
# with these statutory provisions through standardized operational procedures.
