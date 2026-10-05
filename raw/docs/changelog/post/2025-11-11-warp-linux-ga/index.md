---
description: WARP client for Linux (version 2025.9.558.0)
title: WARP client for Linux (version 2025.9.558.0)
image: https://developers.cloudflare.com/changelog/post/2025-11-11-warp-linux-ga/og.png?v=c05ea265bf51749e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 11, 2025

## WARP client for Linux (version 2025.9.558.0)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-11-warp-linux-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A new GA release for the Linux WARP client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release contains minor fixes, improvements, and new features including [Path Maximum Transmission Unit Discovery (PMTUD)](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery). When PMTUD is enabled, the client will dynamically adjust packet sizing to optimize connection performance. There is also a new connection status message in the GUI to inform users that the local network connection may be unstable. This will make it easier to diagnose connectivity issues.

WARP client version 2025.8.779.0 introduced an updated public key for Linux packages. The public key must be updated if it was installed before September 12, 2025 to ensure the repository remains functional after December 4, 2025. Instructions to make this update are available at [pkg.cloudflareclient.com](https://pkg.cloudflareclient.com/).

**Changes and improvements**

- The GUI now displays the health of the tunnel and DNS connections by showing a connection status message when the network may be unstable. This will make it easier to diagnose connectivity issues.
- Fixed an issue where deleting a registration was erroneously reported as having failed.
- Path Maximum Transmission Unit Discovery (PMTUD) may now be used to discover the effective MTU of the connection. This allows the WARP client to improve connectivity optimized for each network. PMTUD is disabled by default. To enable it, refer to the [PMTUD documentation](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/path-mtu-discovery/#enable-path-mtu-discovery).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-11-warp-linux-ga/#page","headline":"WARP client for Linux (version 2025.9.558.0)","description":"WARP client for Linux (version 2025.9.558.0)","url":"https://developers.cloudflare.com/changelog/post/2025-11-11-warp-linux-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-11-warp-linux-ga/og.png?v=c05ea265bf51749e","dateModified":"2025-11-11","datePublished":"2025-11-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
