---
description: Agents SDK v0.12.4 improves chat recovery, fixes Agent state sync during reconnects, adds durable Think submissions, exposes routing retry configuration, and adds Voice connection control.
title: "Agents SDK v0.12.4: chat recovery, routing retries, durable Think submissions, and Voice connection control"
image: https://developers.cloudflare.com/changelog/post/2026-05-13-agents-sdk-v0.12.4/og.png?v=0c643d2c65937470
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 13, 2026

## Agents SDK v0.12.4: chat recovery, routing retries, durable Think submissions, and Voice connection control

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-05-13-agents-sdk-v0.12.4/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The latest release of the [Agents SDK ↗︎](https://github.com/cloudflare/agents) brings more reliable chat recovery, fixes Agent state synchronization during reconnects, adds durable submissions for Think, exposes routing retry configuration, and adds connection control for Voice agents.

#### Chat recovery improvements

`@cloudflare/ai-chat` now keeps server turns running when a browser or client stream is interrupted. This is useful for long-running AI responses where users refresh the page, close a tab, or temporarily lose connection. Calling `stop()` still cancels the server turn.

Set `cancelOnClientAbort: true` if browser or client aborts should also cancel the server turn:

```js
const chat = useAgentChat({
	agent: "assistant",
	name: "user-123",
	cancelOnClientAbort: true,
});
```

```tsx
const chat = useAgentChat({
	agent: "assistant",
	name: "user-123",
	cancelOnClientAbort: true,
});
```

Notable bug fixes:

- Chat stream resume negotiation no longer throws when replay races with a closed WebSocket connection.
- Recovered chat continuations no longer leave `useAgentChat` stuck in a streaming state when the original socket disconnects before a terminal response.
- Approval auto-continuation preserves reasoning parts and persists continuation reasoning in the final message.
- `isServerStreaming` now resets correctly when a resumed stream moves from the fallback observer path to a transport-owned stream.

#### Agent state and routing fixes

`agents@0.12.4` prevents duplicate initial state frames during WebSocket connection setup. This avoids stale initial state messages overwriting state updates already sent by the client.

Agent recovery is also more reliable when tool calls span a Durable Object restart. Recovery now defers user finish hooks until after agent startup and isolates hook failures, so one failed hook does not block other recovered runs from finalizing.

`getAgentByName()` now supports `routingRetry` for transient Durable Object routing failures:

```js
import { getAgentByName } from "agents";

const agent = await getAgentByName(env.AssistantAgent, "user-123", {
	routingRetry: {
		maxAttempts: 3,
	},
});
```

```ts
import { getAgentByName } from "agents";

const agent = await getAgentByName(env.AssistantAgent, "user-123", {
	routingRetry: {
		maxAttempts: 3,
	},
});
```

#### Durable Think submissions

`@cloudflare/think` now supports durable programmatic submissions. `submitMessages()` provides durable acceptance, idempotent retries, status inspection, cancellation, and cleanup for server-driven turns that should continue after the caller returns.

`Think.chat()` RPC turns now run inside chat recovery fibers and persist their stream chunks. Interrupted sub-agent turns can recover partial output instead of starting over.

`ChatOptions.tools` has been removed from the TypeScript API. Define durable tools on the child agent or use agent tools for orchestration. Runtime `options.tools` values passed by legacy callers are ignored with a warning.

#### Think message pruning behavior change

`@cloudflare/think` no longer applies `pruneMessages({ toolCalls: "before-last-2-messages" })` to model context by default. The previous default could strip client-side tool results from longer multi-turn flows.

`truncateOlderMessages` still runs as before, so context cost remains bounded. Subclasses that relied on the old aggressive pruning can opt back in from `beforeTurn`:

```js
import { Think } from "@cloudflare/think";
import { pruneMessages } from "ai";

export class MyAgent extends Think {
	beforeTurn(ctx) {
		return {
			messages: pruneMessages({
				messages: ctx.messages,
				toolCalls: "before-last-2-messages",
			}),
		};
	}
}
```

```ts
import { Think } from "@cloudflare/think";
import { pruneMessages } from "ai";

export class MyAgent extends Think<Env> {
	beforeTurn(ctx) {
		return {
			messages: pruneMessages({
				messages: ctx.messages,
				toolCalls: "before-last-2-messages",
			}),
		};
	}
}
```

#### Voice agent connection control

`@cloudflare/voice` adds an `enabled` option to `useVoiceAgent`. React apps can now delay creating and connecting a `VoiceClient` until prerequisites such as capability tokens are ready.

```js
const voice = useVoiceAgent({
	agent: "MyVoiceAgent",
	enabled: Boolean(token),
});
```

```tsx
const voice = useVoiceAgent({
	agent: "MyVoiceAgent",
	enabled: Boolean(token),
});
```

This release also fixes Workers AI speech-to-text session edge cases and `withVoice` text streaming from AI SDK `textStream` responses.

#### Other improvements

- **Streamable HTTP routing** — Server-to-client requests now route through the originating POST stream when no standalone SSE stream is available.
- **Structured tool output** — Tool output shapes are preserved when truncating older messages or oversized persisted rows.
- **Non-chat Think tool steps** — Think agent-tool children can complete without emitting assistant text and can return structured output through `getAgentToolOutput`.
- **Sub-agent schedules** — Stale sub-agent schedule rows are pruned when their owning facet registry entry no longer exists.
- **`@cloudflare/codemode`** — Adds a browser-safe export with an iframe sandbox executor and resolves OpenAPI specs inside the sandbox to avoid Worker Loader RPC size limits.

#### Upgrade

To update to the latest version:

```sh
npm i agents@latest @cloudflare/ai-chat@latest @cloudflare/think@latest @cloudflare/voice@latest
```

Refer to the [Agents API reference](https://developers.cloudflare.com/agents/runtime/) and [Chat agents documentation](https://developers.cloudflare.com/agents/communication-channels/chat/chat-agents/) for more information.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-05-13-agents-sdk-v0.12.4/#page","headline":"Agents SDK v0.12.4: chat recovery, routing retries, durable Think submissions, and Voice connection control","description":"Agents SDK v0.12.4 improves chat recovery, fixes Agent state sync during reconnects, adds durable Think submissions, exposes routing retry configuration, and adds Voice connection control.","url":"https://developers.cloudflare.com/changelog/post/2026-05-13-agents-sdk-v0.12.4/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-05-13-agents-sdk-v0.12.4/og.png?v=0c643d2c65937470","dateModified":"2026-05-13","datePublished":"2026-05-13","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
