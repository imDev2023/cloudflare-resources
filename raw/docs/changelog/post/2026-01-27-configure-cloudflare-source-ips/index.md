---
description: Configure the source IP range used by Cloudflare services when sending traffic to private networks
title: Configure Cloudflare source IPs (beta)
image: https://developers.cloudflare.com/changelog/post/2026-01-27-configure-cloudflare-source-ips/og.png?v=a2c038b69c49f6ef
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 27, 2026

## Configure Cloudflare source IPs (beta)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-27-configure-cloudflare-source-ips/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare source IPs are the IP addresses used by Cloudflare services (such as Load Balancing, Gateway, and Browser Isolation) when sending traffic to your private networks.

For customers using legacy mode routing, traffic to private networks is sourced from public Cloudflare IPs, which may cause IP conflicts. For customers using Unified Routing mode (beta), traffic to private networks is sourced from dedicated, non-Internet-routable private IPv4 range to ensure:

- Symmetric routing over private network connections
- Proper firewall state preservation
- Private traffic stays on secure paths

Key details:

- **IPv4**: Sourced from `100.64.0.0/12` by default, configurable to any `/12` CIDR
- **IPv6**: Sourced from `2606:4700:cf1:5000::/64` (not configurable)
- **Affected connectors**: GRE, IPsec, CNI, WARP Connector, and WARP Client (Cloudflare Tunnel is not affected)

Configuring Cloudflare source IPs requires Unified Routing (beta) and the `Cloudflare One Networks Write` permission.

For configuration details, refer to [Configure Cloudflare source IPs](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-cloudflare-source-ips/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-27-configure-cloudflare-source-ips/#page","headline":"Configure Cloudflare source IPs (beta)","description":"Configure the source IP range used by Cloudflare services when sending traffic to private networks","url":"https://developers.cloudflare.com/changelog/post/2026-01-27-configure-cloudflare-source-ips/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-27-configure-cloudflare-source-ips/og.png?v=a2c038b69c49f6ef","dateModified":"2026-01-27","datePublished":"2026-01-27","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
