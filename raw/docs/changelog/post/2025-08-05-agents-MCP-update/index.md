---
description: Major update brings  MCP elicitation, enhanced transport options,auto transport selection, improved error handling, and reliable prop updates, task queues, and email support
title: Agents SDK adds MCP Elicitation support, http-streamable support, task queues, email integration and more
image: https://developers.cloudflare.com/changelog/post/2025-08-05-agents-MCP-update/og.png?v=4ec3e8bd403c5ebd
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 5, 2025

## Agents SDK adds MCP Elicitation support, http-streamable support, task queues, email integration and more

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-05-agents-MCP-update/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The latest releases of [@cloudflare/agents ↗︎](https://github.com/cloudflare/agents) brings major improvements to MCP transport protocols support and agents connectivity. Key updates include:

#### MCP elicitation support

MCP servers can now request user input during tool execution, enabling interactive workflows like confirmations, forms, and multi-step processes. This feature uses durable storage to preserve elicitation state even during agent hibernation, ensuring seamless user interactions across agent lifecycle events.

```ts
// Request user confirmation via elicitation
const confirmation = await this.elicitInput({
	message: `Are you sure you want to increment the counter by ${amount}?`,
	requestedSchema: {
		type: "object",
		properties: {
			confirmed: {
				type: "boolean",
				title: "Confirm increment",
				description: "Check to confirm the increment",
			},
		},
		required: ["confirmed"],
	},
});
```

Check out our [demo ↗︎](https://github.com/whoiskatrin/agents/tree/main/examples/mcp-elicitation-demo) to see elicitation in action.

#### HTTP streamable transport for MCP

MCP now supports HTTP streamable transport which is recommended over SSE. This transport type offers:

- **Better performance**: More efficient data streaming and reduced overhead
- **Improved reliability**: Enhanced connection stability and error recover- **Automatic fallback**: If streamable transport is not available, it gracefully falls back to SSE

```ts
export default MyMCP.serve("/mcp", {
	binding: "MyMCP",
});
```

The SDK automatically selects the best available transport method, gracefully falling back from streamable-http to SSE when needed.

#### Enhanced MCP connectivity

Significant improvements to MCP server connections and transport reliability:

- **Auto transport selection**: Automatically determines the best transport method, falling back from streamable-http to SSE as needed
- **Improved error handling**: Better connection state management and error reporting for MCP servers
- **Reliable prop updates**: Centralized agent property updates ensure consistency across different contexts

#### Lightweight .queue for fast task deferral

You can use `.queue()` to enqueue background work — ideal for tasks like processing user messages, sending notifications etc.

```ts
class MyAgent extends Agent {
	doSomethingExpensive(payload) {
		// a long running process that you want to run in the background
	}

	queueSomething() {
		await this.queue("doSomethingExpensive", somePayload); // this will NOT block further execution, and runs in the background
		await this.queue("doSomethingExpensive", someOtherPayload); // the callback will NOT run until the previous callback is complete
		// ... call as many times as you want
	}
}
```

Want to try it yourself? Just define a method like processMessage in your agent, and you’re ready to scale.

#### New email adapter

Want to build an AI agent that can receive and respond to emails automatically? With the new email adapter and onEmail lifecycle method, now you can.

```ts
export class EmailAgent extends Agent {
	async onEmail(email: AgentEmail) {
		const raw = await email.getRaw();
		const parsed = await PostalMime.parse(raw);

		// create a response based on the email contents
		// and then send a reply

		await this.replyToEmail(email, {
			fromName: "Email Agent",
			body: `Thanks for your email! You've sent us "${parsed.subject}". We'll process it shortly.`,
		});
	}
}
```

You route incoming mail like this:

```ts
export default {
	async email(email, env) {
		await routeAgentEmail(email, env, {
			resolver: createAddressBasedEmailResolver("EmailAgent"),
		});
	},
};
```

You can find a full example [here ↗︎](https://github.com/cloudflare/agents/tree/main/examples/email-agent).

#### Automatic context wrapping for custom methods

Custom methods are now automatically wrapped with the agent's context, so calling `getCurrentAgent()` should work regardless of where in an agent's lifecycle it's called. Previously this would not work on RPC calls, but now just works out of the box.

```ts
export class MyAgent extends Agent {
	async suggestReply(message) {
		// getCurrentAgent() now correctly works, even when called inside an RPC method
		const { agent } = getCurrentAgent()!;
		return generateText({
			prompt: `Suggest a reply to: "${message}" from "${agent.name}"`,
			tools: [replyWithEmoji],
		});
	}
}
```

Try it out and tell us what you build!

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-05-agents-MCP-update/#page","headline":"Agents SDK adds MCP Elicitation support, http-streamable support, task queues, email integration and more","description":"Major update brings  MCP elicitation, enhanced transport options,auto transport selection, improved error handling, and reliable prop updates, task queues, and email support","url":"https://developers.cloudflare.com/changelog/post/2025-08-05-agents-MCP-update/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-05-agents-MCP-update/og.png?v=4ec3e8bd403c5ebd","dateModified":"2025-08-05","datePublished":"2025-08-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
