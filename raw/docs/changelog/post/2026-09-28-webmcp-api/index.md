---
description: WebMCP now works in Kitesurf sessions, uses the document.modelContext API, and can be tested in the Chrome DevTools WebMCP panel.
title: Browser Run adds WebMCP to Kitesurf and moves to document.modelContext
image: https://developers.cloudflare.com/changelog/post/2026-09-28-webmcp-api/og.png?v=c1dc93ee8d6fa496
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 28, 2026

## Browser Run adds WebMCP to Kitesurf and moves to document.modelContext

[Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-28-webmcp-api/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[WebMCP](https://developers.cloudflare.com/browser-run/features/webmcp/) now works in [Kitesurf](https://developers.cloudflare.com/browser-run/kitesurf/) sessions as well as [Lab sessions](https://developers.cloudflare.com/browser-run/features/webmcp/#get-started). Both backends use the `document.modelContext` API from the [WebMCP Community Group draft ↗︎](https://webmachinelearning.github.io/webmcp/). Lab sessions no longer expose `navigator.modelContextTesting`.

To list and run page tools:

- **Chrome DevTools**: Use the **Application** > **WebMCP** panel in the live view of a Lab session or in the [Kitesurf playground ↗︎](https://kitesurf.dev/).
- **AI agents**: Start [Chrome DevTools MCP](https://developers.cloudflare.com/browser-run/features/webmcp/#using-an-ai-agent) with the `--category-experimental-webmcp` flag to add the `list_webmcp_tools` and `execute_webmcp_tool` tools.
- **CDP clients**: Use the `WebMCP` CDP domain.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-28-webmcp-api/#page","headline":"Browser Run adds WebMCP to Kitesurf and moves to document.modelContext","description":"WebMCP now works in Kitesurf sessions, uses the document.modelContext API, and can be tested in the Chrome DevTools WebMCP panel.","url":"https://developers.cloudflare.com/changelog/post/2026-09-28-webmcp-api/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-28-webmcp-api/og.png?v=c1dc93ee8d6fa496","dateModified":"2026-09-28","datePublished":"2026-09-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
