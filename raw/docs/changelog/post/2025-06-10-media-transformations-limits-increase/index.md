---
description: "Media Transformations now supports inputs up to 100MB and output videos as long as 1 minute.\n"
title: Increased limits for Media Transformations
image: https://developers.cloudflare.com/changelog/post/2025-06-10-media-transformations-limits-increase/og.png?v=afaca9474f999a74
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 10, 2025

## Increased limits for Media Transformations

[Stream](https://developers.cloudflare.com/stream/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-10-media-transformations-limits-increase/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We have increased the limits for [Media Transformations](https://developers.cloudflare.com/stream/transform-videos/):

- Input file size limit is now 100MB (was 40MB)
- Output video duration limit is now 1 minute (was 30 seconds)

Additionally, we have improved caching of the input asset, resulting in fewer requests to origin storage even when transformation options may differ.

For more information, learn about [Transforming Videos](https://developers.cloudflare.com/stream/transform-videos/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-10-media-transformations-limits-increase/#page","headline":"Increased limits for Media Transformations","description":"Media Transformations now supports inputs up to 100MB and output videos as long as 1 minute.","url":"https://developers.cloudflare.com/changelog/post/2025-06-10-media-transformations-limits-increase/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-10-media-transformations-limits-increase/og.png?v=afaca9474f999a74","dateModified":"2025-06-10","datePublished":"2025-06-10","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
