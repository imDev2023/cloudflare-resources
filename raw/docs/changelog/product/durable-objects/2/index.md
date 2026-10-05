---
title: Durable Objects Changelog
image: https://developers.cloudflare.com/og-changelog.png
---

[Skip to content](#main-content)

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

Aug 21, 2025

[<h2>New getByName() API to access Durable Objects</h2>](https://developers.cloudflare.com/changelog/post/2025-08-21-durable-objects-get-by-name/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

You can now create a client (a [Durable Object stub](https://developers.cloudflare.com/durable-objects/api/stub/)) to a Durable Object with the new `getByName` method, removing the need to convert Durable Object names to IDs and then create a stub.

```js
// Before: (1) translate name to ID then (2) get a client 
const objectId = env.MY_DURABLE_OBJECT.idFromName("foo"); // or .newUniqueId()
const stub = env.MY_DURABLE_OBJECT.get(objectId); 

// Now: retrieve client to Durable Object directly via its name 
const stub = env.MY_DURABLE_OBJECT.getByName("foo");

// Use client to send request to the remote Durable Object
const rpcResponse = await stub.sayHello();
```

Each Durable Object has a globally-unique name, which allows you to send requests to a specific object from anywhere in the world. Thus, a Durable Object can be used to coordinate between multiple clients who need to work together. You can have billions of Durable Objects, providing isolation between application tenants.

To learn more, visit the Durable Objects [API Documentation](https://developers.cloudflare.com/durable-objects/api/namespace/#getbyname) or the [getting started guide](https://developers.cloudflare.com/durable-objects/get-started/).

Jun 25, 2025

[<h2>@cloudflare/actors library - SDK for Durable Objects in beta</h2>](https://developers.cloudflare.com/changelog/post/2025-06-25-actors-package-alpha/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

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

May 16, 2025

[<h2>Durable Objects are now supported in Python Workers</h2>](https://developers.cloudflare.com/changelog/post/2025-05-14-python-worker-durable-object/)

[Workers](https://developers.cloudflare.com/workers/) [Durable Objects](https://developers.cloudflare.com/durable-objects/)

You can now create [Durable Objects](https://developers.cloudflare.com/durable-objects/) using [Python Workers](https://developers.cloudflare.com/workers/languages/python/). A Durable Object is a special kind of Cloudflare Worker which uniquely combines compute with storage, enabling stateful long-running applications which run close to your users. For more info see [here](https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/).

You can define a Durable Object in Python in a similar way to JavaScript:

```python
from workers import DurableObject, Response, WorkerEntrypoint

from urllib.parse import urlparse

class MyDurableObject(DurableObject):
    def __init__(self, ctx, env):
        self.ctx = ctx
        self.env = env

    def fetch(self, request):
        result = self.ctx.storage.sql.exec("SELECT 'Hello, World!' as greeting").one()
        return Response(result.greeting)

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        url = urlparse(request.url)
        id = env.MY_DURABLE_OBJECT.idFromName(url.path)
        stub = env.MY_DURABLE_OBJECT.get(id)
        greeting = await stub.fetch(request.url)
        return greeting
```

Define the Durable Object in your Wrangler configuration file:

```jsonc
{
	"durable_objects": {
		"bindings": [
			{
				"name": "MY_DURABLE_OBJECT",
				"class_name": "MyDurableObject"
			}
		]
	}
}
```

```toml
[[durable_objects.bindings]]
name = "MY_DURABLE_OBJECT"
class_name = "MyDurableObject"
```

Then define the storage backend for your Durable Object:

```jsonc
{
	"migrations": [
		{
			"tag": "v1", // Should be unique for each entry
			"new_sqlite_classes": [ // Array of new classes
				"MyDurableObject"
			]
		}
	]
}
```

```toml
[[migrations]]
tag = "v1"
new_sqlite_classes = [ "MyDurableObject" ]
```

Then test your new Durable Object locally by running `wrangler dev`:

```bash
npx wrangler dev
```

Consult the [Durable Objects documentation](https://developers.cloudflare.com/durable-objects/) for more details.

Apr 7, 2025

[<h2>Durable Objects on Workers Free plan</h2>](https://developers.cloudflare.com/changelog/post/2025-04-07-durable-objects-free-tier/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

Durable Objects can now be used with zero commitment on the [Workers Free plan](https://developers.cloudflare.com/workers/platform/pricing/) allowing you to build AI agents with [Agents SDK](https://developers.cloudflare.com/agents/), collaboration tools, and real-time applications like chat or multiplayer games.

Durable Objects let you build stateful, serverless applications with millions of tiny coordination instances that run your application code alongside (in the same thread!) your durable storage. Each Durable Object can access its own SQLite database through a [Storage API](https://developers.cloudflare.com/durable-objects/best-practices/access-durable-objects-storage/). A Durable Object class is defined in a Worker script encapsulating the Durable Object's behavior when accessed from a Worker. To try the code below, click the button:

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/hello-world-do-template)

```js
import { DurableObject } from "cloudflare:workers";

// Durable Object
export class MyDurableObject extends DurableObject {
  ...
	async sayHello(name) {
		return `Hello, ${name}!`;
	}
}

// Worker
export default {
	async fetch(request, env) {
		// Every unique ID refers to an individual instance of the Durable Object class
		const id = env.MY_DURABLE_OBJECT.idFromName("foo");

		// A stub is a client used to invoke methods on the Durable Object
		const stub = env.MY_DURABLE_OBJECT.get(id);

		// Methods on the Durable Object are invoked via the stub
		const response = await stub.sayHello("world");

		return response;
	},
};
```

Free plan [limits](https://developers.cloudflare.com/durable-objects/platform/pricing/) apply to Durable Objects compute and storage usage. Limits allow developers to build real-world applications, with every Worker request able to call a Durable Object on the free plan.

For more information, checkout:

- [Documentation](https://developers.cloudflare.com/durable-objects/concepts/what-are-durable-objects/)
- [Zero-latency SQLite storage in every Durable Object blog ↗︎](https://blog.cloudflare.com/sqlite-in-durable-objects/)

Apr 7, 2025

[<h2>SQLite in Durable Objects GA with 10GB storage per object</h2>](https://developers.cloudflare.com/changelog/post/2025-04-07-sqlite-in-durable-objects-ga/)

[Durable Objects](https://developers.cloudflare.com/durable-objects/) [Workers](https://developers.cloudflare.com/workers/)

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
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/product/durable-objects/2/#page","headline":"Durable Objects Changelog","url":"https://developers.cloudflare.com/changelog/product/durable-objects/2/","inLanguage":"en","image":"https://developers.cloudflare.com/og-changelog.png","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
