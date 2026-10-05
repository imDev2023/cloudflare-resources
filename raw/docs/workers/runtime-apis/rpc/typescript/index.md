---
description: How TypeScript types for your Worker or Durable Object's RPC methods are generated and exposed to clients
title: TypeScript
image: https://developers.cloudflare.com/workers/runtime-apis/rpc/typescript/og.png?v=4357577e18058c65
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/workers/llms.txt  
> Use this file to discover all available pages before exploring further.

# TypeScript

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/workers/runtime-apis/rpc/typescript/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Running [`wrangler types`](https://developers.cloudflare.com/workers/languages/typescript/#generate-types) generates runtime types including the `Service` and `DurableObjectNamespace` types, each of which accepts a single type parameter for the [`WorkerEntrypoint`](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/rpc) or [`DurableObject`](https://developers.cloudflare.com/durable-objects/best-practices/create-durable-object-stubs-and-send-requests/#call-rpc-methods) types.

Using higher-order types, we automatically generate client-side stub types (e.g., forcing all methods to be async).

[`wrangler types`](https://developers.cloudflare.com/workers/languages/typescript/#generate-types) also generates types for the `env` object. You can pass in the path to the config files of the Worker or Durable Object being called so that the generated types include the type parameters for the `Service` and `DurableObjectNamespace` types.

For example, if your client Worker had bindings to a Worker in `../sum-worker/` and a Durable Object in `../counter/`, you should generate types for the client Worker's `env` by running:

npmyarnpnpm

```
npx wrangler types -c ./client/wrangler.jsonc -c ../sum-worker/wrangler.jsonc -c ../counter/wrangler.jsonc
```

```
yarn wrangler types -c ./client/wrangler.jsonc -c ../sum-worker/wrangler.jsonc -c ../counter/wrangler.jsonc
```

```
pnpm wrangler types -c ./client/wrangler.jsonc -c ../sum-worker/wrangler.jsonc -c ../counter/wrangler.jsonc
```

This will produce a `worker-configuration.d.ts` file that includes:

*worker-configuration.d.tsts*

```ts
interface Env {
	SUM_SERVICE: Service<import("../sum-worker/src/index").SumService>;
	COUNTER_OBJECT: DurableObjectNamespace<
		import("../counter/src/index").Counter
	>;
}
```

Now types for RPC method like the `env.SUM_SERVICE.sum` method will be exposed to the client Worker.

*src/index.tsts*

```ts
export default {
	async fetch(req, env, ctx): Promise<Response> {
		const result = await env.SUM_SERVICE.sum(1, 2);
		return new Response(result.toString());
	},
} satisfies ExportedHandler<Env>;
```
