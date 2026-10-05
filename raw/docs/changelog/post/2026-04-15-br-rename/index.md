---
description: We are renaming Browser Rendering to Browser Run and shipping Live View, Human in the Loop, Session Recordings, WebMCP, 4x higher limits, and more.
title: Browser Rendering is now Browser Run
image: https://developers.cloudflare.com/changelog/post/2026-04-15-br-rename/og.png?v=f575294bcb2d8efb
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 15, 2026

## Browser Rendering is now Browser Run

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-15-br-rename/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We are renaming Browser Rendering to **[Browser Run](https://developers.cloudflare.com/browser-run/)**. The name Browser Rendering never fully captured what the product does. Browser Run lets you run full browser sessions on Cloudflare's global network, drive them with code or AI, record and replay sessions, crawl pages for content, debug in real time, and let humans intervene when your agent needs help.

Along with the rename, we have increased limits for Workers Paid plans and redesigned the Browser Run dashboard.

We have 4x-ed concurrency limits for Workers Paid plan users:

- **Concurrent browsers per account**: 30 → **120 per account**
- **New browser instances**: 30 per minute → **1 per second**
- **REST API rate limits**: recently increased from [3 to 10 requests per second](https://developers.cloudflare.com/changelog/post/2026-03-04-br-rest-api-limit-increase/)

Rate limits across the [limits page](https://developers.cloudflare.com/browser-run/limits/) are now expressed in per-second terms, matching how they are enforced. No action is needed to benefit from the higher limits.

The [redesigned dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/workers/browser-run) now shows every request in a single Runs tab, not just browser sessions but also quick actions like screenshots, PDFs, markdown, and crawls. Filter by endpoint, view target URLs, status, and duration, and expand any row for more detail.

![Browser Run dashboard Runs tab with browser sessions and quick actions visible in one list, and an expanded crawl job showing its progress](https://developers.cloudflare.com/images/browser-run/BRdashboardredesign.png)

We are also shipping several new features:

- **[Live View, Human in the Loop, and Session Recordings](https://developers.cloudflare.com/changelog/post/2026-04-15-br-observability/)** - See what your agent is doing in real time, let humans step in when automation hits a wall, and replay any session after it ends.
- **[WebMCP](https://developers.cloudflare.com/changelog/post/2026-04-15-br-webmcp/)** - Websites can expose structured tools for AI agents to discover and call directly, replacing slow screenshot-analyze-click loops.

For the full story, read our Agents Week blog [Browser Run: Give your agents a browser ↗︎](https://blog.cloudflare.com/browser-run-for-ai-agents).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-15-br-rename/#page","headline":"Browser Rendering is now Browser Run","description":"We are renaming Browser Rendering to Browser Run and shipping Live View, Human in the Loop, Session Recordings, WebMCP, 4x higher limits, and more.","url":"https://developers.cloudflare.com/changelog/post/2026-04-15-br-rename/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-15-br-rename/og.png?v=f575294bcb2d8efb","dateModified":"2026-04-15","datePublished":"2026-04-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
