---
description: Vectorize indexes now support up to 20 million vectors.
title: Vectorize indexes now support up to 20 million vectors
image: https://developers.cloudflare.com/changelog/post/2026-08-04-index-capacity-20-million/og.png?v=6d05137492132a09
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 4, 2026

## Vectorize indexes now support up to 20 million vectors

[Vectorize](https://developers.cloudflare.com/vectorize/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-04-index-capacity-20-million/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now store up to 20 million vectors in a single Vectorize index, doubling the previous limit of 10 million vectors. This enables larger-scale semantic search, recommendation systems, and retrieval-augmented generation (RAG) applications without splitting data across multiple indexes.

Vectorize continues to support indexes with up to 1,536 dimensions per vector at 32-bit precision. Refer to the [Vectorize limits documentation](https://developers.cloudflare.com/vectorize/platform/limits/) for complete details.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-04-index-capacity-20-million/#page","headline":"Vectorize indexes now support up to 20 million vectors","description":"Vectorize indexes now support up to 20 million vectors.","url":"https://developers.cloudflare.com/changelog/post/2026-08-04-index-capacity-20-million/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-04-index-capacity-20-million/og.png?v=6d05137492132a09","dateModified":"2026-08-04","datePublished":"2026-08-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
