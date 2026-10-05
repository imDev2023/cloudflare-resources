---
description: Agents SDK v0.6.0 adds RPC transport so an Agent and McpAgent can run in the same Worker with zero network overhead, makes OAuth optional for non-authenticated MCP servers, hardens the JSON Schema to TypeScript converter, and ships a batch of `@cloudflare/ai-chat` reliability fixes.
title: "Agents SDK v0.6.0: RPC transport for MCP, optional OAuth, hardened schema conversion, and @cloudflare/ai-chat fixes"
image: https://developers.cloudflare.com/changelog/post/2026-02-25-agents-sdk-v0.6.0/og.png?v=01c7f555db1a6897
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 25, 2026

## Agents SDK v0.6.0: RPC transport for MCP, optional OAuth, hardened schema conversion, and @cloudflare/ai-chat fixes

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-25-agents-sdk-v0.6.0/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The latest release of the [Agents SDK ↗︎](https://github.com/cloudflare/agents) lets you define an Agent and an McpAgent in the same Worker and connect them over RPC — no HTTP, no network overhead. It also makes OAuth opt-in for simple MCP connections, hardens the schema converter for production workloads, and ships a batch of `@cloudflare/ai-chat` reliability fixes.

#### RPC transport for MCP

You can now connect an Agent to an McpAgent in the same Worker using a Durable Object binding instead of an HTTP URL. The connection stays entirely within the Cloudflare runtime — no network round-trips, no serialization overhead.

Pass the Durable Object namespace directly to `addMcpServer`:

```js
import { Agent } from "agents";

export class MyAgent extends Agent {
	async onStart() {
		// Connect via DO binding — no HTTP, no network overhead
		await this.addMcpServer("counter", env.MY_MCP);

		// With props for per-user context
		await this.addMcpServer("counter", env.MY_MCP, {
			props: { userId: "user-123", role: "admin" },
		});
	}
}
```

```ts
import { Agent } from "agents";

export class MyAgent extends Agent {
	async onStart() {
		// Connect via DO binding — no HTTP, no network overhead
		await this.addMcpServer("counter", env.MY_MCP);

		// With props for per-user context
		await this.addMcpServer("counter", env.MY_MCP, {
			props: { userId: "user-123", role: "admin" },
		});
	}
}
```

The `addMcpServer` method now accepts `string | DurableObjectNamespace` as the second parameter with full TypeScript overloads, so HTTP and RPC paths are type-safe and cannot be mixed.

Key capabilities:

- **Hibernation support** — RPC connections survive Durable Object hibernation automatically. The binding name and props are persisted to storage and restored on wake-up, matching the behavior of HTTP MCP connections.
- **Deduplication** — Calling `addMcpServer` with the same server name returns the existing connection instead of creating duplicates. Connection IDs are stable across hibernation restore.
- **Smaller surface area** — The RPC transport internals have been rewritten and reduced from 609 lines to 245 lines. `RPCServerTransport` now uses `JSONRPCMessageSchema` from the MCP SDK for validation instead of hand-written checks.

Note

RPC transport is experimental. The API may change based on feedback. Refer to [the tracking issue ↗︎](https://github.com/cloudflare/agents/issues/565) for updates.

#### Optional OAuth for MCP connections

`addMcpServer()` no longer eagerly creates an OAuth provider for every connection. For servers that do not require authentication, a simple call is all you need:

```js
// No callbackHost, no OAuth config — just works
await this.addMcpServer("my-server", "https://mcp.example.com");
```

```ts
// No callbackHost, no OAuth config — just works
await this.addMcpServer("my-server", "https://mcp.example.com");
```

If the server responds with a 401, the SDK throws a clear error: `"This MCP server requires OAuth authentication. Provide callbackHost in addMcpServer options to enable the OAuth flow."` The restore-from-storage flow also handles missing callback URLs gracefully, skipping auth provider creation for non-OAuth servers.

#### Hardened JSON Schema to TypeScript converter

The schema converter used by `generateTypes()` and `getAITools()` now handles edge cases that previously caused crashes in production:

- **Depth and circular reference guards** — Prevents stack overflows on recursive or deeply nested schemas
- **`$ref` resolution** — Supports internal JSON Pointers ( `#/definitions/...`, `#/$defs/...`, `#`)
- **Tuple support** — `prefixItems` (JSON Schema 2020-12) and array `items` (draft-07)
- **OpenAPI 3.0 `nullable: true`** — Supported across all schema branches
- **Per-tool error isolation** — One malformed schema cannot crash the full pipeline in `generateTypes()` or `getAITools()`
- **Missing `inputSchema` fallback** — `getAITools()` falls back to `{ type: "object" }` instead of throwing

#### `@cloudflare/ai-chat` fixes

- **Tool denial flow** — Denied tool approvals ( `approved: false`) now transition to `output-denied` with a `tool_result`, fixing Anthropic provider compatibility. Custom denial messages are supported via `state: "output-error"` and `errorText`.
- **Abort/cancel support** — Streaming responses now properly cancel the reader loop when the abort signal fires and send a done signal to the client.
- **Duplicate message persistence** — `persistMessages()` now reconciles assistant messages by content and order, preventing duplicate rows when clients resend full history.
- **`requestId` in `OnChatMessageOptions`** — Handlers can now send properly-tagged error responses for pre-stream failures.
- **`redacted_thinking` preservation** — The message sanitizer no longer strips Anthropic `redacted_thinking` blocks.
- **`/get-messages` reliability** — Endpoint handling moved from a prototype `onRequest()` override to a constructor wrapper, so it works even when users override `onRequest` without calling `super.onRequest()`.
- **Client tool APIs undeprecated** — `createToolsFromClientSchemas`, `clientTools`, `AITool`, `extractClientToolSchemas`, and the `tools` option on `useAgentChat` are restored for SDK use cases where tools are defined dynamically at runtime.
- **`jsonSchema` initialization** — Fixed `jsonSchema not initialized` error when calling `getAITools()` in `onChatMessage`.

#### Upgrade

To update to the latest version:

```sh
npm i agents@latest @cloudflare/ai-chat@latest
```

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-25-agents-sdk-v0.6.0/#page","headline":"Agents SDK v0.6.0: RPC transport for MCP, optional OAuth, hardened schema conversion, and @cloudflare/ai-chat fixes","description":"Agents SDK v0.6.0 adds RPC transport so an Agent and McpAgent can run in the same Worker with zero network overhead, makes OAuth optional for non-authenticated MCP servers, hardens the JSON Schema to TypeScript converter, and ships a batch of @cloudflare/ai-chat reliability fixes.","url":"https://developers.cloudflare.com/changelog/post/2026-02-25-agents-sdk-v0.6.0/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-25-agents-sdk-v0.6.0/og.png?v=01c7f555db1a6897","dateModified":"2026-02-25","datePublished":"2026-02-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
