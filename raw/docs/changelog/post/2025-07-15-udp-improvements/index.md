---
description: We've re-architected how Cloudflare Tunnel handles UDP traffic. Your real-time applications are now faster and more stable, especially on Tunnels with mixed TCP and UDP traffic.
title: Faster, more reliable UDP traffic for Cloudflare Tunnel
image: https://developers.cloudflare.com/changelog/post/2025-07-15-udp-improvements/og.png?v=11c7ad10d55372d1
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 15, 2025

## Faster, more reliable UDP traffic for Cloudflare Tunnel

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-15-udp-improvements/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Your real-time applications running over [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) are now faster and more reliable. We've completely re-architected the way `cloudflared` proxies UDP traffic in order to isolate it from other traffic, ensuring latency-sensitive applications like private DNS are no longer slowed down by heavy TCP traffic (like file transfers) on the same Tunnel.

This is a foundational improvement to Cloudflare Tunnel, delivered automatically to all customers. There are no settings to configure — your UDP traffic is already flowing faster and more reliably.

**What’s new:**

- **Faster UDP performance**: We've significantly reduced the latency for establishing new UDP sessions, making applications like private DNS much more responsive.
- **Greater reliability for mixed traffic**: UDP packets are no longer affected by heavy TCP traffic, preventing timeouts and connection drops for your real-time services.

Learn more about running [TCP or UDP applications](https://developers.cloudflare.com/reference-architecture/architectures/sase/#connecting-applications) and [private networks](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/) through [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-15-udp-improvements/#page","headline":"Faster, more reliable UDP traffic for Cloudflare Tunnel","description":"We've re-architected how Cloudflare Tunnel handles UDP traffic. Your real-time applications are now faster and more stable, especially on Tunnels with mixed TCP and UDP traffic.","url":"https://developers.cloudflare.com/changelog/post/2025-07-15-udp-improvements/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-07-15-udp-improvements/og.png?v=11c7ad10d55372d1","dateModified":"2025-07-15","datePublished":"2025-07-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
