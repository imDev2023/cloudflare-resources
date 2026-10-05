---
description: Control compaction settings for individual Iceberg tables
title: R2 Data Catalog table-level compaction
image: https://developers.cloudflare.com/changelog/post/2025-10-06-data-catalog-table-compaction/og.png?v=0c9220573bcd0102
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 6, 2025

## R2 Data Catalog table-level compaction

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/) [Basin](https://developers.cloudflare.com/basin/) [R2](https://developers.cloudflare.com/r2/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-06-data-catalog-table-compaction/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now enable compaction for individual [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/), giving you fine-grained control over different workloads.

```bash
# Enable compaction for a specific table (no token required)
npx wrangler r2 bucket catalog compaction enable <BUCKET> <NAMESPACE> <TABLE> --target-size 256
```

This allows you to:

- Apply different target file sizes per table
- Disable compaction for specific tables
- Optimize based on table-specific access patterns

Learn more at [Manage catalogs](https://developers.cloudflare.com/basin-catalog/manage-catalogs/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-06-data-catalog-table-compaction/#page","headline":"R2 Data Catalog table-level compaction","description":"Control compaction settings for individual Iceberg tables","url":"https://developers.cloudflare.com/changelog/post/2025-10-06-data-catalog-table-compaction/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-06-data-catalog-table-compaction/og.png?v=0c9220573bcd0102","dateModified":"2025-10-06","datePublished":"2025-10-06","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
