---
description: Rename tools and prompts and edit their descriptions on MCP server portals without modifying the upstream server.
title: Tool and prompt aliases for MCP server portals
image: https://developers.cloudflare.com/changelog/post/2026-05-28-mcp-portal-tool-prompt-aliases/og.png?v=85af92e5af85ec93
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 28, 2026

## Tool and prompt aliases for MCP server portals

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-28-mcp-portal-tool-prompt-aliases/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

When you connect third-party MCP servers through [MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/), you have no control over how the server author named tools or wrote descriptions. Unclear names make it harder for AI agents to select the right tool and harder for users to understand what is available.

You can now [rename tools and prompts](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#rename-tools-and-prompts-with-aliases) and rewrite their descriptions directly on the portal, without modifying the upstream server. For example, a tool named `super_cool_tool` can become `search_customer_records` with a description tailored to your organization.

![Edit tool modal showing name and description fields for an MCP server tool](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1640,height=1144,format=webp/_astro/portal-edit-tool-modal.DrxORhBl.png)

Modified tools display a **Modified** label in the tools list so administrators can see which tools have been customized at a glance.

![Tools authorized list showing a modified label on a renamed tool](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1862,height=700,format=webp/_astro/portal-tools-authorized-modified.B674Xvip.png)

Aliases override the metadata that MCP clients receive. You can set them at two levels:

- **Per portal**: Applies only within a specific portal. Takes precedence over server-level aliases.
- **Per server**: Applies across all portals that use the server.

You can reset an alias at any time to restore the original upstream name.

For more information, refer to [Tool and prompt aliases](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#rename-tools-and-prompts-with-aliases).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-28-mcp-portal-tool-prompt-aliases/#page","headline":"Tool and prompt aliases for MCP server portals","description":"Rename tools and prompts and edit their descriptions on MCP server portals without modifying the upstream server.","url":"https://developers.cloudflare.com/changelog/post/2026-05-28-mcp-portal-tool-prompt-aliases/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-28-mcp-portal-tool-prompt-aliases/og.png?v=85af92e5af85ec93","dateModified":"2026-05-28","datePublished":"2026-05-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
