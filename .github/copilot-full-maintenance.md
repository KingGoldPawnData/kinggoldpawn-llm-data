# Copilot Full Maintenance Script

## Purpose
This document provides comprehensive automated maintenance instructions for GitHub Copilot to keep the King Gold Pawn LLM data repository up-to-date, consistent, and error-free.

---

## Maintenance Principles

### Core Rules
1. **Zero Hallucination:** Never invent data. Only use verified information.
2. **Explicit Marking:** All missing data must be marked as null or "(Information not provided on website)"
3. **Consistency:** Maintain uniform formatting, language, and structure across all files
4. **Compliance:** All content must reference NY State Article 5 pawn regulations
5. **LLM-Ready:** Maintain clean, parseable markdown and JSON

### When to Run Maintenance
- After adding new location data
- After updating service descriptions
- When new verified information becomes available
- When fixing data inconsistencies
- Quarterly review for data quality
- When updating regulatory compliance language

---

## Automated Maintenance Tasks

### Task 1: Validate Location Files

**Check each file in `/locations/`:**

```markdown
Expected structure for each location:
- # King Gold Pawn - {Location Name}
- ## Location Information
  - Name, Location, Type fields present
- ## Neighborhoods Served
  - Bulleted list matching verified data
- ## Hours of Operation
  - "(Information not provided on website)" if unknown
- ## Services Offered
  - Overview, What We Accept, How It Works, Requirements sections
  - All must reference NY Article 5
- ## Contact Information
  - Address, Phone, Email all marked if missing
- ## Additional Information
  - Regulatory compliance statement
```

**Validation checklist:**
- [ ] All 7 location files present
- [ ] Consistent section headers
- [ ] Neighborhoods match verified lists
- [ ] Service descriptions are identical across locations
- [ ] Missing data properly marked
- [ ] NY Article 5 referenced
- [ ] 4-month loan term mentioned

**Auto-fix rules:**
- If service description differs from standard, replace with standard
- If neighborhood list differs from verified data, correct it
- If missing data not marked, add "(Information not provided on website)"
- If NY Article 5 not mentioned, add it

---

### Task 2: Validate Metadata JSON Files

**Check each file in `/metadata/`:**

```json
Required structure:
{
  "name": "King Gold Pawn - {Location}",
  "location": "{City}, {Region}, NY",
  "type": "Pawnshop",
  "openingHours": null,
  "areaServed": [...verified neighborhoods...],
  "geo": null,
  "priceRange": null,
  "sameAs": null,
  "publicEmail": null,
  "tags": [...inferred from filenames only...],
  "related_files": [...actual file paths...]
}
```

**Validation checklist:**
- [ ] All 7 metadata files present
- [ ] Valid JSON syntax
- [ ] All required fields present
- [ ] Null fields set to null (not missing)
- [ ] areaServed matches location MD file
- [ ] tags are kebab-case
- [ ] related_files paths are valid

**Auto-fix rules:**
- If JSON invalid, correct syntax
- If required field missing, add with null or appropriate value
- If areaServed mismatches location file, synchronize
- If tags contain spaces, convert to kebab-case
- If related_files path invalid, correct or remove

---

### Task 3: Validate Service Files

**Check each file in `/services/`:**

```markdown
Expected structure:
- # {Service Name}
- ## Overview (standard text)
- ## What We Accept (standard text)
- ## How It Works (standard text)
- ## Requirements (standard text)
- ## Additional section (service-specific)
```

**Standard text validation:**
- Overview must mention: fast, secure, regulated, NY Article 5
- What We Accept must list: gold, jewelry, diamonds, watches, coins, precious metals, designer items, electronics (phones, laptops, tablets, cameras, game consoles), authenticity requirement
- How It Works must mention: bring item + ID, evaluation, pawn or sell, immediate cash, 4-month term, extensions
- Requirements must mention: valid photo ID, legal ownership, in-person presentation, NY Article 5, 4-month term

