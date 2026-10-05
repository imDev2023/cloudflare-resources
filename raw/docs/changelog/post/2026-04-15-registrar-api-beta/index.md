---
description: Search, check, and register supported domains with the Cloudflare API.
title: Cloudflare Registrar API is now in beta
image: https://developers.cloudflare.com/changelog/post/2026-04-15-registrar-api-beta/og.png?v=1483d5fd2c3ef99b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 15, 2025

## Cloudflare Registrar API is now in beta

[Registrar](https://developers.cloudflare.com/registrar/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-15-registrar-api-beta/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Registrar API is now in beta.

You can now use the Cloudflare API to:

- Search for domain names.
- Check real-time availability and pricing.
- Register supported domains programmatically.

This beta supports a subset of popular extensions available through Cloudflare Registrar. Search returns suggestions across API-supported extensions, check confirms current availability and pricing, and registration starts a workflow that can complete immediately or be polled if it takes longer.

Because the Registrar API is part of the Cloudflare API, it can also be used in [Cloudflare MCP ↗︎](https://github.com/cloudflare/mcp) and other agent-driven workflows.

If you are using Cloudflare MCP or other agent-driven workflows, prompts can be as simple as:

- `Search for domain ideas for a coffee shop based in Evergreen, Colorado.`
- `Check whether example.com is available and show me the current price.`
- `Register example.com`

For supported operations, extension availability, and workflow details, refer to:

- [Registrar API guide ↗︎](https://developers.cloudflare.com/registrar/registrar-api/)
- [Registrar API reference ↗︎](https://developers.cloudflare.com/api/resources/registrar)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-15-registrar-api-beta/#page","headline":"Cloudflare Registrar API is now in beta","description":"Search, check, and register supported domains with the Cloudflare API.","url":"https://developers.cloudflare.com/changelog/post/2026-04-15-registrar-api-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-15-registrar-api-beta/og.png?v=1483d5fd2c3ef99b","dateModified":"2025-04-15","datePublished":"2025-04-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
