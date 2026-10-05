---
description: Connect to MySQL and MySQL-compatible databases from Workers using Hyperdrive.
title: MySQL support in Hyperdrive is now generally available
image: https://developers.cloudflare.com/changelog/post/2026-08-07-hyperdrive-mysql-ga/og.png?v=157af79faf65dee1
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 7, 2026

## MySQL support in Hyperdrive is now generally available

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-07-hyperdrive-mysql-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Support for MySQL in Hyperdrive is now generally available. You can connect to any MySQL database from your Workers using Hyperdrive.

Hyperdrive makes your regional, MySQL databases fast when connecting from Cloudflare Workers. It eliminates unnecessary network roundtrips during connection setup, pools database connections globally, and can cache query results to provide the fastest possible response times.

You can connect using your existing drivers, ORMs, and query builders with Hyperdrive's secure credentials, with no code changes required. MySQL support is available at the same [pricing](https://developers.cloudflare.com/hyperdrive/platform/pricing/) as Postgres.

```js
import { createConnection } from "mysql2/promise";

export default {
	async fetch(request, env, ctx) {
		const connection = await createConnection({
			host: env.HYPERDRIVE.host,
			user: env.HYPERDRIVE.user,
			password: env.HYPERDRIVE.password,
			database: env.HYPERDRIVE.database,
			port: env.HYPERDRIVE.port,
			disableEval: true, // Required for Workers compatibility
		});

		const [results, fields] = await connection.query("SHOW tables;");

		ctx.waitUntil(connection.end());

		return new Response(JSON.stringify({ results, fields }), {
			headers: {
				"Content-Type": "application/json",
				"Access-Control-Allow-Origin": "*",
			},
		});
	},
};
```

```ts
import { createConnection } from "mysql2/promise";

export interface Env {
	HYPERDRIVE: Hyperdrive;
}

export default {
	async fetch(request, env, ctx): Promise<Response> {
		const connection = await createConnection({
			host: env.HYPERDRIVE.host,
			user: env.HYPERDRIVE.user,
			password: env.HYPERDRIVE.password,
			database: env.HYPERDRIVE.database,
			port: env.HYPERDRIVE.port,
			disableEval: true, // Required for Workers compatibility
		});

		const [results, fields] = await connection.query("SHOW tables;");

		ctx.waitUntil(connection.end());

		return new Response(JSON.stringify({ results, fields }), {
			headers: {
				"Content-Type": "application/json",
				"Access-Control-Allow-Origin": "*",
			},
		});
	},
} satisfies ExportedHandler<Env>;
```

Learn more about [how Hyperdrive works](https://developers.cloudflare.com/hyperdrive/concepts/how-hyperdrive-works/) and [get started building Workers that connect to MySQL with Hyperdrive](https://developers.cloudflare.com/hyperdrive/get-started/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-07-hyperdrive-mysql-ga/#page","headline":"MySQL support in Hyperdrive is now generally available","description":"Connect to MySQL and MySQL-compatible databases from Workers using Hyperdrive.","url":"https://developers.cloudflare.com/changelog/post/2026-08-07-hyperdrive-mysql-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-07-hyperdrive-mysql-ga/og.png?v=157af79faf65dee1","dateModified":"2026-08-07","datePublished":"2026-08-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
