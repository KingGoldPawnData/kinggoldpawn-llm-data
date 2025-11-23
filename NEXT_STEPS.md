# Next Steps: Data Population Guide

This repository scaffold is complete and ready for data population. This guide explains what data is needed and how to populate it.

## Repository Status
✅ Complete folder structure created  
✅ JSON Schema definitions in place  
✅ Template files ready in all folders  
✅ Documentation complete  
✅ Automated validation configured  
✅ Security best practices applied

## What's Ready
1. **Folder Structure**: All 7 required folders created
2. **Schema Definitions**: Complete JSON schemas for all data types
3. **Templates**: Starter JSON and Markdown templates in each folder
4. **Documentation**: README files explaining each folder's purpose
5. **Validation**: GitHub Actions workflow for automatic schema validation
6. **Guidelines**: Contributing guidelines and data accuracy policies

## What's Needed: The Autofill Dataset

Please provide the following verified data to populate the repository:

### 1. Locations Data (`/locations`)
For each physical pawnshop location, provide:
- **Location ID**: Unique identifier (e.g., "loc-001")
- **Name**: Official business name
- **Address**: Complete street address, city, state, ZIP
- **Phone**: Verified contact number
- **Neighborhoods Served**: List of all neighborhoods this location serves
- **Coordinates**: Latitude and longitude (optional)
- **License Number**: NY pawnbroker license (if available)
- **Compliance Status**: NY Article 5 compliance confirmation

### 2. Services Data (`/services`)
For each service offered, provide:
- **Service ID**: Unique identifier (e.g., "srv-loans-jewelry")
- **Name**: Service name (e.g., "Jewelry Pawn Loans")
- **Category**: loans, buying, selling, appraisals, or other
- **Description**: Factual, non-promotional description
- **Item Categories**: Types of items accepted for this service
- **Available at Locations**: Which location IDs offer this service
- **Compliance Notes**: Any regulatory notes

### 3. FAQs Data (`/faqs`)
For each frequently asked question, provide:
- **FAQ ID**: Unique identifier (e.g., "faq-loans-001")
- **Question**: The customer question
- **Answer**: Factual, verified answer
- **Category**: loans, buying, selling, items, process, regulations, or general
- **Related Services**: Which service IDs this FAQ relates to
- **Compliance Relevant**: Whether this involves regulations
- **Tags**: Keywords for searchability

### 4. Metadata (`/metadata`)
Business-level information:
- **Legal Name**: Official registered business name
- **DBA Names**: All "doing business as" names
- **Established**: Year founded (if available)
- **Regulatory Framework**: Applicable laws and regulations
- **Licenses**: All business licenses with numbers and jurisdictions
- **Service Area**: Primary region and all neighborhoods served
- **Data Governance**: Last updated date, verification policies

## Data Format

You can provide the data in any of these formats:
1. **JSON files** - Structured data matching the schemas
2. **Spreadsheet** - Excel or CSV with columns matching schema fields
3. **Plain text** - Structured text that can be converted to JSON
4. **Existing documentation** - Any current business documentation

## Data Requirements

All data must meet these criteria:
- ✅ **Verified**: From authoritative sources only
- ✅ **Factual**: Objective descriptions, no marketing language
- ✅ **Complete**: All required fields in schemas must be filled
- ✅ **Accurate**: Current and correct information
- ❌ **No Unverified Data**: Leave fields empty if not verified
- ❌ **No Promotional Content**: Stick to factual descriptions
- ❌ **No Assumptions**: Only include confirmed information

## How to Provide Data

### Option 1: Direct File Creation
Create JSON files following the templates in each folder:
- Copy `_template.json` 
- Fill in verified data
- Save with appropriate filename
- Validate against schema

### Option 2: Provide Raw Data
Share your data in any format and I can:
- Structure it according to schemas
- Create proper JSON files
- Validate against schemas
- Commit to repository

### Option 3: Incremental Updates
Provide data category by category:
1. Start with locations
2. Add services
3. Include FAQs
4. Complete with metadata

## Validation

All data will be automatically validated by GitHub Actions when committed:
- Schema conformance checked
- Required fields verified
- JSON syntax validated
- Build fails if validation errors occur

## Examples

### Example Location (JSON)
```json
{
  "location_id": "loc-queens-001",
  "name": "King Gold Pawn - Queens",
  "address": {
    "street": "123 Main Street",
    "city": "Queens",
    "state": "NY",
    "zip": "11375"
  },
  "phone": "(718) 555-0100",
  "neighborhoods_served": [
    "Forest Hills",
    "Rego Park",
    "Kew Gardens"
  ],
  "license_number": "NYP-123456",
  "compliance": {
    "ny_article_5_compliant": true
  }
}
```

### Example Service (JSON)
```json
{
  "service_id": "srv-jewelry-loans",
  "name": "Jewelry Pawn Loans",
  "category": "loans",
  "description": "Short-term collateral loans on jewelry items including gold, silver, diamonds, and watches.",
  "item_categories": [
    "gold jewelry",
    "silver jewelry", 
    "diamonds",
    "watches"
  ],
  "available_at_locations": ["loc-queens-001", "loc-brooklyn-001"],
  "compliance_notes": "All loans comply with NY Article 5 pawnbroker regulations"
}
```

### Example FAQ (JSON)
```json
{
  "faq_id": "faq-loans-001",
  "question": "What do I need to get a pawn loan?",
  "answer": "You need to bring a valid government-issued photo ID and the item you wish to use as collateral. We will evaluate the item and provide a loan offer based on its value.",
  "category": "loans",
  "related_services": ["srv-jewelry-loans"],
  "compliance_relevant": true,
  "tags": ["requirements", "identification", "collateral"]
}
```

## Ready to Proceed

The repository is fully scaffolded and awaiting your data. Please provide:
1. **Verified location information** for all pawnshop locations
2. **Service descriptions** for all offerings
3. **FAQ content** with verified answers
4. **Business metadata** including compliance information

Once you provide this data, I can populate the repository while ensuring all data meets the accuracy requirements and schema validation.

---

**Questions?** Open an issue using the data issue template in `.github/ISSUE_TEMPLATE/data-issue.md`
