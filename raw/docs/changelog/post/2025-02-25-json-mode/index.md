---
description: Workers AI JSON Mode adds structured outputs support
title: Workers AI now supports structured JSON outputs.
image: https://developers.cloudflare.com/changelog/post/2025-02-25-json-mode/og.png?v=d397c771b7a582a1
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 25, 2025

## Workers AI now supports structured JSON outputs.

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-25-json-mode/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers AI now supports structured JSON outputs with [JSON mode](https://developers.cloudflare.com/workers-ai/features/json-mode/), which allows you to request a structured output response when interacting with AI models.

This makes it much easier to retrieve structured data from your AI models, and avoids the (error prone!) need to parse large unstructured text responses to extract your data.

JSON mode in Workers AI is compatible with the OpenAI SDK's [structured outputs ↗︎](https://platform.openai.com/docs/guides/structured-outputs) `response_format` API, which can be used directly in a Worker:

```js
import { OpenAI } from "openai";

// Define your JSON schema for a calendar event
const CalendarEventSchema = {
	type: "object",
	properties: {
		name: { type: "string" },
		date: { type: "string" },
		participants: { type: "array", items: { type: "string" } },
	},
	required: ["name", "date", "participants"],
};

export default {
	async fetch(request, env) {
		const client = new OpenAI({
			apiKey: env.OPENAI_API_KEY,
			// Optional: use AI Gateway to bring logs, evals & caching to your AI requests
			// https://developers.cloudflare.com/ai-gateway/usage/providers/openai/
			// baseUrl: "https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai"
		});

		const response = await client.chat.completions.create({
			model: "gpt-4o-2024-08-06",
			messages: [
				{ role: "system", content: "Extract the event information." },
				{
					role: "user",
					content: "Alice and Bob are going to a science fair on Friday.",
				},
			],
			// Use the `response_format` option to request a structured JSON output
			response_format: {
				// Set json_schema and provide ra schema, or json_object and parse it yourself
				type: "json_schema",
				schema: CalendarEventSchema, // provide a schema
			},
		});

		// This will be of type CalendarEventSchema
		const event = response.choices[0].message.parsed;

		return Response.json({
			calendar_event: event,
		});
	},
};
```

```ts
import { OpenAI } from "openai";

interface Env {
	OPENAI_API_KEY: string;
}

// Define your JSON schema for a calendar event
const CalendarEventSchema = {
	type: "object",
	properties: {
		name: { type: "string" },
		date: { type: "string" },
		participants: { type: "array", items: { type: "string" } },
	},
	required: ["name", "date", "participants"],
};

export default {
	async fetch(request: Request, env: Env) {
		const client = new OpenAI({
			apiKey: env.OPENAI_API_KEY,
			// Optional: use AI Gateway to bring logs, evals & caching to your AI requests
			// https://developers.cloudflare.com/ai-gateway/usage/providers/openai/
			// baseUrl: "https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai"
		});

		const response = await client.chat.completions.create({
			model: "gpt-4o-2024-08-06",
			messages: [
				{ role: "system", content: "Extract the event information." },
				{
					role: "user",
					content: "Alice and Bob are going to a science fair on Friday.",
				},
			],
			// Use the `response_format` option to request a structured JSON output
			response_format: {
				// Set json_schema and provide ra schema, or json_object and parse it yourself
				type: "json_schema",
				schema: CalendarEventSchema, // provide a schema
			},
		});

		// This will be of type CalendarEventSchema
		const event = response.choices[0].message.parsed;

		return Response.json({
			calendar_event: event,
		});
	},
};
```

To learn more about JSON mode and structured outputs, visit the [Workers AI documentation](https://developers.cloudflare.com/workers-ai/features/json-mode/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-25-json-mode/#page","headline":"Workers AI now supports structured JSON outputs.","description":"Workers AI JSON Mode adds structured outputs support","url":"https://developers.cloudflare.com/changelog/post/2025-02-25-json-mode/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-25-json-mode/og.png?v=d397c771b7a582a1","dateModified":"2025-02-25","datePublished":"2025-02-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