**Validation checklist:**
- [ ] All 4 service files present
- [ ] Standard sections present
- [ ] Standard text matches template
- [ ] NY Article 5 referenced
- [ ] 4-month term mentioned
- [ ] Extension options mentioned

**Auto-fix rules:**
- If standard text missing elements, add them
- If NY Article 5 not mentioned, add it
- If loan term incorrect, correct to 4 months with extensions

---

### Task 4: Validate FAQ Files

**Check each file in `/faqs/`:**

```markdown
Required structure:
- # {FAQ Category Name}
- ## Section Headers
- ### Question
- Answer text or "(Information not provided on website)"
```

**Validation checklist:**
- [ ] All 3 FAQ files present
- [ ] Questions are clear and specific
- [ ] Answers are factual or use safe fallback
- [ ] No invented policies or prices
- [ ] NY Article 5 referenced where appropriate
- [ ] Consistent safe fallback text

**Auto-fix rules:**
- If answer invents data not in verified sources, replace with "(Information not provided on website)"
- If safe fallback text inconsistent, standardize to "(Information not provided on website)"
- If regulatory answer missing NY Article 5, add reference

---

### Task 5: Validate Schema Files

**Check `/schema/schema.json`:**
- [ ] Valid JSON syntax
- [ ] Location definition complete
- [ ] Service definition complete
- [ ] All required fields defined
- [ ] Null types properly specified

**Check `/schema/schema.md`:**
- [ ] Version number present
- [ ] All schema sections documented
- [ ] Example structures provided
- [ ] Regulatory compliance noted
- [ ] LLM optimization explained

**Auto-fix rules:**
- If JSON invalid, correct syntax
- If definition incomplete, add missing properties
- If documentation out of sync with JSON, update

---

### Task 6: Validate Structured Data

**Check `structured-data.json`:**

```json
Required for each location:
{
  "@type": "LocalBusiness",
  "@id": "#{location-slug}",
  "name": "King Gold Pawn - {Location}",
  "description": "Pawnshop offering...",
  "address": { PostalAddress with locality, region, country },
  "areaServed": [...neighborhoods...],
  "openingHours": null,
  "geo": null,
  "priceRange": null,
  "paymentAccepted": "Cash",
  "currenciesAccepted": "USD"
}
```

**Validation checklist:**
- [ ] Valid JSON-LD syntax
- [ ] @context is schema.org
- [ ] @graph contains all 7 locations
- [ ] Each location has all required fields
- [ ] Null fields set properly
- [ ] areaServed matches metadata

**Auto-fix rules:**
- If JSON invalid, correct syntax
- If location missing, add from metadata
- If areaServed mismatches, synchronize with metadata
- If required field missing, add with appropriate value

---

### Task 7: Validate Index Files

**Check `ai-index.json`:**
- [ ] All 7 locations listed
- [ ] All 4 services listed
- [ ] All 3 FAQs listed
- [ ] File paths valid
- [ ] Counts accurate (total_locations, total_neighborhoods)
- [ ] Accepted items list complete

**Check `TAGS.md`:**
- [ ] All location tags present
- [ ] All service tags present
- [ ] No invented tags
- [ ] Kebab-case formatting
- [ ] Tag usage rules documented

**Check `perplexity-index.json`:**
- [ ] All locations listed with correct data
- [ ] All services listed with categories
- [ ] Accepted items complete
- [ ] Regulatory info accurate
- [ ] Query optimization hints present

**Auto-fix rules:**
- If location count wrong, recalculate
- If file path invalid, correct
- If tag not kebab-case, convert
- If item missing from accepted list, add if verified

---

### Task 8: Validate Navigation Files

**Check `sitemap.md`:**
- [ ] All directories listed
- [ ] All files documented
- [ ] File counts accurate
- [ ] Structure description complete

**Check `sitemap.xml.md`:**
- [ ] All files listed as URLs
- [ ] Priority values appropriate
- [ ] Change frequency realistic
- [ ] XML syntax valid

**Auto-fix rules:**
- If file not listed, add to sitemap
- If file count wrong, recalculate
- If XML invalid, correct syntax

---

