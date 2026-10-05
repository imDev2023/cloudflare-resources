---
description: New instances come with built-in storage and a vector index. Access AI Search from Workers with the new namespace binding and search across multiple instances in one call.
title: AI Search instances now include built-in storage and namespace Workers Bindings
image: https://developers.cloudflare.com/changelog/post/2026-04-16-ai-search-namespace-binding/og.png?v=da8184d6fe49df20
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 16, 2026

## AI Search instances now include built-in storage and namespace Workers Bindings

[AI Search](https://developers.cloudflare.com/ai-search/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-16-ai-search-namespace-binding/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

New [AI Search](https://developers.cloudflare.com/ai-search/) instances created after today will work differently. New instances come with built-in storage and a vector index, so you can upload a file, have it indexed immediately, and search it right away.

Additionally new Workers Bindings are now available to use with AI Search. The new namespace binding lets you create and manage instances at runtime, and cross-instance search API lets you query across multiple instances in one call.

#### Built-in storage and vector index

All new instances now comes with built-in storage which allows you to upload files directly to it using the [Items API](https://developers.cloudflare.com/ai-search/api/items/workers-binding/) or the dashboard. No R2 buckets to set up, no external data sources to connect first.

```ts
const instance = env.AI_SEARCH.get("my-instance");

// upload and wait for indexing to complete
const item = await instance.items.uploadAndPoll("faq.md", content);

// search immediately after indexing
const results = await instance.search({
	messages: [{ role: "user", content: "onboarding guide" }],
});
```

#### Namespace binding

The new `ai_search_namespaces` binding replaces the previous `env.AI.autorag()` API provided through the `AI` binding. It gives your Worker access to all instances within a [namespace](https://developers.cloudflare.com/ai-search/concepts/namespaces/) and lets you create, update, and delete instances at runtime without redeploying.

```jsonc
// wrangler.jsonc
{
	"ai_search_namespaces": [
		{
			"binding": "AI_SEARCH",
			"namespace": "default",
		},
	],
}
```

```ts
// create an instance at runtime
const instance = await env.AI_SEARCH.create({
	id: "my-instance",
});
```

For migration details, refer to [Workers binding migration](https://developers.cloudflare.com/ai-search/api/migration/workers-binding/). For more on namespaces, refer to [Namespaces](https://developers.cloudflare.com/ai-search/concepts/namespaces/).

#### Cross-instance search

Within the new AI Search binding, you now have access to a Search and Chat API on the namespace level. Pass an array of instance IDs and get one ranked list of results back.

```ts
const results = await env.AI_SEARCH.search({
	messages: [{ role: "user", content: "What is Cloudflare?" }],
	ai_search_options: {
		instance_ids: ["product-docs", "customer-abc123"],
	},
});
```

Refer to [Namespace-level search](https://developers.cloudflare.com/ai-search/api/search/workers-binding/#namespace-level) for details.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-16-ai-search-namespace-binding/#page","headline":"AI Search instances now include built-in storage and namespace Workers Bindings","description":"New instances come with built-in storage and a vector index. Access AI Search from Workers with the new namespace binding and search across multiple instances in one call.","url":"https://developers.cloudflare.com/changelog/post/2026-04-16-ai-search-namespace-binding/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-16-ai-search-namespace-binding/og.png?v=da8184d6fe49df20","dateModified":"2026-04-16","datePublished":"2026-04-16","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
