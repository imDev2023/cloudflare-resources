---
description: Workers KV adds new storage providers on Cloudflare's infrastructure, delivering significant latency improvements with p95 latency reduced by 67% and p99 by 29%.
title: Workers KV completes hybrid storage provider rollout for improved performance, fault-tolerance
image: https://developers.cloudflare.com/changelog/post/2025-08-22-kv-performance-improvements/og.png?v=4fceba58c0cbd2cb
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 22, 2025

## Workers KV completes hybrid storage provider rollout for improved performance, fault-tolerance

[KV](https://developers.cloudflare.com/kv/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-22-kv-performance-improvements/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers KV has completed rolling out performance improvements across all KV namespaces, providing a significant latency reduction on read operations for all KV users. This is due to architectural changes to KV's underlying storage infrastructure, which introduces a new metadata later and substantially improves redundancy.

![Workers KV latency improvements showing P95 and P99 performance gains in Europe, Asia, Africa and Middle East regions as measured within KV's internal storage gateway worker.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1486,height=796,format=webp/_astro/kv-hybrid-providers-performance-improvements.D6MBO22S.png)

#### Performance improvements

The new hybrid architecture delivers substantial latency reductions throughout Europe, Asia, Middle East, Africa regions. Over the past 2 weeks, we have observed the following:

- **p95 latency**: Reduced from \~150ms to \~50ms (67% decrease)
- **p99 latency**: Reduced from \~350ms to \~250ms (29% decrease)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-22-kv-performance-improvements/#page","headline":"Workers KV completes hybrid storage provider rollout for improved performance, fault-tolerance","description":"Workers KV adds new storage providers on Cloudflare's infrastructure, delivering significant latency improvements with p95 latency reduced by 67% and p99 by 29%.","url":"https://developers.cloudflare.com/changelog/post/2025-08-22-kv-performance-improvements/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-22-kv-performance-improvements/og.png?v=4fceba58c0cbd2cb","dateModified":"2025-08-22","datePublished":"2025-08-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
