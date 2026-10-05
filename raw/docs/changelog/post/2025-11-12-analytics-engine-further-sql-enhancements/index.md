---
description: Workers Analytics Engine now supports more SQL functions for aggregation and for working with dates and times
title: More SQL aggregate, date and time functions available in Workers Analytics Engine
image: https://developers.cloudflare.com/changelog/post/2025-11-12-analytics-engine-further-sql-enhancements/og.png?v=a379771e0820363e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 12, 2025

## More SQL aggregate, date and time functions available in Workers Analytics Engine

[Workers Analytics Engine](https://developers.cloudflare.com/analytics/analytics-engine/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-12-analytics-engine-further-sql-enhancements/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now perform more powerful queries directly in [Workers Analytics Engine ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/) with a major expansion of our SQL function library.

Workers Analytics Engine allows you to ingest and store high-cardinality data at scale (such as custom analytics) and query your data through a simple SQL API.

Today, we've expanded Workers Analytics Engine's SQL capabilities with several new functions:

[**New aggregate functions:** ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/aggregate-functions/)

- `countIf()` - count the number of rows which satisfy a provided condition
- `sumIf()` - calculate a sum from rows which satisfy a provided condition
- `avgIf()` - calculate an average from rows which satisfy a provided condition

[**New date and time functions:** ↗︎](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/date-time-functions/)

- `toYear()`
- `toMonth()`
- `toDayOfMonth()`
- `toDayOfWeek()`
- `toHour()`
- `toMinute()`
- `toSecond()`
- `toStartOfYear()`
- `toStartOfMonth()`
- `toStartOfWeek()`
- `toStartOfDay()`
- `toStartOfHour()`
- `toStartOfFifteenMinutes()`
- `toStartOfTenMinutes()`
- `toStartOfFiveMinutes()`
- `toStartOfMinute()`
- `today()`
- `toYYYYMM()`

#### Ready to get started?

Whether you're building usage-based billing systems, customer analytics dashboards, or other custom analytics, these functions let you get the most out of your data. [Get started](https://developers.cloudflare.com/analytics/analytics-engine/get-started/) with Workers Analytics Engine and explore all available functions in our [SQL reference documentation](https://developers.cloudflare.com/analytics/analytics-engine/sql-reference/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-12-analytics-engine-further-sql-enhancements/#page","headline":"More SQL aggregate, date and time functions available in Workers Analytics Engine","description":"Workers Analytics Engine now supports more SQL functions for aggregation and for working with dates and times","url":"https://developers.cloudflare.com/changelog/post/2025-11-12-analytics-engine-further-sql-enhancements/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-12-analytics-engine-further-sql-enhancements/og.png?v=a379771e0820363e","dateModified":"2025-11-12","datePublished":"2025-11-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
