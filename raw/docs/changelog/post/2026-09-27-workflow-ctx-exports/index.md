---
description: Workflows declared in the `exports` field of your Wrangler configuration are available on `ctx.exports`, including in local development.
title: Call Workflows declared in `exports` through `ctx.exports`
image: https://developers.cloudflare.com/changelog/post/2026-09-27-workflow-ctx-exports/og.png?v=0556f4588a74eeb1
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 27, 2026

## Call Workflows declared in \`exports\` through \`ctx.exports\`

[Workflows](https://developers.cloudflare.com/workflows/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-27-workflow-ctx-exports/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A Worker can now call the Workflows it declares in the [`exports`](https://developers.cloudflare.com/workers/wrangler/configuration/#workflow-exports) field of its Wrangler configuration through [`ctx.exports`](https://developers.cloudflare.com/workers/runtime-apis/context/#exports). You no longer need a `workflows` binding to call a Workflow from the Worker that defines it.

Each Workflow is keyed by class name, and has the same API as a Workflow binding:

*src/index.jsjs*

```js
export default {
	async fetch(request, env, ctx) {
		const instance = await ctx.exports.MyWorkflow.create({
			params: { name: "World" },
		});
		return Response.json({ id: instance.id });
	},
};
```

*src/index.tsts*

```ts
export default {
	async fetch(request, env, ctx): Promise<Response> {
		const instance = await ctx.exports.MyWorkflow.create({
			params: { name: "World" },
		});
		return Response.json({ id: instance.id });
	},
} satisfies ExportedHandler<Env>;
```

A `workflows` binding and a `workflow` export with the same `name` share their instances. You can move a Workflow from a binding to an export without losing its instances.

`wrangler dev`, the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/), and the [Workers Vitest integration](https://developers.cloudflare.com/workers/testing/vitest-integration/) run Workflows on `ctx.exports` locally. Local development requires Wrangler 4.142.0, `@cloudflare/vite-plugin` 1.61.0, or `@cloudflare/vitest-plugin` 1.3.0 or above.

In Vitest, `introspectWorkflow()` and `introspectWorkflowInstance()` still need a Workflow binding. To introspect a Workflow declared in `exports`, add a [test-only binding](https://developers.cloudflare.com/workers/testing/vitest-integration/test-apis/#introspect-workflows-declared-in-exports) to it.

For more information, refer to [Call a Workflow through `ctx.exports`](https://developers.cloudflare.com/workflows/build/workers-api/#call-a-workflow-through-ctxexports).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-27-workflow-ctx-exports/#page","headline":"Call Workflows declared in `exports` through `ctx.exports`","description":"Workflows declared in the exports field of your Wrangler configuration are available on ctx.exports, including in local development.","url":"https://developers.cloudflare.com/changelog/post/2026-09-27-workflow-ctx-exports/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-27-workflow-ctx-exports/og.png?v=0556f4588a74eeb1","dateModified":"2026-09-27","datePublished":"2026-09-27","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
