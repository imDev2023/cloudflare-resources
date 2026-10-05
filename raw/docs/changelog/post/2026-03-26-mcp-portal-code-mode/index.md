---
description: MCP server portals support Code Mode, which reduces context window usage by collapsing tools into a single code execution tool.
title: Code Mode for MCP server portals
image: https://developers.cloudflare.com/changelog/post/2026-03-26-mcp-portal-code-mode/og.png?v=b98e8aa432e769fe
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 26, 2026

## Code Mode for MCP server portals

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-26-mcp-portal-code-mode/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) support [Code Mode MCP server patterns](https://developers.cloudflare.com/agents/model-context-protocol/codemode/), a technique that reduces context window usage by replacing individual tool definitions with a single code execution tool. Code Mode is turned on by default on all portals.

To turn it off, edit the portal in **Access controls** > **AI controls** and turn off **Code Mode** under **Basic information**.

When Code Mode is active, the portal exposes a single `code` tool instead of listing every tool from every upstream MCP server. The connected AI agent writes JavaScript that calls typed `codemode.*` methods for each upstream tool. The generated code runs in an isolated [Dynamic Worker](https://developers.cloudflare.com/workers/runtime-apis/bindings/worker-loader/) environment, keeping authentication credentials and environment variables out of the model context.

To use Code Mode, append `?codemode=search_and_execute` to your portal URL when connecting from an MCP client:

```txt
https://<subdomain>.<domain>/mcp?codemode=search_and_execute
```

For more information, refer to [Code Mode](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#code-mode).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-26-mcp-portal-code-mode/#page","headline":"Code Mode for MCP server portals","description":"MCP server portals support Code Mode, which reduces context window usage by collapsing tools into a single code execution tool.","url":"https://developers.cloudflare.com/changelog/post/2026-03-26-mcp-portal-code-mode/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-26-mcp-portal-code-mode/og.png?v=b98e8aa432e769fe","dateModified":"2026-03-26","datePublished":"2026-03-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
