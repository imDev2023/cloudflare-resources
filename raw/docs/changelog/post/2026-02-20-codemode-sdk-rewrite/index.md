---
description: The Code Mode SDK has been rewritten with `createCodeTool()`, `DynamicWorkerExecutor`, and a new `Executor` interface that allows for Bring Your Own (BYO) sandbox.
title: "@cloudflare/codemode v0.1.0: a new runtime agnostic modular architecture"
image: https://developers.cloudflare.com/changelog/post/2026-02-20-codemode-sdk-rewrite/og.png?v=d23e3a8df0911973
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 20, 2026

## @cloudflare/codemode v0.1.0: a new runtime agnostic modular architecture

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-20-codemode-sdk-rewrite/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The [`@cloudflare/codemode` ↗︎](https://www.npmjs.com/package/@cloudflare/codemode) package has been rewritten into a modular, runtime-agnostic SDK.

[Code Mode ↗︎](https://blog.cloudflare.com/code-mode/) enables LLMs to write and execute code that orchestrates your tools, instead of calling them one at a time. This can (and does) yield significant token savings, reduces context window pressure and improves overall model performance on a task.

The new `Executor` interface is runtime agnostic and comes with a prebuilt `DynamicWorkerExecutor` to run generated code in a [Dynamic Worker Loader](https://developers.cloudflare.com/workers/runtime-apis/bindings/worker-loader/).

#### Breaking changes

- Removed `experimental_codemode()` and `CodeModeProxy` — the package no longer owns an LLM call or model choice
- New import path: `createCodeTool()` is now exported from `@cloudflare/codemode/ai`

#### New features

- **`createCodeTool()`** — Returns a standard AI SDK `Tool` to use in your AI agents.
- **`Executor` interface** — Minimal `execute(code, fns)` contract. Implement for any code sandboxing primitive or runtime.

#### `DynamicWorkerExecutor`

Runs code in a [Dynamic Worker](https://developers.cloudflare.com/workers/runtime-apis/bindings/worker-loader/). It comes with the following features:

- **Network isolation** — `fetch()` and `connect()` blocked by default ( `globalOutbound: null`) when using `DynamicWorkerExecutor`
- **Console capture** — `console.log/warn/error` captured and returned in `ExecuteResult.logs`
- **Execution timeout** — Configurable via `timeout` option (default 30s)

#### Usage

```js
import { createCodeTool } from "@cloudflare/codemode/ai";
import { DynamicWorkerExecutor } from "@cloudflare/codemode";
import { streamText } from "ai";

const executor = new DynamicWorkerExecutor({ loader: env.LOADER });
const codemode = createCodeTool({ tools: myTools, executor });

const result = streamText({
	model,
	tools: { codemode },
	messages,
});
```

```ts
import { createCodeTool } from "@cloudflare/codemode/ai";
import { DynamicWorkerExecutor } from "@cloudflare/codemode";
import { streamText } from "ai";

const executor = new DynamicWorkerExecutor({ loader: env.LOADER });
const codemode = createCodeTool({ tools: myTools, executor });

const result = streamText({
	model,
	tools: { codemode },
	messages,
});
```

#### Wrangler configuration

```jsonc
{
	"worker_loaders": [{ "binding": "LOADER" }],
}
```

```toml
[[worker_loaders]]
binding = "LOADER"
```

See the [Code Mode documentation](https://developers.cloudflare.com/agents/tools/codemode/) for full API reference and examples.

#### Upgrade

```sh
npm i @cloudflare/codemode@latest
```

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-20-codemode-sdk-rewrite/#page","headline":"@cloudflare/codemode v0.1.0: a new runtime agnostic modular architecture","description":"The Code Mode SDK has been rewritten with createCodeTool(), DynamicWorkerExecutor, and a new Executor interface that allows for Bring Your Own (BYO) sandbox.","url":"https://developers.cloudflare.com/changelog/post/2026-02-20-codemode-sdk-rewrite/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-20-codemode-sdk-rewrite/og.png?v=d23e3a8df0911973","dateModified":"2026-02-20","datePublished":"2026-02-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
