---
description: The ip.src.metro_code field is now populated with DMA (Designated Market Area) data for IP geolocation.
title: Metro code field now available in Rules
image: https://developers.cloudflare.com/changelog/post/2026-01-12-dma-metro-code-field/og.png?v=9da7d1574631e4a4
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 12, 2026

## Metro code field now available in Rules

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-12-dma-metro-code-field/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The `ip.src.metro_code` field in the Ruleset Engine is now populated with DMA (Designated Market Area) data.

You can use this field to build rules that target traffic based on geographic market areas, enabling more granular location-based policies for your applications.

#### Field details

| Field | Type | Description |
| --- | --- | --- |
| `ip.src.metro_code` | String \| null | The metro code (DMA) of the incoming request's IP address. Returns the designated market area code for the client's location. |

Example filter expression:

```plaintext
ip.src.metro_code eq "501"
```

For more information, refer to the [Fields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/ip.src.metro_code/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-12-dma-metro-code-field/#page","headline":"Metro code field now available in Rules","description":"The ip.src.metro_code field is now populated with DMA (Designated Market Area) data for IP geolocation.","url":"https://developers.cloudflare.com/changelog/post/2026-01-12-dma-metro-code-field/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-12-dma-metro-code-field/og.png?v=9da7d1574631e4a4","dateModified":"2026-01-12","datePublished":"2026-01-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
