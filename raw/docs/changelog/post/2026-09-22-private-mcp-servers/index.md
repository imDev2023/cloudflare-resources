---
description: MCP server portals can now connect to MCP servers available only on your private network.
title: Private MCP server support for MCP server portals
image: https://developers.cloudflare.com/changelog/post/2026-09-22-private-mcp-servers/og.png?v=72543f6196af0567
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 22, 2026

## Private MCP server support for MCP server portals

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-22-private-mcp-servers/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) can now connect to MCP servers available only on your private network. The portal uses [Cloudflare Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) to reach [private hostnames](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/) and IP addresses without exposing the MCP server to the public Internet.

Connect the server network to Cloudflare with [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/), [Cloudflare Mesh](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-mesh/), or another [Cloudflare One connector](https://developers.cloudflare.com/cloudflare-one/networks/connectors/). Configure a private hostname or CIDR route, then turn on **Route traffic through Cloudflare Gateway** when you add the server. OAuth authorization server endpoints, such as the authorization and token endpoints, must be accessible on the public Internet. If Cloudflare automatically registers the OAuth client through Dynamic Client Registration (DCR), the registration endpoint must also be accessible on the public Internet.

For setup instructions, refer to [Connect a private MCP server](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#connect-a-private-mcp-server).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-22-private-mcp-servers/#page","headline":"Private MCP server support for MCP server portals","description":"MCP server portals can now connect to MCP servers available only on your private network.","url":"https://developers.cloudflare.com/changelog/post/2026-09-22-private-mcp-servers/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-22-private-mcp-servers/og.png?v=72543f6196af0567","dateModified":"2026-09-22","datePublished":"2026-09-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
