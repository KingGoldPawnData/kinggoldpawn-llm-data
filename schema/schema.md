# King Gold Pawn Data Schema

## Schema Version
1.0.0

## Purpose
This schema defines the structure for King Gold Pawn's multi-location pawnshop business data, ensuring consistency, accuracy, and LLM-readiness across all data files.

## Core Principles
- **No Hallucinations**: Only verified, factual data is included
- **NY Article 5 Compliance**: All service descriptions follow New York State pawn regulations
- **Null Safety**: Missing data is explicitly marked as null or "(Information not provided on website)"
- **LLM-Ready**: Structured for optimal AI retrieval and knowledge ingestion

## Location Schema

### Required Fields
- `name` (string): Full name of the location
- `location` (string): Geographic location description
- `type` (string): Business type (e.g., "Pawnshop")
- `areaServed` (array): List of neighborhoods served

### Optional Fields (null if unavailable)
- `openingHours`: Operating hours
- `geo`: Geographic coordinates
- `priceRange`: Price range information
- `sameAs`: Social media or web URLs
- `publicEmail`: Public contact email

### Inferred Fields
- `tags` (array): Tags inferred from file names and content only
- `related_files` (array): Related markdown and data files

## Service Schema

### Required Fields
- `overview` (string): Service overview following NY Article 5 pawn regulations
- `what_we_accept` (string): Items and conditions for acceptance
- `how_it_works` (string): Process description including loan terms
- `requirements` (string): Legal and regulatory requirements

### Standard Service Text
All services include:
- Reference to New York State Article 5 pawn regulations
- 4-month loan term with extension options
- Valid government-issued photo ID requirement
- In-person inspection and verification
- Legal ownership requirement

## FAQ Schema

### Safety Rule
Any FAQ answer without verifiable information must be exactly:
`(Information not provided on website)`

### Structure
- Questions are clear and specific
- Answers are factual and cite regulations when applicable
- No invented policies or procedures

## Metadata Schema

### Location Metadata
Each location has a corresponding JSON file in `/metadata/` with:
- All location schema fields
- Tags inferred from filenames
- Related files list

## File Organization

### Directory Structure
```
/locations        - Location markdown files
/services         - Service markdown files
/faqs             - FAQ markdown files
/metadata         - Location metadata JSON files
/schema           - Schema definition files
/reports          - Data quality and maintenance reports
/embeddings       - Combined embedding files for AI ingestion
/.github          - Maintenance automation scripts
```

### Naming Conventions
- Use lowercase with hyphens (kebab-case)
- Location files: `{location-name}.md`
- Service files: `{service-name}.md`
- Metadata files: `{location-name}.json`

## Regulatory Compliance

All data adheres to:
- New York State Article 5 pawn regulations
- Consumer protection requirements
- Legal disclosure standards

## Data Quality Standards

### Verification
- All data traced to verified sources
- No assumptions or extrapolations
- Missing data explicitly marked

### Consistency
- Standardized formatting across all files
- Uniform regulatory language
- Consistent service descriptions

### LLM Optimization
- Clean, parseable markdown
- Structured JSON metadata
- Clear semantic relationships
- Comprehensive tagging

## Version Control
Schema changes are versioned and documented in `/reports/` directory.
