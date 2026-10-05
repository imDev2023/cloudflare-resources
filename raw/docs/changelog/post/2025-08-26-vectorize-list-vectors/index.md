---
description: Enumerate all vector identifiers in your Vectorize indexes for bulk operations, auditing, and data migration.
title: List all vectors in a Vectorize index with the new list-vectors operation
image: https://developers.cloudflare.com/changelog/post/2025-08-26-vectorize-list-vectors/og.png?v=254b1a000dbea795
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 26, 2025

## List all vectors in a Vectorize index with the new list-vectors operation

[Vectorize](https://developers.cloudflare.com/vectorize/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-26-vectorize-list-vectors/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now list all vector identifiers in a Vectorize index using the new `list-vectors` operation. This enables bulk operations, auditing, and data migration workflows through paginated requests that maintain snapshot consistency.

The operation is available via Wrangler CLI and REST API. Refer to the [list-vectors best practices guide](https://developers.cloudflare.com/vectorize/best-practices/list-vectors/) for detailed usage guidance.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-26-vectorize-list-vectors/#page","headline":"List all vectors in a Vectorize index with the new list-vectors operation","description":"Enumerate all vector identifiers in your Vectorize indexes for bulk operations, auditing, and data migration.","url":"https://developers.cloudflare.com/changelog/post/2025-08-26-vectorize-list-vectors/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-26-vectorize-list-vectors/og.png?v=254b1a000dbea795","dateModified":"2025-08-26","datePublished":"2025-08-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
