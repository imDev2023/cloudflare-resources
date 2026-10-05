---
description: Define breakout and priority rules by source LAN, VLAN, or CIDR — in addition to destination application.
title: Source-based breakout and prioritization on Cloudflare One Appliance
image: https://developers.cloudflare.com/changelog/post/2026-05-07-appliance-source-based-breakout/og.png?v=80259cd58ccf93d8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 7, 2026

## Source-based breakout and prioritization on Cloudflare One Appliance

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-07-appliance-source-based-breakout/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Breakout and traffic prioritization rules on the Cloudflare One Appliance can now match by **source** in addition to destination application. You can pin breakout or priority behavior to:

- A source LAN interface — VLANs attached to that LAN are included automatically.
- A source IP address, range, or CIDR block.

This is the natural way to break out a guest VLAN to the local Internet, or to prioritize traffic from a specific subnet, without enumerating destination applications.

For details, refer to [Breakout traffic](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#breakout-by-source).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-07-appliance-source-based-breakout/#page","headline":"Source-based breakout and prioritization on Cloudflare One Appliance","description":"Define breakout and priority rules by source LAN, VLAN, or CIDR — in addition to destination application.","url":"https://developers.cloudflare.com/changelog/post/2026-05-07-appliance-source-based-breakout/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-07-appliance-source-based-breakout/og.png?v=80259cd58ccf93d8","dateModified":"2026-05-07","datePublished":"2026-05-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
