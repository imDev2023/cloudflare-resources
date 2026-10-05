---
description: Install the latest version of the `agents` SDK to build multi-agent applications, use the new RPC API, and visit the latest documentation updates.
title: npm i agents
image: https://developers.cloudflare.com/changelog/post/2025-03-18-npm-i-agents/og.png?v=30e727566d17e31f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 18, 2025

## npm i agents

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-18-npm-i-agents/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

![npm i agents](https://developers.cloudflare.com/_astro/npm-i-agents.CXCpJ1-7.apng)

#### `agents-sdk` -> `agents` Updated

📝 **We've renamed the Agents package to `agents`**!

If you've already been building with the Agents SDK, you can update your dependencies to use the new package name, and replace references to `agents-sdk` with `agents`:

```sh
# Install the new package
npm i agents
```

```sh
# Remove the old (deprecated) package
npm uninstall agents-sdk

# Find instances of the old package name in your codebase
grep -r 'agents-sdk' .
# Replace instances of the old package name with the new one
# (or use find-replace in your editor)
sed -i 's/agents-sdk/agents/g' $(grep -rl 'agents-sdk' .)
```

All future updates will be pushed to the new `agents` package, and the older package has been marked as deprecated.

#### Agents SDK updates New

We've added a number of big new features to the Agents SDK over the past few weeks, including:

- You can now set `cors: true` when using `routeAgentRequest` to return permissive default CORS headers to Agent responses.
- The regular client now syncs state on the agent (just like the React version).
- `useAgentChat` bug fixes for passing headers/credentials, including properly clearing cache on unmount.
- Experimental `/schedule` module with a prompt/schema for adding scheduling to your app (with evals!).
- Changed the internal `zod` schema to be compatible with the limitations of Google's Gemini models by removing the discriminated union, allowing you to use Gemini models with the scheduling API.

We've also fixed a number of bugs with state synchronization and the React hooks.

```js
// via https://github.com/cloudflare/agents/tree/main/examples/cross-domain
export default {
	async fetch(request, env) {
		return (
			// Set { cors: true } to enable CORS headers.
			(await routeAgentRequest(request, env, { cors: true })) ||
			new Response("Not found", { status: 404 })
		);
	},
};
```

```ts
// via https://github.com/cloudflare/agents/tree/main/examples/cross-domain
export default {
	async fetch(request: Request, env: Env) {
		return (
			// Set { cors: true } to enable CORS headers.
			(await routeAgentRequest(request, env, { cors: true })) ||
			new Response("Not found", { status: 404 })
		);
	},
} satisfies ExportedHandler<Env>;
```

#### Call Agent methods from your client code New

We've added a new [`@unstable_callable()`](https://developers.cloudflare.com/agents/runtime/agents-api/) decorator for defining methods that can be called directly from clients. This allows you call methods from within your client code: you can call methods (with arguments) and get native JavaScript objects back.

```js
// server.ts
import { unstable_callable, Agent } from "agents";

export class Rpc extends Agent {
	// Use the decorator to define a callable method
	@unstable_callable({
		description: "rpc test",
	})
	async getHistory() {
		return this.sql`SELECT * FROM history ORDER BY created_at DESC LIMIT 10`;
	}
}
```

```ts
// server.ts
import { unstable_callable, Agent, type StreamingResponse } from "agents";
import type { Env } from "../server";

export class Rpc extends Agent<Env> {
	// Use the decorator to define a callable method
	@unstable_callable({
		description: "rpc test",
	})
	async getHistory() {
		return this.sql`SELECT * FROM history ORDER BY created_at DESC LIMIT 10`;
	}
}
```

```tsx
// client.tsx
const { call } = useAgent({ agent: "rpc" });

const fetchUserHistory = async () => {
	try {
		setLoading(true);
		// Call methods directly on the Agent!
		const result = await call("getHistory");
		addToast(`RPC result: ${result}`, "success");
	} catch (error) {
		addToast(`Error: ${error}`, "error");
	} finally {
		setLoading(false);
	}
};
```

#### agents-starter Updated

We've fixed a number of small bugs in the [`agents-starter` ↗︎](https://github.com/cloudflare/agents-starter) project — a real-time, chat-based example application with tool-calling & human-in-the-loop built using the Agents SDK. The starter has also been upgraded to use the latest [wrangler v4](https://developers.cloudflare.com/changelog/2025-03-13-wrangler-v4/) release.

If you're new to Agents, you can install and run the `agents-starter` project in two commands:

```sh
# Install it
$ npm create cloudflare@latest agents-starter -- --template="cloudflare/agents-starter"
# Run it
$ npm run start
```

You can use the starter as a template for your own Agents projects: open up `src/server.ts` and `src/client.tsx` to see how the Agents SDK is used.

#### More documentation Updated

We've heard your feedback on the Agents SDK documentation, and we're shipping more API reference material and usage examples, including:

- Expanded [API reference documentation](https://developers.cloudflare.com/agents/runtime/), covering the methods and properties exposed by the Agents SDK, as well as more usage examples.
- More [Client API](https://developers.cloudflare.com/agents/runtime/agents-api/#client-api) documentation that documents `useAgent`, `useAgentChat` and the new `@unstable_callable` RPC decorator exposed by the SDK.
- New documentation on how to [route requests to agents](https://developers.cloudflare.com/agents/runtime/communication/routing/) and (optionally) authenticate clients before they connect to your Agents.

Note that the Agents SDK is continually growing: the type definitions included in the SDK will always include the latest APIs exposed by the `agents` package.

If you're still wondering what Agents are, [read our blog on building AI Agents on Cloudflare ↗︎](https://blog.cloudflare.com/build-ai-agents-on-cloudflare/) and/or visit the [Agents documentation](https://developers.cloudflare.com/agents/) to learn more.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-18-npm-i-agents/#page","headline":"npm i agents","description":"Install the latest version of the agents SDK to build multi-agent applications, use the new RPC API, and visit the latest documentation updates.","url":"https://developers.cloudflare.com/changelog/post/2025-03-18-npm-i-agents/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-03-18-npm-i-agents/og.png?v=30e727566d17e31f","dateModified":"2025-03-18","datePublished":"2025-03-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
