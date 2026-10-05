---
description: A new standalone dashboard for R2 Data Catalog with a guided setup wizard, settings management, and built-in metrics.
title: R2 Data Catalog gets a dedicated dashboard experience
image: https://developers.cloudflare.com/changelog/post/2026-05-28-r2-data-catalog-dashboard/og.png?v=0ac640f2025b5275
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 28, 2026

## R2 Data Catalog gets a dedicated dashboard experience

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/) [Basin](https://developers.cloudflare.com/basin/) [R2](https://developers.cloudflare.com/r2/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-28-r2-data-catalog-dashboard/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/) is a managed [Apache Iceberg ↗︎](https://iceberg.apache.org/) data catalog built directly into your R2 bucket. It exposes a standard Iceberg REST catalog interface so you can connect query engines like [Spark](https://developers.cloudflare.com/basin-catalog/config-examples/spark-scala/), [Snowflake](https://developers.cloudflare.com/basin-catalog/config-examples/snowflake/), [DuckDB](https://developers.cloudflare.com/basin-catalog/config-examples/duckdb/), and [R2 SQL](https://developers.cloudflare.com/basin-sql/) to your data in R2.

R2 Data Catalog now has a dedicated section in the Cloudflare dashboard, replacing the previous settings panel embedded in R2 bucket configuration. The new experience includes:

![R2 Data Catalog dashboard overview](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3070,height=1486,format=webp/_astro/data-catalog-dashboard.BsKDvUQn.png)

- **Catalog overview** — View all your catalogs in one place with catalog request counts, bucket sizes, and table maintenance status at a glance.
- **Guided setup wizard** — Create a catalog in three steps: choose or create an R2 bucket, configure table maintenance (compaction and snapshot expiration), and review. The wizard creates the bucket and generates a service credential automatically.
- **Settings management** — A dedicated settings page for each catalog with sections for general configuration, table maintenance, service credentials, and disabling the catalog. You can now enable and configure [snapshot expiration](https://developers.cloudflare.com/basin-catalog/table-maintenance/) directly from the dashboard.
- **Built-in metrics** — Five charts on each catalog's metrics tab: bytes compacted, files compacted, catalog requests, storage size, and snapshots expired.

To get started, go to **R2 Data Catalog** in the Cloudflare dashboard or refer to the [getting started guide](https://developers.cloudflare.com/basin-catalog/get-started/) and [manage catalogs documentation](https://developers.cloudflare.com/basin-catalog/manage-catalogs/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-28-r2-data-catalog-dashboard/#page","headline":"R2 Data Catalog gets a dedicated dashboard experience","description":"A new standalone dashboard for R2 Data Catalog with a guided setup wizard, settings management, and built-in metrics.","url":"https://developers.cloudflare.com/changelog/post/2026-05-28-r2-data-catalog-dashboard/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-28-r2-data-catalog-dashboard/og.png?v=0ac640f2025b5275","dateModified":"2026-05-28","datePublished":"2026-05-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
