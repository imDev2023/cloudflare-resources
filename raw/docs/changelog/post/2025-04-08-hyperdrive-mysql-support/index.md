---
description: You can now connect to MySQL databases from your Workers using Hyperdrive for optimal performance
title: Hyperdrive introduces support for MySQL and MySQL-compatible databases
image: https://developers.cloudflare.com/changelog/post/2025-04-08-hyperdrive-mysql-support/og.png?v=4f834cd400bf9256
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 8, 2025

## Hyperdrive introduces support for MySQL and MySQL-compatible databases

[Hyperdrive](https://developers.cloudflare.com/hyperdrive/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-08-hyperdrive-mysql-support/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Hyperdrive now supports connecting to MySQL and MySQL-compatible databases, including Amazon RDS and Aurora MySQL, Google Cloud SQL for MySQL, Azure Database for MySQL, PlanetScale and MariaDB.

Hyperdrive makes your regional, MySQL databases fast when connecting from Cloudflare Workers. It eliminates unnecessary network roundtrips during connection setup, pools database connections globally, and can cache query results to provide the fastest possible response times.

Best of all, you can connect using your existing drivers, ORMs, and query builders with Hyperdrive's secure credentials, no code changes required.

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
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-08-hyperdrive-mysql-support/#page","headline":"Hyperdrive introduces support for MySQL and MySQL-compatible databases","description":"You can now connect to MySQL databases from your Workers using Hyperdrive for optimal performance","url":"https://developers.cloudflare.com/changelog/post/2025-04-08-hyperdrive-mysql-support/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-08-hyperdrive-mysql-support/og.png?v=4f834cd400bf9256","dateModified":"2025-04-08","datePublished":"2025-04-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
