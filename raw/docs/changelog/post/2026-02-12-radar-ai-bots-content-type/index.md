---
description: New content type dimension showing distribution of content types returned to AI crawlers
title: Content Type Dimension for AI Bots in Cloudflare Radar
image: https://developers.cloudflare.com/changelog/post/2026-02-12-radar-ai-bots-content-type/og.png?v=d5398b62c1e9c1b7
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 12, 2026

## Content Type Dimension for AI Bots in Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-12-radar-ai-bots-content-type/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) now includes content type insights for AI bot and crawler traffic. The new `content_type` dimension and filter shows the distribution of content types returned to AI crawlers, grouped by MIME type category.

The content type dimension and filter are available via the following API endpoints:

- [`/ai/bots/summary/content_type`](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/bots/methods/summary_v2/)
- [`/ai/bots/timeseries_groups/content_type`](https://developers.cloudflare.com/api/resources/radar/subresources/ai/subresources/bots/methods/timeseries_groups/)

Content type categories:

- **HTML** - Web pages ( `text/html`)
- **Images** - All image formats ( `image/*`)
- **JSON** - JSON data and API responses ( `application/json`, `*+json`)
- **JavaScript** - Scripts ( `application/javascript`, `text/javascript`)
- **CSS** - Stylesheets ( `text/css`)
- **Plain Text** - Unformatted text ( `text/plain`)
- **Fonts** - Web fonts ( `font/*`, `application/font-*`)
- **XML** - XML documents and feeds ( `text/xml`, `application/xml`, `application/rss+xml`, `application/atom+xml`)
- **YAML** - Configuration files ( `text/yaml`, `application/yaml`)
- **Video** - Video content and streaming ( `video/*`, `application/ogg`, `*mpegurl`)
- **Audio** - Audio content ( `audio/*`)
- **Markdown** - Markdown documents ( `text/markdown`)
- **Documents** - PDFs, Office documents, ePub, CSV ( `application/pdf`, `application/msword`, `text/csv`)
- **Binary** - Executables, archives, WebAssembly ( `application/octet-stream`, `application/zip`, `application/wasm`)
- **Serialization** - Binary API formats ( `application/protobuf`, `application/grpc`, `application/msgpack`)
- **Other** - All other content types

Additionally, individual [bot information pages ↗︎](https://radar.cloudflare.com/bots/directory/gptbot) now display content type distribution for AI crawlers that exist in both the Verified Bots and AI Bots datasets.

![Screenshot of the Content Type Distribution chart on the AI Insights page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1600,height=874,format=webp/_astro/ai-bots-content-type.B7xP9p4S.png)

Check out the [AI Insights page ↗︎](https://radar.cloudflare.com/ai-insights#content-type) to explore the data.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-12-radar-ai-bots-content-type/#page","headline":"Content Type Dimension for AI Bots in Cloudflare Radar","description":"New content type dimension showing distribution of content types returned to AI crawlers","url":"https://developers.cloudflare.com/changelog/post/2026-02-12-radar-ai-bots-content-type/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-12-radar-ai-bots-content-type/og.png?v=d5398b62c1e9c1b7","dateModified":"2026-02-12","datePublished":"2026-02-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
