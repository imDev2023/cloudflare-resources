---
description: Draw a watermark from KV on an image from R2
title: Watermarks
image: https://developers.cloudflare.com/images/examples/watermark-from-kv/og.png?v=5d5ec62a8e3805a5
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/images/llms.txt  
> Use this file to discover all available pages before exploring further.

# Watermarks

Draw a watermark from KV on an image from R2

Last updated Jul 8, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/images/examples/watermark-from-kv/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Enable [Workers Cache](https://developers.cloudflare.com/workers/cache/) so repeat requests for the same watermarked image are served from cache without re-running the Worker or re-transforming the image:

```jsonc
{
	"cache": {
		"enabled": true,
	},
}
```

```toml
[cache]
enabled = true
```

Then set `Cache-Control` headers on your response to control the cache lifetime:

```js
export default {
	async fetch(request, env) {
		const watermarkKey = "my-watermark";
		const sourceKey = "my-source-image";

		const watermark = await env.NAMESPACE.get(watermarkKey, "stream");
		const source = await env.BUCKET.get(sourceKey);

		if (!watermark || !source) {
			return new Response("Not found", { status: 404 });
		}

		const result = await env.IMAGES.input(source.body)
			.draw(watermark)
			.output({ format: "image/jpeg" });

		const response = result.response();

		return new Response(response.body, {
			headers: {
				...Object.fromEntries(response.headers),
				"Cache-Control": "public, max-age=3600, stale-while-revalidate=86400",
			},
		});
	},
};
```

```ts
interface Env {
	BUCKET: R2Bucket;
	NAMESPACE: KVNamespace;
	IMAGES: ImagesBinding;
}
export default {
	async fetch(request, env): Promise<Response> {
		const watermarkKey = "my-watermark";
		const sourceKey = "my-source-image";

		const watermark = await env.NAMESPACE.get(watermarkKey, "stream");
		const source = await env.BUCKET.get(sourceKey);

		if (!watermark || !source) {
			return new Response("Not found", { status: 404 });
		}

		const result = await env.IMAGES.input(source.body)
			.draw(watermark)
			.output({ format: "image/jpeg" });

		const response = result.response();

		return new Response(response.body, {
			headers: {
				...Object.fromEntries(response.headers),
				"Cache-Control": "public, max-age=3600, stale-while-revalidate=86400",
			},
		});
	},
} satisfies ExportedHandler<Env>;
```
