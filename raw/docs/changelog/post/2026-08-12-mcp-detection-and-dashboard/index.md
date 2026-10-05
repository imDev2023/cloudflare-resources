---
description: Cloudflare Gateway now detects Model Context Protocol (MCP) traffic and surfaces MCP usage data in a new AI Security dashboard.
title: MCP protocol detection and AI Security dashboard
image: https://developers.cloudflare.com/changelog/post/2026-08-12-mcp-detection-and-dashboard/og.png?v=debd250b40b10da2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 12, 2026

## MCP protocol detection and AI Security dashboard

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-12-mcp-detection-and-dashboard/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Gateway now automatically detects [Model Context Protocol (MCP) ↗︎](https://www.cloudflare.com/learning/ai/what-is-model-context-protocol-mcp/) traffic flowing through your network. MCP is the standard protocol used by AI agents to connect to external tools and data sources. Gateway identifies MCP requests by inspecting protocol-specific headers and payload characteristics.

#### MCP policy selector

A new **Is MCP** selector (`experimental.is_mcp`) is available in [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#is-mcp). Use this selector to build Gateway rules that allow, block, or isolate MCP traffic.

This selector is currently in beta and may change before general availability.

For example, the following policy blocks MCP traffic that does not arrive through an approved [MCP portal](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/):

| Selector | Operator | Value | Logic | Action |
| --- | --- | --- | --- | --- |
| Is MCP | is | *True* | And | Block |
| Traffic Source | is not | *MCP portal* |  | |

![Example Gateway policy that blocks MCP traffic not arriving through an MCP portal](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1104,height=664,format=webp/_astro/gateway-block-unknown-mcp.B2Ainj8x.png)

#### AI security report

A new **AI security report** dashboard under **Insights & Logs > Dashboards** provides visibility into MCP usage across your organization. The dashboard includes:

- Total MCP request volume, unique users, and unique MCP servers
- A timeseries chart of unique MCP servers observed over time
- A summary of Gateway policies that target MCP traffic

![AI security report dashboard showing MCP detection data including total MCP requests, users, servers, and Gateway policies for MCP](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2406,height=928,format=webp/_astro/gateway-mcp-dashboard.C9jPahkp.png)

For more information, refer to [HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-12-mcp-detection-and-dashboard/#page","headline":"MCP protocol detection and AI Security dashboard","description":"Cloudflare Gateway now detects Model Context Protocol (MCP) traffic and surfaces MCP usage data in a new AI Security dashboard.","url":"https://developers.cloudflare.com/changelog/post/2026-08-12-mcp-detection-and-dashboard/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-12-mcp-detection-and-dashboard/og.png?v=debd250b40b10da2","dateModified":"2026-08-12","datePublished":"2026-08-12","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
