---
description: Magic WAN learns return paths for on-ramped traffic without static routes
title: Automatic Return Routing (Beta)
image: https://developers.cloudflare.com/changelog/post/2025-11-06-automatic-return-routing-beta/og.png?v=fa5fc1243e4424b8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 6, 2025

## Automatic Return Routing (Beta)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-06-automatic-return-routing-beta/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Magic WAN now supports Automatic Return Routing (ARR), allowing customers to configure Magic on-ramps (IPsec/GRE/CNI) to learn the return path for traffic flows without requiring static routes.

Key benefits:

- **Route-less mode**: Static or dynamic routes are optional when using ARR.
- **Overlapping IP space support**: Traffic originating from customer sites can use overlapping private IP ranges.
- **Symmetric routing**: Return traffic is guaranteed to use the same connection as the original on-ramp.

This feature is currently in beta and requires the new Unified Routing mode (beta).

For configuration details, refer to [Configure Automatic Return Routing](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/#configure-automatic-return-routing).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-06-automatic-return-routing-beta/#page","headline":"Automatic Return Routing (Beta)","description":"Magic WAN learns return paths for on-ramped traffic without static routes","url":"https://developers.cloudflare.com/changelog/post/2025-11-06-automatic-return-routing-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-06-automatic-return-routing-beta/og.png?v=fa5fc1243e4424b8","dateModified":"2025-11-06","datePublished":"2025-11-06","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
