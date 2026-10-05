---
description: SQLite-backed Durable Objects are generally available.
title: SQLite in Durable Objects GA with 10GB storage per object
image: https://developers.cloudflare.com/changelog/post/2025-04-07-sqlite-in-durable-objects-ga/og.png?v=250c8ba4e7ea3c7a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 7, 2025

## SQLite in Durable Objects GA with 10GB storage per object

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-07-sqlite-in-durable-objects-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

SQLite in Durable Objects is now generally available (GA) with 10GB SQLite database per Durable Object. Since the [public beta ↗︎](https://blog.cloudflare.com/sqlite-in-durable-objects/) in September 2024, we've added feature parity and robustness for the SQLite storage backend compared to the preexisting key-value (KV) storage backend for Durable Objects.

SQLite-backed Durable Objects are recommended for all new Durable Object classes, using `new_sqlite_classes` [Wrangler configuration](https://developers.cloudflare.com/durable-objects/best-practices/access-durable-objects-storage/#create-sqlite-backed-durable-object-class). Only SQLite-backed Durable Objects have access to Storage API's [SQL](https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/#sql-api) and [point-in-time recovery](https://developers.cloudflare.com/durable-objects/api/sqlite-storage-api/#pitr-point-in-time-recovery-api) methods, which provide relational data modeling, SQL querying, and better data management.

```js
export class MyDurableObject extends DurableObject {
  sql: SqlStorage
  constructor(ctx: DurableObjectState, env: Env) {
    super(ctx, env);
    this.sql = ctx.storage.sql;
  }

  async sayHello() {
    let result = this.sql
      .exec("SELECT 'Hello, World!' AS greeting")
      .one();
    return result.greeting;
  }
}
```

KV-backed Durable Objects remain for backwards compatibility, and a migration path from key-value storage to SQL storage for existing Durable Object classes will be offered in the future.

For more details on SQLite storage, checkout [Zero-latency SQLite storage in every Durable Object blog ↗︎](https://blog.cloudflare.com/sqlite-in-durable-objects/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-07-sqlite-in-durable-objects-ga/#page","headline":"SQLite in Durable Objects GA with 10GB storage per object","description":"SQLite-backed Durable Objects are generally available.","url":"https://developers.cloudflare.com/changelog/post/2025-04-07-sqlite-in-durable-objects-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-07-sqlite-in-durable-objects-ga/og.png?v=250c8ba4e7ea3c7a","dateModified":"2025-04-07","datePublished":"2025-04-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
