---
description: Configure BGP peering over IPsec and GRE tunnels for dynamic routing
title: BGP over GRE and IPsec tunnels
image: https://developers.cloudflare.com/changelog/post/2026-01-30-bgp-over-tunnels/og.png?v=6f61e7ebcf70d9df
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 30, 2026

## BGP over GRE and IPsec tunnels

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Magic Transit](https://developers.cloudflare.com/magic-transit/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-30-bgp-over-tunnels/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Magic WAN and Magic Transit customers can use the Cloudflare dashboard to configure and manage BGP peering between their networks and their Magic routing table when using IPsec and GRE tunnel on-ramps (beta).

Using BGP peering allows customers to:

- Automate the process of adding or removing networks and subnets.
- Take advantage of failure detection and session recovery features.

With this functionality, customers can:

- Establish an eBGP session between their devices and the Magic WAN / Magic Transit service when connected via IPsec and GRE tunnel on-ramps.
- Secure the session by MD5 authentication to prevent misconfigurations.
- Exchange routes dynamically between their devices and their Magic routing table.

For configuration details, refer to:

- [Configure BGP routes for Magic WAN](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/#configure-bgp-routes)
- [Configure BGP routes for Magic Transit](https://developers.cloudflare.com/magic-transit/how-to/configure-routes/#configure-bgp-routes)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-30-bgp-over-tunnels/#page","headline":"BGP over GRE and IPsec tunnels","description":"Configure BGP peering over IPsec and GRE tunnels for dynamic routing","url":"https://developers.cloudflare.com/changelog/post/2026-01-30-bgp-over-tunnels/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-30-bgp-over-tunnels/og.png?v=6f61e7ebcf70d9df","dateModified":"2026-01-30","datePublished":"2026-01-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
