---
description: Run SQL queries against Apache Iceberg tables in R2 Data Catalog
title: Announcing R2 SQL
image: https://developers.cloudflare.com/changelog/post/2025-09-25-announcing-r2-sql-open-beta/og.png?v=274a7b97c26cd370
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 25, 2025

## Announcing R2 SQL

[Basin SQL](https://developers.cloudflare.com/basin-sql/) [Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-25-announcing-r2-sql-open-beta/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Today, we are launching the **open beta** for [R2 SQL](https://developers.cloudflare.com/basin-sql/): A serverless, distributed query engine that can efficiently analyze petabytes of data in [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables managed by [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/).

R2 SQL is ideal for exploring analytical and time-series data stored in R2, such as logs, events from [Pipelines](https://developers.cloudflare.com/basin-pipelines/), or clickstream and user behavior data.

If you already have a table in R2 Data Catalog, running queries is as simple as:

```bash
npx wrangler r2 sql query YOUR_WAREHOUSE "
SELECT
    user_id,
    event_type,
    value
FROM events.user_events
WHERE event_type = 'CHANGELOG' or event_type = 'BLOG'
  AND __ingest_ts > '2025-09-24T00:00:00Z'
ORDER BY __ingest_ts DESC
LIMIT 100"
```

To get started with R2 SQL, check out our [getting started guide](https://developers.cloudflare.com/basin-sql/get-started/) or learn more about supported features in the [SQL reference](https://developers.cloudflare.com/basin-sql/sql-reference/). For a technical deep dive into how we built R2 SQL, read our [blog post ↗︎](https://blog.cloudflare.com/r2-sql-deep-dive/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-25-announcing-r2-sql-open-beta/#page","headline":"Announcing R2 SQL","description":"Run SQL queries against Apache Iceberg tables in R2 Data Catalog","url":"https://developers.cloudflare.com/changelog/post/2025-09-25-announcing-r2-sql-open-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-25-announcing-r2-sql-open-beta/og.png?v=274a7b97c26cd370","dateModified":"2025-09-25","datePublished":"2025-09-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
