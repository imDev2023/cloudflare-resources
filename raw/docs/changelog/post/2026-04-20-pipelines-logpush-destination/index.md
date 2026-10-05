---
description: Send Cloudflare logs to Pipelines for SQL transformation and storage in R2 as Parquet or Apache Iceberg tables.
title: Cloudflare Pipelines as a Logpush destination
image: https://developers.cloudflare.com/changelog/post/2026-04-20-pipelines-logpush-destination/og.png?v=21980a737995c8cb
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 20, 2026

## Cloudflare Pipelines as a Logpush destination

[Logs](https://developers.cloudflare.com/logs/) [Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-20-pipelines-logpush-destination/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Logpush has traditionally been great at delivering Cloudflare logs to a variety of destinations in JSON format. While JSON is flexible and easily readable, it can be inefficient to store and query at scale.

With this release, you can now send your logs directly to [Pipelines](https://developers.cloudflare.com/basin-pipelines/) to ingest, transform, and store your logs in [R2](https://developers.cloudflare.com/r2/) as Parquet files or Apache Iceberg tables managed by [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/). This makes the data footprint more compact and more efficient at querying your logs instantly with [R2 SQL](https://developers.cloudflare.com/basin-sql/) or any other query engine that supports Apache Iceberg or Parquet.

#### Transform logs before storage

Pipelines SQL runs on each log record in-flight, so you can reshape your data before it is written. For example, you can drop noisy fields, redact sensitive values, or derive new columns:

```sql
INSERT INTO http_logs_sink
SELECT
  ClientIP,
  EdgeResponseStatus,
  to_timestamp_micros(EdgeStartTimestamp) AS event_time,
  upper(ClientRequestMethod) AS method,
  sha256(ClientIP) AS hashed_ip
FROM http_logs_stream
WHERE EdgeResponseStatus >= 400;
```

Pipelines SQL supports string functions, regex, hashing, JSON extraction, timestamp conversion, conditional expressions, and more. For the full list, refer to the [Pipelines SQL reference](https://developers.cloudflare.com/basin-pipelines/sql-reference/).

#### Get started

To configure Pipelines as a Logpush destination, refer to [Enable Cloudflare Pipelines](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/pipelines/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-20-pipelines-logpush-destination/#page","headline":"Cloudflare Pipelines as a Logpush destination","description":"Send Cloudflare logs to Pipelines for SQL transformation and storage in R2 as Parquet or Apache Iceberg tables.","url":"https://developers.cloudflare.com/changelog/post/2026-04-20-pipelines-logpush-destination/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-20-pipelines-logpush-destination/og.png?v=21980a737995c8cb","dateModified":"2026-04-20","datePublished":"2026-04-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
