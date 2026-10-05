---
description: Query Iceberg tables with CASE expressions, column aliases, scalar functions, statistical aggregates, and full struct/array/map support.
title: R2 SQL now supports over 190 new functions, expressions, and complex types
image: https://developers.cloudflare.com/changelog/post/2026-03-23-expanded-sql-functions-expressions-complex-types/og.png?v=667950dfbc25e92c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 23, 2026

## R2 SQL now supports over 190 new functions, expressions, and complex types

[Basin SQL](https://developers.cloudflare.com/basin-sql/) [Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-23-expanded-sql-functions-expressions-complex-types/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[R2 SQL](https://developers.cloudflare.com/basin-sql/) now supports an expanded SQL grammar so you can write richer analytical queries without exporting data. This release adds CASE expressions, column aliases, arithmetic in clauses, 163 scalar functions, 33 aggregate functions, EXPLAIN, Common Table Expressions (CTEs),and full struct/array/map access. R2 SQL is Cloudflare's serverless, distributed, analytics query engine for querying [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables stored in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/). This page documents the supported SQL syntax.

#### Highlights

- **Column aliases** — `SELECT col AS alias` now works in all clauses
- **CASE expressions** — conditional logic directly in SQL (searched and simple forms)
- **Scalar functions** — 163 new functions across math, string, datetime, regex, crypto, encoding, and type inspection categories
- **Aggregate functions** — statistical (variance, stddev, correlation, regression), bitwise, boolean, and positional aggregates join the existing basic and approximate functions
- **Complex types** — query struct fields with bracket notation, use 46 array functions, and extract map keys/values
- **Common table expressions (CTEs)** — use `WITH ... AS` to define named temporary result sets. Chained CTEs are supported. All CTEs must reference the same single table.
- **Full expression support** — arithmetic, type casting ( `CAST`, `TRY_CAST`, `::` shorthand), and `EXTRACT` in SELECT, WHERE, GROUP BY, HAVING, and ORDER BY

#### Examples

#### CASE expressions with statistical aggregates

```sql
SELECT source,
    CASE
        WHEN AVG(price) > 30 THEN 'premium'
        WHEN AVG(price) > 10 THEN 'mid-tier'
        ELSE 'budget'
    END AS tier,
    round(stddev(price), 2) AS price_volatility,
    approx_percentile_cont(price, 0.95) AS p95_price
FROM my_namespace.sales_data
GROUP BY source
```

#### Struct and array access

```sql
SELECT product_name,
    pricing['price'] AS price,
    array_to_string(tags, ', ') AS tag_list
FROM my_namespace.products
WHERE array_has(tags, 'Action')
ORDER BY pricing['price'] DESC
LIMIT 10
```

#### Chained CTEs with time-series analysis

```sql
WITH monthly AS (
    SELECT date_trunc('month', sale_timestamp) AS month,
        department,
        COUNT(*) AS transactions,
        round(AVG(total_amount), 2) AS avg_amount
    FROM my_namespace.sales_data
    WHERE sale_timestamp BETWEEN '2025-01-01T00:00:00Z' AND '2025-12-31T23:59:59Z'
    GROUP BY date_trunc('month', sale_timestamp), department
),
ranked AS (
    SELECT month, department, transactions, avg_amount,
        CASE
            WHEN avg_amount > 1000 THEN 'high-value'
            WHEN avg_amount > 500 THEN 'mid-value'
            ELSE 'standard'
        END AS tier
    FROM monthly
    WHERE transactions > 100
)
SELECT * FROM ranked
ORDER BY month, avg_amount DESC
```

For the full function reference and syntax details, refer to the [SQL reference](https://developers.cloudflare.com/basin-sql/sql-reference/). For limitations and best practices, refer to [Limitations and best practices](https://developers.cloudflare.com/basin-sql/reference/limitations-best-practices/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-23-expanded-sql-functions-expressions-complex-types/#page","headline":"R2 SQL now supports over 190 new functions, expressions, and complex types","description":"Query Iceberg tables with CASE expressions, column aliases, scalar functions, statistical aggregates, and full struct/array/map support.","url":"https://developers.cloudflare.com/changelog/post/2026-03-23-expanded-sql-functions-expressions-complex-types/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-23-expanded-sql-functions-expressions-complex-types/og.png?v=667950dfbc25e92c","dateModified":"2026-03-23","datePublished":"2026-03-23","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
