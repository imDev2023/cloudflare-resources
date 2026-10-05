---
description: We are changing how Python Workers are structured by default.
title: Python Workers handlers now live in an entrypoint class
image: https://developers.cloudflare.com/changelog/post/2025-08-14-new-python-handlers/og.png?v=4ad4a819f2aa8a32
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 14, 2025

## Python Workers handlers now live in an entrypoint class

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-14-new-python-handlers/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We are changing how Python Workers are structured by default. Previously, handlers were defined at the top-level of a module as `on_fetch`, `on_scheduled`, etc. methods, but now they live in an entrypoint class.

Here's an example of how to now define a Worker with a fetch handler:

```python
from workers import Response, WorkerEntrypoint

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        return Response("Hello World!")
```

To keep using the old-style handlers, you can specify the `disable_python_no_global_handlers` compatibility flag in your wrangler file:

```jsonc
{
	"compatibility_flags": [
		"disable_python_no_global_handlers"
	]
}
```

```toml
compatibility_flags = [ "disable_python_no_global_handlers" ]
```

Consult the [Python Workers documentation](https://developers.cloudflare.com/workers/languages/python/) for more details.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-14-new-python-handlers/#page","headline":"Python Workers handlers now live in an entrypoint class","description":"We are changing how Python Workers are structured by default.","url":"https://developers.cloudflare.com/changelog/post/2025-08-14-new-python-handlers/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-14-new-python-handlers/og.png?v=4ad4a819f2aa8a32","dateModified":"2025-08-14","datePublished":"2025-08-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
