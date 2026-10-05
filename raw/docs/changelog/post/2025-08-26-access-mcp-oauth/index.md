---
description: Access self-hosted applications now support MCP OAuth. This allows MCP clients to connect to self-hosted applications through an Access-protected MCP server.
title: Manage and restrict access to internal MCP servers with Cloudflare Access
image: https://developers.cloudflare.com/changelog/post/2025-08-26-access-mcp-oauth/og.png?v=fb1d3e3f691357ac
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 26, 2025

## Manage and restrict access to internal MCP servers with Cloudflare Access

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-26-access-mcp-oauth/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now control who within your organization has access to internal MCP servers, by putting internal MCP servers behind [Cloudflare Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/).

[Self-hosted applications](https://developers.cloudflare.com/cloudflare-one/access-controls/ai-controls/linked-apps/) in Cloudflare Access now support OAuth for MCP server authentication. This allows Cloudflare to delegate access from any self-hosted application to an MCP server via OAuth. The OAuth access token authorizes the MCP server to make requests to your self-hosted applications on behalf of the authorized user, using that user's specific permissions and scopes.

For example, if you have an MCP server designed for internal use within your organization, you can configure Access policies to ensure that only authorized users can access it, regardless of which MCP client they use. Support for internal, self-hosted MCP servers also works with MCP server portals, allowing you to provide a single MCP endpoint for multiple MCP servers. For more on MCP server portals, read the [blog post ↗︎](https://blog.cloudflare.com/zero-trust-mcp-server-portals/) on the Cloudflare Blog.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-26-access-mcp-oauth/#page","headline":"Manage and restrict access to internal MCP servers with Cloudflare Access","description":"Access self-hosted applications now support MCP OAuth. This allows MCP clients to connect to self-hosted applications through an Access-protected MCP server.","url":"https://developers.cloudflare.com/changelog/post/2025-08-26-access-mcp-oauth/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-26-access-mcp-oauth/og.png?v=fb1d3e3f691357ac","dateModified":"2025-08-26","datePublished":"2025-08-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
