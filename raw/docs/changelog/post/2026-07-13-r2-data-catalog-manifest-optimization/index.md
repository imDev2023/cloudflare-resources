---
description: Compaction automatically rewrites and clusters Apache Iceberg manifest files to reduce metadata overhead and speed up query planning
title: R2 Data Catalog compaction now optimizes manifest files
image: https://developers.cloudflare.com/changelog/post/2026-07-13-r2-data-catalog-manifest-optimization/og.png?v=7a2fd89d8cc72a31
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 13, 2026

## R2 Data Catalog compaction now optimizes manifest files

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/) [Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-13-r2-data-catalog-manifest-optimization/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/), a managed [Apache Iceberg ↗︎](https://iceberg.apache.org/) catalog built into R2, now automatically optimizes manifest files as part of [compaction](https://developers.cloudflare.com/basin-catalog/table-maintenance/).

Manifest files track the data files that make up an Iceberg table. As a table accumulates many small or fragmented manifests, query engines must read more metadata during query planning, which slows down queries even before any data is scanned.

When compaction runs, R2 Data Catalog now rewrites and clusters manifest files by partition as a best-effort pre-step. This consolidates fragmented manifests, reduces the number of manifests a query engine must open, and lowers metadata I/O overhead. Tables that are already well-clustered are skipped, so the operation only runs when it provides a benefit.

This happens automatically for tables with compaction enabled — no configuration changes are required.

For more information, refer to [Table maintenance](https://developers.cloudflare.com/basin-catalog/table-maintenance/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-13-r2-data-catalog-manifest-optimization/#page","headline":"R2 Data Catalog compaction now optimizes manifest files","description":"Compaction automatically rewrites and clusters Apache Iceberg manifest files to reduce metadata overhead and speed up query planning","url":"https://developers.cloudflare.com/changelog/post/2026-07-13-r2-data-catalog-manifest-optimization/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-13-r2-data-catalog-manifest-optimization/og.png?v=7a2fd89d8cc72a31","dateModified":"2026-07-13","datePublished":"2026-07-13","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
