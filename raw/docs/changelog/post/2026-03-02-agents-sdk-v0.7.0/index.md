---
description: Agents SDK v0.7.0 replaces the old console.log-based observability with diagnostics_channel events across 7 named channels, adds keepAlive() to prevent idle eviction during long-running work, and introduces waitForMcpConnections to guarantee MCP tools are ready before chat handlers run.
title: "Agents SDK v0.7.0: Observability rewrite, keepAlive, and waitForMcpConnections"
image: https://developers.cloudflare.com/changelog/post/2026-03-02-agents-sdk-v0.7.0/og.png?v=8b1af9b6e0ea1fbd
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 2, 2026

## Agents SDK v0.7.0: Observability rewrite, keepAlive, and waitForMcpConnections

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-02-agents-sdk-v0.7.0/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The latest release of the [Agents SDK ↗︎](https://github.com/cloudflare/agents) rewrites observability from scratch with `diagnostics_channel`, adds `keepAlive()` to prevent Durable Object eviction during long-running work, and introduces `waitForMcpConnections` so MCP tools are always available when `onChatMessage` runs.

#### Observability rewrite

The previous observability system used `console.log()` with a custom `Observability.emit()` interface. v0.7.0 replaces it with structured events published to [diagnostics channels](https://developers.cloudflare.com/workers/runtime-apis/nodejs/diagnostics-channel/) — silent by default, zero overhead when nobody is listening.

Every event has a `type`, `payload`, and `timestamp`. Events are routed to seven named channels:

| Channel | Event types |
| --- | --- |
| `agents:state` | `state:update` |
| `agents:rpc` | `rpc`, `rpc:error` |
| `agents:message` | `message:request`, `message:response`, `message:clear`, `message:cancel`, `message:error`, `tool:result`, `tool:approval` |
| `agents:schedule` | `schedule:create`, `schedule:execute`, `schedule:cancel`, `schedule:retry`, `schedule:error`, `queue:retry`, `queue:error` |
| `agents:lifecycle` | `connect`, `destroy` |
| `agents:workflow` | `workflow:start`, `workflow:event`, `workflow:approved`, `workflow:rejected`, `workflow:terminated`, `workflow:paused`, `workflow:resumed`, `workflow:restarted` |
| `agents:mcp` | `mcp:client:preconnect`, `mcp:client:connect`, `mcp:client:authorize`, `mcp:client:discover` |

Use the typed `subscribe()` helper from `agents/observability` for type-safe access:

```js
import { subscribe } from "agents/observability";

const unsub = subscribe("rpc", (event) => {
	if (event.type === "rpc") {
		console.log(`RPC call: ${event.payload.method}`);
	}
	if (event.type === "rpc:error") {
		console.error(
			`RPC failed: ${event.payload.method} — ${event.payload.error}`,
		);
	}
});

// Clean up when done
unsub();
```

```ts
import { subscribe } from "agents/observability";

const unsub = subscribe("rpc", (event) => {
	if (event.type === "rpc") {
		console.log(`RPC call: ${event.payload.method}`);
	}
	if (event.type === "rpc:error") {
		console.error(
			`RPC failed: ${event.payload.method} — ${event.payload.error}`,
		);
	}
});

// Clean up when done
unsub();
```

In production, all diagnostics channel messages are automatically forwarded to [Tail Workers](https://developers.cloudflare.com/workers/observability/logs/tail-workers/) — no subscription code needed in the agent itself:

```js
export default {
	async tail(events) {
		for (const event of events) {
			for (const msg of event.diagnosticsChannelEvents) {
				// msg.channel is "agents:rpc", "agents:workflow", etc.
				console.log(msg.timestamp, msg.channel, msg.message);
			}
		}
	},
};
```

```ts
export default {
	async tail(events) {
		for (const event of events) {
			for (const msg of event.diagnosticsChannelEvents) {
				// msg.channel is "agents:rpc", "agents:workflow", etc.
				console.log(msg.timestamp, msg.channel, msg.message);
			}
		}
	},
};
```

The custom `Observability` override interface is still supported for users who need to filter or forward events to external services.

For the full event reference, refer to the [Diagnostics channels documentation](https://developers.cloudflare.com/agents/runtime/operations/observability/diagnostics-channels/).

#### `keepAlive()` and `keepAliveWhile()`

Durable Objects are evicted after a period of inactivity (typically 70-140 seconds with no incoming requests, WebSocket messages, or alarms). During long-running operations — streaming LLM responses, waiting on external APIs, running multi-step computations — the agent can be evicted mid-flight.

`keepAlive()` prevents this by creating a 30-second heartbeat schedule. The alarm firing resets the inactivity timer. Returns a disposer function that cancels the heartbeat when called.

```js
const dispose = await this.keepAlive();
try {
	const result = await longRunningComputation();
	await sendResults(result);
} finally {
	dispose();
}
```

```ts
const dispose = await this.keepAlive();
try {
	const result = await longRunningComputation();
	await sendResults(result);
} finally {
	dispose();
}
```

`keepAliveWhile()` wraps an async function with automatic cleanup — the heartbeat starts before the function runs and stops when it completes:

```js
const result = await this.keepAliveWhile(async () => {
	const data = await longRunningComputation();
	return data;
});
```

```ts
const result = await this.keepAliveWhile(async () => {
	const data = await longRunningComputation();
	return data;
});
```

Key details:

- **Multiple concurrent callers** — Each `keepAlive()` call returns an independent disposer. Disposing one does not affect others.
- **AIChatAgent built-in** — `AIChatAgent` automatically calls `keepAlive()` during streaming responses. You do not need to add it yourself.
- **Uses the scheduling system** — The heartbeat does not conflict with your own schedules. It shows up in `getSchedules()` if you need to inspect it.

Note

`keepAlive()` is marked `@experimental` and may change between releases.

For the full API reference and when-to-use guidance, refer to [Schedule tasks — Keeping the agent alive](https://developers.cloudflare.com/agents/runtime/execution/schedule-tasks/#keeping-the-agent-alive).

#### `waitForMcpConnections`

`AIChatAgent` now waits for MCP server connections to settle before calling `onChatMessage`. This ensures `this.mcp.getAITools()` returns the full set of tools, especially after Durable Object hibernation when connections are being restored in the background.

```js
export class ChatAgent extends AIChatAgent {
	// Default — waits up to 10 seconds
	// waitForMcpConnections = { timeout: 10_000 };

	// Wait forever
	waitForMcpConnections = true;

	// Disable waiting
	waitForMcpConnections = false;
}
```

```ts
export class ChatAgent extends AIChatAgent {
	// Default — waits up to 10 seconds
	// waitForMcpConnections = { timeout: 10_000 };

	// Wait forever
	waitForMcpConnections = true;

	// Disable waiting
	waitForMcpConnections = false;
}
```

| Value | Behavior |
| --- | --- |
| `{ timeout: 10_000 }` | Wait up to 10 seconds (default) |
| `{ timeout: N }` | Wait up to `N` milliseconds |
| `true` | Wait indefinitely until all connections ready |
| `false` | Do not wait (old behavior before 0.2.0) |

For lower-level control, call `this.mcp.waitForConnections()` directly inside `onChatMessage` instead.

#### Other improvements

- **MCP deduplication by name and URL** — `addMcpServer` with HTTP transport now deduplicates on both server name and URL. Calling it with the same name but a different URL creates a new connection. URLs are normalized before comparison (trailing slashes, default ports, hostname case).
- **`callbackHost` optional for non-OAuth servers** — `addMcpServer` no longer requires `callbackHost` when connecting to MCP servers that do not use OAuth.
- **MCP URL security** — Server URLs are validated before connection to prevent SSRF. Private IP ranges, loopback addresses, link-local addresses, and cloud metadata endpoints are blocked.
- **Custom denial messages** — `addToolOutput` now supports `state: "output-error"` with `errorText` for custom denial messages in human-in-the-loop tool approval flows.
- **`requestId` in chat options** — `onChatMessage` options now include a `requestId` for logging and correlating events.

#### Upgrade

To update to the latest version:

```sh
npm i agents@latest @cloudflare/ai-chat@latest
```

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-02-agents-sdk-v0.7.0/#page","headline":"Agents SDK v0.7.0: Observability rewrite, keepAlive, and waitForMcpConnections","description":"Agents SDK v0.7.0 replaces the old console.log-based observability with diagnostics_channel events across 7 named channels, adds keepAlive() to prevent idle eviction during long-running work, and introduces waitForMcpConnections to guarantee MCP tools are ready before chat handlers run.","url":"https://developers.cloudflare.com/changelog/post/2026-03-02-agents-sdk-v0.7.0/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-02-agents-sdk-v0.7.0/og.png?v=8b1af9b6e0ea1fbd","dateModified":"2026-03-02","datePublished":"2026-03-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
