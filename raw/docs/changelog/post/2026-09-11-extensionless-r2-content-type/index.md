---
description: Index extensionless R2 objects by setting supported Content-Type metadata.
title: AI Search supports extensionless R2 objects with Content-Type metadata
image: https://developers.cloudflare.com/changelog/post/2026-09-11-extensionless-r2-content-type/og.png?v=a8a5f2e7b791e13c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 11, 2026

## AI Search supports extensionless R2 objects with Content-Type metadata

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-11-extensionless-r2-content-type/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Search can index R2 objects without filename extensions when they include supported `Content-Type` metadata. This supports object keys that do not include file extensions while preserving file-type validation during indexing.

For supported file types and Content-Type requirements, refer to [R2 data sources](https://developers.cloudflare.com/ai-search/configuration/data-source/r2/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-11-extensionless-r2-content-type/#page","headline":"AI Search supports extensionless R2 objects with Content-Type metadata","description":"Index extensionless R2 objects by setting supported Content-Type metadata.","url":"https://developers.cloudflare.com/changelog/post/2026-09-11-extensionless-r2-content-type/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-11-extensionless-r2-content-type/og.png?v=a8a5f2e7b791e13c","dateModified":"2026-09-11","datePublished":"2026-09-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
