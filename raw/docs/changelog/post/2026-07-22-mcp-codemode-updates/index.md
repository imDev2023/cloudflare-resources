---
description: Agents SDK reduces repeated MCP schema conversion and adds direct Code Mode runtime APIs for hosts that do not use the AI SDK.
title: Agents SDK reduces MCP schema conversion, adds exposure controls for MCP in Think and Code Mode SDK adds direct host APIs
image: https://developers.cloudflare.com/changelog/post/2026-07-22-mcp-codemode-updates/og.png?v=31ce61542ebfda04
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 22, 2026

## Agents SDK reduces MCP schema conversion, adds exposure controls for MCP in Think and Code Mode SDK adds direct host APIs

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-22-mcp-codemode-updates/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This release reduces repeated MCP schema conversion and adds an opt-out for Think's automatic MCP tool exposure. It also lets non-AI-SDK hosts invoke the durable Code Mode runtime directly.

#### Control direct MCP tool exposure in Think

Agents SDK MCP clients now reuse converted input and output schemas while a live connection keeps the same tool catalog. This avoids converting every MCP JSON Schema to Zod again for each model turn.

`@cloudflare/think` also adds `includeMcpTools`. Set it to `false` when you expose MCP tools through Code Mode or another mechanism outside Think's automatic tool set:

```js
import { Think } from "@cloudflare/think";

export class MyAgent extends Think {
	includeMcpTools = false;
	waitForMcpConnections = true;
}
```

```ts
import { Think } from "@cloudflare/think";

export class MyAgent extends Think<Env> {
	includeMcpTools = false;
	waitForMcpConnections = true;
}
```

This setting skips Think's automatic `getAITools()` call. MCP registration, restoration, discovery, raw catalog access, direct calls, and Code Mode connectors continue to work.

Use [`listTools()`](https://developers.cloudflare.com/agents/model-context-protocol/apis/client-api/#thismcplisttools) when you only need the raw MCP catalog. For connector setup, refer to [Use MCP tools with Code Mode](https://developers.cloudflare.com/agents/tools/codemode/mcp/).

#### Invoke the Code Mode runtime without the AI SDK

`@cloudflare/codemode@latest` adds `execute()`, `search()`, and `describe()` to the durable runtime handle. MCP servers and other hosts can now execute code and discover connector methods without adapting the runtime to an AI SDK tool.

```js
const matches = await runtime.search("create issue");
const docs = await runtime.describe(matches.results[0].path);
const outcome = await runtime.execute({
	code: `async () => github.create_issue({ title: "Bug" })`,
});
```

```ts
const matches = await runtime.search("create issue");
const docs = await runtime.describe(matches.results[0].path);
const outcome = await runtime.execute({
	code: `async () => github.create_issue({ title: "Bug" })`,
});
```

Search and describe results include `requiresApproval: true` for protected connector methods. Resolve a paused execution with the existing `approve()` and `reject()` methods.

For setup and exact method types, refer to [Create a durable Code Mode runtime](https://developers.cloudflare.com/agents/tools/codemode/durable-runtime/) and the [Code Mode API reference](https://developers.cloudflare.com/agents/tools/codemode/api-reference/).

#### Upgrade

npmyarnpnpmbun

```
npm i agents@latest @cloudflare/think@latest @cloudflare/codemode@latest
```

```
yarn add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest
```

```
pnpm add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest
```

```
bun add agents@latest @cloudflare/think@latest @cloudflare/codemode@latest
```

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-22-mcp-codemode-updates/#page","headline":"Agents SDK reduces MCP schema conversion, adds exposure controls for MCP in Think and Code Mode SDK adds direct host APIs","description":"Agents SDK reduces repeated MCP schema conversion and adds direct Code Mode runtime APIs for hosts that do not use the AI SDK.","url":"https://developers.cloudflare.com/changelog/post/2026-07-22-mcp-codemode-updates/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-22-mcp-codemode-updates/og.png?v=31ce61542ebfda04","dateModified":"2026-07-22","datePublished":"2026-07-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
