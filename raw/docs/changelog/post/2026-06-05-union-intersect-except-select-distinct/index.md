---
description: Combine query results with set operations and eliminate duplicates with SELECT DISTINCT.
title: R2 SQL now supports UNION, INTERSECT, EXCEPT, and SELECT DISTINCT
image: https://developers.cloudflare.com/changelog/post/2026-06-05-union-intersect-except-select-distinct/og.png?v=fdee84c46fa2ff0c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 8, 2026

## R2 SQL now supports UNION, INTERSECT, EXCEPT, and SELECT DISTINCT

[Basin SQL](https://developers.cloudflare.com/basin-sql/) [Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-05-union-intersect-except-select-distinct/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[R2 SQL](https://developers.cloudflare.com/basin-sql/) now supports set operations (`UNION`, `INTERSECT`, `EXCEPT`) and `SELECT DISTINCT`, expanding the range of analytical queries you can run directly on [Apache Iceberg ↗︎](https://iceberg.apache.org/) tables in [R2 Data Catalog](https://developers.cloudflare.com/basin-catalog/).

#### Set operations

Combine the results of multiple `SELECT` statements:

- **`UNION`** — returns all rows from both queries, removing duplicates
- **`UNION ALL`** — returns all rows from both queries, including duplicates
- **`INTERSECT`** — returns only rows that appear in both queries
- **`EXCEPT`** — returns rows from the first query that do not appear in the second

```sql
-- Find zones that had either firewall blocks OR high-risk requests
SELECT zone_id FROM my_namespace.firewall_events WHERE action = 'block'
UNION
SELECT zone_id FROM my_namespace.http_requests WHERE risk_score > 0.8
```

```sql
-- Find zones with both firewall blocks AND high traffic
SELECT zone_id FROM my_namespace.firewall_events WHERE action = 'block'
INTERSECT
SELECT zone_id FROM my_namespace.http_requests
GROUP BY zone_id
HAVING COUNT(*) > 10000
```

```sql
-- Find enterprise zones that have not been compacted
SELECT zone_id FROM my_namespace.zones WHERE plan = 'enterprise'
EXCEPT
SELECT zone_id FROM my_namespace.compaction_history
```

#### Select distinct

Eliminate duplicate rows from query results:

```sql
SELECT DISTINCT region, department
FROM my_namespace.sales_data
WHERE total_amount > 1000
ORDER BY region, department
LIMIT 100
```

For large datasets where approximate results are acceptable, `approx_distinct()` remains a faster alternative for counting unique values.

For the full syntax reference, refer to the [SQL reference](https://developers.cloudflare.com/basin-sql/sql-reference/). For performance guidance, refer to [Limitations and best practices](https://developers.cloudflare.com/basin-sql/reference/limitations-best-practices/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-05-union-intersect-except-select-distinct/#page","headline":"R2 SQL now supports UNION, INTERSECT, EXCEPT, and SELECT DISTINCT","description":"Combine query results with set operations and eliminate duplicates with SELECT DISTINCT.","url":"https://developers.cloudflare.com/changelog/post/2026-06-05-union-intersect-except-select-distinct/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-05-union-intersect-except-select-distinct/og.png?v=fdee84c46fa2ff0c","dateModified":"2026-06-08","datePublished":"2026-06-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
