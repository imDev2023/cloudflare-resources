---
description: Purging by tag, hostname, prefix, or everything now forces a cache miss for Cache Reserve content instead of revalidating it. To keep revalidating content, use invalidation.
title: Purge now forces a cache miss for Cache Reserve content
image: https://developers.cloudflare.com/changelog/post/2026-09-28-cache-reserve-purge-behavior/og.png?v=7d0bb45fdbc98846
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 28, 2026

## Purge now forces a cache miss for Cache Reserve content

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-28-cache-reserve-purge-behavior/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Purge requests now force a cache miss for [Cache Reserve](https://developers.cloudflare.com/cache/advanced-configuration/cache-reserve/) content, regardless of purge type. Previously, purging by cache tag, hostname, prefix, or everything marked matching Cache Reserve content for revalidation. Purging by URL already removed content from Cache Reserve and is unchanged.

This change applies to purge requests from the API and the dashboard. Cache Reserve now handles purges the same way as the edge cache.

#### Cost impact

After a purge, the next request for affected content is a Cache Reserve miss. Your origin must deliver the content in full, even if it has not changed. Cloudflare then writes the content to Cache Reserve again, which is billed as a [Class A operation](https://developers.cloudflare.com/cache/advanced-configuration/cache-reserve/#pricing).

Purging by tag, hostname, prefix, or everything does not delete content from Cache Reserve right away. Matching content continues to incur storage costs until a later request replaces it or its retention period ends.

If you frequently purge Cache Reserve content by tag, hostname, prefix, or everything, review the effect on your origin egress and Cache Reserve usage.

#### Keep revalidating Cache Reserve content

To keep content in Cache Reserve and revalidate it instead, send the same request to the new `invalidate_cache` endpoint:

```bash
curl --request POST \
  "https://api.cloudflare.com/client/v4/zones/$ZONE_ID/invalidate_cache" \
  --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  --header "Content-Type: application/json" \
  --data '{"tags":["product-images"]}'
```

In the dashboard, use **Invalidate Cache** on the **Caching** > **Configuration** page.

If your origin responds with `304 Not Modified`, Cloudflare reuses the stored content instead of fetching it from your origin again. Compared with purging, invalidation reduces origin egress but not Cache Reserve operations. Updating the stored content after a `304` response is still a Class A operation. Invalidating by URL also updates the stored content when you send the request, which is a Class A operation.

Unlike the previous purge behavior, invalidation can serve stale content while it revalidates if your cache settings allow it. This applies only to copies in the edge cache, not to content served from Cache Reserve. Cloudflare can also serve invalidated content stale if your origin returns a `5xx` error or cannot be reached. For details, refer to [Invalidate cached content](https://developers.cloudflare.com/cache/guides/invalidate-cache/#stale-content-during-revalidation).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-28-cache-reserve-purge-behavior/#page","headline":"Purge now forces a cache miss for Cache Reserve content","description":"Purging by tag, hostname, prefix, or everything now forces a cache miss for Cache Reserve content instead of revalidating it. To keep revalidating content, use invalidation.","url":"https://developers.cloudflare.com/changelog/post/2026-09-28-cache-reserve-purge-behavior/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-28-cache-reserve-purge-behavior/og.png?v=7d0bb45fdbc98846","dateModified":"2026-09-28","datePublished":"2026-09-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
