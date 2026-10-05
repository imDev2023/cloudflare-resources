---
description: evictDurableObject and evictAllDurableObjects let you test how Durable Objects behave across evictions in your Vitest tests.
title: Test Durable Object eviction with new cloudflare:test helpers
image: https://developers.cloudflare.com/changelog/post/2026-06-25-durable-object-eviction-test-helpers/og.png?v=90a70461c3484f3c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 25, 2026

## Test Durable Object eviction with new cloudflare:test helpers

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-25-durable-object-eviction-test-helpers/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The `@cloudflare/vitest-pool-workers` package now includes `evictDurableObject` and `evictAllDurableObjects` test helpers, exported from `cloudflare:test`.

These helpers let you test how a Durable Object behaves across evictions, simulating the production lifecycle where an idle Durable Object can be evicted from memory.

For more context, refer to [Lifecycle of a Durable Object](https://developers.cloudflare.com/durable-objects/concepts/durable-object-lifecycle/).

```ts
import { evictDurableObject, evictAllDurableObjects } from "cloudflare:test";
import { env } from "cloudflare:workers";

const id = env.COUNTER.idFromName("my-counter");
const stub = env.COUNTER.get(id);

// Evict the Durable Object instance pointed to by a specific stub
await evictDurableObject(stub);

// Close WebSockets instead of hibernating them
await evictDurableObject(stub, { webSockets: "close" });

// Evict all currently-running Durable Objects in evictable namespaces
await evictAllDurableObjects();
```

These helpers are available in `@cloudflare/vitest-pool-workers@0.16.20` and later.

Learn more in the [Test APIs reference](https://developers.cloudflare.com/workers/testing/vitest-integration/test-apis/#durable-objects) and the [Testing Durable Objects guide](https://developers.cloudflare.com/durable-objects/examples/testing-with-durable-objects/#testing-eviction).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-25-durable-object-eviction-test-helpers/#page","headline":"Test Durable Object eviction with new cloudflare:test helpers","description":"evictDurableObject and evictAllDurableObjects let you test how Durable Objects behave across evictions in your Vitest tests.","url":"https://developers.cloudflare.com/changelog/post/2026-06-25-durable-object-eviction-test-helpers/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-25-durable-object-eviction-test-helpers/og.png?v=90a70461c3484f3c","dateModified":"2026-06-25","datePublished":"2026-06-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
