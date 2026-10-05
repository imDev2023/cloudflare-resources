---
description: Pin breakout traffic to specific WAN ports for deterministic egress control
title: Designate WAN link for breakout traffic
image: https://developers.cloudflare.com/changelog/post/2025-11-06-connector-designate-wan-link-breakout/og.png?v=320b2a1254512c1c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 6, 2025

## Designate WAN link for breakout traffic

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-06-connector-designate-wan-link-breakout/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Magic WAN Connector now allows you to designate a specific WAN port for breakout traffic, giving you deterministic control over the egress path for latency-sensitive applications.

With this feature, you can:

- Pin breakout traffic for specific applications to a preferred WAN port.
- Ensure critical traffic (such as Zoom or Teams) always uses your fastest or most reliable connection.
- Benefit from automatic failover to standard WAN port priority if the preferred port goes down.

This is useful for organizations with multiple ISP uplinks who need predictable egress behavior for performance-sensitive traffic.

For configuration details, refer to [Designate WAN ports for breakout apps](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/application-based-policies/breakout-traffic/#designate-wan-ports-for-breakout-apps).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-06-connector-designate-wan-link-breakout/#page","headline":"Designate WAN link for breakout traffic","description":"Pin breakout traffic to specific WAN ports for deterministic egress control","url":"https://developers.cloudflare.com/changelog/post/2025-11-06-connector-designate-wan-link-breakout/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-06-connector-designate-wan-link-breakout/og.png?v=320b2a1254512c1c","dateModified":"2025-11-06","datePublished":"2025-11-06","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
