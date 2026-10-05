---
description: Python Workers now support WSGI web frameworks like Django and Flask.
title: Python Workers now support WSGI web frameworks like Django and Flask
image: https://developers.cloudflare.com/changelog/post/2026-09-02-python-workers-web-framework-support/og.png?v=4f44d602ba9371e1
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 2, 2026

## Python Workers now support WSGI web frameworks like Django and Flask

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-02-python-workers-web-framework-support/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Python web frameworks following the [Web Server Gateway Interface (WSGI) ↗︎](https://peps.python.org/pep-3333/) or [Asynchronous Server Gateway Interface (ASGI) ↗︎](https://asgi.readthedocs.io/) specification can now be used in Python Workers.

#### Using web frameworks with Python Workers

Based on the web framework you are using, you can use either `wsgi` or `asgi` from the `workers` module.

#### WSGI frameworks

For WSGI frameworks like Django or Flask:

```python
from workers import wsgi

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()
Default = wsgi.entrypoint(app)
```

The `wsgi.entrypoint` is equivalent to creating a `WorkerEntrypoint` class and using the `wsgi.fetch` method. If you want more control over the `WorkerEntrypoint` class, you can do so:

```python
from workers import wsgi, WorkerEntrypoint

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        return await wsgi.fetch(app, request, self.env)
```

#### ASGI frameworks

For ASGI frameworks like FastAPI or Starlette:

```python
from workers import asgi

from fastapi import FastAPI

app = FastAPI()
Default = asgi.entrypoint(app)
```

For more information about using individual web frameworks, refer to the [packages documentation in Python Workers](https://developers.cloudflare.com/workers/languages/python/packages/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-02-python-workers-web-framework-support/#page","headline":"Python Workers now support WSGI web frameworks like Django and Flask","description":"Python Workers now support WSGI web frameworks like Django and Flask.","url":"https://developers.cloudflare.com/changelog/post/2026-09-02-python-workers-web-framework-support/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-02-python-workers-web-framework-support/og.png?v=4f44d602ba9371e1","dateModified":"2026-09-02","datePublished":"2026-09-02","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
