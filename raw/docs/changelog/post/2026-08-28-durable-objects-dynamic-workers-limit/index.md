---
description: Each Durable Object can use up to ten Dynamic Workers with in-flight requests.
title: Durable Objects can use up to ten Dynamic Workers concurrently
image: https://developers.cloudflare.com/changelog/post/2026-08-28-durable-objects-dynamic-workers-limit/og.png?v=a29e394d49491ca2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 28, 2026

## Durable Objects can use up to ten Dynamic Workers concurrently

[Workers](https://developers.cloudflare.com/workers/) [Durable Objects](https://developers.cloudflare.com/durable-objects/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-28-durable-objects-dynamic-workers-limit/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/) can have up to ten distinct [Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/) with in-flight requests, increased from four. This limit applies across all concurrent requests to the same Durable Object because they share an input/output (I/O) context. Other Workers can have up to four distinct Dynamic Workers with in-flight requests per request.

Multiple in-flight requests to the same Dynamic Worker count as one toward this limit.

For more information, refer to [Dynamic Workers limits](https://developers.cloudflare.com/dynamic-workers/platform/limits/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-28-durable-objects-dynamic-workers-limit/#page","headline":"Durable Objects can use up to ten Dynamic Workers concurrently","description":"Each Durable Object can use up to ten Dynamic Workers with in-flight requests.","url":"https://developers.cloudflare.com/changelog/post/2026-08-28-durable-objects-dynamic-workers-limit/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-28-durable-objects-dynamic-workers-limit/og.png?v=a29e394d49491ca2","dateModified":"2026-08-28","datePublished":"2026-08-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
