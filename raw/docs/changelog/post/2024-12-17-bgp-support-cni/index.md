---
description: BGP support for Cloudflare Network Interconnect (CNI)
title: Establish BGP peering over Direct CNI circuits
image: https://developers.cloudflare.com/changelog/post/2024-12-17-bgp-support-cni/og.png?v=be15bee7d83edc5e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 17, 2024

## Establish BGP peering over Direct CNI circuits

[Magic Transit](https://developers.cloudflare.com/magic-transit/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Network Interconnect](https://developers.cloudflare.com/network-interconnect/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2024-12-17-bgp-support-cni/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Magic WAN and Magic Transit customers can use the Cloudflare dashboard to configure and manage BGP peering between their networks and their Magic routing table when using a Direct CNI on-ramp.

Using BGP peering allows customers to:

- Automate the process of adding or removing networks and subnets.
- Take advantage of failure detection and session recovery features.

With this functionality, customers can:

- Establish an eBGP session between their devices and the Magic WAN / Magic Transit service when connected via CNI.
- Secure the session by MD5 authentication to prevent misconfigurations.
- Exchange routes dynamically between their devices and their Magic routing table.

Refer to [Magic WAN BGP peering](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes) or [Magic Transit BGP peering](https://developers.cloudflare.com/magic-transit/how-to/configure-routes/#configure-bgp-routes) to learn more about this feature and how to set it up.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-12-17-bgp-support-cni/#page","headline":"Establish BGP peering over Direct CNI circuits","description":"BGP support for Cloudflare Network Interconnect (CNI)","url":"https://developers.cloudflare.com/changelog/post/2024-12-17-bgp-support-cni/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2024-12-17-bgp-support-cni/og.png?v=be15bee7d83edc5e","dateModified":"2024-12-17","datePublished":"2024-12-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
