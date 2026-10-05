---
description: Generate Workers AI function calling tools from an OpenAPI specification using the ai-utils package.
title: Tools based on OpenAPI Spec
image: https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/openapi/og.png?v=d57cb6344a7eb170
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/workers-ai/llms.txt  
> Use this file to discover all available pages before exploring further.

# Tools based on OpenAPI Spec

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/workers-ai/features/function-calling/embedded/examples/openapi/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Oftentimes APIs are defined and documented via [OpenAPI specification ↗︎](https://swagger.io/specification/). The Cloudflare `ai-utils` package's `createToolsFromOpenAPISpec` function creates tools from the OpenAPI spec, which the LLM can then leverage to fulfill the prompt.

In this example the LLM will describe the a Github user, based Github's API and its OpenAPI spec.

*Embedded function calling example from OpenAPI Spects*

```ts
import { createToolsFromOpenAPISpec, runWithTools } from '@cloudflare/ai-utils';

type Env = {
	AI: Ai;
};

const APP_NAME = 'cf-fn-calling-example-app';

export default {
	async fetch(request, env, ctx) {
		const toolsFromOpenAPISpec = [
			// You can pass the OpenAPI spec link or contents directly
			...(await createToolsFromOpenAPISpec(
				'https://gist.githubusercontent.com/mchenco/fd8f20c8f06d50af40b94b0671273dc1/raw/f9d4b5cd5944cc32d6b34cad0406d96fd3acaca6/partial_api.github.com.json',
				{
					overrides: [
						{
							matcher: ({ url }) => {
								return url.hostname === 'api.github.com';
							},
							// for all requests on *.github.com, we'll need to add a User-Agent.
							values: {
								headers: {
									'User-Agent': APP_NAME,
								},
							},
						},
					],
				}
			)),
		];

		const response = await runWithTools(
			env.AI,
			'@hf/nousresearch/hermes-2-pro-mistral-7b',
			{
				messages: [
					{
						role: 'user',
						content: 'Who is cloudflare on Github and how many repos does the organization have?',
					},
				],
				tools: toolsFromOpenAPISpec,
			}
		);

		return new Response(JSON.stringify(response));
	},
} satisfies ExportedHandler<Env>;
```
