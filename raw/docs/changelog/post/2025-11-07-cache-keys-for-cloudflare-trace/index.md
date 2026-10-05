---
description: View the specific cache key generated for requests to troubleshoot caching behavior and rules configuration.
title: Inspect Cache Keys with Cloudflare Trace
image: https://developers.cloudflare.com/changelog/post/2025-11-07-cache-keys-for-cloudflare-trace/og.png?v=fe25771ccb4cc866
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 7, 2025

## Inspect Cache Keys with Cloudflare Trace

[Cache / CDN](https://developers.cloudflare.com/cache/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-07-cache-keys-for-cloudflare-trace/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now see the exact cache key generated for any request directly in Cloudflare Trace. This visibility helps you troubleshoot cache hits and misses, and verify that your Custom Cache Keys — configured via Cache Rules or Page Rules — are working as intended.

Previously, diagnosing caching behavior required inferring the key from configuration settings. Now, you can confirm that your custom logic for headers, query strings, and device types is correctly applied.

Access Trace via the [dashboard](https://developers.cloudflare.com/rules/trace-request/how-to/#use-trace-in-the-dashboard) or [API](https://developers.cloudflare.com/api/resources/request_tracer/methods/trace/), either manually for ad-hoc debugging or automated as part of your quality-of-service monitoring.

#### Example scenario

If you have a Cache Rule that segments content based on a specific cookie (for example, `user_region`), run a Trace with that cookie present to confirm the `user_region` value appears in the resulting cache key.

The Trace response includes the cache key in the `cache` object:

```json
{
  "step_name": "request",
  "type": "cache",
  "matched": true,
  "public_name": "Cache Parameters",
  "cache": {
    "key": {
      "zone_id": "023e105f4ecef8ad9ca31a8372d0c353",
      "scheme": "https",
      "host": "example.com",
      "uri": "/images/hero.jpg"
    },
    "key_string": "023e105f4ecef8ad9ca31a8372d0c353::::https://example.com/images/hero.jpg:::::"
  }
}
```

#### Get started

To learn more, refer to the [Trace documentation](https://developers.cloudflare.com/rules/trace-request/) and our guide on [Custom Cache Keys](https://developers.cloudflare.com/cache/how-to/cache-keys/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-07-cache-keys-for-cloudflare-trace/#page","headline":"Inspect Cache Keys with Cloudflare Trace","description":"View the specific cache key generated for requests to troubleshoot caching behavior and rules configuration.","url":"https://developers.cloudflare.com/changelog/post/2025-11-07-cache-keys-for-cloudflare-trace/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-07-cache-keys-for-cloudflare-trace/og.png?v=fe25771ccb4cc866","dateModified":"2025-11-07","datePublished":"2025-11-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
