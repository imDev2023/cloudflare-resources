---
description: Automatically remove old Apache Iceberg table snapshots to improve performance and reduce storage costs
title: R2 Data Catalog now supports automatic snapshot expiration
image: https://developers.cloudflare.com/changelog/post/2025-12-18-r2-data-catalog-snapshot-expiration/og.png?v=93978511977ec7c8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 18, 2025

## R2 Data Catalog now supports automatic snapshot expiration

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/) [Basin](https://developers.cloudflare.com/basin/) [R2](https://developers.cloudflare.com/r2/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-18-r2-data-catalog-snapshot-expiration/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) now supports automatic snapshot expiration for Apache Iceberg tables.

In Apache Iceberg, a snapshot is metadata that represents the state of a table at a given point in time. Every mutation creates a new snapshot which enable powerful features like time travel queries and rollback capabilities but will accumulate over time.

Without regular cleanup, these accumulated snapshots can lead to:

- Metadata overhead
- Slower table operations
- Increased storage costs.

Snapshot expiration in R2 Data Catalog automatically removes old table snapshots based on your configured retention policy, improving performance and storage costs.

```bash
# Enable catalog-level snapshot expiration
# Expire snapshots older than 7 days, always retain at least 10 recent snapshots
npx wrangler r2 bucket catalog snapshot-expiration enable my-bucket \
  --older-than-days 7 \
  --retain-last 10
```

Snapshot expiration uses two parameters to determine which snapshots to remove:

- `--older-than-days`: age threshold in days
- `--retain-last`: minimum snapshot count to retain

Both conditions must be met before a snapshot is expired, ensuring you always retain recent snapshots even if they exceed the age threshold.

This feature complements [automatic compaction](https://developers.cloudflare.com/basin-catalog/table-maintenance/), which optimizes query performance by combining small data files into larger ones. Together, these automatic maintenance operations keep your Iceberg tables performant and cost-efficient without manual intervention.

For more information, refer to [Table maintenance](https://developers.cloudflare.com/basin-catalog/table-maintenance/) or [Manage catalogs](https://developers.cloudflare.com/basin-catalog/manage-catalogs/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-18-r2-data-catalog-snapshot-expiration/#page","headline":"R2 Data Catalog now supports automatic snapshot expiration","description":"Automatically remove old Apache Iceberg table snapshots to improve performance and reduce storage costs","url":"https://developers.cloudflare.com/changelog/post/2025-12-18-r2-data-catalog-snapshot-expiration/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-18-r2-data-catalog-snapshot-expiration/og.png?v=93978511977ec7c8","dateModified":"2025-12-18","datePublished":"2025-12-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
