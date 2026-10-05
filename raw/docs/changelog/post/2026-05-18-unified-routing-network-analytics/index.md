---
description: Network Analytics is now fully supported for accounts using Unified Routing mode on Cloudflare WAN and Magic Transit.
title: Network Analytics support for Unified Routing
image: https://developers.cloudflare.com/changelog/post/2026-05-18-unified-routing-network-analytics/og.png?v=e77468bf10cc4ce2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 18, 2026

## Network Analytics support for Unified Routing

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Magic Transit](https://developers.cloudflare.com/magic-transit/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-18-unified-routing-network-analytics/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Network Analytics](https://developers.cloudflare.com/analytics/network-analytics/) is now fully supported for accounts using [Unified Routing](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#unified-routing) mode. Traffic that traverses Unified Routing onramps and offramps is now visible in Network Analytics with the same dimensions and filters as traffic on the standard data plane.

This closes a parity gap for customers who had moved tunnels onto Unified Routing and lost visibility into their dataplane traffic in the Network Analytics dashboard. No configuration change is required — analytics data is collected automatically for all accounts with Unified Routing enabled.

For the remaining beta limitations, refer to [Traffic steering beta limitations](https://developers.cloudflare.com/cloudflare-wan/reference/traffic-steering/#check-feature-availability-before-upgrading).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-18-unified-routing-network-analytics/#page","headline":"Network Analytics support for Unified Routing","description":"Network Analytics is now fully supported for accounts using Unified Routing mode on Cloudflare WAN and Magic Transit.","url":"https://developers.cloudflare.com/changelog/post/2026-05-18-unified-routing-network-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-18-unified-routing-network-analytics/og.png?v=e77468bf10cc4ce2","dateModified":"2026-05-18","datePublished":"2026-05-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
