---
description: Mark cached content as stale so Cloudflare revalidates it with your origin and reuses content that has not changed.
title: Invalidate cached content instead of purging it
image: https://developers.cloudflare.com/changelog/post/2026-09-28-cache-invalidation/og.png?v=811ceca1b7927686
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 28, 2026

## Invalidate cached content instead of purging it

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-28-cache-invalidation/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now invalidate cached content instead of purging it. Invalidation marks matching content as stale. On the next request, Cloudflare revalidates the content with your origin. If your origin responds with `304 Not Modified`, Cloudflare reuses the cached content instead of downloading it again.

Use invalidation to refresh a group of assets when only some of them have changed. For example, invalidate all content that shares a cache tag. Cloudflare reuses unchanged assets instead of downloading them again. This requires your origin to return an `ETag` or `Last-Modified` header and support conditional requests.

Invalidation supports the same selectors as purge: URLs, cache tags, hostnames, URL prefixes, and everything. To invalidate content, send a `POST` request to the new `invalidate_cache` endpoint:

```bash
curl --request POST \
  "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/invalidate_cache" \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{"tags":["product-images"]}'
```

In the dashboard, use **Invalidate Cache** on the **Caching** > **Configuration** page.

Your cache settings determine whether Cloudflare serves stale content while it revalidates. Cloudflare can also serve invalidated content stale if your origin returns a `5xx` error or cannot be reached. To stop serving cached content, purge it instead.

Invalidation requests count toward the same [rate limits](https://developers.cloudflare.com/cache/guides/invalidate-cache/#limits) as purge requests.

Purge behavior for Cache Reserve also changes with this release. For details, refer to [Cache Reserve purge behavior](https://developers.cloudflare.com/cache/advanced-configuration/cache-reserve/#purge-behavior).

For more information, refer to [Invalidate cached content](https://developers.cloudflare.com/cache/guides/invalidate-cache/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-28-cache-invalidation/#page","headline":"Invalidate cached content instead of purging it","description":"Mark cached content as stale so Cloudflare revalidates it with your origin and reuses content that has not changed.","url":"https://developers.cloudflare.com/changelog/post/2026-09-28-cache-invalidation/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-28-cache-invalidation/og.png?v=811ceca1b7927686","dateModified":"2026-09-28","datePublished":"2026-09-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
