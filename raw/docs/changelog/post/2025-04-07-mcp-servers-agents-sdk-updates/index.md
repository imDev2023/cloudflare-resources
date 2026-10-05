---
description: The Agents SDK now includes built-in support for building remote MCP servers directly as part of your Agent.
title: Build MCP servers with the Agents SDK
image: https://developers.cloudflare.com/changelog/post/2025-04-07-mcp-servers-agents-sdk-updates/og.png?v=a51da5fdc0bc6703
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 7, 2025

## Build MCP servers with the Agents SDK

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-07-mcp-servers-agents-sdk-updates/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The Agents SDK now includes built-in support for building remote MCP (Model Context Protocol) servers directly as part of your Agent. This allows you to easily create and manage MCP servers, without the need for additional infrastructure or configuration.

The SDK includes a new `MCPAgent` class that extends the `Agent` class and allows you to expose resources and tools over the MCP protocol, as well as authorization and authentication to enable remote MCP servers.

```js
export class MyMCP extends McpAgent {
	server = new McpServer({
		name: "Demo",
		version: "1.0.0",
	});

	async init() {
		this.server.resource(`counter`, `mcp://resource/counter`, (uri) => {
			// ...
		});

		this.server.tool(
			"add",
			"Add two numbers together",
			{ a: z.number(), b: z.number() },
			async ({ a, b }) => {
				// ...
			},
		);
	}
}
```

```ts
export class MyMCP extends McpAgent<Env> {
	server = new McpServer({
		name: "Demo",
		version: "1.0.0",
	});

	async init() {
		this.server.resource(`counter`, `mcp://resource/counter`, (uri) => {
			// ...
		});

		this.server.tool(
			"add",
			"Add two numbers together",
			{ a: z.number(), b: z.number() },
			async ({ a, b }) => {
				// ...
			},
		);
	}
}
```

See [the example ↗︎](https://github.com/cloudflare/agents/tree/main/examples/mcp) for the full code and as the basis for building your own MCP servers, and the [client example ↗︎](https://github.com/cloudflare/agents/tree/main/examples/mcp-client) for how to build an Agent that acts as an MCP client.

To learn more, review the [announcement blog ↗︎](https://blog.cloudflare.com/building-ai-agents-with-mcp-authn-authz-and-durable-objects) as part of Developer Week 2025.

#### Agents SDK updates

We've made a number of improvements to the [Agents SDK](https://developers.cloudflare.com/agents/), including:

- Support for building MCP servers with the new `MCPAgent` class.
- The ability to export the current agent, request and WebSocket connection context using `import { context } from "agents"`, allowing you to minimize or avoid direct dependency injection when calling tools.
- Fixed a bug that prevented query parameters from being sent to the Agent server from the `useAgent` React hook.
- Automatically converting the `agent` name in `useAgent` or `useAgentChat` to kebab-case to ensure it matches the naming convention expected by [`routeAgentRequest`](https://developers.cloudflare.com/agents/runtime/communication/routing/).

To install or update the Agents SDK, run `npm i agents@latest` in an existing project, or explore the `agents-starter` project:

```sh
npm create cloudflare@latest -- --template cloudflare/agents-starter
```

See the full release notes and changelog [on the Agents SDK repository ↗︎](https://github.com/cloudflare/agents/blob/main/packages/agents/CHANGELOG.md) and

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-07-mcp-servers-agents-sdk-updates/#page","headline":"Build MCP servers with the Agents SDK","description":"The Agents SDK now includes built-in support for building remote MCP servers directly as part of your Agent.","url":"https://developers.cloudflare.com/changelog/post/2025-04-07-mcp-servers-agents-sdk-updates/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-07-mcp-servers-agents-sdk-updates/og.png?v=a51da5fdc0bc6703","dateModified":"2025-04-07","datePublished":"2025-04-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
