---
description: D1 now detects read-only queries and automatically attempts up to two retries to execute those queries in the event of failures with retryable errors.
title: D1 automatically retries read-only queries
image: https://developers.cloudflare.com/changelog/post/2025-09-11-d1-automatic-read-retries/og.png?v=3fd14af71c7838dd
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 11, 2025

## D1 automatically retries read-only queries

[D1](https://developers.cloudflare.com/d1/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-11-d1-automatic-read-retries/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

D1 now detects read-only queries and automatically attempts up to two retries to execute those queries in the event of failures with retryable errors. You can access the number of execution attempts in the returned [response metadata](https://developers.cloudflare.com/d1/worker-api/return-object/#d1result) property `total_attempts`.

At the moment, only read-only queries are retried, that is, queries containing only the following SQLite keywords: `SELECT`, `EXPLAIN`, `WITH`. Queries containing any [SQLite keyword ↗︎](https://sqlite.org/lang_keywords.html) that leads to database writes are not retried.

The retry success ratio among read-only retryable errors varies from 5% all the way up to 95%, depending on the underlying error and its duration (like network errors or other internal errors).

The retry success ratio among all retryable errors is lower, indicating that there are write-queries that could be retried. Therefore, we recommend D1 users to continue applying [retries in their own code](https://developers.cloudflare.com/d1/best-practices/retry-queries/) for queries that are not read-only but are idempotent according to the business logic of the application.

![D1 automatically query retries success ratio](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=946,format=webp/_astro/d1-auto-retry-success-ratio.yPw8B0tB.png)

D1 ensures that any retry attempt does not cause database writes, making the automatic retries safe from side-effects, even if a query causing changes slips through the read-only detection. D1 achieves this by checking for modifications after every query execution, and if any write occurred due to a retry attempt, the query is rolled back.

The read-only query detection heuristics are simple for now, and there is room for improvement to capture more cases of queries that can be retried, so this is just the beginning.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-11-d1-automatic-read-retries/#page","headline":"D1 automatically retries read-only queries","description":"D1 now detects read-only queries and automatically attempts up to two retries to execute those queries in the event of failures with retryable errors.","url":"https://developers.cloudflare.com/changelog/post/2025-09-11-d1-automatic-read-retries/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-11-d1-automatic-read-retries/og.png?v=3fd14af71c7838dd","dateModified":"2025-09-11","datePublished":"2025-09-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
