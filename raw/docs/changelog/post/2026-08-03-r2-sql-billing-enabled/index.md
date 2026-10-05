---
description: R2 SQL usage is now billed on non-enterprise accounts. R2 SQL usage beyond the included free tier will appear on your next invoice.
title: Billing is now enabled for R2 SQL
image: https://developers.cloudflare.com/changelog/post/2026-08-03-r2-sql-billing-enabled/og.png?v=e25841c11441aa8c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 3, 2026

## Billing is now enabled for R2 SQL

[Basin SQL](https://developers.cloudflare.com/basin-sql/) [Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-03-r2-sql-billing-enabled/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Billing is now enabled for [R2 SQL](https://developers.cloudflare.com/basin-sql/) on non-enterprise accounts. R2 SQL usage beyond the included free tier will appear on your next invoice.

R2 SQL charges based on a single dimension:

- **Data scanned**: $0.0025 / GB ($2.50 / TB) of compressed data read from R2 to execute your query.

All plans include 10 GB of data scanned per month. Each query is billed for a minimum of 10 MB of data scanned. R2 SQL pricing is additive to standard [R2 storage and operations](https://developers.cloudflare.com/r2/pricing/) and [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/platform/pricing/) charges. R2 does not charge for egress, so there is no additional data transfer cost.

For example, a user who stores 500 GB of Parquet data in R2 Data Catalog and runs queries that scan a total of 50 GB of compressed data during the month would be billed as follows:

| Dimension | Usage | Included | Billable | Cost |
| --- | --- | --- | --- | --- |
| R2 storage | 500 GB-month | 10 GB-month | 490 GB-month | $7.35 |
| R2 SQL (data scanned) | 50 GB | 10 GB | 40 GB | $0.10 |
| **Total** |  |  |  | **$7.45** |

For full pricing details and billing examples, refer to [R2 SQL pricing](https://developers.cloudflare.com/basin-sql/platform/pricing/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-03-r2-sql-billing-enabled/#page","headline":"Billing is now enabled for R2 SQL","description":"R2 SQL usage is now billed on non-enterprise accounts. R2 SQL usage beyond the included free tier will appear on your next invoice.","url":"https://developers.cloudflare.com/changelog/post/2026-08-03-r2-sql-billing-enabled/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-03-r2-sql-billing-enabled/og.png?v=e25841c11441aa8c","dateModified":"2026-08-03","datePublished":"2026-08-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
