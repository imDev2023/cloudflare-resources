---
description: The maximum WebSocket message size limit for all Workers has been increased from 1 MiB to 32 MiB.
title: Workers WebSocket message size limit increased from 1 MiB to 32 MiB
image: https://developers.cloudflare.com/changelog/post/2025-10-31-increased-websocket-message-size-limit/og.png?v=13f68e2aef93be4b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 31, 2025

## Workers WebSocket message size limit increased from 1 MiB to 32 MiB

[Workers](https://developers.cloudflare.com/workers/) [Durable Objects](https://developers.cloudflare.com/durable-objects/) [Browser Run](https://developers.cloudflare.com/browser-run/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-31-increased-websocket-message-size-limit/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers, including those using [Durable Objects](https://developers.cloudflare.com/durable-objects/) and [Browser Rendering](https://developers.cloudflare.com/browser-run/), may now process WebSocket messages up to 32 MiB in size. Previously, this limit was 1 MiB.

This change allows Workers to handle use cases requiring large message sizes, such as processing Chrome Devtools Protocol messages.

For more information, please see the [Durable Objects startup limits](https://developers.cloudflare.com/durable-objects/platform/limits/#sqlite-backed-durable-objects-general-limits).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-31-increased-websocket-message-size-limit/#page","headline":"Workers WebSocket message size limit increased from 1 MiB to 32 MiB","description":"The maximum WebSocket message size limit for all Workers has been increased from 1 MiB to 32 MiB.","url":"https://developers.cloudflare.com/changelog/post/2025-10-31-increased-websocket-message-size-limit/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-31-increased-websocket-message-size-limit/og.png?v=13f68e2aef93be4b","dateModified":"2025-10-31","datePublished":"2025-10-31","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
