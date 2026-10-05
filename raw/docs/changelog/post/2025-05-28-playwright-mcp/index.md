---
description: You can now deploy Playwright MCP and use any MCP client to get AI models to interact with Browser Rendering
title: Playwright MCP server is now compatible with Browser Rendering
image: https://developers.cloudflare.com/changelog/post/2025-05-28-playwright-mcp/og.png?v=5a44d6b67f30e4ef
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 28, 2025

## Playwright MCP server is now compatible with Browser Rendering

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-28-playwright-mcp/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We're excited to share that you can now use the [Playwright MCP ↗︎](https://github.com/cloudflare/playwright-mcp) server with Browser Rendering.

Once you [deploy the server](https://developers.cloudflare.com/browser-run/playwright/playwright-mcp/#deploying), you can use any MCP client with it to interact with Browser Rendering. This allows you to run AI models that can automate browser tasks, such as taking screenshots, filling out forms, or scraping data.

![Access Analytics](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1420,height=914,format=webp/_astro/playground-ai-screenshot.v44jFMBu.png)

Playwright MCP is available as an npm package at [`@cloudflare/playwright-mcp` ↗︎](https://www.npmjs.com/package/@cloudflare/playwright-mcp). To install it, type:

npmyarnpnpmbun

```
npm i -D @cloudflare/playwright-mcp
```

```
yarn add -D @cloudflare/playwright-mcp
```

```
pnpm add -D @cloudflare/playwright-mcp
```

```
bun add -d @cloudflare/playwright-mcp
```

Deploying the server is then as easy as:

```ts
import { env } from "cloudflare:workers";
import { createMcpAgent } from "@cloudflare/playwright-mcp";

export const PlaywrightMCP = createMcpAgent(env.BROWSER);
export default PlaywrightMCP.mount("/sse");
```

Check out the full code at [GitHub ↗︎](https://github.com/cloudflare/playwright-mcp).

Learn more about Playwright MCP in our [documentation](https://developers.cloudflare.com/browser-run/playwright/playwright-mcp/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-28-playwright-mcp/#page","headline":"Playwright MCP server is now compatible with Browser Rendering","description":"You can now deploy Playwright MCP and use any MCP client to get AI models to interact with Browser Rendering","url":"https://developers.cloudflare.com/changelog/post/2025-05-28-playwright-mcp/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-28-playwright-mcp/og.png?v=5a44d6b67f30e4ef","dateModified":"2025-05-28","datePublished":"2025-05-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
