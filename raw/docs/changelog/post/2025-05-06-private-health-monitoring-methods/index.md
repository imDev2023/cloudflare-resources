---
description: Use UDP or ICMP to monitor the health of your private IP-based applications.
title: UDP and ICMP Monitor Support for Private Load Balancing Endpoints
image: https://developers.cloudflare.com/changelog/post/2025-05-06-private-health-monitoring-methods/og.png?v=a097463f9598ad05
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 6, 2025

## UDP and ICMP Monitor Support for Private Load Balancing Endpoints

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-06-private-health-monitoring-methods/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Load Balancing now supports **UDP (Layer 4)** and **ICMP (Layer 3)** health monitors for **private endpoints**. This makes it simple to track the health and availability of internal services that don’t respond to HTTP, TCP, or other protocol probes.

#### What you can do:

- Set up **ICMP ping monitors** to check if your private endpoints are reachable.
- Use **UDP monitors** for lightweight health checks on non-TCP workloads, such as DNS, VoIP, or custom UDP-based services.
- Gain better visibility and uptime guarantees for services running behind **Private Network Load Balancing**, without requiring public IP addresses.

This enhancement is ideal for internal applications that rely on low-level protocols, especially when used in conjunction with [**Cloudflare Tunnel**](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/), [**WARP**](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/), and [**Magic WAN**](https://developers.cloudflare.com/cloudflare-wan/) to create a secure and observable private network.

Learn more about [Private Network Load Balancing](https://developers.cloudflare.com/load-balancing/private-network/) or view the full list of [supported health monitor protocols](https://developers.cloudflare.com/load-balancing/monitors/#supported-protocols).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-06-private-health-monitoring-methods/#page","headline":"UDP and ICMP Monitor Support for Private Load Balancing Endpoints","description":"Use UDP or ICMP to monitor the health of your private IP-based applications.","url":"https://developers.cloudflare.com/changelog/post/2025-05-06-private-health-monitoring-methods/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-06-private-health-monitoring-methods/og.png?v=a097463f9598ad05","dateModified":"2025-05-06","datePublished":"2025-05-06","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
