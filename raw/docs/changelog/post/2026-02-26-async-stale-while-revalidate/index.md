---
description: The first request after cache expiry now receives stale content immediately with an UPDATING status while revalidation happens asynchronously, instead of blocking until the origin responds.
title: Asynchronous stale-while-revalidate
image: https://developers.cloudflare.com/changelog/post/2026-02-26-async-stale-while-revalidate/og.png?v=f391b3e5c83b684e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 26, 2026

## Asynchronous stale-while-revalidate

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-26-async-stale-while-revalidate/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare's [`stale-while-revalidate`](https://developers.cloudflare.com/cache/concepts/cache-control/#revalidation) support is now fully asynchronous. Previously, the first request for a stale (expired) asset in cache had to wait for an origin response, after which that visitor received a REVALIDATED or EXPIRED status. Now, the first request after the asset expires triggers revalidation in the background and immediately receives stale content with an UPDATING status. All following requests also receive stale content with an `UPDATING` status until the origin responds, after which subsequent requests receive fresh content with a `HIT` status.

`stale-while-revalidate` is a `Cache-Control` directive set by your origin server that allows Cloudflare to serve an expired cached asset while a fresh copy is fetched from the origin.

Asynchronous revalidation brings:

- **Lower latency**: No visitor is waiting for the origin when the asset is already in cache. Every request is served from cache during revalidation.
- **Consistent experience**: All visitors receive the same cached response during revalidation.
- **Reduced error exposure**: The first request is no longer vulnerable to origin timeouts or errors. All visitors receive a cached response while revalidation happens in the background.

#### Availability

This change is live for all Free, Pro, and Business zones. Approximately 75% of Enterprise zones have been migrated, with the remaining zones rolling out throughout the quarter.

#### Get started

To use this feature, make sure your origin includes the `stale-while-revalidate` directive in the `Cache-Control` header. Refer to the [Cache-Control documentation](https://developers.cloudflare.com/cache/concepts/cache-control/#revalidation) for details.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-26-async-stale-while-revalidate/#page","headline":"Asynchronous stale-while-revalidate","description":"The first request after cache expiry now receives stale content immediately with an UPDATING status while revalidation happens asynchronously, instead of blocking until the origin responds.","url":"https://developers.cloudflare.com/changelog/post/2026-02-26-async-stale-while-revalidate/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-26-async-stale-while-revalidate/og.png?v=f391b3e5c83b684e","dateModified":"2026-02-26","datePublished":"2026-02-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
