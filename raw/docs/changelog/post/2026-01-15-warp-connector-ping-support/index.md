---
description: You can now ping the WARP Connector host directly on its LAN IP to quickly validate connectivity after installation.
title: Verify WARP Connector connectivity with a simple ping
image: https://developers.cloudflare.com/changelog/post/2026-01-15-warp-connector-ping-support/og.png?v=573da52f5fc78939
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 15, 2026

## Verify WARP Connector connectivity with a simple ping

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-15-warp-connector-ping-support/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We have made it easier to validate connectivity when deploying [WARP Connector](https://developers.cloudflare.com/mesh/) as part of your [software-defined private network](https://developers.cloudflare.com/reference-architecture/architectures/sase/#connecting-networks).

You can now `ping` the WARP Connector host directly on its LAN IP address immediately after installation. This provides a fast, familiar way to confirm that the Connector is online and reachable within your network before testing access to downstream services.

Starting with [version 2025.10.186.0](https://developers.cloudflare.com/changelog/2026-01-13-warp-linux-ga/), WARP Connector responds to traffic addressed to its own LAN IP, giving you immediate visibility into Connector reachability.

Learn more about deploying [WARP Connector](https://developers.cloudflare.com/mesh/) and building private network connectivity with [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-15-warp-connector-ping-support/#page","headline":"Verify WARP Connector connectivity with a simple ping","description":"You can now ping the WARP Connector host directly on its LAN IP to quickly validate connectivity after installation.","url":"https://developers.cloudflare.com/changelog/post/2026-01-15-warp-connector-ping-support/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-15-warp-connector-ping-support/og.png?v=573da52f5fc78939","dateModified":"2026-01-15","datePublished":"2026-01-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
