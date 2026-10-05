---
description: A new declarative `exports` field in your Wrangler configuration replaces the imperative `migrations` array for managing Durable Object class lifecycle.
title: Declare Durable Object class lifecycle with `exports`
image: https://developers.cloudflare.com/changelog/post/2026-06-30-declarative-do-class-exports/og.png?v=614dee203ba9098f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 4, 2026

## Declare Durable Object class lifecycle with \`exports\`

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-30-declarative-do-class-exports/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A new declarative [`exports`](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/) field in your Wrangler configuration file replaces the imperative [`migrations`](https://developers.cloudflare.com/durable-objects/reference/durable-object-class-migrations-legacy/) array for managing Durable Object class lifecycle. Instead of writing an ordered list of migration steps with unique tags, you declare each Durable Object class your Worker exports and Cloudflare compares that against what's already deployed to determine what Durable Object state needs to be created, renamed, or deleted.

With legacy migrations, renaming `ChatRoom` to `Room` requires retaining both tagged steps:

*Before — legacy migrationsjsonc*

```jsonc
{
	"migrations": [
		{ "tag": "v1", "new_sqlite_classes": ["ChatRoom"] },
		{
			"tag": "v2",
			"renamed_classes": [{ "from": "ChatRoom", "to": "Room" }],
		},
	],
}
```

With `exports`, you instead declare `Room` as the current class and mark `ChatRoom` as renamed:

*After — declarative exportsjsonc*

```jsonc
{
	"exports": {
		"ChatRoom": {
			"type": "durable-object",
			"state": "renamed",
			"renamed_to": "Room",
		},
		"Room": { "type": "durable-object", "storage": "sqlite" },
	},
}
```

Each entry is keyed by class name. The `state` field carries the lifecycle (`created` by default — a live class — plus tombstone states `deleted`, `renamed`, and `transferred`, and the `expecting-transfer` receiving state for cross-Worker transfers).

Key improvements over the legacy `migrations` array:

- **No migration tags.** The current `exports` map is the source of truth — there is no historical chain of `v1`, `v2`, `v3` entries to maintain.
- **Structured deployment output.** Wrangler reports when it creates, updates, deletes, renames, or transfers Durable Object classes. It also identifies stale configuration entries that are safe to remove. Deployments with no changes or notices do not print this output.
- **Zero-downtime rename and transfer patterns are first-class.** Tombstones may coexist with the source class still in code, enabling a [three-deploy rename](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/#avoid-downtime-during-a-rename) and a [four-deploy cross-Worker transfer](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/#transfer-a-durable-object-class-between-workers) without runtime errors during the rollout window.
- **Cross-Worker safety.** When you delete or rename a class, Cloudflare lists every other Worker in your account whose bindings still reference the namespace, so you can redeploy them before the change goes live.

Existing Workers using the legacy [`migrations`](https://developers.cloudflare.com/durable-objects/reference/durable-object-class-migrations-legacy/) array continue to work unchanged. To move to `exports`, refer to the [migration guide](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/#migrate-from-the-legacy-migrations-flow). `exports` and `migrations` are mutually exclusive within a single Worker.

For the full reference, refer to [Durable Object class exports](https://developers.cloudflare.com/durable-objects/reference/durable-objects-migrations/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-30-declarative-do-class-exports/#page","headline":"Declare Durable Object class lifecycle with `exports`","description":"A new declarative exports field in your Wrangler configuration replaces the imperative migrations array for managing Durable Object class lifecycle.","url":"https://developers.cloudflare.com/changelog/post/2026-06-30-declarative-do-class-exports/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-30-declarative-do-class-exports/og.png?v=614dee203ba9098f","dateModified":"2026-07-04","datePublished":"2026-07-04","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
