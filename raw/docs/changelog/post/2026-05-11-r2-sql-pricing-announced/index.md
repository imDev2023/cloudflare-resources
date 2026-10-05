---
description: Usage-based pricing for R2 SQL at $2.50/TB of data scanned, with a free tier included on all plans.
title: R2 SQL pricing announced
image: https://developers.cloudflare.com/changelog/post/2026-05-11-r2-sql-pricing-announced/og.png?v=77cb1d281b2128d4
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 28, 2026

## R2 SQL pricing announced

[Basin SQL](https://developers.cloudflare.com/basin-sql/) [Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-11-r2-sql-pricing-announced/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[R2 SQL](https://developers.cloudflare.com/basin-sql/) is a serverless, distributed query engine that runs SQL against [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables stored in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/). R2 SQL now has published pricing based on a single dimension: the volume of compressed data scanned to execute your queries. At $2.50 / TB ($0.0025 / GB), R2 SQL is priced at half the cost of AWS Athena and less than half of Google BigQuery on-demand.

Billing is not yet enabled. We will provide at least 30 days notice before we start charging for R2 SQL usage.

Data scanned is measured on compressed bytes read from R2 object storage. This matches what you see in your R2 bucket — if a Parquet file is 100 MB on disk, scanning that file bills for 100 MB. Each query has a minimum billing increment of 10 MB.

All plans include 10 GB of data scanned per month. Standard [R2 storage and operations](https://developers.cloudflare.com/r2/pricing/) and [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/platform/pricing/) charges apply separately.

For full pricing details and billing examples, refer to [R2 SQL pricing](https://developers.cloudflare.com/basin-sql/platform/pricing/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-11-r2-sql-pricing-announced/#page","headline":"R2 SQL pricing announced","description":"Usage-based pricing for R2 SQL at $2.50/TB of data scanned, with a free tier included on all plans.","url":"https://developers.cloudflare.com/changelog/post/2026-05-11-r2-sql-pricing-announced/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-11-r2-sql-pricing-announced/og.png?v=77cb1d281b2128d4","dateModified":"2026-05-28","datePublished":"2026-05-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
