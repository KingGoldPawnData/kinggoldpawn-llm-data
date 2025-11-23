# kinggoldpawn-llm-data

Structured, factual, non-promotional business data for a multi-location pawnshop operation. Includes verified locations, services, neighborhoods served, FAQs, metadata, compliance rules, and schema-based files designed for LLM retrieval, AI ranking, and knowledge ingestion. All content follows strict accuracy requirements and NY Article 5 pawn regulations.

## Repository Structure

```
/
├── locations/      # Verified location data (addresses, contacts, service areas)
├── services/       # Factual service descriptions and availability
├── faqs/          # Frequently asked questions with verified answers
├── metadata/      # Business-level metadata and compliance information
├── schema/        # JSON Schema definitions for all data structures
├── reports/       # Data quality and analysis reports
└── .github/       # Repository configuration and workflows
```

## Data Principles

### ✅ What We Include
- Verified addresses and contact information
- Factual service descriptions
- Accurate compliance and regulatory information
- Confirmed neighborhood coverage
- Validated FAQ answers

### ❌ What We Exclude
- Operating hours (unless verified)
- Pricing information (unless verified)
- Promotional or marketing language
- Unverified claims or assumptions
- Invented or speculative data

## Getting Started

### Understanding the Schema
All data files conform to JSON Schema definitions in the `/schema` folder:
- `location-schema.json` - Location data structure
- `service-schema.json` - Service offering structure
- `faq-schema.json` - FAQ structure
- `metadata-schema.json` - Business metadata structure

### Adding Data
1. Review the appropriate schema in `/schema`
2. Use the template file (`_template.json` or `_template.md`) in the target folder
3. Fill in only verified information
4. Validate against schema before committing
5. Submit via pull request with verification sources

### File Formats
- **JSON files**: Machine-readable, schema-validated data
- **Markdown files**: Human-readable documentation

## Data Validation
GitHub Actions automatically validate all JSON files against their schemas on pull requests. See `.github/workflows/validate.yml` for details.

## Compliance
This repository maintains data in accordance with:
- NY General Business Law Article 5 (Pawnbrokers)
- Data accuracy and verification requirements
- LLM retrieval best practices

## Contributing
See `.github/CONTRIBUTING.md` for detailed contribution guidelines.

## Folder Details

### `/locations`
Verified data for each physical pawnshop location including addresses, contact information, neighborhoods served, and compliance status.

### `/services`
Factual descriptions of services offered, including loan types, buying/selling services, and appraisals. No pricing unless verified.

### `/faqs`
Common questions organized by category (loans, buying, selling, items, process, regulations, general) with factual, verified answers.

### `/metadata`
Business-level information including legal names, regulatory framework, service area overview, and data governance policies.

### `/schema`
JSON Schema definitions that ensure data consistency and provide clear documentation of expected fields.

### `/reports`
Data quality reports, coverage analysis, compliance reports, and LLM performance metrics.

## Data Accuracy Policy
**All information in this repository must be verified before inclusion.** No hours, pricing, or promotional content unless explicitly verified. This ensures reliability for LLM retrieval and AI knowledge systems.

## Status
Repository scaffolded and ready for data population. Awaiting verified data for:
- Location details (addresses, neighborhoods, contacts)
- Service offerings and availability
- FAQ content
- Business metadata
- Compliance information

---

*This repository is designed for factual data storage optimized for LLM and AI systems. All content is non-promotional and accuracy-focused.*
