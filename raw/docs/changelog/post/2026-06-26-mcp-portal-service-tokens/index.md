---
description: You can now use an Access service token to connect autonomous agents and bots to an MCP server portal with full access to upstream MCP servers.
title: Service token support for MCP server portals
image: https://developers.cloudflare.com/changelog/post/2026-06-26-mcp-portal-service-tokens/og.png?v=5d9b6fc556a9d133
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 26, 2026

## Service token support for MCP server portals

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-26-mcp-portal-service-tokens/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now connect autonomous agents and bots to an [MCP server portal](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) using an [Access service token](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/). Service token sessions can reach upstream MCP servers through the portal without a browser-based OAuth flow.

To set this up:

- Add a [Service Auth policy](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/#service-auth) that matches your service token to the portal's Access application.
- Add a Service Auth policy that matches the same token to each linked MCP server's Access application.
- Turn **Require user auth** off ( `on_behalf: false`) for each linked server so the portal uses the admin credential instead of a per-user OAuth grant.

The bot connects with `CF-Access-Client-Id` and `CF-Access-Client-Secret` headers and sees the tools from every linked server it is authorized for. Servers that still require per-user OAuth are excluded from service token sessions because a service token cannot complete a per-user OAuth grant.

For step-by-step setup, refer to [Connect with a service token](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#connect-with-a-service-token).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-26-mcp-portal-service-tokens/#page","headline":"Service token support for MCP server portals","description":"You can now use an Access service token to connect autonomous agents and bots to an MCP server portal with full access to upstream MCP servers.","url":"https://developers.cloudflare.com/changelog/post/2026-06-26-mcp-portal-service-tokens/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-26-mcp-portal-service-tokens/og.png?v=5d9b6fc556a9d133","dateModified":"2026-06-26","datePublished":"2026-06-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
