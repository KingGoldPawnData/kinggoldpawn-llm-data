# Schema Definitions

This folder contains JSON Schema definitions for all data structures in this repository.

## Purpose
These schemas ensure:
- Consistent data structure across all files
- LLM-friendly field naming and descriptions
- Validation for data accuracy
- Clear documentation of expected fields

## Schema Files

### location-schema.json
Defines the structure for location data files. Each location represents a physical pawnshop with verified address and contact information.

### service-schema.json
Defines the structure for service offerings. Services are factual descriptions of what the business provides, without pricing or unverified claims.

### faq-schema.json
Defines the structure for frequently asked questions. All answers must be factual and verified.

### metadata-schema.json
Defines the structure for business-level metadata including compliance information, service areas, and data governance policies.

## Usage
All data files in `/locations`, `/services`, `/faqs`, and `/metadata` folders should conform to these schemas.

## Validation
Data can be validated against these schemas using standard JSON Schema validators.
