---
description: Enterprise customers can now shard cache using previously restricted accept*, referer, and user-agent headers.
title: Shard cache using custom cache key values
image: https://developers.cloudflare.com/changelog/post/2024-11-07-shard-cache-by-cache-key/og.png?v=80f022c475c786e4
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 7, 2024

## Shard cache using custom cache key values

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2024-11-07-shard-cache-by-cache-key/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Enterprise customers can now optimize cache hit ratios for content that varies by device, language, or referrer by **sharding cache** using up to ten values from previously restricted headers with [custom cache keys](https://developers.cloudflare.com/cache/how-to/cache-keys/).

#### How it works

When configuring [custom cache keys](https://developers.cloudflare.com/cache/how-to/cache-keys/), you can now include values from these headers to create distinct cache entries:

- **`accept*` headers** (for example, `accept`, `accept-encoding`, `accept-language`): Serve different cached versions based on content negotiation.
- **`referer` header**: Cache content differently based on the referring page or site.
- **`user-agent` header**: Maintain separate caches for different browsers, devices, or bots.

#### When to use cache sharding

- Content varies significantly by device type (mobile vs desktop).
- Different language or encoding preferences require distinct responses.
- Referrer-specific content optimization is needed.

#### Example configuration

```json
{
  "cache_key": {
    "custom_key": {
      "header": {
        "include": ["accept-language", "user-agent"],
        "check_presence": ["referer"]
      }
    }
  }
}
```

This configuration creates separate cache entries based on the `accept-language` and `user-agent` headers, while also considering whether the `referer` header is present.

#### Get started

To get started, refer to the [custom cache keys documentation](https://developers.cloudflare.com/cache/how-to/cache-keys/).

Note

While cache sharding can improve hit ratios for specific use cases, overly sharding your cache can reduce overall cache efficiency and negatively impact performance. Carefully evaluate whether sharding benefits your specific traffic patterns.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-11-07-shard-cache-by-cache-key/#page","headline":"Shard cache using custom cache key values","description":"Enterprise customers can now shard cache using previously restricted accept*, referer, and user-agent headers.","url":"https://developers.cloudflare.com/changelog/post/2024-11-07-shard-cache-by-cache-key/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2024-11-07-shard-cache-by-cache-key/og.png?v=80f022c475c786e4","dateModified":"2024-11-07","datePublished":"2024-11-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
