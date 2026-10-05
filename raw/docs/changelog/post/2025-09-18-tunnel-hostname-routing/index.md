---
description: Create Tunnel routes based on hostnames or domains — not just IPs — to simplify Zero Trust and egress policies.
title: Connect and secure any private or public app by hostname, not IP — with hostname routing for Cloudflare Tunnel
image: https://developers.cloudflare.com/changelog/post/2025-09-18-tunnel-hostname-routing/og.png?v=a918a671719dbbb8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 18, 2025

## Connect and secure any private or public app by hostname, not IP — with hostname routing for Cloudflare Tunnel

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-18-tunnel-hostname-routing/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now route private traffic to [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) based on a hostname or domain, moving beyond the limitations of IP-based routing. This new capability is **free for all Cloudflare One customers**.

Previously, Tunnel routes could only be defined by IP address or [CIDR range](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/). This created a challenge for modern applications with dynamic or ephemeral IP addresses, often forcing administrators to maintain complex and brittle IP lists.

![Hostname-based routing in Cloudflare Tunnel](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1990,height=530,format=webp/_astro/tunnel-hostname-routing.DSi8MP_7.webp)

**What’s new:**

- **Hostname & Domain Routing**: Create routes for individual hostnames (e.g., `payroll.acme.local`) or entire domains (e.g., `*.acme.local`) and direct their traffic to a specific Tunnel.
- **Simplified Zero Trust Policies**: Build resilient policies in Cloudflare Access and Gateway using stable hostnames, making it dramatically easier to apply per-resource authorization for your private applications.
- **Precise Egress Control**: Route traffic for public hostnames (e.g., `bank.example.com`) through a specific Tunnel to enforce a dedicated source IP, solving the IP allowlist problem for third-party services.
- **No More IP Lists**: This feature makes the workaround of maintaining dynamic IP Lists for Tunnel connections obsolete.

Get started in the Tunnels section of the Zero Trust dashboard with your first [private hostname](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/) or [public hostname](https://developers.cloudflare.com/cloudflare-one/traffic-policies/egress-policies/egress-cloudflared/) route.

Learn more in our [blog post ↗︎](https://blog.cloudflare.com/tunnel-hostname-routing/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-18-tunnel-hostname-routing/#page","headline":"Connect and secure any private or public app by hostname, not IP — with hostname routing for Cloudflare Tunnel","description":"Create Tunnel routes based on hostnames or domains — not just IPs — to simplify Zero Trust and egress policies.","url":"https://developers.cloudflare.com/changelog/post/2025-09-18-tunnel-hostname-routing/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-18-tunnel-hostname-routing/og.png?v=a918a671719dbbb8","dateModified":"2025-09-18","datePublished":"2025-09-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
