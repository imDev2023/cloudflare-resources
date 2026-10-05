---
description: AI Search supports larger custom metadata values within a shared 10 KiB metadata envelope for each vector.
title: Store larger custom metadata values in AI Search
image: https://developers.cloudflare.com/changelog/post/2026-08-25-larger-custom-metadata-values/og.png?v=dea166db3c4e365a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 25, 2026

## Store larger custom metadata values in AI Search

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-25-larger-custom-metadata-values/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

AI Search supports larger custom metadata values within a shared 10 KiB metadata envelope for each vector. The envelope includes AI Search system metadata and JSON overhead, so it is not a per-field limit. The first 64 UTF-8 bytes of each indexed string remain filterable.

For details, refer to [Metadata attributes](https://developers.cloudflare.com/ai-search/configuration/indexing/metadata/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-25-larger-custom-metadata-values/#page","headline":"Store larger custom metadata values in AI Search","description":"AI Search supports larger custom metadata values within a shared 10 KiB metadata envelope for each vector.","url":"https://developers.cloudflare.com/changelog/post/2026-08-25-larger-custom-metadata-values/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-25-larger-custom-metadata-values/og.png?v=dea166db3c4e365a","dateModified":"2026-08-25","datePublished":"2026-08-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
