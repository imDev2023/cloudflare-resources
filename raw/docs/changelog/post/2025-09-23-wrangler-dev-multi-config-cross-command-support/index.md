---
description: Workers running with wrangler dev using multiple config files can now communicate with Workers running in separate dev commands.
title: Improved support for running multiple Workers with `wrangler dev`
image: https://developers.cloudflare.com/changelog/post/2025-09-23-wrangler-dev-multi-config-cross-command-support/og.png?v=afa5a52d2178f78b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 23, 2025

## Improved support for running multiple Workers with \`wrangler dev\`

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-23-wrangler-dev-multi-config-cross-command-support/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can run multiple Workers in a single dev command by passing multiple config files to `wrangler dev`:

```sh
wrangler dev --config ./web/wrangler.jsonc --config ./api/wrangler.jsonc
```

Previously, if you ran the command above and then also ran wrangler dev for a different Worker, the Workers running in separate wrangler dev sessions could not communicate with each other. This prevented you from being able to use [Service Bindings ↗︎](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/) and [Tail Workers ↗︎](https://developers.cloudflare.com/workers/observability/logs/tail-workers/) in local development, when running separate wrangler dev sessions.

Now, the following works as expected:

```sh
# Terminal 1: Run your application that includes both Web and API workers
wrangler dev --config ./web/wrangler.jsonc --config ./api/wrangler.jsonc

# Terminal 2: Run your auth worker separately
wrangler dev --config ./auth/wrangler.jsonc
```

These Workers can now communicate with each other across separate dev commands, regardless of your development setup.

*./api/src/index.tsjs*

```js
export default {
	async fetch(request, env) {
		// This service binding call now works across dev commands
		const authorized = await env.AUTH.isAuthorized(request);

		if (!authorized) {
			return new Response("Unauthorized", { status: 401 });
		}

		return new Response("Hello from API Worker!", { status: 200 });
	},
};
```

Check out the [Developing with multiple Workers](https://developers.cloudflare.com/workers/local-development/multi-workers) guide to learn more about the different approaches and when to use each one.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-23-wrangler-dev-multi-config-cross-command-support/#page","headline":"Improved support for running multiple Workers with `wrangler dev`","description":"Workers running with wrangler dev using multiple config files can now communicate with Workers running in separate dev commands.","url":"https://developers.cloudflare.com/changelog/post/2025-09-23-wrangler-dev-multi-config-cross-command-support/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-23-wrangler-dev-multi-config-cross-command-support/og.png?v=afa5a52d2178f78b","dateModified":"2025-09-23","datePublished":"2025-09-23","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
