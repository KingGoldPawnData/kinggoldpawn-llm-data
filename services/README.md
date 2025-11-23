# Services

This folder contains verified service offering data.

## Purpose
Store factual information about services provided by the business including:
- Service types (loans, buying, selling, appraisals)
- Item categories accepted
- Location availability
- Compliance notes

## File Format
- **JSON files**: Structured service data conforming to `/schema/service-schema.json`
- **Markdown files**: Human-readable service descriptions

## Data Policy
- ✅ Include only verified service offerings
- ✅ Factual descriptions only
- ❌ No pricing information
- ❌ No promotional language
- ❌ No service hours unless verified
- ❌ No invented services or capabilities

## Template
See `_template.json` for the structure to use when adding new services.

## Naming Convention
Files should be named: `{service-id}.json` or `{service-id}.md`
