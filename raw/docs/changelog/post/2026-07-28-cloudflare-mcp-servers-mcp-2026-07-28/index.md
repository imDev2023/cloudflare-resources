---
description: Cloudflare's product-specific MCP servers now support the new MCP 2026-07-28 Specification with compatibility for 2025 Streamable HTTP clients.
title: Cloudflare MCP servers support the new MCP 2026-07-28 Specification
image: https://developers.cloudflare.com/changelog/post/2026-07-28-cloudflare-mcp-servers-mcp-2026-07-28/og.png?v=bf8cab965ebc8a87
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 28, 2026

## Cloudflare MCP servers support the new MCP 2026-07-28 Specification

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-28-cloudflare-mcp-servers-mcp-2026-07-28/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare's [product-specific MCP servers](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/#product-specific-mcp-servers) now support the new MCP 2026-07-28 Specification. Each request runs on a fresh stateless server without an MCP protocol session or protocol-specific Durable Object.

The `/mcp` endpoint also accepts stateless requests from 2025 Streamable HTTP clients. Most clients can reconnect without configuration changes.

Use `/mcp` for new connections. Historical `/sse` URLs continue to work as aliases for the same Streamable HTTP handler, but they no longer serve the deprecated HTTP+SSE transport. If a client forces SSE transport, change it to Streamable HTTP or automatic transport detection.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-28-cloudflare-mcp-servers-mcp-2026-07-28/#page","headline":"Cloudflare MCP servers support the new MCP 2026-07-28 Specification","description":"Cloudflare's product-specific MCP servers now support the new MCP 2026-07-28 Specification with compatibility for 2025 Streamable HTTP clients.","url":"https://developers.cloudflare.com/changelog/post/2026-07-28-cloudflare-mcp-servers-mcp-2026-07-28/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-28-cloudflare-mcp-servers-mcp-2026-07-28/og.png?v=bf8cab965ebc8a87","dateModified":"2026-07-28","datePublished":"2026-07-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
