---
description: Five new approximate functions for percentiles, medians, distinct counts, and top-k analysis on Apache Iceberg tables in R2 Data Catalog.
title: R2 SQL now supports approximate aggregation functions
image: https://developers.cloudflare.com/changelog/post/2026-02-09-approximate-aggregation-functions/og.png?v=e38f5bbf0055daa7
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 9, 2026

## R2 SQL now supports approximate aggregation functions

[Basin SQL](https://developers.cloudflare.com/basin-sql/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-09-approximate-aggregation-functions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

R2 SQL now supports five approximate aggregation functions for fast analysis of large datasets. These functions trade minor precision for improved performance on high-cardinality data.

#### New functions

- `APPROX_PERCENTILE_CONT(column, percentile)` — Returns the approximate value at a given percentile (0.0 to 1.0). Works on integer and decimal columns.
- `APPROX_PERCENTILE_CONT_WITH_WEIGHT(column, weight, percentile)` — Weighted percentile calculation where each row contributes proportionally to its weight column value.
- `APPROX_MEDIAN(column)` — Returns the approximate median. Equivalent to `APPROX_PERCENTILE_CONT(column, 0.5)`.
- `APPROX_DISTINCT(column)` — Returns the approximate number of distinct values. Works on any column type.
- `APPROX_TOP_K(column, k)` — Returns the `k` most frequent values with their counts as a JSON array.

All functions support `WHERE` filters. All except `APPROX_TOP_K` support `GROUP BY`.

#### Examples

```sql
-- Percentile analysis on revenue data
SELECT approx_percentile_cont(total_amount, 0.25),
       approx_percentile_cont(total_amount, 0.5),
       approx_percentile_cont(total_amount, 0.75)
FROM my_namespace.sales_data
```

```sql
-- Median per department
SELECT department, approx_median(total_amount)
FROM my_namespace.sales_data
GROUP BY department
```

```sql
-- Approximate distinct customers by region
SELECT region, approx_distinct(customer_id)
FROM my_namespace.sales_data
GROUP BY region
```

```sql
-- Top 5 most frequent departments
SELECT approx_top_k(department, 5)
FROM my_namespace.sales_data
```

```sql
-- Combine approximate and standard aggregations
SELECT COUNT(*),
       AVG(total_amount),
       approx_percentile_cont(total_amount, 0.5),
       approx_distinct(customer_id)
FROM my_namespace.sales_data
WHERE region = 'North'
```

For the full syntax and additional examples, refer to the [SQL reference](https://developers.cloudflare.com/basin-sql/sql-reference/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-09-approximate-aggregation-functions/#page","headline":"R2 SQL now supports approximate aggregation functions","description":"Five new approximate functions for percentiles, medians, distinct counts, and top-k analysis on Apache Iceberg tables in R2 Data Catalog.","url":"https://developers.cloudflare.com/changelog/post/2026-02-09-approximate-aggregation-functions/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-09-approximate-aggregation-functions/og.png?v=e38f5bbf0055daa7","dateModified":"2026-02-09","datePublished":"2026-02-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
