---
description: Cloudflare One Client for macOS (version 2026.6.880.0)
title: Cloudflare One Client for macOS (version 2026.6.880.0)
image: https://developers.cloudflare.com/changelog/post/2026-07-21-warp-macos-ga/og.png?v=5ea956fbacc3a091
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 21, 2026

## Cloudflare One Client for macOS (version 2026.6.880.0)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-21-warp-macos-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A new GA release for the macOS Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix resolves a regression that caused a large increase in DNS-over-TCP queries to fallback and internal DNS servers. The client now sends fallback DNS queries over UDP first, falling back to TCP only when a response is truncated, instead of querying both protocols in parallel.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-21-warp-macos-ga/#page","headline":"Cloudflare One Client for macOS (version 2026.6.880.0)","description":"Cloudflare One Client for macOS (version 2026.6.880.0)","url":"https://developers.cloudflare.com/changelog/post/2026-07-21-warp-macos-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-21-warp-macos-ga/og.png?v=5ea956fbacc3a091","dateModified":"2026-07-21","datePublished":"2026-07-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
