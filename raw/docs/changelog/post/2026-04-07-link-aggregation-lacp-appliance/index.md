---
description: Bundle physical LAN ports into a single logical interface for redundancy and bandwidth.
title: Link aggregation (LACP) support for Cloudflare One Appliance
image: https://developers.cloudflare.com/changelog/post/2026-04-07-link-aggregation-lacp-appliance/og.png?v=e3cab97a43f085a5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 7, 2026

## Link aggregation (LACP) support for Cloudflare One Appliance

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-07-link-aggregation-lacp-appliance/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare One Appliance now supports Link Aggregation Control Protocol (LACP), allowing you to bundle up to six physical LAN ports into a single logical interface. Link aggregation increases available bandwidth and eliminates single points of failure on the LAN side of the appliance.

This feature is available in beta on physical appliance hardware with the latest OS. No entitlement is required.

To configure a Link Aggregation Group, refer to [Configure link aggregation groups](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/network-options/link-aggregation/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-07-link-aggregation-lacp-appliance/#page","headline":"Link aggregation (LACP) support for Cloudflare One Appliance","description":"Bundle physical LAN ports into a single logical interface for redundancy and bandwidth.","url":"https://developers.cloudflare.com/changelog/post/2026-04-07-link-aggregation-lacp-appliance/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-07-link-aggregation-lacp-appliance/og.png?v=e3cab97a43f085a5","dateModified":"2026-04-07","datePublished":"2026-04-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
