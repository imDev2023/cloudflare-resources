---
description: Active outbound TCP sockets and outbound WebSocket connections now prevent a Durable Object from being evicted while the connection is open.
title: Outbound connections keep Durable Objects alive
image: https://developers.cloudflare.com/changelog/post/2026-06-19-outbound-connections-keep-dos-alive/og.png?v=3e95175c69a145d0
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 19, 2026

## Outbound connections keep Durable Objects alive

[Durable Objects](https://developers.cloudflare.com/durable-objects/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-19-outbound-connections-keep-dos-alive/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Durable Objects now remain alive for the duration of active outbound connections created via [`connect()`](https://developers.cloudflare.com/workers/runtime-apis/tcp-sockets/) or an outbound WebSocket. Previously, a Durable Object would be evicted after 70-140 seconds of no incoming traffic, even if the object had an open outbound connection, which is a common pattern when streaming responses from a large language model (LLM) over TCP or an outbound WebSocket.

With this change, each active outbound connection prevents eviction. Once all outbound connections close, the standard 70-140 second inactivity window applies before the Durable Object is evicted.

#### Before: streaming connections were cut off by eviction

![Timeline showing a Durable Object evicted 70-140 seconds after the last incoming request, cutting off an in-flight LLM stream while the outbound connection is still open](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=820,height=360,format=svg/_astro/outbound-connection-before.jZgN3tY3.svg)

#### After: active outbound connections keep the Durable Object alive

![Timeline showing the same outbound stream completing because the active connection keeps the Durable Object alive, with the inactivity window starting only after the connection closes](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=820,height=360,format=svg/_astro/outbound-connection-after.CxPT16q0.svg)

If you are [building agents on Cloudflare](https://developers.cloudflare.com/agents/), this is especially relevant. An agent that streams tokens from an LLM while [calling models](https://developers.cloudflare.com/agents/concepts/calling-llms/), or that performs [long-running tasks](https://developers.cloudflare.com/agents/concepts/agentic-patterns/long-running-agents/) over an outbound connection, now stays alive for the duration of that connection instead of being evicted mid-stream.

**Limits:**

- Each outbound connection keeps the Durable Object alive for a maximum of **15 minutes**. After 15 minutes, the connection stops preventing eviction (the connection itself continues operating), and the [standard eviction rules](https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/) resume.
- The Durable Object's existing [per-account instance limits](https://developers.cloudflare.com/durable-objects/platform/limits/) still apply.

For more information, refer to [Lifecycle of a Durable Object](https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-19-outbound-connections-keep-dos-alive/#page","headline":"Outbound connections keep Durable Objects alive","description":"Active outbound TCP sockets and outbound WebSocket connections now prevent a Durable Object from being evicted while the connection is open.","url":"https://developers.cloudflare.com/changelog/post/2026-06-19-outbound-connections-keep-dos-alive/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-19-outbound-connections-keep-dos-alive/og.png?v=3e95175c69a145d0","dateModified":"2026-06-19","datePublished":"2026-06-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
