---
description: Configure AS prepending on BYOIP prefixes for smoother traffic migration
title: Graceful withdrawal of BYOIP prefixes
image: https://developers.cloudflare.com/changelog/post/2025-06-30-graceful-byoip-withdrawal/og.png?v=bd50c06a0231c3f4
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 30, 2025

## Graceful withdrawal of BYOIP prefixes

[Magic Transit](https://developers.cloudflare.com/magic-transit/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-30-graceful-byoip-withdrawal/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Magic Transit customers can now configure AS prepending on their BYOIP prefixes advertised at the Cloudflare edge. This allows for smoother traffic migration and minimizes packet loss when changing providers.

AS prepending makes the Cloudflare route less preferred by increasing the AS path length. You can use this to gradually shift traffic away from Cloudflare before withdrawing a prefix, avoiding abrupt routing changes.

Prepending can be configured via the API or through BGP community values when peering with the Magic Transit routing table. For more information, refer to [Advertise prefixes](https://developers.cloudflare.com/magic-transit/how-to/advertise-prefixes/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-30-graceful-byoip-withdrawal/#page","headline":"Graceful withdrawal of BYOIP prefixes","description":"Configure AS prepending on BYOIP prefixes for smoother traffic migration","url":"https://developers.cloudflare.com/changelog/post/2025-06-30-graceful-byoip-withdrawal/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-30-graceful-byoip-withdrawal/og.png?v=bd50c06a0231c3f4","dateModified":"2025-06-30","datePublished":"2025-06-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
