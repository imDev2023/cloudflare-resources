---
description: Easily explore, build, and run GraphQL queries with two new tools
title: New GraphQL Analytics API Explorer and MCP Server
image: https://developers.cloudflare.com/changelog/post/2025-05-23-graphql-api-explorer/og.png?v=91ee50e38ea19aa5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 23, 2025

## New GraphQL Analytics API Explorer and MCP Server

[Analytics](https://developers.cloudflare.com/analytics/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-23-graphql-api-explorer/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We’ve launched two powerful new tools to make the GraphQL Analytics API more accessible:

#### GraphQL API Explorer

The new [GraphQL API Explorer ↗︎](https://graphql.cloudflare.com/explorer) helps you build, test, and run queries directly in your browser. Features include:

- In-browser schema documentation to browse available datasets and fields
- Interactive query editor with autocomplete and inline documentation
- A "Run in GraphQL API Explorer" button to execute example queries from our docs
- Seamless OAuth authentication — no manual setup required

![GraphQL API Explorer](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2626,height=974,format=webp/_astro/graphql-api-explorer.CPUNZZ5B.png)

#### GraphQL Model Context Protocol (MCP) Server

MCP Servers let you use natural language tools like Claude to generate structured queries against your data. See our [blog post ↗︎](https://blog.cloudflare.com/thirteen-new-mcp-servers-from-cloudflare/) for details on how they work and which servers are available. The new [GraphQL MCP server ↗︎](https://github.com/cloudflare/mcp-server-cloudflare/tree/main/apps/graphql) helps you discover and generate useful queries for the GraphQL Analytics API. With this server, you can:

- Explore what data is available to query
- Generate and refine queries using natural language, with one-click links to run them in the API Explorer
- Build dashboards and visualizations from structured query outputs

Example prompts include:

- “Show me HTTP traffic for the last 7 days for example.com”
- “What GraphQL node returns firewall events?”
- “Can you generate a link to the Cloudflare GraphQL API Explorer with a pre-populated query and variables?”

We’re continuing to expand these tools, and your feedback helps shape what’s next. [Explore the documentation](https://developers.cloudflare.com/analytics/graphql-api/) to learn more and get started.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-23-graphql-api-explorer/#page","headline":"New GraphQL Analytics API Explorer and MCP Server","description":"Easily explore, build, and run GraphQL queries with two new tools","url":"https://developers.cloudflare.com/changelog/post/2025-05-23-graphql-api-explorer/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-23-graphql-api-explorer/og.png?v=91ee50e38ea19aa5","dateModified":"2025-05-23","datePublished":"2025-05-23","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
