---
description: Enterprise Bot Management customers can control whether Cloudflare uses JavaScript Detections API results.
title: Control JavaScript Detections API results
image: https://developers.cloudflare.com/changelog/post/2026-09-16-jsd-api-results/og.png?v=f2656dfb299ccc4a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 16, 2026

## Control JavaScript Detections API results

[Bots](https://developers.cloudflare.com/bots/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-16-jsd-api-results/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Enterprise Bot Management customers can control whether Cloudflare uses results created through the JavaScript Detections API for bot scoring and detections.

Turn **JavaScript Detections for API traffic** on or off in **Security** > **Settings**. You can also configure the zone through the Bot Management API by setting `jsd_api_results_enabled`:

```json
{
	"jsd_api_results_enabled": true
}
```

This setting is separate from zone-wide script injection. When it is off, the API script can still execute and return `success` to the callback, but Cloudflare does not consume the result.

For more information, refer to [JavaScript Detections](https://developers.cloudflare.com/cloudflare-challenges/challenge-types/javascript-detections/#api).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-16-jsd-api-results/#page","headline":"Control JavaScript Detections API results","description":"Enterprise Bot Management customers can control whether Cloudflare uses JavaScript Detections API results.","url":"https://developers.cloudflare.com/changelog/post/2026-09-16-jsd-api-results/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-16-jsd-api-results/og.png?v=f2656dfb299ccc4a","dateModified":"2026-09-16","datePublished":"2026-09-16","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
