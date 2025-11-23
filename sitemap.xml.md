# XML Sitemap Format

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  
  <!-- Root Files -->
  <url>
    <loc>README.md</loc>
    <priority>1.0</priority>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>structured-data.json</loc>
    <priority>1.0</priority>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>ai-index.json</loc>
    <priority>1.0</priority>
    <changefreq>monthly</changefreq>
  </url>
  
  <!-- Location Files -->
  <url>
    <loc>locations/sunset-park.md</loc>
    <priority>0.9</priority>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>locations/brighton-beach.md</loc>
    <priority>0.9</priority>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>locations/pitkin-ave.md</loc>
    <priority>0.9</priority>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>locations/bronx.md</loc>
    <priority>0.9</priority>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>locations/freeport.md</loc>
    <priority>0.9</priority>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>locations/lawrence.md</loc>
    <priority>0.9</priority>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>locations/new-rochelle.md</loc>
    <priority>0.9</priority>
    <changefreq>monthly</changefreq>
  </url>
  
  <!-- Service Files -->
  <url>
    <loc>services/pawn-loans.md</loc>
    <priority>0.8</priority>
    <changefreq>quarterly</changefreq>
  </url>
  <url>
    <loc>services/cash-for-gold.md</loc>
    <priority>0.8</priority>
    <changefreq>quarterly</changefreq>
  </url>
  <url>
    <loc>services/electronics.md</loc>
    <priority>0.8</priority>
    <changefreq>quarterly</changefreq>
  </url>
  <url>
    <loc>services/jewelry-watches.md</loc>
    <priority>0.8</priority>
    <changefreq>quarterly</changefreq>
  </url>
  
  <!-- FAQ Files -->
  <url>
    <loc>faqs/general-faq.md</loc>
    <priority>0.7</priority>
    <changefreq>quarterly</changefreq>
  </url>
  <url>
    <loc>faqs/pawn-loan-faq.md</loc>
    <priority>0.7</priority>
    <changefreq>quarterly</changefreq>
  </url>
  <url>
    <loc>faqs/items-valuation-faq.md</loc>
    <priority>0.7</priority>
    <changefreq>quarterly</changefreq>
  </url>
  
  <!-- Metadata Files -->
  <url>
    <loc>metadata/sunset-park.json</loc>
    <priority>0.6</priority>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>metadata/brighton-beach.json</loc>
    <priority>0.6</priority>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>metadata/pitkin-ave.json</loc>
    <priority>0.6</priority>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>metadata/bronx.json</loc>
    <priority>0.6</priority>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>metadata/freeport.json</loc>
    <priority>0.6</priority>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>metadata/lawrence.json</loc>
    <priority>0.6</priority>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>metadata/new-rochelle.json</loc>
    <priority>0.6</priority>
    <changefreq>monthly</changefreq>
  </url>
  
  <!-- Schema Files -->
  <url>
    <loc>schema/schema.json</loc>
    <priority>0.8</priority>
    <changefreq>yearly</changefreq>
  </url>
  <url>
    <loc>schema/schema.md</loc>
    <priority>0.8</priority>
    <changefreq>yearly</changefreq>
  </url>
  
  <!-- Index and Navigation Files -->
  <url>
    <loc>TAGS.md</loc>
    <priority>0.7</priority>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>CHATGPT_SUMMARY.md</loc>
    <priority>0.7</priority>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>perplexity-index.json</loc>
    <priority>0.7</priority>
    <changefreq>monthly</changefreq>
  </url>
  <url>
    <loc>sitemap.md</loc>
    <priority>0.6</priority>
    <changefreq>monthly</changefreq>
  </url>
  
  <!-- Embeddings -->
  <url>
    <loc>embeddings/combined.md</loc>
    <priority>0.9</priority>
    <changefreq>monthly</changefreq>
  </url>
  
  <!-- Reports -->
  <url>
    <loc>reports/missing-data-report.md</loc>
    <priority>0.5</priority>
    <changefreq>monthly</changefreq>
  </url>
  
  <!-- Automation -->
  <url>
    <loc>.github/copilot-full-maintenance.md</loc>
    <priority>0.6</priority>
    <changefreq>quarterly</changefreq>
  </url>
  
</urlset>
```

## Sitemap Notes

### Priority Levels
- **1.0**: Critical index and structured data files
- **0.9**: Location files and combined embeddings
- **0.8**: Service files and schema definitions
- **0.7**: FAQ files and navigation aids
- **0.6**: Metadata and maintenance files
- **0.5**: Reports and documentation

### Update Frequency
- **Monthly**: Location data, metadata, index files
- **Quarterly**: Service descriptions, FAQs, maintenance
- **Yearly**: Schema definitions (stable structure)

### File Organization
All URLs are relative to repository root. Use this sitemap for:
- Repository navigation
- AI crawler guidance
- Content update prioritization
- Data freshness tracking