### Task 9: Validate Summary Files

**Check `CHATGPT_SUMMARY.md`:**
- [ ] All 7 locations summarized
- [ ] All 4 services summarized
- [ ] Service area neighborhoods listed
- [ ] Missing data section present
- [ ] Data quality notes present
- [ ] Version and date present

**Auto-fix rules:**
- If location missing, add summary
- If neighborhood count wrong, recalculate
- If missing data list incomplete, update from missing-data-report.md

---

### Task 10: Validate Embeddings

**Check `embeddings/combined.md`:**
- [ ] All location information included
- [ ] All service descriptions included
- [ ] FAQ content included
- [ ] Regulatory compliance section present
- [ ] Data quality statement present
- [ ] Version and date present

**Auto-fix rules:**
- If location missing, add from location file
- If service description outdated, update from service file
- If FAQ content missing, add from FAQ files

---

### Task 11: Update Missing Data Report

**Check `reports/missing-data-report.md`:**
- [ ] Timestamp current
- [ ] Autofilled fields documented
- [ ] Missing data list complete
- [ ] Safe fallback implementation shown
- [ ] Hallucination status confirmed
- [ ] Recommendations section present

**Auto-fix rules:**
- If new verified data added, update missing data list
- If timestamp old, update to current date
- If hallucination check missing, add confirmation

---

## Data Synchronization Rules

### When a Location is Updated

1. Update location MD file in `/locations/`
2. Update corresponding JSON in `/metadata/`
3. Update structured-data.json entry
4. Update ai-index.json location entry
5. Update perplexity-index.json location entry
6. Update CHATGPT_SUMMARY.md location section
7. Update embeddings/combined.md location section
8. Update sitemap.md if new files added
9. Regenerate missing-data-report.md if data status changed

### When a Service is Updated

1. Update service MD file in `/services/`
2. Update ai-index.json service entry
3. Update perplexity-index.json service entry
4. Update CHATGPT_SUMMARY.md service section
5. Update embeddings/combined.md service section
6. Update ALL location MD files with new service description (if standard text changed)
7. Regenerate missing-data-report.md if needed

### When an FAQ is Updated

1. Update FAQ MD file in `/faqs/`
2. Update ai-index.json FAQ entry if structure changed
3. Update embeddings/combined.md FAQ section
4. Regenerate missing-data-report.md if safe fallback added/removed

### When Verified Data is Added

1. Remove null or safe fallback from relevant files
2. Add verified data
3. Update missing-data-report.md to remove from missing list
4. Update CHATGPT_SUMMARY.md to remove from missing data section
5. Commit with clear data source documentation

---

## Quality Assurance Checks

### Pre-Commit Validation

Run these checks before committing any changes:

```bash
# 1. Validate all JSON files
find . -name "*.json" -exec python3 -m json.tool {} \; > /dev/null

# 2. Check for hallucination indicators
grep -r "maybe\|probably\|approximately\|around\|about" locations/ services/ faqs/

# 3. Check for invented contact info
grep -r "[0-9]\{3\}-[0-9]\{3\}-[0-9]\{4\}" locations/
grep -r "@.*\.com" locations/

# 4. Verify NY Article 5 references
grep -L "Article 5" locations/*.md services/*.md

# 5. Verify safe fallback consistency
grep -r "Information not provided" locations/ faqs/ | grep -v "Information not provided on website"

# 6. Count files
echo "Locations: $(ls -1 locations/*.md | wc -l) (expect 7)"
echo "Metadata: $(ls -1 metadata/*.json | wc -l) (expect 7)"
echo "Services: $(ls -1 services/*.md | wc -l) (expect 4)"
echo "FAQs: $(ls -1 faqs/*.md | wc -l) (expect 3)"
```

### Post-Update Validation

After any update, verify:
- [ ] No broken file references
- [ ] All JSON is valid
- [ ] All markdown renders correctly
- [ ] No hallucinated data introduced
- [ ] Missing data still properly marked
- [ ] Regulatory compliance maintained
- [ ] File counts correct in index files
- [ ] Timestamps updated where appropriate

