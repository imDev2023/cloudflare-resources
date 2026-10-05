---
description: Code Mode v0.2.0–v0.2.1 adds a new @cloudflare/codemode/mcp export with codeMcpServer and openApiMcpServer, makes the main entry point dependency-free, and lets you inject custom modules into the sandbox.
title: "@cloudflare/codemode v0.2.1: MCP barrel export, zero-dependency main entry point, and custom sandbox modules"
image: https://developers.cloudflare.com/changelog/post/2026-03-17-codemode-sdk-v0.2.1/og.png?v=53123f8e384087ba
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 17, 2026

## @cloudflare/codemode v0.2.1: MCP barrel export, zero-dependency main entry point, and custom sandbox modules

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-17-codemode-sdk-v0.2.1/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The latest releases of [`@cloudflare/codemode` ↗︎](https://www.npmjs.com/package/@cloudflare/codemode) add a new MCP barrel export, remove `ai` and `zod` as required peer dependencies from the main entry point, and give you more control over the sandbox.

#### New `@cloudflare/codemode/mcp` export

A new `@cloudflare/codemode/mcp` entry point provides two functions that wrap MCP servers with Code Mode:

- **`codeMcpServer({ server, executor })`** — wraps an existing MCP server with a single `code` tool where each upstream tool becomes a typed `codemode.*` method.
- **`openApiMcpServer({ spec, executor, request })`** — creates `search` and `execute` MCP tools from an OpenAPI spec with host-side request proxying and automatic `$ref` resolution.

```js
import { codeMcpServer } from "@cloudflare/codemode/mcp";
import { DynamicWorkerExecutor } from "@cloudflare/codemode";

const executor = new DynamicWorkerExecutor({ loader: env.LOADER });

// Wrap an existing MCP server — all its tools become
// typed methods the LLM can call from generated code
const server = await codeMcpServer({ server: upstreamMcp, executor });
```

```ts
import { codeMcpServer } from "@cloudflare/codemode/mcp";
import { DynamicWorkerExecutor } from "@cloudflare/codemode";

const executor = new DynamicWorkerExecutor({ loader: env.LOADER });

// Wrap an existing MCP server — all its tools become
// typed methods the LLM can call from generated code
const server = await codeMcpServer({ server: upstreamMcp, executor });
```

#### Zero-dependency main entry point

**Breaking change in v0.2.0:** `generateTypes` and the `ToolDescriptor` / `ToolDescriptors` types have moved to `@cloudflare/codemode/ai`:

```js
// Before
import { generateTypes } from "@cloudflare/codemode";

// After
import { generateTypes } from "@cloudflare/codemode/ai";
```

```ts
// Before
import { generateTypes } from "@cloudflare/codemode";

// After
import { generateTypes } from "@cloudflare/codemode/ai";
```

The main entry point (`@cloudflare/codemode`) no longer requires the `ai` or `zod` peer dependencies. It now exports:

| Export | Description |
| --- | --- |
| `sanitizeToolName` | Sanitize tool names into valid JS identifiers |
| `normalizeCode` | Normalize LLM-generated code into async arrow functions |
| `generateTypesFromJsonSchema` | Generate TypeScript type definitions from plain JSON Schema |
| `jsonSchemaToType` | Convert a single JSON Schema to a TypeScript type string |
| `DynamicWorkerExecutor` | Sandboxed code execution via Dynamic Worker Loader |
| `ToolDispatcher` | RPC target for dispatching tool calls from sandbox to host |

The `ai` and `zod` peer dependencies are now optional — only required when importing from `@cloudflare/codemode/ai`.

#### Custom sandbox modules

`DynamicWorkerExecutor` now accepts an optional `modules` option to inject custom ES modules into the sandbox:

```js
const executor = new DynamicWorkerExecutor({
	loader: env.LOADER,
	modules: {
		"utils.js": `export function add(a, b) { return a + b; }`,
	},
});

// Sandbox code can then: import { add } from "utils.js"
```

```ts
const executor = new DynamicWorkerExecutor({
	loader: env.LOADER,
	modules: {
		"utils.js": `export function add(a, b) { return a + b; }`,
	},
});

// Sandbox code can then: import { add } from "utils.js"
```

#### Internal normalization and sanitization

`DynamicWorkerExecutor` now normalizes code and sanitizes tool names internally. You no longer need to call `normalizeCode()` or `sanitizeToolName()` before passing code and functions to `execute()`.

#### Upgrade

```sh
npm i @cloudflare/codemode@latest
```

See the [Code Mode documentation](https://developers.cloudflare.com/agents/tools/codemode/) for the full API reference.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-17-codemode-sdk-v0.2.1/#page","headline":"@cloudflare/codemode v0.2.1: MCP barrel export, zero-dependency main entry point, and custom sandbox modules","description":"Code Mode v0.2.0–v0.2.1 adds a new @cloudflare/codemode/mcp export with codeMcpServer and openApiMcpServer, makes the main entry point dependency-free, and lets you inject custom modules into the sandbox.","url":"https://developers.cloudflare.com/changelog/post/2026-03-17-codemode-sdk-v0.2.1/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-17-codemode-sdk-v0.2.1/og.png?v=53123f8e384087ba","dateModified":"2026-03-17","datePublished":"2026-03-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
