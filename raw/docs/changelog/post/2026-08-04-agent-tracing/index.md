---
description: Agent traces show model calls, tool runs, approvals, token usage, and runtime operations for each turn.
title: Agent traces for Think, Flue, and AI SDK instrumented by Agents SDK
image: https://developers.cloudflare.com/changelog/post/2026-08-04-agent-tracing/og.png?v=4d28587707f5cc68
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 4, 2026

## Agent traces for Think, Flue, and AI SDK instrumented by Agents SDK

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-04-agent-tracing/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Agent tracing is now available for applications built with the Agents SDK. Traces show each agent turn alongside model calls, tool runs, approvals, token usage, and Workers runtime operations.

Turn on Workers tracing in your Wrangler configuration:

```jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  "observability": {
    "traces": {
      "enabled": true
    }
  }
}
```

```toml
[observability.traces]
enabled = true
```

Think and Flue applications emit agent traces automatically. For direct AI SDK calls, wrap the AI SDK namespace once. `wrapAISDK()` supports AI SDK v6 and v7. This AI SDK v7 example also supplies the agent identity:

```js
import * as ai from "ai";
import { wrapAISDK } from "agents/observability/ai";

const tracedAI = wrapAISDK(ai);

await tracedAI.generateText({
	model,
	prompt: "Find an available appointment",
	runtimeContext: {
		agentId: "booking-agent-production",
		conversationId: "conversation-123",
	},
	telemetry: {
		functionId: "booking-agent",
		includeRuntimeContext: {
			agentId: true,
			conversationId: true,
		},
	},
});
```

```ts
import * as ai from "ai";
import { wrapAISDK } from "agents/observability/ai";

const tracedAI = wrapAISDK(ai);

await tracedAI.generateText({
	model,
	prompt: "Find an available appointment",
	runtimeContext: {
		agentId: "booking-agent-production",
		conversationId: "conversation-123",
	},
	telemetry: {
		functionId: "booking-agent",
		includeRuntimeContext: {
			agentId: true,
			conversationId: true,
		},
	},
});
```

Message and tool payload recording is off by default. Turn it on only when the payloads are safe to store:

```js
const tracedAI = wrapAISDK(ai, {
	storeMessages: true,
	storeTools: true,
});
```

```ts
const tracedAI = wrapAISDK(ai, {
	storeMessages: true,
	storeTools: true,
});
```

Open the [**Agents** tab ↗︎](https://dash.cloudflare.com/?to=/:account/agents) in the Cloudflare dashboard to inspect sessions, replay conversations, and view trace waterfalls. For advanced setup, privacy controls, and trace structure, refer to [Agent tracing](https://developers.cloudflare.com/agents/runtime/operations/observability/tracing/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-04-agent-tracing/#page","headline":"Agent traces for Think, Flue, and AI SDK instrumented by Agents SDK","description":"Agent traces show model calls, tool runs, approvals, token usage, and runtime operations for each turn.","url":"https://developers.cloudflare.com/changelog/post/2026-08-04-agent-tracing/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-04-agent-tracing/og.png?v=4d28587707f5cc68","dateModified":"2026-08-04","datePublished":"2026-08-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
