---
description: Increase cacheability with the ability to modify cache-control directives, manage cache tags, or strip Set-Cookie headers from origin responses before they are cached.
title: Cache Response Rules
image: https://developers.cloudflare.com/changelog/post/2026-03-24-cache-response-rules/og.png?v=89f62f658424aafc
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 24, 2026

## Cache Response Rules

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-24-cache-response-rules/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now control how Cloudflare handles origin responses without changing your origin. Cache Response Rules let you modify `Cache-Control` directives, manage cache tags, and strip headers like `Set-Cookie` from origin responses *before* they reach Cloudflare's cache. Whether traffic is cached or passed through dynamically, these rules give you control over origin response behavior that was previously out of reach.

#### What changed

Cache Rules previously only operated on request attributes. Cache Response Rules introduce a new response phase that evaluates origin responses and lets you act on them before caching. You can now:

- **Modify `Cache-Control` directives**: Set or remove individual directives like `no-store`, `no-cache`, `max-age`, `s-maxage`, `stale-while-revalidate`, `immutable`, and more. For example, remove a `no-cache` directive your origin sends so Cloudflare can cache the asset, or set an `s-maxage` to control how long Cloudflare stores it.
- **Set a different browser `Cache-Control`**: Send a different `Cache-Control` header downstream to browsers and other clients than what Cloudflare uses internally, giving you independent control over edge and browser caching strategies.
- **Manage cache tags**: Add, set, or remove cache tags on responses, including converting tags from another CDN's header format into Cloudflare's `Cache-Tag` header. This is especially useful if you are migrating from a CDN that uses a different tag header or delimiter.
- **Strip headers that block caching**: Remove `Set-Cookie`, `ETag`, or `Last-Modified` headers from origin responses before caching, so responses that would otherwise be treated as uncacheable can be stored and served from cache.

#### Benefits

- **No origin changes required**: Fix caching behavior entirely from Cloudflare, even when your origin configuration is locked down or managed by a different team.
- **Simpler CDN migration**: Match caching behavior from other CDN providers without rewriting your origin. Translate cache tag formats and override directives that do not align with Cloudflare's defaults.
- **Native support, fewer workarounds**: Functionality that previously required workarounds is now built into Cache Rules with full Tiered Cache compatibility.
- **Fine-grained control**: Use expressions to match on request and response attributes, then apply precise cache settings per rule. Rules are stackable and composable with existing Cache Rules.

#### Get started

Configure Cache Response Rules in the [Cloudflare dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/:zone/caching/cache-rules) under **Caching** > **Cache Rules**, or via the [Rulesets API ↗︎](https://developers.cloudflare.com/ruleset-engine/rulesets-api/). For more details, refer to the [Cache Rules documentation ↗︎](https://developers.cloudflare.com/cache/how-to/cache-response-rules/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-24-cache-response-rules/#page","headline":"Cache Response Rules","description":"Increase cacheability with the ability to modify cache-control directives, manage cache tags, or strip Set-Cookie headers from origin responses before they are cached.","url":"https://developers.cloudflare.com/changelog/post/2026-03-24-cache-response-rules/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-24-cache-response-rules/og.png?v=89f62f658424aafc","dateModified":"2026-03-24","datePublished":"2026-03-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
