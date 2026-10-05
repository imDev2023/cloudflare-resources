---
description: You no longer have to configure bindings explicitly when they point back to your own Worker's top-level exports
title: Automatic loopback bindings via ctx.exports
image: https://developers.cloudflare.com/changelog/post/2025-09-26-ctx-exports/og.png?v=acdd1cc857044dd6
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 26, 2025

## Automatic loopback bindings via ctx.exports

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-26-ctx-exports/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The [`ctx.exports` API](https://developers.cloudflare.com/workers/runtime-apis/context/#exports) contains automatically-configured bindings corresponding to your Worker's top-level exports. For each top-level export extending `WorkerEntrypoint`, `ctx.exports` will contain a [Service Binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings) by the same name, and for each export extending `DurableObject` (and for which storage has been configured via a [migration](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/)), `ctx.exports` will contain a [Durable Object namespace binding](https://developers.cloudflare.com/durable-objects/api/namespace/). This means you no longer have to configure these bindings explicitly in `wrangler.jsonc`/`wrangler.toml`.

Example:

```js
import { WorkerEntrypoint } from "cloudflare:workers";

export class Greeter extends WorkerEntrypoint {
  greet(name) {
    return `Hello, ${name}!`;
  }
}

export default {
  async fetch(request, env, ctx) {
    let greeting = await ctx.exports.Greeter.greet("World")
    return new Response(greeting);
  }
}
```

At present, you must use [the `enable_ctx_exports` compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags#enable-ctxexports) to enable this API, though it will be on by default in the future.

[See the API reference for more information.](https://developers.cloudflare.com/workers/runtime-apis/context/#exports)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-26-ctx-exports/#page","headline":"Automatic loopback bindings via ctx.exports","description":"You no longer have to configure bindings explicitly when they point back to your own Worker's top-level exports","url":"https://developers.cloudflare.com/changelog/post/2025-09-26-ctx-exports/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-26-ctx-exports/og.png?v=acdd1cc857044dd6","dateModified":"2025-09-26","datePublished":"2025-09-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
