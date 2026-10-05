---
description: You can now create Durable Objects using Python
title: Durable Objects are now supported in Python Workers
image: https://developers.cloudflare.com/changelog/post/2025-05-14-python-worker-durable-object/og.png?v=faaf0cfad1f9171a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 16, 2025

## Durable Objects are now supported in Python Workers

[Workers](https://developers.cloudflare.com/workers/) [Durable Objects](https://developers.cloudflare.com/durable-objects/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-14-python-worker-durable-object/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

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

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-14-python-worker-durable-object/#page","headline":"Durable Objects are now supported in Python Workers","description":"You can now create Durable Objects using Python","url":"https://developers.cloudflare.com/changelog/post/2025-05-14-python-worker-durable-object/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-14-python-worker-durable-object/og.png?v=faaf0cfad1f9171a","dateModified":"2025-05-16","datePublished":"2025-05-16","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
