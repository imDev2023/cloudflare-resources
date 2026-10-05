---
description: Cloudflare One Client for Windows (version 2026.8.1290.1)
title: Cloudflare One Client for Windows (version 2026.8.1290.1)
image: https://developers.cloudflare.com/changelog/post/2026-09-09-warp-windows-beta/og.png?v=d0cc00b2bbbcc98d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 9, 2026

## Cloudflare One Client for Windows (version 2026.8.1290.1)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-09-warp-windows-beta/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A new Beta release for the Windows Cloudflare One Client is now available on the [beta releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/beta-releases/).

This beta release includes the following changes and improvements:

- Added support for routing non-RFC 1918 local IPv4 networks through the WARP tunnel when unrestricted LAN inclusion is enabled by policy or MDM.
- Improved DNS reliability on networks with lower MTUs by clamping the TCP maximum segment size (MSS) for DNS-over-HTTPS connections sent through the tunnel.
- Improved API reliability by retrying requests dropped when reusing pooled connections.
- The client no longer requires the Windows WLAN AutoConfig service to be running.
- Implemented a service recovery mechanism backed by Windows scheduler task to start WARP service on system unlock if not already started.
- Fixed slow captive portal checks causing the client service to become unresponsive or restart while connecting.
- Fixed a race when switching tunnel protocols during key rotation that could prevent WireGuard from connecting.
- Fixed the client continuing to report 'No network' after a successful manual disconnect.
- Fixed Digital Experience Monitoring (DEX) HTTP tests failing TLS validation on Windows.
- Fixed the client UI crashing at startup when it could not write to the Windows registry.
- Fixed latency spikes and traffic interruptions during TPM-backed API authentication when hardware-backed registration is enabled.
- Fixed trailing whitespace in BIOS serial numbers causing serial-number and client-certificate device posture checks to fail.
- Fixed a client UI crash that could occur when the daemon connection was reset during an IPC request.
- Fixed a startup crash when date formatting data for the system locale had not yet loaded.

**Known issues**

- None

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-09-warp-windows-beta/#page","headline":"Cloudflare One Client for Windows (version 2026.8.1290.1)","description":"Cloudflare One Client for Windows (version 2026.8.1290.1)","url":"https://developers.cloudflare.com/changelog/post/2026-09-09-warp-windows-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-09-warp-windows-beta/og.png?v=d0cc00b2bbbcc98d","dateModified":"2026-09-09","datePublished":"2026-09-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
