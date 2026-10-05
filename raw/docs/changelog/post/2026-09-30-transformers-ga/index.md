---
description: Use SQL to filter, reshape, redact, and enrich Logpush records before delivery.
title: Transformers are now generally available
image: https://developers.cloudflare.com/changelog/post/2026-09-30-transformers-ga/og.png?v=7f1c217167eb4ef5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 30, 2026

## Transformers are now generally available

[Logpush](https://developers.cloudflare.com/logs/logpush/) [Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-30-transformers-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Transformers are now generally available for supported Logpush datasets on Free, Pro, Business, and Enterprise plans. Use SQL to filter records, reshape fields, redact sensitive values, compute new fields, or add metadata before Logpush delivers each batch.

Create and preview Transformers in Transformer Studio or through the Cloudflare API, then attach them to eligible account-scoped or zone-scoped Logpush jobs that use NDJSON output. Cloudflare validates each query against the dataset schema before saving it.

Each account includes 1 GB of transformation input per month. Additional input costs $0.04 per GB. For setup instructions, supported SQL, limits, and examples, refer to [Transformers](https://developers.cloudflare.com/logs/logpush/transformers/). For billing details, refer to [Logpush pricing](https://developers.cloudflare.com/logs/logpush/pricing/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-30-transformers-ga/#page","headline":"Transformers are now generally available","description":"Use SQL to filter, reshape, redact, and enrich Logpush records before delivery.","url":"https://developers.cloudflare.com/changelog/post/2026-09-30-transformers-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-30-transformers-ga/og.png?v=7f1c217167eb4ef5","dateModified":"2026-09-30","datePublished":"2026-09-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
