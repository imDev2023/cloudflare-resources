---
description: Create a Worker that spins up other Workers at runtime to execute code on-demand in milliseconds, in a secure, sandboxed environment.
title: Dynamic Workers, now in open beta
image: https://developers.cloudflare.com/changelog/post/2026-03-24-dynamic-workers-open-beta/og.png?v=0c8d22d69de625a8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 24, 2026

## Dynamic Workers, now in open beta

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-24-dynamic-workers-open-beta/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/) are now in [open beta ↗︎](https://blog.cloudflare.com/dynamic-workers/) for all paid Workers users. You can now have a Worker spin up other Workers, called Dynamic Workers, at runtime to execute code on-demand in a secure, sandboxed environment. Dynamic Workers start in milliseconds, making them well suited for fast, secure code execution at scale.

#### Use Dynamic Workers for

- **[Code Mode](https://developers.cloudflare.com/agents/tools/codemode/)**: LLMs are trained to write code. Run tool-calling logic written in code instead of stepping through many tool calls, which can save up to 80% in inference tokens and cost.
- **AI agents executing code**: Run code for tasks like data analysis, file transformation, API calls, and chained actions.
- **Running AI-generated code**: Run generated code for prototypes, projects, and automations in a secure, isolated sandboxed environment.
- **Fast development and previews**: Load prototypes, previews, and playgrounds in milliseconds.
- **Custom automations**: Create custom tools on the fly that execute a task, call an integration, or automate a workflow.

#### Executing Dynamic Workers

Dynamic Workers support two loading modes:

- `load(code)` — for one-time code execution (equivalent to calling `get()` with a null ID).
- `get(id, callback)` — caches a Dynamic Worker by ID so it can stay warm across requests. Use this when the same code will receive subsequent requests.

```js
export default {
	async fetch(request, env) {
		const worker = env.LOADER.load({
			compatibilityDate: "2026-01-01",
			mainModule: "src/index.js",
			modules: {
				"src/index.js": `
					export default {
						fetch() {
							return new Response("Hello from a dynamic Worker");
						},
					};
				`,
			},
			// Block all outbound network access from the Dynamic Worker.
			globalOutbound: null,
		});

		return worker.getEntrypoint().fetch(request);
	},
};
```

```ts
export default {
	async fetch(request: Request, env: Env): Promise<Response> {
		const worker = env.LOADER.load({
			compatibilityDate: "2026-01-01",
			mainModule: "src/index.js",
			modules: {
				"src/index.js": `
					export default {
						fetch() {
							return new Response("Hello from a dynamic Worker");
						},
					};
				`,
			},
			// Block all outbound network access from the Dynamic Worker.
			globalOutbound: null,
		});

		return worker.getEntrypoint().fetch(request);
	},
};
```

#### Helper libraries for Dynamic Workers

Here are 3 new libraries to help you build with Dynamic Workers:

- **[`@cloudflare/codemode` ↗︎](https://www.npmjs.com/package/@cloudflare/codemode)**: Replace individual tool calls with a single `code()` tool, so LLMs write and execute TypeScript that orchestrates multiple API calls in one pass.
- **[`@cloudflare/worker-bundler` ↗︎](https://www.npmjs.com/package/@cloudflare/worker-bundler)**: Resolve npm dependencies and bundle source files into ready-to-load modules for Dynamic Workers, all at runtime.
- **[`@cloudflare/shell` ↗︎](https://www.npmjs.com/package/@cloudflare/shell)**: Give your agent a virtual filesystem inside a Dynamic Worker with persistent storage backed by SQLite and R2.

#### Try it out

**Dynamic Workers Starter**

[![Deploy to Workers](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers)

Use this [starter ↗︎](https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers) to deploy a Worker that can load and execute Dynamic Workers.

**Dynamic Workers Playground**

[![Deploy to Workers](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers-playground)

Deploy the [Dynamic Workers Playground ↗︎](https://github.com/cloudflare/agents/tree/main/examples/dynamic-workers-playground) to write or import code, bundle it at runtime with `@cloudflare/worker-bundler`, execute it through a Dynamic Worker, and see real-time responses and execution logs.

For the full API reference and configuration options, refer to the [Dynamic Workers documentation](https://developers.cloudflare.com/dynamic-workers/).

#### Pricing

Dynamic Workers [pricing](https://developers.cloudflare.com/dynamic-workers/pricing/) is based on three dimensions: Dynamic Workers created daily, requests, and CPU time.

|  | Included | Additional usage |
| --- | --- | --- |
| **Dynamic Workers created daily** | 1,000 unique Dynamic Workers per month | +$0.002 per Dynamic Worker per day |
| **Requests** ¹ | 10 million per month | +$0.30 per million requests |
| **CPU time** ¹ | 30 million CPU milliseconds per month | +$0.02 per million CPU milliseconds |

¹ Uses [Workers Standard rates](https://developers.cloudflare.com/workers/platform/pricing/#workers) and will appear as part of your existing Workers bill, not as separate Dynamic Workers charges.

Note: Dynamic Workers requests and CPU time are already billed as part of your Workers plan and will count toward your Workers requests and CPU usage. The Dynamic Workers created daily charge is not yet active — you will not be billed for the number of Dynamic Workers created at this time. Pricing information is shared in advance so you can estimate future costs.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-24-dynamic-workers-open-beta/#page","headline":"Dynamic Workers, now in open beta","description":"Create a Worker that spins up other Workers at runtime to execute code on-demand in milliseconds, in a secure, sandboxed environment.","url":"https://developers.cloudflare.com/changelog/post/2026-03-24-dynamic-workers-open-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-24-dynamic-workers-open-beta/og.png?v=0c8d22d69de625a8","dateModified":"2026-03-24","datePublished":"2026-03-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
