---
description: Durable Objects now available on Workers Free plan.
title: Durable Objects on Workers Free plan
image: https://developers.cloudflare.com/changelog/post/2025-04-07-durable-objects-free-tier/og.png?v=cf791258ac719ee6
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 7, 2025

## Durable Objects on Workers Free plan

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-07-durable-objects-free-tier/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Durable Objects can now be used with zero commitment on the [Workers Free plan](https://developers.cloudflare.com/workers/platform/pricing/) allowing you to build AI agents with [Agents SDK](https://developers.cloudflare.com/agents/), collaboration tools, and real-time applications like chat or multiplayer games.

Durable Objects let you build stateful, serverless applications with millions of tiny coordination instances that run your application code alongside (in the same thread!) your durable storage. Each Durable Object can access its own SQLite database through a [Storage API](https://developers.cloudflare.com/durable-objects/best-practices/access-durable-objects-storage/). A Durable Object class is defined in a Worker script encapsulating the Durable Object's behavior when accessed from a Worker. To try the code below, click the button:

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/hello-world-do-template)

```js
import { DurableObject } from "cloudflare:workers";

// Durable Object
export class MyDurableObject extends DurableObject {
  ...
	async sayHello(name) {
		return `Hello, ${name}!`;
	}
}

// Worker
export default {
	async fetch(request, env) {
		// Every unique ID refers to an individual instance of the Durable Object class
		const id = env.MY_DURABLE_OBJECT.idFromName("foo");

		// A stub is a client used to invoke methods on the Durable Object
		const stub = env.MY_DURABLE_OBJECT.get(id);

		// Methods on the Durable Object are invoked via the stub
		const response = await stub.sayHello("world");

		return response;
	},
};
```

Free plan [limits](https://developers.cloudflare.com/durable-objects/platform/pricing/) apply to Durable Objects compute and storage usage. Limits allow developers to build real-world applications, with every Worker request able to call a Durable Object on the free plan.

For more information, checkout:

- [Documentation](https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/)
- [Zero-latency SQLite storage in every Durable Object blog ↗︎](https://blog.cloudflare.com/sqlite-in-durable-objects/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-07-durable-objects-free-tier/#page","headline":"Durable Objects on Workers Free plan","description":"Durable Objects now available on Workers Free plan.","url":"https://developers.cloudflare.com/changelog/post/2025-04-07-durable-objects-free-tier/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-07-durable-objects-free-tier/og.png?v=cf791258ac719ee6","dateModified":"2025-04-07","datePublished":"2025-04-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
