---
description: More easily configure your Worker and call bindings from anywhere with an importable `env`
title: Import `env` to access bindings in your Worker's global scope
image: https://developers.cloudflare.com/changelog/post/2025-03-17-importable-env/og.png?v=a6a6bcaef544b8f3
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 17, 2025

## Import \`env\` to access bindings in your Worker's global scope

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-17-importable-env/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now access [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/) from anywhere in your Worker by importing the `env` object from `cloudflare:workers`.

Previously, `env` could only be accessed during a request. This meant that bindings could not be used in the top-level context of a Worker.

Now, you can import `env` and access bindings such as [secrets](https://developers.cloudflare.com/workers/configuration/secrets/) or [environment variables](https://developers.cloudflare.com/workers/configuration/environment-variables/) in the initial setup for your Worker:

```js
import { env } from "cloudflare:workers";
import ApiClient from "example-api-client";

// API_KEY and LOG_LEVEL now usable in top-level scope
const apiClient = ApiClient.new({ apiKey: env.API_KEY });
const LOG_LEVEL = env.LOG_LEVEL || "info";

export default {
	fetch(req) {
		// you can use apiClient or LOG_LEVEL, configured before any request is handled
	},
};
```

Note

Workers do not allow I/O from outside a request context. This means that even though `env` is accessible from the top-level scope, you will not be able to access every binding's methods.

For instance, environment variables and secrets are accessible, and you are able to call `env.NAMESPACE.get` to get a [Durable Object stub](https://developers.cloudflare.com/durable-objects/api/stub/) in the top-level context. However, calling methods on the Durable Object stub, making [calls to a KV store](https://developers.cloudflare.com/kv/api/), and [calling to other Workers](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings) will not work.

Additionally, `env` was normally accessed as a argument to a Worker's entrypoint handler, such as [`fetch`](https://developers.cloudflare.com/workers/runtime-apis/fetch/). This meant that if you needed to access a binding from a deeply nested function, you had to pass `env` as an argument through many functions to get it to the right spot. This could be cumbersome in complex codebases.

Now, you can access the bindings from anywhere in your codebase without passing `env` as an argument:

```js
// helpers.js
import { env } from "cloudflare:workers";

// env is *not* an argument to this function
export async function getValue(key) {
	let prefix = env.KV_PREFIX;
	return await env.KV.get(`${prefix}-${key}`);
}
```

For more information, see [documentation on accessing `env`](https://developers.cloudflare.com/workers/runtime-apis/bindings#how-to-access-env).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-17-importable-env/#page","headline":"Import `env` to access bindings in your Worker's global scope","description":"More easily configure your Worker and call bindings from anywhere with an importable env","url":"https://developers.cloudflare.com/changelog/post/2025-03-17-importable-env/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-03-17-importable-env/og.png?v=a6a6bcaef544b8f3","dateModified":"2025-03-17","datePublished":"2025-03-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
