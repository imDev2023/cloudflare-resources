---
description: MCP server portals display a homepage with connection instructions and support a sign-out flow that revokes all portal sessions.
title: Homepage and sign-out for MCP server portals
image: https://developers.cloudflare.com/changelog/post/2026-04-17-mcp-portal-homepage-and-sign-out/og.png?v=4c8f28f49d047f33
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 17, 2026

## Homepage and sign-out for MCP server portals

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-17-mcp-portal-homepage-and-sign-out/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/) display a homepage when users visit the portal domain in a browser.

![MCP server portal homepage showing connection status and setup instructions](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1037,height=631,format=webp/_astro/portals-homepage-disconnected.BHbOwayQ.png)

The homepage shows:

- The portal name and organization branding
- The MCP endpoint URL with a copy button
- Per-client connection instructions for Claude Desktop, Workers AI Playground, OpenCode, Windsurf, and other MCP clients

Authenticated users see their email address and a **Sign out** button. Selecting **Sign out** revokes all portal-level OAuth grants, deletes upstream server OAuth states, and redirects through Cloudflare Access logout. A confirmation page shows a summary of the revoked sessions.

For more information, refer to [MCP server portals](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/mcp-portals/#portal-homepage).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-17-mcp-portal-homepage-and-sign-out/#page","headline":"Homepage and sign-out for MCP server portals","description":"MCP server portals display a homepage with connection instructions and support a sign-out flow that revokes all portal sessions.","url":"https://developers.cloudflare.com/changelog/post/2026-04-17-mcp-portal-homepage-and-sign-out/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-17-mcp-portal-homepage-and-sign-out/og.png?v=4c8f28f49d047f33","dateModified":"2026-04-17","datePublished":"2026-04-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
