---
description: WARP client for macOS (version 2025.10.186.0)
title: WARP client for macOS (version 2025.10.186.0)
image: https://developers.cloudflare.com/changelog/post/2026-01-13-warp-macos-ga/og.png?v=749a9136b993ff91
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 13, 2026

## WARP client for macOS (version 2025.10.186.0)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-13-warp-macos-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A new GA release for the macOS WARP client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release contains minor fixes, improvements, and new features, including the ability to manage WARP client connectivity for all devices in your fleet using an [external signal](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect).

**Changes and improvements**

- The [Local Domain Fallback](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/) feature has been fixed for devices running WARP client version 2025.4.929.0 and newer. Previously, these devices could experience failures with Local Domain Fallback unless a fallback server was explicitly configured. This configuration is no longer a requirement for the feature to function correctly.
- [Proxy mode](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/modes/#local-proxy-mode) now supports transparent HTTP proxying in addition to CONNECT-based proxying.
- Added a new feature to manage WARP client connectivity for all devices using an [external signal](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/emergency-disconnect/#set-up-external-emergency-disconnect). This feature allows administrators to send a global signal from an on-premises HTTPS endpoint that force disconnects or reconnects all WARP clients in an account based on configuration set on the endpoint.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-13-warp-macos-ga/#page","headline":"WARP client for macOS (version 2025.10.186.0)","description":"WARP client for macOS (version 2025.10.186.0)","url":"https://developers.cloudflare.com/changelog/post/2026-01-13-warp-macos-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-13-warp-macos-ga/og.png?v=749a9136b993ff91","dateModified":"2026-01-13","datePublished":"2026-01-13","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
