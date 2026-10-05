---
description: R2 storage buckets now automatically benefit from Smart Tiered Cache with intelligent Upper Tier selection.
title: Smart Tiered Cache automatically optimizes R2 caching
image: https://developers.cloudflare.com/changelog/post/2024-11-20-smart-tiered-cache-for-r2/og.png?v=9ec2cc9a6480bbad
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 20, 2024

## Smart Tiered Cache automatically optimizes R2 caching

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2024-11-20-smart-tiered-cache-for-r2/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now reduce latency and lower R2 egress costs automatically when using [Smart Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/) with [R2](https://developers.cloudflare.com/r2/). Cloudflare intelligently selects a tiered data center close to your R2 bucket location, creating an efficient caching topology without additional configuration.

#### How it works

When you enable [Smart Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/) for zones using [R2](https://developers.cloudflare.com/r2/) as an origin, Cloudflare automatically:

1. **Identifies your R2 bucket location**: Determines the geographical region where your R2 bucket is stored.
2. **Selects an optimal Upper Tier**: Chooses a data center close to your bucket as the common Upper Tier cache.
3. **Routes requests efficiently**: All cache misses in edge locations route through this Upper Tier before reaching R2.

#### Benefits

- **Automatic optimization**: No manual configuration required.
- **Lower egress costs**: Fewer requests to R2 reduce egress charges.
- **Improved hit ratio**: Common Upper Tier increases cache efficiency.
- **Reduced latency**: Upper Tier proximity to R2 minimizes fetch times.

#### Get started

To get started, enable [Smart Tiered Cache](https://developers.cloudflare.com/cache/how-to/tiered-cache/) on your zone using R2 as an origin.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-11-20-smart-tiered-cache-for-r2/#page","headline":"Smart Tiered Cache automatically optimizes R2 caching","description":"R2 storage buckets now automatically benefit from Smart Tiered Cache with intelligent Upper Tier selection.","url":"https://developers.cloudflare.com/changelog/post/2024-11-20-smart-tiered-cache-for-r2/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2024-11-20-smart-tiered-cache-for-r2/og.png?v=9ec2cc9a6480bbad","dateModified":"2024-11-20","datePublished":"2024-11-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
