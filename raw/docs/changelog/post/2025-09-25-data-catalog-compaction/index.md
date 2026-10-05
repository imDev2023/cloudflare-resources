---
description: Users can now enable compaction on R2 Data Catalog
title: R2 Data Catalog now supports compaction
image: https://developers.cloudflare.com/changelog/post/2025-09-25-data-catalog-compaction/og.png?v=10ad8eb1c1d01f08
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 25, 2025

## R2 Data Catalog now supports compaction

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/) [Basin](https://developers.cloudflare.com/basin/) [R2](https://developers.cloudflare.com/r2/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-25-data-catalog-compaction/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now enable automatic compaction for [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) to improve query performance.

Compaction is the process of taking a group of small files and combining them into fewer larger files. This is an important maintenance operation as it helps ensure that query performance remains consistent by reducing the number of files that needs to be scanned.

To enable automatic compaction in R2 Data Catalog, find it under **R2 Data Catalog** in your R2 bucket settings in the dashboard.

![compaction-dash](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=799,height=400,format=webp/_astro/compaction.MLojYuHL.png)

Or with [Wrangler](https://developers.cloudflare.com/workers/wrangler/), run:

```bash
npx wrangler r2 bucket catalog compaction enable <BUCKET_NAME>  --target-size 128 --token <API_TOKEN>
```

To get started with compaction, check out [manage catalogs](https://developers.cloudflare.com/basin-catalog/manage-catalogs/). For best practices and limitations, refer to [about compaction](https://developers.cloudflare.com/basin-catalog/table-maintenance/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-25-data-catalog-compaction/#page","headline":"R2 Data Catalog now supports compaction","description":"Users can now enable compaction on R2 Data Catalog","url":"https://developers.cloudflare.com/changelog/post/2025-09-25-data-catalog-compaction/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-25-data-catalog-compaction/og.png?v=10ad8eb1c1d01f08","dateModified":"2025-09-25","datePublished":"2025-09-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
