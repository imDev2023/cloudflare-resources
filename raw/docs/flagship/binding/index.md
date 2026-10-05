---
description: Evaluate Flagship feature flags directly in Cloudflare Workers using the native binding with type-safe methods and automatic fallback.
title: Binding API
image: https://developers.cloudflare.com/flagship/binding/og.png?v=8621ceb4eb796d20
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/flagship/llms.txt  
> Use this file to discover all available pages before exploring further.

# Binding API

Last updated Apr 30, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/flagship/binding/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Workers access Flagship through a binding that you add to your Wrangler configuration file. The `binding` field sets the variable name you use in your Worker code.

```jsonc
{
	"flagship": [
		{
			"binding": "FLAGS",
			"app_id": "<APP_ID>",
		},
	],
}
```

```toml
[[flagship]]
binding = "FLAGS"
app_id = "<APP_ID>"
```

Replace `<APP_ID>` with the app ID from your Flagship app. If you have not created an app yet, refer to the [Get started guide](https://developers.cloudflare.com/flagship/get-started/#create-an-app-and-a-flag). With this configuration, the binding is available as `env.FLAGS`. Refer to [Configuration](https://developers.cloudflare.com/flagship/configuration/) for additional options such as binding to multiple apps.

The binding provides type-safe methods for evaluating feature flags. If an evaluation fails or a flag is not found, the method returns the default value you provide.

```js
export default {
	async fetch(request, env) {
		const enabled = await env.FLAGS.getBooleanValue("new-feature", false, {
			userId: "user-42",
		});
		return new Response(enabled ? "Feature on" : "Feature off");
	},
};
```

```ts
export default {
	async fetch(request: Request, env: Env): Promise<Response> {
		const enabled = await env.FLAGS.getBooleanValue("new-feature", false, {
			userId: "user-42",
		});
		return new Response(enabled ? "Feature on" : "Feature off");
	},
};
```

The binding has the type `Flagship` from the `@cloudflare/workers-types` package.

- [Types](https://developers.cloudflare.com/flagship/binding/types/)
- [Methods](https://developers.cloudflare.com/flagship/binding/methods/)
