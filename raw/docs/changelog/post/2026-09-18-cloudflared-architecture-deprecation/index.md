---
description: Starting in 2027, Cloudflare will deprecate 32-bit Windows and Intel-based macOS builds of cloudflared and stop publishing releases for either architecture.
title: cloudflared to deprecate 32-bit Windows and Intel-based macOS builds in 2027
image: https://developers.cloudflare.com/changelog/post/2026-09-18-cloudflared-architecture-deprecation/og.png?v=172c445b36bef289
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 18, 2026

## cloudflared to deprecate 32-bit Windows and Intel-based macOS builds in 2027

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-18-cloudflared-architecture-deprecation/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Starting in 2027, Cloudflare will deprecate 32-bit Windows and Intel-based macOS builds of `cloudflared`. After the deprecation takes effect, Cloudflare will no longer publish new `cloudflared` releases for either architecture.

Windows 10, the last Windows release to support 32-bit systems, reached end of support in October 2025. Apple has also deprecated Intel-based Mac computers. macOS 26 Tahoe, released in September 2025, was the final macOS release to support Intel-based Macs. macOS 27, released in September 2026, no longer supports them.

Focusing development on currently supported architectures allows `cloudflared` to align with operating system support and continue receiving updates on supported platforms. For available downloads and supported platforms, refer to the [Cloudflare Tunnel downloads](https://developers.cloudflare.com/tunnel/downloads/) documentation.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-18-cloudflared-architecture-deprecation/#page","headline":"cloudflared to deprecate 32-bit Windows and Intel-based macOS builds in 2027","description":"Starting in 2027, Cloudflare will deprecate 32-bit Windows and Intel-based macOS builds of cloudflared and stop publishing releases for either architecture.","url":"https://developers.cloudflare.com/changelog/post/2026-09-18-cloudflared-architecture-deprecation/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-18-cloudflared-architecture-deprecation/og.png?v=172c445b36bef289","dateModified":"2026-09-18","datePublished":"2026-09-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
