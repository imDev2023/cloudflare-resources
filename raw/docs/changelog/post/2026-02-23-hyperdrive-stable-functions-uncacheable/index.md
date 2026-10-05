---
description: Hyperdrive marks queries containing STABLE PostgreSQL functions as uncacheable, preventing stale cached results.
title: Hyperdrive no longer caches queries using STABLE PostgreSQL functions
image: https://developers.cloudflare.com/changelog/post/2026-02-23-hyperdrive-stable-functions-uncacheable/og.png?v=c41d9800b54a5229
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 23, 2026

## Hyperdrive no longer caches queries using STABLE PostgreSQL functions

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-23-hyperdrive-stable-functions-uncacheable/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Hyperdrive now treats queries containing PostgreSQL `STABLE` functions as uncacheable, in addition to `VOLATILE` functions.

Previously, only functions [that PostgreSQL categorizes ↗︎](https://www.postgresql.org/docs/current/xfunc-volatility.html) as `VOLATILE` (for example, `RANDOM()`, `LASTVAL()`) were detected as uncacheable. `STABLE` functions (for example, `NOW()`, `CURRENT_TIMESTAMP`, `CURRENT_DATE`) were incorrectly allowed to be cached.

Because `STABLE` functions can return different results across different SQL statements within the same transaction, caching their results could serve stale or incorrect data. This change aligns Hyperdrive's caching behavior with PostgreSQL's function volatility semantics.

If your queries use `STABLE` functions, and you were relying on them being cached, move the function call to your application code and pass the result as a query parameter. For example, instead of `WHERE created_at > NOW()`, compute the timestamp in your Worker and pass it as `WHERE created_at > $1`.

Hyperdrive uses text-based pattern matching to detect uncacheable functions. References to function names like `NOW()` in SQL comments also cause the query to be marked as uncacheable.

For more information, refer to [Query caching](https://developers.cloudflare.com/hyperdrive/concepts/query-caching/) and [Troubleshoot and debug](https://developers.cloudflare.com/hyperdrive/observability/troubleshooting/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-23-hyperdrive-stable-functions-uncacheable/#page","headline":"Hyperdrive no longer caches queries using STABLE PostgreSQL functions","description":"Hyperdrive marks queries containing STABLE PostgreSQL functions as uncacheable, preventing stale cached results.","url":"https://developers.cloudflare.com/changelog/post/2026-02-23-hyperdrive-stable-functions-uncacheable/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-23-hyperdrive-stable-functions-uncacheable/og.png?v=c41d9800b54a5229","dateModified":"2026-02-23","datePublished":"2026-02-23","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