---

## Emergency Fixes

### If Hallucinated Data Detected

1. Immediately replace with null or "(Information not provided on website)"
2. Document in git commit message
3. Update missing-data-report.md
4. Review all related files for similar issues
5. Run full validation suite

### If Schema.org Validation Fails

1. Check structured-data.json syntax
2. Verify @context and @type values
3. Ensure all required LocalBusiness properties present
4. Validate against schema.org documentation
5. Test with Google Structured Data Testing Tool if available

### If Regulatory Language Incorrect

1. Review NY State Article 5 pawn regulations
2. Update standard service text templates
3. Propagate to all location files
4. Update service files
5. Update schema documentation
6. Verify in all FAQ answers

---

## Version Control Best Practices

### Commit Messages

Format: `[Category] Brief description`

Examples:
- `[Location] Add verified hours for Sunset Park location`
- `[Service] Update pawn loan description for clarity`
- `[Fix] Correct neighborhood list for Brighton Beach`
- `[Maintenance] Synchronize all location service descriptions`
- `[Data] Remove safe fallback for Lawrence phone number (verified)`

### Commit Frequency

- Commit after each logical change
- Commit all synchronization changes together
- Commit missing-data-report.md updates separately
- Commit emergency fixes immediately

---

## Monitoring and Alerts

### Data Quality Indicators

Monitor these metrics:
- Number of null fields (should decrease over time)
- Number of safe fallback uses (should decrease over time)
- File count consistency
- JSON validation success rate
- Schema.org compliance

### Red Flags

Alert if:
- JSON validation fails
- File count changes unexpectedly
- New files added without metadata
- Safe fallback text inconsistent
- NY Article 5 not referenced in new content
- Invented data patterns detected

---

## Automation Opportunities

### Potential Scripts

1. **validate-all.sh** - Run all validation checks
2. **sync-service-text.sh** - Propagate service descriptions to all locations
3. **update-counts.sh** - Recalculate all file and item counts
4. **generate-report.sh** - Regenerate missing-data-report.md
5. **check-json.sh** - Validate all JSON files

### Integration Points

- Pre-commit hooks for validation
- CI/CD pipeline for testing
- Automated missing data reports
- Schema validation in PR checks

---

## Maintenance Schedule

### Weekly
- Validate all JSON files
- Check for broken file references
- Verify file counts

### Monthly
- Full validation suite
- Review missing-data-report.md
- Update timestamps in index files
- Check for regulatory updates

### Quarterly
- Review all location data for accuracy
- Update service descriptions if needed
- Review FAQ answers for completeness
- Update schema if data structure evolved
- Full documentation review

### Annually
- Review NY Article 5 for regulatory changes
- Update schema version if needed
- Comprehensive data quality audit
- Review and update automation scripts

---

## Contact and Support

For questions about maintenance procedures:
1. Review this document thoroughly
2. Check schema documentation in `/schema/`
3. Review missing-data-report.md for data status
4. Consult NY State Article 5 pawn regulations for compliance questions

---

**Document Version:** 1.0.0  
**Last Updated:** 2025-11-23  
**Next Review:** 2026-02-23  

---

## Quick Reference Commands

```bash
# Validate all JSON
find . -name "*.json" -type f -exec sh -c 'echo "Checking {}"; python3 -m json.tool {} > /dev/null' \;

# Count files
echo "Locations: $(ls -1 locations/*.md 2>/dev/null | wc -l)"
echo "Services: $(ls -1 services/*.md 2>/dev/null | wc -l)"
echo "FAQs: $(ls -1 faqs/*.md 2>/dev/null | wc -l)"
echo "Metadata: $(ls -1 metadata/*.json 2>/dev/null | wc -l)"

# Find safe fallbacks
grep -r "Information not provided on website" locations/ faqs/

# Check for NY Article 5
grep -l "Article 5" locations/*.md services/*.md

# Verify no invented data patterns
grep -r "approximately\|about\|around\|maybe\|probably" locations/ services/ faqs/
```
