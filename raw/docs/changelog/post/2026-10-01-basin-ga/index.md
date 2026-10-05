---
description: Cloudflare Data Platform is now Basin, bringing generally available ingestion, Iceberg table management, and SQL analytics together on R2.
title: Cloudflare Basin is now generally available
image: https://developers.cloudflare.com/changelog/post/2026-10-01-basin-ga/og.png?v=cb42c4b226f41dee
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 1, 2026

## Cloudflare Basin is now generally available

[Basin](https://developers.cloudflare.com/basin/) [Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/) [Basin Catalog](https://developers.cloudflare.com/basin-catalog/) [Basin SQL](https://developers.cloudflare.com/basin-sql/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-01-basin-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Basin](https://developers.cloudflare.com/basin/), formerly the Cloudflare Data Platform, is now generally available. Basin brings an end-to-end analytics platform to the Developer Platform, enabling you to collect data from a variety of sources, such as apps, infrastructure, devices, and other Cloudflare services, then query it to answer analytical questions.

#### Basin Pipelines

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/), formerly Cloudflare Pipelines, ingests events from Workers, HTTP endpoints, and Cloudflare [Logpush](https://developers.cloudflare.com/logpush/). It transforms events with SQL and ingests them into Iceberg tables or files on R2. With Basin Pipelines you can:

- Ingest application and device events through HTTP endpoints or Workers bindings.
- Filter and reshape Cloudflare logs before storing them as Iceberg tables, Parquet, or JSON.
- Catch schema mismatches with typed bindings and investigate dropped events in the dashboard.

#### Basin Catalog

[Basin Catalog](https://developers.cloudflare.com/basin-catalog/), formerly R2 Data Catalog, manages and automatically maintains [Apache Iceberg tables ↗︎](https://iceberg.apache.org/) to keep them fast, cost-efficient, and accessible to any compatible query engine. With Basin Catalog you can:

- Connect DuckDB, Spark, Snowflake, or PyIceberg to the same tables.
- Maintain growing tables with compaction, snapshot expiration, and manifest optimization.
- Share analytical data across tools and clouds without paying egress fees.

#### Basin SQL

[Basin SQL](https://developers.cloudflare.com/basin-sql/), formerly R2 SQL, is a serverless, distributed SQL engine for querying large Apache Iceberg tables in Basin Catalog without managing or scaling compute. With Basin SQL you can:

- Summarize and rank data with standard and approximate aggregates, grouping sets, and window functions.
- Combine and inspect datasets with joins, subqueries, common table expressions, set operations, schema discovery, and `EXPLAIN`.
- Transform strings, timestamps, JSON, and complex values with more than 190 functions.

#### Get started

To get started with creating an end-to-end data pipeline, run:

npmyarnpnpm

```
npx wrangler basin pipelines setup
```

```
yarn wrangler basin pipelines setup
```

```
pnpm wrangler basin pipelines setup
```

Or get started by referring to the [Basin getting started guide](https://developers.cloudflare.com/basin/get-started/guide/).

Note

Existing Cloudflare Pipelines, R2 Data Catalog, and R2 SQL resources and configurations will continue to work and will be deprecated over time.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-10-01-basin-ga/#page","headline":"Cloudflare Basin is now generally available","description":"Cloudflare Data Platform is now Basin, bringing generally available ingestion, Iceberg table management, and SQL analytics together on R2.","url":"https://developers.cloudflare.com/changelog/post/2026-10-01-basin-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-10-01-basin-ga/og.png?v=cb42c4b226f41dee","dateModified":"2026-10-01","datePublished":"2026-10-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
