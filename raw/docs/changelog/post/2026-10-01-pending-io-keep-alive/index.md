---
description: For Workers with a compatibility date of 2026-10-01 or later, pending I/O prevents eviction for up to 15 minutes.
title: Pending I/O operations allow Durable Objects to continue long-running work without a connected client
image: https://developers.cloudflare.com/changelog/post/2026-10-01-pending-io-keep-alive/og.png?v=c225f474af7edfd9
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 1, 2026

## Pending I/O operations allow Durable Objects to continue long-running work without a connected client

[Durable Objects](https://developers.cloudflare.com/durable-objects/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-01-pending-io-keep-alive/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Durable Objects remain active while handling a request from a connected client. This change applies when no client is connected, such as when an agent continues a submitted job after its client disconnects.

This behavior is the default for Workers with a compatibility date of `2026-10-01` or later. To use it with an earlier date, add the [`durable_object_io_tasks_prevent_eviction`](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#durable-object-io-tasks-prevent-eviction) compatibility flag. To opt out, add the `durable_object_io_tasks_do_not_prevent_eviction` flag.

Pending [service binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/) requests now keep Durable Objects running while they wait for a response. Pending calls to another Durable Object through remote procedure call (RPC) or `fetch()`, as well as `this.ctx.container.monitor()`, now also keep the Durable Object running.

Promises passed to `this.ctx.waitUntil()` and pending `setTimeout()` and `setInterval()` timers also receive this protection.

Previously, Cloudflare could shut down an idle Durable Object while one of these operations remained pending without a connected client. This could stop unfinished work.

This change helps you run long-running tasks such as agents. An agent can call tools through service bindings, coordinate with other Durable Objects, or wait for a container process without relying on the original client to remain connected.

Outbound `fetch()` requests to external services, TCP sockets, and outbound WebSockets already keep Durable Objects running.

Each pending operation prevents idle shutdown for up to 15 minutes. Starting another one later can extend the Durable Object's time in memory. The limit applies to each operation, not to the total time in memory.

![Timeline of a service binding fetch, an RPC call, and monitor() each preventing eviction for up to 15 minutes](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=820,height=360,format=svg/_astro/pending-io-keep-alive.vVfDqYTX.svg)

Duration charges continue while an operation prevents eviction.

For more information, refer to [Lifecycle of a Durable Object](https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-10-01-pending-io-keep-alive/#page","headline":"Pending I/O operations allow Durable Objects to continue long-running work without a connected client","description":"For Workers with a compatibility date of 2026-10-01 or later, pending I/O prevents eviction for up to 15 minutes.","url":"https://developers.cloudflare.com/changelog/post/2026-10-01-pending-io-keep-alive/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-10-01-pending-io-keep-alive/og.png?v=c225f474af7edfd9","dateModified":"2026-10-01","datePublished":"2026-10-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
