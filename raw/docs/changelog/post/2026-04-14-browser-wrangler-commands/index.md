---
description: Use wrangler browser commands to manage Browser Rendering sessions from the CLI.
title: Manage Browser Rendering sessions with Wrangler CLI
image: https://developers.cloudflare.com/changelog/post/2026-04-14-browser-wrangler-commands/og.png?v=490c6040ba0a8db2
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 14, 2026

## Manage Browser Rendering sessions with Wrangler CLI

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-14-browser-wrangler-commands/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Rendering](https://developers.cloudflare.com/browser-run/) now supports `wrangler browser` commands, letting you create, manage, and view browser sessions directly from your terminal, streamlining your workflow. Since Wrangler handles authentication, you do not need to pass API tokens in your commands.

The following commands are available:

| Command | Description |
| --- | --- |
| `wrangler browser create` | Create a new browser session |
| `wrangler browser close` | Close a session |
| `wrangler browser list` | List active sessions |
| `wrangler browser view` | View a live browser session |

The `create` command spins up a browser instance on Cloudflare's network and returns a session URL. Once created, you can connect to the session using any [CDP](https://developers.cloudflare.com/browser-run/cdp/)-compatible client like [Puppeteer](https://developers.cloudflare.com/browser-run/cdp/puppeteer/), [Playwright](https://developers.cloudflare.com/browser-run/cdp/playwright/), or [MCP clients](https://developers.cloudflare.com/browser-run/cdp/mcp-clients/) to automate browsing, scrape content, or debug remotely.

```sh
wrangler browser create
```

Use `--keepAlive` to set the session keep-alive duration (60-600 seconds):

```sh
wrangler browser create --keepAlive 300
```

The `view` command auto-selects when only one session exists, or prompts for selection when multiple sessions are available.

All commands support `--json` for structured output, and because these are CLI commands, you can incorporate them into scripts to automate session management.

For full usage details, refer to the [Wrangler commands documentation](https://developers.cloudflare.com/browser-run/reference/wrangler-commands/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-14-browser-wrangler-commands/#page","headline":"Manage Browser Rendering sessions with Wrangler CLI","description":"Use wrangler browser commands to manage Browser Rendering sessions from the CLI.","url":"https://developers.cloudflare.com/changelog/post/2026-04-14-browser-wrangler-commands/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-14-browser-wrangler-commands/og.png?v=490c6040ba0a8db2","dateModified":"2026-04-14","datePublished":"2026-04-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
