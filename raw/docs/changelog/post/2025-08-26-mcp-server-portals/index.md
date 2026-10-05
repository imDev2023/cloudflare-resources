---
description: Cloudflare Zero Trust MCP server portals allow admins to centralize all of their MCP servers and enforce user-specific security policies.
title: MCP server portals
image: https://developers.cloudflare.com/changelog/post/2025-08-26-mcp-server-portals/og.png?v=ea1480d40350e469
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 26, 2025

## MCP server portals

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-26-mcp-server-portals/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

![MCP server portal](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1557,height=420,format=webp/_astro/mcp-server-portal.BOKqTCoI.png)

An [MCP server portal](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) centralizes multiple Model Context Protocol (MCP) servers onto a single HTTP endpoint. Key benefits include:

- **Streamlined access to multiple MCP servers**: MCP server portals support both unauthenticated MCP servers as well as MCP servers secured using any third-party or custom OAuth provider. Users log in to the portal URL through Cloudflare Access and are prompted to authenticate separately to each server that requires OAuth.
- **Customized tools per portal**: Admins can tailor an MCP portal to a particular use case by choosing the specific tools and prompt templates that they want to make available to users through the portal. This allows users to access a curated set of tools and prompts — the less external context exposed to the AI model, the better the AI responses tend to be.
- **Observability**: Once the user's AI agent is connected to the portal, Cloudflare Access logs the individual requests made using the tools in the portal.

This is available in an open beta for all customers across all plans! For more information check out our [blog ↗︎](https://blog.cloudflare.com/zero-trust-mcp-server-portals/) for this release.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-26-mcp-server-portals/#page","headline":"MCP server portals","description":"Cloudflare Zero Trust MCP server portals allow admins to centralize all of their MCP servers and enforce user-specific security policies.","url":"https://developers.cloudflare.com/changelog/post/2025-08-26-mcp-server-portals/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-26-mcp-server-portals/og.png?v=ea1480d40350e469","dateModified":"2025-08-26","datePublished":"2025-08-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
