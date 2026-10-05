---
description: Gateway HTTP and Network policies now support a Traffic Destination selector to match traffic based on how it exits Cloudflare.
title: Traffic Destination selector in Gateway policies
image: https://developers.cloudflare.com/changelog/post/2026-09-23-traffic-destination-selector/og.png?v=118cbe9c1f7fe2f6
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 23, 2026

## Traffic Destination selector in Gateway policies

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-23-traffic-destination-selector/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Gateway [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) and [Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) policies now include a **Traffic Destination** selector that identifies how traffic exits Cloudflare. This allows administrators to write policies that target specific off-ramp methods - for example, applying different rules to traffic destined for the public Internet compared to traffic routed through Cloudflare Tunnel or Cloudflare WAN.

#### Available traffic destination values

| UI name | API value | Description |
| --- | --- | --- |
| Internet | `internet` | Traffic to the public Internet |
| Cloudflare WAN | `cloudflare_wan` | Traffic through a [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-wan/) connection |
| Cloudflare Tunnel | `cloudflare_tunnel` | Traffic to a private origin through [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/) |
| Cloudflare One Client | `device_client` | Traffic to another device running the [Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) |
| Mesh | `mesh` | Traffic through a [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) node |

The selector uses the `net.offramp.type` API field in both HTTP and Network policies.

| UI name | API example |
| --- | --- |
| Traffic Destination | `net.offramp.type == "internet"` |

For more information, refer to [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) and [Network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-23-traffic-destination-selector/#page","headline":"Traffic Destination selector in Gateway policies","description":"Gateway HTTP and Network policies now support a Traffic Destination selector to match traffic based on how it exits Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-09-23-traffic-destination-selector/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-23-traffic-destination-selector/og.png?v=118cbe9c1f7fe2f6","dateModified":"2026-09-23","datePublished":"2026-09-23","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
