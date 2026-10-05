---
description: Automatic snapshot expiration now cleans up unreferenced data files in addition to Iceberg metadata
title: R2 Data Catalog snapshot expiration now removes unreferenced data files
image: https://developers.cloudflare.com/changelog/post/2026-04-22-snapshot-expiration-cleans-data-files/og.png?v=96ba0a8515503e25
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 22, 2026

## R2 Data Catalog snapshot expiration now removes unreferenced data files

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/) [Basin](https://developers.cloudflare.com/basin/) [R2](https://developers.cloudflare.com/r2/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-22-snapshot-expiration-cleans-data-files/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/), a managed [Apache Iceberg ↗︎](https://iceberg.apache.org/) catalog built into R2, now removes unreferenced data files during automatic snapshot expiration. This improvement reduces storage costs and eliminates the need to run manual maintenance jobs to reclaim space from deleted data.

Previously, snapshot expiration only cleaned up Iceberg metadata files such as manifests and manifest lists. Data files that were no longer referenced by active snapshots remained in R2 storage until you manually ran `remove_orphan_files` or `expire_snapshots` through an engine like Spark. This required extra operational overhead and left stale data files consuming storage.

Snapshot expiration now handles both metadata and data file cleanup automatically. When a snapshot is expired, any data files that are no longer referenced by retained snapshots are removed from R2 storage.

```bash
# Enable catalog-level snapshot expiration
npx wrangler r2 bucket catalog snapshot-expiration enable my-bucket \
  --older-than-days 7 \
  --retain-last 10
```

For more information, refer to the [table maintenance documentation](https://developers.cloudflare.com/basin-catalog/table-maintenance/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-22-snapshot-expiration-cleans-data-files/#page","headline":"R2 Data Catalog snapshot expiration now removes unreferenced data files","description":"Automatic snapshot expiration now cleans up unreferenced data files in addition to Iceberg metadata","url":"https://developers.cloudflare.com/changelog/post/2026-04-22-snapshot-expiration-cleans-data-files/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-22-snapshot-expiration-cleans-data-files/og.png?v=96ba0a8515503e25","dateModified":"2026-04-22","datePublished":"2026-04-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
