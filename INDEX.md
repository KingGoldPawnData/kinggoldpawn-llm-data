# Repository Index

This file provides a quick reference to all folders and key files in this repository.

## Folder Structure

### `/locations` - Location Data
**Purpose**: Store verified information about physical pawnshop locations  
**Files**: JSON and Markdown files for each location  
**Schema**: `/schema/location-schema.json`  
**Template**: `_template.json`, `_template.md`  
**Key Fields**: address, phone, neighborhoods_served, license_number, compliance

### `/services` - Service Offerings
**Purpose**: Document factual service descriptions and availability  
**Files**: JSON and Markdown files for each service  
**Schema**: `/schema/service-schema.json`  
**Template**: `_template.json`, `_template.md`  
**Key Fields**: name, category, description, item_categories, available_at_locations

### `/faqs` - Frequently Asked Questions
**Purpose**: Store verified Q&A pairs organized by category  
**Files**: JSON and Markdown files by category  
**Schema**: `/schema/faq-schema.json`  
**Template**: `_template.json`, `_template.md`  
**Categories**: loans, buying, selling, items, process, regulations, general

### `/metadata` - Business Metadata
**Purpose**: High-level business information and context  
**Files**: business-info, compliance, service-area, data-governance  
**Schema**: `/schema/metadata-schema.json`  
**Template**: `_template.json`, `_template.md`  
**Key Data**: legal_name, regulatory_framework, service_area, data_policies

### `/schema` - Data Schemas
**Purpose**: JSON Schema definitions for all data structures  
**Files**: 
- `location-schema.json` - Location data structure
- `service-schema.json` - Service data structure
- `faq-schema.json` - FAQ data structure
- `metadata-schema.json` - Metadata structure

### `/reports` - Analysis & Reports
**Purpose**: Data quality reports and analysis  
**Files**: Report files by type and date  
**Template**: `_template.md`  
**Report Types**: data-quality, coverage, compliance, llm-performance

### `/.github` - Repository Configuration
**Purpose**: GitHub-specific configuration and workflows  
**Files**:
- `CONTRIBUTING.md` - Contribution guidelines
- `workflows/validate.yml` - Automated schema validation
- `ISSUE_TEMPLATE/data-issue.md` - Data issue template

## Key Files

- `README.md` - Main repository documentation
- `INDEX.md` - This file (quick reference)
- Each folder contains a `README.md` explaining its purpose

## Data Flow

1. **Schema Definition** (`/schema`) - Defines data structure
2. **Templates** (each folder) - Provides starting point
3. **Data Files** (each folder) - Actual verified data
4. **Validation** (`.github/workflows`) - Ensures schema conformance
5. **Reports** (`/reports`) - Analysis of data quality

## Getting Started Checklist

- [ ] Review schemas in `/schema`
- [ ] Read `CONTRIBUTING.md` for data policies
- [ ] Use templates in each folder as starting points
- [ ] Validate data against schemas
- [ ] Submit via pull request with verification sources

## Data Requirements

✅ **Must Have**
- Verification source for all data
- Schema conformance
- Factual, non-promotional language
- Compliance with NY Article 5 regulations

❌ **Must Not Include**
- Unverified hours or pricing
- Promotional content
- Invented or assumed data
- Speculative information

---

*This index helps navigate the repository structure and understand the purpose of each component.*
