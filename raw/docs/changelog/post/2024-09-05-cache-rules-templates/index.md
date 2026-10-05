---
description: Pre-built templates in the Cloudflare dashboard make it easy to create optimized cache rules instantly.
title: One-click Cache Rules templates now available
image: https://developers.cloudflare.com/changelog/post/2024-09-05-cache-rules-templates/og.png?v=c84b3838f025819e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 5, 2024

## One-click Cache Rules templates now available

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2024-09-05-cache-rules-templates/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now create optimized cache rules instantly with **one-click templates**, eliminating the complexity of manual rule configuration.

#### How it works

1. Navigate to **Rules** > **Templates** in your Cloudflare dashboard.
2. Select a template for your use case.
3. Click to apply the template with sensible defaults.
4. Customize as needed for your specific requirements.

#### Available cache templates

- **Cache everything**: Adjust the cache level for all requests.
- **Bypass cache for everything**: Bypass cache for all requests.
- **Cache default file extensions**: Replicate Page Rules caching behavior by making only default extensions eligible for cache.
- **Bypass cache on cookie**: Bypass cache for requests containing specific cookies.
- **Set edge cache time**: Cache responses with status code between 200 and 599 on the Cloudflare edge.
- **Set browser cache time**: Adjust how long a browser should cache a resource.

#### Get started

To get started, go to [**Rules > Templates** ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/caching/cache-rules) in the dashboard. For more information, refer to the [Cache Rules documentation](https://developers.cloudflare.com/cache/how-to/cache-rules/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-09-05-cache-rules-templates/#page","headline":"One-click Cache Rules templates now available","description":"Pre-built templates in the Cloudflare dashboard make it easy to create optimized cache rules instantly.","url":"https://developers.cloudflare.com/changelog/post/2024-09-05-cache-rules-templates/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2024-09-05-cache-rules-templates/og.png?v=c84b3838f025819e","dateModified":"2024-09-05","datePublished":"2024-09-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
