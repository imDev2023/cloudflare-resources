---
description: Use window functions, QUALIFY, SELECT DISTINCT, set operations, and exact aggregates in R2 SQL.
title: R2 SQL now supports window functions, DISTINCT, and set operations
image: https://developers.cloudflare.com/changelog/post/2026-06-21-window-functions-distinct-set-operations/og.png?v=5b1d355bbfa5e8c5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 22, 2026

## R2 SQL now supports window functions, DISTINCT, and set operations

[Basin SQL](https://developers.cloudflare.com/basin-sql/) [Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-21-window-functions-distinct-set-operations/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

R2 SQL now supports window functions, `SELECT DISTINCT`, set operations, and additional aggregates, making it easier to write analytical queries without preprocessing your data elsewhere.

[R2 SQL](https://developers.cloudflare.com/basin-sql/) is Cloudflare's serverless, distributed SQL engine for querying [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables stored in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/).

#### New capabilities

- **Window functions** — `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `PERCENT_RANK`, `CUME_DIST`, `NTILE`, `LAG`, `LEAD`, `FIRST_VALUE`, `LAST_VALUE`, `NTH_VALUE`, and aggregates with an `OVER (...)` clause, including `PARTITION BY` and explicit frames
- **QUALIFY** — filter rows based on a window function result
- **DISTINCT** — `SELECT DISTINCT`, `DISTINCT ON (...)`, and the `DISTINCT` modifier on aggregates such as `COUNT(DISTINCT ...)`
- **Set operations** — `UNION`, `UNION ALL`, `INTERSECT`, and `EXCEPT`
- **Grouping extensions** — `GROUPING SETS`, `ROLLUP`, and `CUBE`
- **Exact aggregates** — `MEDIAN`, `PERCENTILE_CONT`, `ARRAY_AGG`, and `STRING_AGG`

#### Examples

#### Rank rows with a window function

```sql
SELECT customer_id, region,
       ROW_NUMBER() OVER (PARTITION BY region ORDER BY total_amount DESC) AS rank_in_region
FROM my_namespace.sales_data
```

#### Filter with QUALIFY

```sql
SELECT customer_id, region, total_amount
FROM my_namespace.sales_data
QUALIFY ROW_NUMBER() OVER (PARTITION BY region ORDER BY total_amount DESC) <= 3
```

#### Combine tables with a set operation

```sql
SELECT customer_id FROM my_namespace.sales_data
EXCEPT
SELECT customer_id FROM my_namespace.archived_sales
```

The named `WINDOW` clause is not supported — inline the `OVER (...)` specification at each call site. For the full syntax reference, refer to the [SQL reference](https://developers.cloudflare.com/basin-sql/sql-reference/). For supported features and performance guidance, refer to [Limitations and best practices](https://developers.cloudflare.com/basin-sql/reference/limitations-best-practices/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-21-window-functions-distinct-set-operations/#page","headline":"R2 SQL now supports window functions, DISTINCT, and set operations","description":"Use window functions, QUALIFY, SELECT DISTINCT, set operations, and exact aggregates in R2 SQL.","url":"https://developers.cloudflare.com/changelog/post/2026-06-21-window-functions-distinct-set-operations/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-21-window-functions-distinct-set-operations/og.png?v=5b1d355bbfa5e8c5","dateModified":"2026-06-22","datePublished":"2026-06-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
