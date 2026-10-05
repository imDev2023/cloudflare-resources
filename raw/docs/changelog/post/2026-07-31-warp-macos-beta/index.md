---
description: Cloudflare One Client for macOS (version 2026.7.1210.1)
title: Cloudflare One Client for macOS (version 2026.7.1210.1)
image: https://developers.cloudflare.com/changelog/post/2026-07-31-warp-macos-beta/og.png?v=305b73351693de0a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 31, 2026

## Cloudflare One Client for macOS (version 2026.7.1210.1)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-31-warp-macos-beta/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A new Beta release for the macOS Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

- Improved connection reliability: the client now swaps protocol order after repeated connectivity-check failures, which helps when HTTP/3 is blocked after the QUIC handshake.
- Fixed issue where a certificate error could be incorrectly displayed right after the connection is established.
- A [DNS search domain](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#dns-search-suffixes) parsing failure no longer prevents connection.
- Fixed a [MASQUE](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#device-tunnel-protocol) issue where the tunnel could stall while uploading at a high rate.
- Fixed being unable to [switch organizations](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/switch-organizations/) when the client was stuck in the "Device not in organization" state.
- Fixed the Home Screen dropdown popup not anchoring correctly.
- Fixed a crash during dialog dismissal.
- Increased tolerance for configurations with a large number of [local domain fallback](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/route-traffic/local-domains/) resolver IPs, so DNS resolution behaves correctly even when more fallback resolvers are configured than recommended.
- Fixed the WARP client stealing window focus (for example, during reauth).
- Fixed a client crash when connecting to a captive portal over Wi-Fi.
- Fixed the system tray icon showing "disconnected" while the UI showed "connected".
- A successful re-authentication will cause the [device profile](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/device-profiles/) to be re-evaluated.
- Improved [dashboard-managed client updates](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/deployment/mdm-deployment/client-version-assignments/) by running the updater only when needed.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-31-warp-macos-beta/#page","headline":"Cloudflare One Client for macOS (version 2026.7.1210.1)","description":"Cloudflare One Client for macOS (version 2026.7.1210.1)","url":"https://developers.cloudflare.com/changelog/post/2026-07-31-warp-macos-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-31-warp-macos-beta/og.png?v=305b73351693de0a","dateModified":"2026-07-31","datePublished":"2026-07-31","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
