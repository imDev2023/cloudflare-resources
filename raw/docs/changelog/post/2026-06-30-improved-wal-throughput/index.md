---
description: Improvements to Vectorize WAL throughput reduce p99 end-to-end latency for vector changes to under 2 minutes.
title: Reduced end-to-end latency for vector changes
image: https://developers.cloudflare.com/changelog/post/2026-06-30-improved-wal-throughput/og.png?v=1fbd726a69e93265
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 1, 2026

## Reduced end-to-end latency for vector changes

[Vectorize](https://developers.cloudflare.com/vectorize/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-30-improved-wal-throughput/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We have greatly improved the throughput of the Vectorize [write-ahead log (WAL) ↗︎](https://blog.cloudflare.com/building-vectorize-a-distributed-vector-database-on-cloudflare-developer-platform/#the-wal). As a result, we have significantly reduced the end-to-end latency for a vector change to become queryable: median latency has dropped from 2 minutes to under 30 seconds, and p99 latency from 5 minutes to under 2 minutes.

![Vectorize p99 WAL batch end-to-end latency improved](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2542,height=1184,format=webp/_astro/vectorize-p99-wal-batch-end-to-end-latency-improvement.k8gtzlG7.png)

This means inserts, upserts, and deletes are reflected in query results faster, improving the freshness of semantic search, recommendation, and retrieval-augmented generation (RAG) workloads. You do not need to change your code or configuration to benefit from this improvement.

For more information, refer to the [Vectorize documentation](https://developers.cloudflare.com/vectorize/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-30-improved-wal-throughput/#page","headline":"Reduced end-to-end latency for vector changes","description":"Improvements to Vectorize WAL throughput reduce p99 end-to-end latency for vector changes to under 2 minutes.","url":"https://developers.cloudflare.com/changelog/post/2026-06-30-improved-wal-throughput/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-30-improved-wal-throughput/og.png?v=1fbd726a69e93265","dateModified":"2026-07-01","datePublished":"2026-07-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
