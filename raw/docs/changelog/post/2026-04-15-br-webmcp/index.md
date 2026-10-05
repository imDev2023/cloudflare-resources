---
description: AI agents can now discover and execute website tools directly using WebMCP, enabling faster and more reliable browser automation.
title: Browser Run adds WebMCP support
image: https://developers.cloudflare.com/changelog/post/2026-04-15-br-webmcp/og.png?v=5e5ad98e632ce4c7
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 15, 2026

## Browser Run adds WebMCP support

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-15-br-webmcp/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Run](https://developers.cloudflare.com/browser-run/) (formerly Browser Rendering) now supports [WebMCP ↗︎](https://webmachinelearning.github.io/webmcp/) (Web Model Context Protocol), a new browser API from the Google Chrome team.

The Internet was built for humans, so navigating as an AI agent today is unreliable. WebMCP lets websites expose structured tools for AI agents to discover and call directly. Instead of slow screenshot-analyze-click loops, agents can call website functions like `searchFlights()` or `bookTicket()` with typed parameters, making browser automation faster, more reliable, and less fragile.

![Browser Run lab session showing WebMCP tools being discovered and executed in the Chrome DevTools console to book a hotel](https://developers.cloudflare.com/images/browser-run/webMCP.gif)

With WebMCP, you can:

- **Discover website tools** - Use `navigator.modelContextTesting.listTools()` to see available actions on any WebMCP-enabled site
- **Execute tools directly** - Call `navigator.modelContextTesting.executeTool()` with typed parameters
- **Handle human-in-the-loop interactions** - Some tools pause for user confirmation before completing sensitive actions

WebMCP requires Chrome beta features. We have an experimental pool with browser instances running Chrome beta so you can test emerging browser features before they reach stable Chrome. To start a WebMCP session, add `lab=true` to your `/devtools/browser` request:

```bash
curl -X POST "https://api.cloudflare.com/client/v4/accounts/{account_id}/browser-rendering/devtools/browser?lab=true&keep_alive=300000" \
  -H "Authorization: Bearer {api_token}"
```

Combined with the recently launched [CDP endpoint](https://developers.cloudflare.com/browser-run/cdp/), AI agents can also use WebMCP. Connect an [MCP client](https://developers.cloudflare.com/browser-run/cdp/mcp-clients/) to Browser Run via CDP, and your agent can discover and call website tools directly. Here's the same hotel booking demo, this time driven by an AI agent through OpenCode:

![Browser Run Live View showing an AI agent navigating a hotel booking site in real time](https://developers.cloudflare.com/images/browser-run/webMCPagent.gif)

For a step-by-step guide, refer to the [WebMCP documentation](https://developers.cloudflare.com/browser-run/features/webmcp/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-15-br-webmcp/#page","headline":"Browser Run adds WebMCP support","description":"AI agents can now discover and execute website tools directly using WebMCP, enabling faster and more reliable browser automation.","url":"https://developers.cloudflare.com/changelog/post/2026-04-15-br-webmcp/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-15-br-webmcp/og.png?v=5e5ad98e632ce4c7","dateModified":"2026-04-15","datePublished":"2026-04-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
