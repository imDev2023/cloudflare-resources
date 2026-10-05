---
description: Query JSON data, analyze query plans programmatically, and query unpartitioned Iceberg tables
title: R2 SQL adds JSON functions, EXPLAIN FORMAT JSON, and unpartitioned table support
image: https://developers.cloudflare.com/changelog/post/2026-04-20-r2-sql-json-functions-explain-format/og.png?v=82c659ea477f568e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 20, 2026

## R2 SQL adds JSON functions, EXPLAIN FORMAT JSON, and unpartitioned table support

[Basin SQL](https://developers.cloudflare.com/basin-sql/) [Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-20-r2-sql-json-functions-explain-format/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[R2 SQL](https://developers.cloudflare.com/basin-sql/) is Cloudflare's serverless, distributed, analytics query engine for querying [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables stored in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/).

R2 SQL now supports functions for querying JSON data stored in Apache Iceberg tables, an easier way to parse query plans with `EXPLAIN FORMAT JSON`, and querying tables without partition keys stored in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/).

JSON functions extract and manipulate JSON values directly in SQL without client-side processing:

```sql
SELECT
  json_get_str(doc, 'name') AS name,
  json_get_int(doc, 'user', 'profile', 'level') AS level,
  json_get_bool(doc, 'active') AS is_active
FROM my_namespace.sales_data
WHERE json_contains(doc, 'email')
```

For a full list of available functions, refer to [JSON functions](https://developers.cloudflare.com/basin-sql/sql-reference/scalar-functions/#json-functions).

`EXPLAIN FORMAT JSON` returns query execution plans as structured JSON for programmatic analysis and observability integrations:

```bash
npx wrangler r2 sql query "${WAREHOUSE}" "EXPLAIN FORMAT JSON SELECT * FROM logpush.requests LIMIT 10;"

┌──────────────────────────────────────┐
│ plan                                 │
├──────────────────────────────────────┤
│ {                                    │
│   "name": "CoalescePartitionsExec",  │
│   "output_partitions": 1,            │
│   "rows": 10,                        │
│   "size_approx": "310B",             │
│   "children": [                      │
│     {                                │
│       "name": "DataSourceExec",      │
│       "output_partitions": 4,        │
│       "rows": 28951,                 │
│       "size_approx": "900.0KB",      │
│       "table": "logpush.requests",   │
│       "files": 7,                    │
│       "bytes": 900019,               │
│       "projection": [                │
│         "__ingest_ts",               │
│         "CPUTimeMs",                 │
│         "DispatchNamespace",         │
│         "Entrypoint",                │
│         "Event",                     │
│         "EventTimestampMs",          │
│         "EventType",                 │
│         "Exceptions",                │
│         "Logs",                      │
│         "Outcome",                   │
│         "ScriptName",                │
│         "ScriptTags",                │
│         "ScriptVersion",             │
│         "WallTimeMs"                 │
│       ],                             │
│       "limit": 10                    │
│     }                                │
│   ]                                  │
│ }                                    │
└──────────────────────────────────────┘
```

For more details, refer to [EXPLAIN](https://developers.cloudflare.com/basin-sql/sql-reference/#explain).

Unpartitioned Iceberg tables can now be queried directly, which is useful for smaller datasets or data without natural time dimensions. For tables with more than 1000 files, partitioning is still recommended for better performance.

Refer to [Limitations and best practices](https://developers.cloudflare.com/basin-sql/reference/limitations-best-practices/) for the latest guidance on using R2 SQL.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-20-r2-sql-json-functions-explain-format/#page","headline":"R2 SQL adds JSON functions, EXPLAIN FORMAT JSON, and unpartitioned table support","description":"Query JSON data, analyze query plans programmatically, and query unpartitioned Iceberg tables","url":"https://developers.cloudflare.com/changelog/post/2026-04-20-r2-sql-json-functions-explain-format/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-20-r2-sql-json-functions-explain-format/og.png?v=82c659ea477f568e","dateModified":"2026-04-20","datePublished":"2026-04-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
