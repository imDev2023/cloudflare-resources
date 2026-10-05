---
description: MCP server portals support the latest stateless MCP specification while retaining compatibility with 2025 clients and servers.
title: MCP server portals support MCP 2026-07-28 specification
image: https://developers.cloudflare.com/changelog/post/2026-08-25-mcp-portals-mcp-2026-07-28/og.png?v=969ee62c25023ced
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 25, 2026

## MCP server portals support MCP 2026-07-28 specification

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-25-mcp-portals-mcp-2026-07-28/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) support the stateless MCP `2026-07-28` specification for client and upstream server connections.

The portal's `/mcp` endpoint automatically accepts stateless MCP `2026-07-28` requests and earlier 2025 Streamable HTTP clients. When the portal connects to an upstream Streamable HTTP server, it checks for MCP `2026-07-28` support and falls back to the 2025 handshake when needed. Client and upstream protocol selection are independent, so clients and servers can upgrade separately without portal configuration changes.

SSE connections continue to use the legacy protocol. For details, refer to [MCP server portal transport and protocol compatibility](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#transport).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-25-mcp-portals-mcp-2026-07-28/#page","headline":"MCP server portals support MCP 2026-07-28 specification","description":"MCP server portals support the latest stateless MCP specification while retaining compatibility with 2025 clients and servers.","url":"https://developers.cloudflare.com/changelog/post/2026-08-25-mcp-portals-mcp-2026-07-28/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-25-mcp-portals-mcp-2026-07-28/og.png?v=969ee62c25023ced","dateModified":"2026-08-25","datePublished":"2026-08-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
