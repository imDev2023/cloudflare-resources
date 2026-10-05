---
description: Basin Pipelines streams can ingest up to 1 GB/s each, increased from the previous 5 MB/s limit.
title: Basin Pipelines ingest limit increased to 1 GB/s
image: https://developers.cloudflare.com/changelog/post/2026-10-01-stream-ingest-limit-increase/og.png?v=2e1614c76a62c3f4
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 1, 2026

## Basin Pipelines ingest limit increased to 1 GB/s

[Basin Pipelines](https://developers.cloudflare.com/basin-pipelines/) [Basin](https://developers.cloudflare.com/basin/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-01-stream-ingest-limit-increase/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Each [Basin Pipelines stream](https://developers.cloudflare.com/basin-pipelines/streams/) can now ingest up to 1 GB/s, increased from 5 MB/s.

The higher per-stream limit gives high-volume application events, telemetry, and logs more room to grow without splitting ingestion across streams solely to stay within the previous limit.

For the full list of stream, sink, and pipeline limits, refer to [Basin Pipelines limits](https://developers.cloudflare.com/basin-pipelines/platform/limits/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-10-01-stream-ingest-limit-increase/#page","headline":"Basin Pipelines ingest limit increased to 1 GB/s","description":"Basin Pipelines streams can ingest up to 1 GB/s each, increased from the previous 5 MB/s limit.","url":"https://developers.cloudflare.com/changelog/post/2026-10-01-stream-ingest-limit-increase/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-10-01-stream-ingest-limit-increase/og.png?v=2e1614c76a62c3f4","dateModified":"2026-10-01","datePublished":"2026-10-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
