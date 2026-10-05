---
description: Reduce context window usage for MCP servers protected by portals with minimize_tools and search_and_execute query parameters.
title: Context optimization for MCP server portals
image: https://developers.cloudflare.com/changelog/post/2026-03-26-mcp-portal-context-optimization/og.png?v=b9c30694d7d0bb6c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 26, 2026

## Context optimization for MCP server portals

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-26-mcp-portal-context-optimization/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) support two context optimization options that reduce how many tokens tool definitions consume in the model's context window. Both options are activated by appending the `optimize_context` query parameter to the portal URL.

#### `minimize_tools`

Strips tool descriptions and input schemas from all upstream tools, leaving only their names. The portal exposes a special `query` tool that agents use to retrieve full definitions on demand. This provides up to 5x savings in token usage.

```txt
https://<subdomain>.<domain>/mcp?optimize_context=minimize_tools
```

#### `search_and_execute`

Hides all upstream tools and exposes only two tools: `query` and `execute`. The `query` tool searches and retrieves tool definitions. The `execute` tool runs the upstream tools in an isolated [Dynamic Worker](https://developers.cloudflare.com/workers/runtime-apis/bindings/worker-loader/) environment. This reduces the initial token cost to a small constant, regardless of how many tools are available through the portal.

```txt
https://<subdomain>.<domain>/mcp?optimize_context=search_and_execute
```

For more information, refer to [Optimize context](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#optimize-context).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-26-mcp-portal-context-optimization/#page","headline":"Context optimization for MCP server portals","description":"Reduce context window usage for MCP servers protected by portals with minimize_tools and search_and_execute query parameters.","url":"https://developers.cloudflare.com/changelog/post/2026-03-26-mcp-portal-context-optimization/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-26-mcp-portal-context-optimization/og.png?v=b9c30694d7d0bb6c","dateModified":"2026-03-26","datePublished":"2026-03-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
