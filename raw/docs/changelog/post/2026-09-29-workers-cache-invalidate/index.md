---
description: invalidate() marks matching Workers Cache responses stale instead of deleting them, so your Worker can revalidate them with a 304 Not Modified response instead of regenerating them.
title: Workers Cache — mark cached responses stale with invalidate()
image: https://developers.cloudflare.com/changelog/post/2026-09-29-workers-cache-invalidate/og.png?v=b9ff9438b0928b54
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 29, 2026

## Workers Cache — mark cached responses stale with invalidate()

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-29-workers-cache-invalidate/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workers Cache](https://developers.cloudflare.com/workers/cache/) now supports `invalidate()`, the soft counterpart of `purge()`. `purge()` deletes matching cached responses, so the next request is a cache miss. `invalidate()` keeps them but marks them stale, so the cache revalidates them with your Worker instead.

To revalidate a response, the cache sends your Worker a conditional request built from the validators stored with it — for example, `If-None-Match` carrying the cached `ETag`. If your Worker answers `304 Not Modified`, the cache keeps the stored body. If your Worker answers with a full `200` response, that response replaces the cached one.

`invalidate()` accepts the same options as `purge()`: `tags`, `pathPrefixes`, or `purgeEverything`. It follows the same per-entrypoint scoping and resolves to the same result object. Call it as `ctx.cache.invalidate()`, or import `cache` from `cloudflare:workers` and call `cache.invalidate()`.

Use `invalidate()` when one call covers many cached responses but only some of them changed. Your Worker needs to emit `ETag` or `Last-Modified` and answer matching conditional requests with `304`. Each unchanged response then costs a validator check instead of a full regeneration:

*src/index.jsjs*

```js
export default {
	async fetch(request, env, ctx) {
		if (request.method === "POST") {
			// Write the updated catalog, then mark every cached product page stale.
			await syncCatalog(env, await request.json());
			await ctx.cache.invalidate({ tags: ["products"] });
			return new Response("Synced");
		}

		const product = await getProduct(env, request);
		const etag = `"${product.revision}"`;
		const headers = {
			"Cache-Control": "public, max-age=86400",
			"Cache-Tag": "products",
			ETag: etag,
		};

		// The product has not changed since it was cached. Answer 304, and the
		// cache keeps the body it already has.
		if (request.headers.get("If-None-Match") === etag) {
			return new Response(null, { status: 304, headers });
		}

		return new Response(renderProductPage(product), { headers });
	},
};
```

*src/index.tsts*

```ts
export default {
	async fetch(request, env, ctx): Promise<Response> {
		if (request.method === "POST") {
			// Write the updated catalog, then mark every cached product page stale.
			await syncCatalog(env, await request.json());
			await ctx.cache.invalidate({ tags: ["products"] });
			return new Response("Synced");
		}

		const product = await getProduct(env, request);
		const etag = `"${product.revision}"`;
		const headers = {
			"Cache-Control": "public, max-age=86400",
			"Cache-Tag": "products",
			ETag: etag,
		};

		// The product has not changed since it was cached. Answer 304, and the
		// cache keeps the body it already has.
		if (request.headers.get("If-None-Match") === etag) {
			return new Response(null, { status: 304, headers });
		}

		return new Response(renderProductPage(product), { headers });
	},
} satisfies ExportedHandler<Env>;
```

For more information, refer to [Invalidate cached responses](https://developers.cloudflare.com/workers/cache/purge/#invalidate-cached-responses).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-29-workers-cache-invalidate/#page","headline":"Workers Cache — mark cached responses stale with invalidate()","description":"invalidate() marks matching Workers Cache responses stale instead of deleting them, so your Worker can revalidate them with a 304 Not Modified response instead of regenerating them.","url":"https://developers.cloudflare.com/changelog/post/2026-09-29-workers-cache-invalidate/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-29-workers-cache-invalidate/og.png?v=b9ff9438b0928b54","dateModified":"2026-09-29","datePublished":"2026-09-29","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
