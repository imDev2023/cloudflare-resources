---
description: WARP client for macOS (version 2026.1.150.0)
title: WARP client for macOS (version 2026.1.150.0)
image: https://developers.cloudflare.com/changelog/post/2026-02-24-warp-macos-ga/og.png?v=ae64e0800cf97894
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 24, 2026

## WARP client for macOS (version 2026.1.150.0)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-24-warp-macos-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A new GA release for the macOS WARP client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This release contains minor fixes and improvements.

**Changes and improvements**

- Fixed an issue causing failure of the [local network exclusion](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/configure/settings/#allow-users-to-enable-local-network-exclusion) feature when configured with a timeout of `0`.
- Improvement for more accurate reporting of device colocation information in the Cloudflare One dashboard.
- Fixed an issue with DNS server configuration failures that caused tunnel connection delays.
- Fixed an issue where misconfigured DEX HTTP tests prevented new registrations.
- Fixed an issue causing DNS requests to fail with clients in Traffic and DNS mode.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-24-warp-macos-ga/#page","headline":"WARP client for macOS (version 2026.1.150.0)","description":"WARP client for macOS (version 2026.1.150.0)","url":"https://developers.cloudflare.com/changelog/post/2026-02-24-warp-macos-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-24-warp-macos-ga/og.png?v=ae64e0800cf97894","dateModified":"2026-02-24","datePublished":"2026-02-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
