---
description: "@cloudflare/actors library with Durable Objects helpers and patterns."
title: "@cloudflare/actors library - SDK for Durable Objects in beta"
image: https://developers.cloudflare.com/changelog/post/2025-06-25-actors-package-alpha/og.png?v=6600cf273307b0b7
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 25, 2025

## @cloudflare/actors library - SDK for Durable Objects in beta

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-25-actors-package-alpha/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The new [@cloudflare/actors ↗︎](https://www.npmjs.com/package/@cloudflare/actors) library is now in beta!

The `@cloudflare/actors` library is a new SDK for Durable Objects and provides a powerful set of abstractions for building real-time, interactive, and multiplayer applications on top of Durable Objects. With beta usage and feedback, `@cloudflare/actors` will become the recommended way to build on Durable Objects and draws upon Cloudflare's experience building products/features on Durable Objects.

The name "actors" originates from the [actor programming model](https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/#actor-programming-model), which closely ties to how Durable Objects are modelled.

The `@cloudflare/actors` library includes:

- Storage helpers for querying embeddeded, per-object SQLite storage
- Storage helpers for managing SQL schema migrations
- Alarm helpers for scheduling multiple alarms provided a date, delay in seconds, or cron expression
- `Actor` class for using Durable Objects with a defined pattern
- Durable Objects [Workers API ↗︎](https://developers.cloudflare.com/durable-objects/api/base/) is always available for your application as needed

Storage and alarm helper methods can be combined with [any Javascript class ↗︎](https://github.com/cloudflare/actors?tab=readme-ov-file#storage--alarms-with-durableobject-class) that defines your Durable Object, i.e, ones that extend `DurableObject` including the `Actor` class.

```js
import { Storage } from "@cloudflare/actors/storage";

export class ChatRoom extends DurableObject<Env> {
    storage: Storage;

    constructor(ctx: DurableObjectState, env: Env) {
        super(ctx, env)
        this.storage = new Storage(ctx.storage);
        this.storage.migrations = [{
            idMonotonicInc: 1,
            description: "Create users table",
            sql: "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY)"
        }]
    }
    async fetch(request: Request): Promise<Response> {
        // Run migrations before executing SQL query
        await this.storage.runMigrations();

        // Query with SQL template
        let userId = new URL(request.url).searchParams.get("userId");
        const query = this.storage.sql`SELECT * FROM users WHERE id = ${userId};`
        return new Response(`${JSON.stringify(query)}`);
    }
}
```

`@cloudflare/actors` library introduces the `Actor` class pattern. `Actor` lets you access Durable Objects without writing the Worker that communicates with your Durable Object (the Worker is created for you). By default, requests are routed to a Durable Object named "default".

```js
export class MyActor extends Actor<Env> {
    async fetch(request: Request): Promise<Response> {
        return new Response('Hello, World!')
    }
}

export default handler(MyActor);
```

You can [route](https://developers.cloudflare.com/durable-objects/get-started/#3-instantiate-and-communicate-with-a-durable-object) to different Durable Objects by name within your `Actor` class using [`nameFromRequest` ↗︎](https://github.com/cloudflare/actors?tab=readme-ov-file#actor-with-custom-name).

```js
export class MyActor extends Actor<Env> {
    static nameFromRequest(request: Request): string {
        let url = new URL(request.url);
        return url.searchParams.get("userId") ?? "foo";
    }

    async fetch(request: Request): Promise<Response> {
        return new Response(`Actor identifier (Durable Object name): ${this.identifier}`);
    }
}

export default handler(MyActor);
```

For more examples, check out the library [README ↗︎](https://github.com/cloudflare/actors?tab=readme-ov-file#getting-started). `@cloudflare/actors` library is a place for more helpers and built-in patterns, like retry handling and Websocket-based applications, to reduce development overhead for common Durable Objects functionality. Please share feedback and what more you would like to see on our [Discord channel ↗︎](https://discord.com/channels/595317990191398933/773219443911819284).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-25-actors-package-alpha/#page","headline":"@cloudflare/actors library - SDK for Durable Objects in beta","description":"@cloudflare/actors library with Durable Objects helpers and patterns.","url":"https://developers.cloudflare.com/changelog/post/2025-06-25-actors-package-alpha/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-25-actors-package-alpha/og.png?v=6600cf273307b0b7","dateModified":"2025-06-25","datePublished":"2025-06-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
