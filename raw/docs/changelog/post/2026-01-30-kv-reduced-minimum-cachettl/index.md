---
description: The minimum cacheTtl parameter has been reduced from 60 seconds to 30 seconds, enabling faster cache refreshes and more granular cache control.
title: Reduced minimum cache TTL for Workers KV to 30 seconds
image: https://developers.cloudflare.com/changelog/post/2026-01-30-kv-reduced-minimum-cachettl/og.png?v=2e0bfc3d7a1b60b7
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 30, 2026

## Reduced minimum cache TTL for Workers KV to 30 seconds

[KV](https://developers.cloudflare.com/kv/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-30-kv-reduced-minimum-cachettl/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The minimum `cacheTtl` parameter for Workers KV has been reduced from 60 seconds to 30 seconds. This change applies to both `get()` and `getWithMetadata()` methods.

This reduction allows you to maintain more up-to-date cached data and have finer-grained control over cache behavior. Applications requiring faster data refresh rates can now configure cache durations as low as 30 seconds instead of the previous 60-second minimum.

The `cacheTtl` parameter defines how long a KV result is cached at the global network location it is accessed from:

```js
// Read with custom cache TTL
const value = await env.NAMESPACE.get("my-key", {
	cacheTtl: 30, // Cache for minimum 30 seconds (previously 60)
});

// getWithMetadata also supports the reduced cache TTL
const valueWithMetadata = await env.NAMESPACE.getWithMetadata("my-key", {
	cacheTtl: 30, // Cache for minimum 30 seconds
});
```

The default cache TTL remains unchanged at 60 seconds. Upgrade to the latest version of Wrangler to be able to use 30 seconds `cacheTtl`.

This change affects all KV read operations using the binding API. For more information, consult the [Workers KV cache TTL documentation](https://developers.cloudflare.com/kv/api/read-key-value-pairs/#cachettl-parameter).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-30-kv-reduced-minimum-cachettl/#page","headline":"Reduced minimum cache TTL for Workers KV to 30 seconds","description":"The minimum cacheTtl parameter has been reduced from 60 seconds to 30 seconds, enabling faster cache refreshes and more granular cache control.","url":"https://developers.cloudflare.com/changelog/post/2026-01-30-kv-reduced-minimum-cachettl/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-30-kv-reduced-minimum-cachettl/og.png?v=2e0bfc3d7a1b60b7","dateModified":"2026-01-30","datePublished":"2026-01-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
