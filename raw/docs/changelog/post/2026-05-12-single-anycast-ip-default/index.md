---
description: New Magic Transit and Cloudflare WAN accounts are now assigned a single IPv4 anycast address by default
title: New accounts assigned a single IPv4 anycast address
image: https://developers.cloudflare.com/changelog/post/2026-05-12-single-anycast-ip-default/og.png?v=045ca20f7e8dd51f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 12, 2026

## New accounts assigned a single IPv4 anycast address

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/) [Magic Transit](https://developers.cloudflare.com/magic-transit/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-12-single-anycast-ip-default/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

New Magic Transit and Cloudflare WAN accounts are now assigned a single IPv4 anycast address by default.

Cloudflare handles failures on its network automatically by advertising your endpoint IP from multiple nodes across many globally distributed data centers. To handle failures on your network, configure two tunnels from separate routers.

To request additional anycast IP addresses for your account, contact your account team.

For tunnel configuration guidance, refer to [Configure tunnel endpoints](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-tunnel-endpoints/) for Cloudflare WAN or [Configure tunnel endpoints](https://developers.cloudflare.com/magic-transit/how-to/configure-tunnel-endpoints/) for Magic Transit.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-12-single-anycast-ip-default/#page","headline":"New accounts assigned a single IPv4 anycast address","description":"New Magic Transit and Cloudflare WAN accounts are now assigned a single IPv4 anycast address by default","url":"https://developers.cloudflare.com/changelog/post/2026-05-12-single-anycast-ip-default/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-12-single-anycast-ip-default/og.png?v=045ca20f7e8dd51f","dateModified":"2026-05-12","datePublished":"2026-05-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
