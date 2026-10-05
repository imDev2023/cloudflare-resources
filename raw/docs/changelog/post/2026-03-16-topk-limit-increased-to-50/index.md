---
description: Vectorize increases the `topK` limit to 50 when queries return values or full metadata.
title: Return up to 50 query results with values or metadata
image: https://developers.cloudflare.com/changelog/post/2026-03-16-topk-limit-increased-to-50/og.png?v=0b90e1c989c709db
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 16, 2026

## Return up to 50 query results with values or metadata

[Vectorize](https://developers.cloudflare.com/vectorize/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-16-topk-limit-increased-to-50/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now set `topK` up to `50` when a Vectorize query returns values or full metadata. This raises the previous limit of `20` for queries that use `returnValues: true` or `returnMetadata: "all"`.

Use the higher limit when you need more matches in a single query response without dropping values or metadata. Refer to the [Vectorize API reference](https://developers.cloudflare.com/vectorize/reference/client-api/) for query options and current `topK` limits.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-16-topk-limit-increased-to-50/#page","headline":"Return up to 50 query results with values or metadata","description":"Vectorize increases the topK limit to 50 when queries return values or full metadata.","url":"https://developers.cloudflare.com/changelog/post/2026-03-16-topk-limit-increased-to-50/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-16-topk-limit-increased-to-50/og.png?v=0b90e1c989c709db","dateModified":"2026-03-16","datePublished":"2026-03-16","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
