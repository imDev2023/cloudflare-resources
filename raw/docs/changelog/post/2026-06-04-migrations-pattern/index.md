---
description: Configure `wrangler d1 migrations apply` to discover migrations in nested layouts produced by ORMs like Drizzle.
title: D1 migrations support nested layouts via `migrations_pattern`
image: https://developers.cloudflare.com/changelog/post/2026-06-04-migrations-pattern/og.png?v=f5ea7879d5b79ccd
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 29, 2026

## D1 migrations support nested layouts via \`migrations\_pattern\`

[D1](https://developers.cloudflare.com/d1/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-04-migrations-pattern/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now point `wrangler d1 migrations apply` at a nested migrations layout — such as the one produced by [Drizzle ↗︎](https://orm.drizzle.team/) (`migrations/0001_init/migration.sql`) — using the new `migrations_pattern` D1 binding config:

```jsonc
{
	"d1_databases": [
		{
			"binding": "DB",
			"database_name": "my-database",
			"database_id": "<UUID>",
			"migrations_dir": "migrations",
			"migrations_pattern": "migrations/*/migration.sql",
		},
	],
}
```

`migrations_pattern` is a glob (relative to your Wrangler config file) used to discover migration files. It defaults to `${migrations_dir}/*.sql`, so existing projects keep working unchanged. Each migration's name is recorded in the migrations table as a path relative to `migrations_dir`.

To learn more, visit D1's [migrations documentation](https://developers.cloudflare.com/d1/reference/migrations/#nested-migration-layouts).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-04-migrations-pattern/#page","headline":"D1 migrations support nested layouts via `migrations_pattern`","description":"Configure wrangler d1 migrations apply to discover migrations in nested layouts produced by ORMs like Drizzle.","url":"https://developers.cloudflare.com/changelog/post/2026-06-04-migrations-pattern/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-04-migrations-pattern/og.png?v=f5ea7879d5b79ccd","dateModified":"2026-05-29","datePublished":"2026-05-29","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
