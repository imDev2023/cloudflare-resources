---
description: Workers Analytics Engine's SQL API now supports SQL's HAVING and LIKE features
title: Workers Analytics Engine SQL now supports filtering using HAVING and LIKE
image: https://developers.cloudflare.com/changelog/post/2026-01-07-analytics-engine-support-for-like-and-having/og.png?v=ae39d6ba9b613211
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 7, 2026

## Workers Analytics Engine SQL now supports filtering using HAVING and LIKE

[Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-07-analytics-engine-support-for-like-and-having/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now use the `HAVING` clause and `LIKE` pattern matching operators in [Workers Analytics Engine ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/).

Workers Analytics Engine allows you to ingest and store high-cardinality data at scale and query your data through a simple SQL API.

#### Filtering using `HAVING`

The `HAVING` clause complements the `WHERE` clause by enabling you to filter groups based on aggregate values. While `WHERE` filters rows before aggregation, `HAVING` filters groups after aggregation is complete.

You can use `HAVING` to filter groups where the average exceeds a threshold:

```sql
SELECT
    blob1 AS probe_name,
    avg(double1) AS average_temp
FROM temperature_readings
GROUP BY probe_name
HAVING average_temp > 10
```

You can also filter groups based on aggregates such as the number of items in the group:

```sql
SELECT
    blob1 AS probe_name,
    count() AS num_readings
FROM temperature_readings
GROUP BY probe_name
HAVING num_readings > 100
```

#### Pattern matching using `LIKE`

The new pattern matching operators enable you to search for strings that match specific patterns using wildcard characters:

- `LIKE` - case-sensitive pattern matching
- `NOT LIKE` - case-sensitive pattern exclusion
- `ILIKE` - case-insensitive pattern matching
- `NOT ILIKE` - case-insensitive pattern exclusion

Pattern matching supports two wildcard characters: `%` (matches zero or more characters) and `_` (matches exactly one character).

You can match strings starting with a prefix:

```sql
SELECT *
FROM logs
WHERE blob1 LIKE 'error%'
```

You can also match file extensions (case-insensitive):

```sql
SELECT *
FROM requests
WHERE blob2 ILIKE '%.jpg'
```

Another example is excluding strings containing specific text:

```sql
SELECT *
FROM events
WHERE blob3 NOT ILIKE '%debug%'
```

#### Ready to get started?

Learn more about the [`HAVING` clause](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/statements/#having-clause) or [pattern matching operators](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/operators/#pattern-matching-operators) in the Workers Analytics Engine SQL reference documentation.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-07-analytics-engine-support-for-like-and-having/#page","headline":"Workers Analytics Engine SQL now supports filtering using HAVING and LIKE","description":"Workers Analytics Engine's SQL API now supports SQL's HAVING and LIKE features","url":"https://developers.cloudflare.com/changelog/post/2026-01-07-analytics-engine-support-for-like-and-having/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-07-analytics-engine-support-for-like-and-having/og.png?v=ae39d6ba9b613211","dateModified":"2026-01-07","datePublished":"2026-01-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
