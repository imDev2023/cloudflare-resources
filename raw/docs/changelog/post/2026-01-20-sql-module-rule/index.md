---
description: The `.sql` file extension is now automatically configured to be importable in your Worker code
title: Import SQL files as additional modules by default
image: https://developers.cloudflare.com/changelog/post/2026-01-20-sql-module-rule/og.png?v=93d431832e87ccc7
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 20, 2026

## Import SQL files as additional modules by default

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-20-sql-module-rule/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The `.sql` file extension is now automatically configured to be importable in your Worker code when using [Wrangler](https://developers.cloudflare.com/workers/wrangler/bundling/#including-non-javascript-modules) or the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/reference/non-javascript-modules/). This is particular useful for importing migrations in Durable Objects and means you no longer need to configure custom rules when using [Drizzle ↗︎](https://orm.drizzle.team/docs/connect-cloudflare-do).

SQL files are imported as JavaScript strings:

```ts
// `example` will be a JavaScript string
import example from "./example.sql";
```

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-20-sql-module-rule/#page","headline":"Import SQL files as additional modules by default","description":"The .sql file extension is now automatically configured to be importable in your Worker code","url":"https://developers.cloudflare.com/changelog/post/2026-01-20-sql-module-rule/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-20-sql-module-rule/og.png?v=93d431832e87ccc7","dateModified":"2026-01-20","datePublished":"2026-01-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
