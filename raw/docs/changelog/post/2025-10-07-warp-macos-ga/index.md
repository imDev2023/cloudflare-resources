---
description: WARP client for macOS (version 2025.8.779.0)
title: WARP client for macOS (version 2025.8.779.0)
image: https://developers.cloudflare.com/changelog/post/2025-10-07-warp-macos-ga/og.png?v=491682b3cceec385
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 7, 2025

## WARP client for macOS (version 2025.8.779.0)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-07-warp-macos-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A new GA release for the macOS WARP client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release contains significant fixes and improvements.

**Changes and improvements**

- [Proxy mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode) has been enhanced for even faster resolution. Proxy mode now supports SOCKS4, SOCK5, and HTTP CONNECT over an L4 tunnel with custom congestion control optimizations instead of the previous L3 tunnel to Cloudflare's network. This has more than doubled Proxy mode throughput in lab speed testing, by an order of magnitude in some cases.
- The MASQUE protocol is now the only protocol that can use [Proxy mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode). If you previously configured a device profile to use Proxy mode with Wireguard, you will need to select a new WARP mode or switch to the MASQUE protocol. Otherwise, all devices matching the profile will lose connectivity.

**Known issues**

- macOS Sequoia: Due to changes Apple introduced in macOS 15.0.x, the WARP client may not behave as expected. Cloudflare recommends the use of macOS 15.4 or later.
- Devices using WARP client 2025.4.929.0 and up may experience Local Domain Fallback failures if a fallback server has not been configured. To configure a fallback server, refer to [Route traffic to fallback server](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/#route-traffic-to-fallback-server).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-07-warp-macos-ga/#page","headline":"WARP client for macOS (version 2025.8.779.0)","description":"WARP client for macOS (version 2025.8.779.0)","url":"https://developers.cloudflare.com/changelog/post/2025-10-07-warp-macos-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-07-warp-macos-ga/og.png?v=491682b3cceec385","dateModified":"2025-10-07","datePublished":"2025-10-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
