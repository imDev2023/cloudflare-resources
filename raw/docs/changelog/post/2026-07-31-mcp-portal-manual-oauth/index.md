---
description: Connect MCP servers that require a pre-registered OAuth client to an MCP server portal.
title: Static OAuth client credentials for MCP server portals
image: https://developers.cloudflare.com/changelog/post/2026-07-31-mcp-portal-manual-oauth/og.png?v=aad00bc5f850be82
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 31, 2026

## Static OAuth client credentials for MCP server portals

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-31-mcp-portal-manual-oauth/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) can now connect to upstream MCP servers that require a pre-registered OAuth client. This supports OAuth providers that do not offer Dynamic Client Registration or have disabled it. This unlocks portal connections to major SaaS providers such as Slack and GitHub, whose MCP servers do not yet support DCR.

When adding an MCP server, administrators can enter the client ID and client secret from an OAuth application registered with the upstream provider. The configuration also supports custom OAuth endpoints, scopes, and the `client_secret_post` and `client_secret_basic` token endpoint authentication methods.

Cloudflare stores the client secret encrypted. Users still authenticate to the upstream server with their own accounts when they connect through a portal.

For setup instructions, refer to [Configure manual OAuth credentials](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#configure-manual-oauth-credentials).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-31-mcp-portal-manual-oauth/#page","headline":"Static OAuth client credentials for MCP server portals","description":"Connect MCP servers that require a pre-registered OAuth client to an MCP server portal.","url":"https://developers.cloudflare.com/changelog/post/2026-07-31-mcp-portal-manual-oauth/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-31-mcp-portal-manual-oauth/og.png?v=aad00bc5f850be82","dateModified":"2026-07-31","datePublished":"2026-07-31","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
