---
description: Gateway HTTP and Network policies now support a Traffic Source selector to match traffic based on how it reaches Cloudflare.
title: Traffic Source selector in Gateway policies
image: https://developers.cloudflare.com/changelog/post/2026-08-12-traffic-source-selector/og.png?v=d464a4de5c690097
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 12, 2026

## Traffic Source selector in Gateway policies

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-12-traffic-source-selector/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Gateway [HTTP](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) and [Network](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/) policies now include a **Traffic Source** selector that identifies how traffic reaches Cloudflare. This allows administrators to write policies that target specific on-ramp methods - for example, applying different rules to traffic arriving via the Cloudflare One Client compared to traffic routed through an MCP portal or a proxy endpoint.

#### Available traffic source values

| UI name | API value | Description |
| --- | --- | --- |
| Device client | `device_client` | Traffic from the [Cloudflare One Client (WARP)](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/) |
| Mesh | `mesh` | Traffic from a [Cloudflare Mesh](https://developers.cloudflare.com/mesh/) connector |
| Cloudflare WAN | `cloudflare_wan` | Traffic from [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/zero-trust/cloudflare-gateway/) (Magic WAN) |
| Clientless RDP | `clientless_rdp` | Traffic from a clientless RDP session |
| Proxy endpoint | `proxy_endpoint` | Traffic from a [proxy endpoint](https://developers.cloudflare.com/cloudflare-one/networks/resolvers-and-proxies/proxy-endpoints/) (PAC file) |
| Clientless Browser Isolation | `agentless_biso` | Traffic from [clientless Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) |
| MCP portal | `mcp_portal` | Traffic from an [MCP portal](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) |

The selector uses the `net.onramp.type` API field in both HTTP and Network policies.

| UI name | API example |
| --- | --- |
| Traffic Source | `net.onramp.type == "device_client"` |

#### Browser Isolation selector

A **Browser Isolation** selector is also available in Network and HTTP policies. This selector identifies whether the current session is running inside [Remote Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/), allowing administrators to apply different policy behavior to isolated traffic.

| UI name | API example |
| --- | --- |
| Browser Isolation | `net.is_isolated == true` |

For more information, refer to [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/) and [Network policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/network-policies/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-12-traffic-source-selector/#page","headline":"Traffic Source selector in Gateway policies","description":"Gateway HTTP and Network policies now support a Traffic Source selector to match traffic based on how it reaches Cloudflare.","url":"https://developers.cloudflare.com/changelog/post/2026-08-12-traffic-source-selector/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-12-traffic-source-selector/og.png?v=d464a4de5c690097","dateModified":"2026-08-12","datePublished":"2026-08-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
