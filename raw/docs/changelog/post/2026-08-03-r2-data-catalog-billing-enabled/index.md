---
description: R2 Data Catalog usage is now billed on non-enterprise accounts. R2 Data Catalog usage beyond the included free tier will appear on your next invoice.
title: Billing is now enabled for R2 Data Catalog
image: https://developers.cloudflare.com/changelog/post/2026-08-03-r2-data-catalog-billing-enabled/og.png?v=a173e2c3b5131196
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 3, 2026

## Billing is now enabled for R2 Data Catalog

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/) [Basin](https://developers.cloudflare.com/basin/) [R2](https://developers.cloudflare.com/r2/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-03-r2-data-catalog-billing-enabled/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Billing is now enabled for [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) on non-enterprise accounts. R2 Data Catalog usage beyond the included free tier will appear on your next invoice.

R2 Data Catalog charges based on two dimensions, in addition to standard [R2 storage and operations](https://developers.cloudflare.com/r2/pricing/):

- **Catalog operations**: $9.00 / million operations for metadata requests such as creating tables, reading table metadata, and updating table properties.
- **Compaction**: $0.005 / GB processed and $2.00 / million objects processed. These charges only apply when [automatic compaction](https://developers.cloudflare.com/basin-catalog/table-maintenance/) is turned on for a table.

Each dimension includes a monthly free tier: 1 million catalog operations, 10 GB of compaction data processed, and 1 million compaction objects processed.

For example, a single Iceberg table with 50 GB of data, 500,000 catalog operations per month, and compaction turned on that processes 20 GB across 200,000 files would be billed as follows:

| Dimension | Usage | Included | Billable | Cost |
| --- | --- | --- | --- | --- |
| Catalog operations | 500,000 | 1,000,000 | 0 | $0.00 |
| Compaction (data processed) | 20 GB | 10 GB | 10 GB | $0.05 |
| Compaction (objects) | 200,000 | 1,000,000 | 0 | $0.00 |
| **Total (Data Catalog)** |  |  |  | **$0.05** |

Standard R2 storage charges ($0.015 / GB-month) apply separately for the 50 GB of data stored.

For full pricing details and billing examples, refer to [R2 Data Catalog pricing](https://developers.cloudflare.com/basin-catalog/platform/pricing/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-03-r2-data-catalog-billing-enabled/#page","headline":"Billing is now enabled for R2 Data Catalog","description":"R2 Data Catalog usage is now billed on non-enterprise accounts. R2 Data Catalog usage beyond the included free tier will appear on your next invoice.","url":"https://developers.cloudflare.com/changelog/post/2026-08-03-r2-data-catalog-billing-enabled/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-03-r2-data-catalog-billing-enabled/og.png?v=a173e2c3b5131196","dateModified":"2026-08-03","datePublished":"2026-08-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
