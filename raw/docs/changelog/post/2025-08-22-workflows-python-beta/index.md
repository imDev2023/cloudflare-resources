---
description: Python Workflows is now open beta - build Workflows in Python.
title: Build durable multi-step applications in Python with Workflows (now in beta)
image: https://developers.cloudflare.com/changelog/post/2025-08-22-workflows-python-beta/og.png?v=94b274255e842837
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 22, 2025

## Build durable multi-step applications in Python with Workflows (now in beta)

[Workflows](https://developers.cloudflare.com/workflows/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-22-workflows-python-beta/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now build [Workflows](https://developers.cloudflare.com/workflows/) using Python. With Python Workflows, you get automatic retries, state persistence, and the ability to run multi-step operations that can span minutes, hours, or weeks using Python’s familiar syntax and the [Python Workers](https://developers.cloudflare.com/workers/languages/python/) runtime.

Python Workflows use the same step-based execution model as JavaScript Workflows, but with Python syntax and access to Python’s ecosystem. Python Workflows also enable [DAG (Directed Acyclic Graph) workflows](https://developers.cloudflare.com/workflows/python/dag/), where you can define complex dependencies between steps using the depends parameter.

Here’s a simple example:

```python
from workers import Response, WorkflowEntrypoint

class PythonWorkflowStarter(WorkflowEntrypoint):
    async def run(self, event, step):
        @step.do("my first step")
        async def my_first_step():
            # do some work
            return "Hello Python!"

        await my_first_step()

        await step.sleep("my-sleep-step", "10 seconds")

        @step.do("my second step")
        async def my_second_step():
            # do some more work
            return "Hello again!"

        await my_second_step()

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        await self.env.MY_WORKFLOW.create()
        return Response("Hello Workflow creation!")
```

Note

Python Workflows requires a `compatibility_date = "2025-08-01"`, or lower, in your wrangler toml file.

Python Workflows support the same core capabilities as JavaScript Workflows, including sleep scheduling, event-driven workflows, and built-in error handling with configurable retry policies.

To learn more and get started, refer to [Python Workflows documentation](https://developers.cloudflare.com/workflows/python/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-22-workflows-python-beta/#page","headline":"Build durable multi-step applications in Python with Workflows (now in beta)","description":"Python Workflows is now open beta - build Workflows in Python.","url":"https://developers.cloudflare.com/changelog/post/2025-08-22-workflows-python-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-22-workflows-python-beta/og.png?v=94b274255e842837","dateModified":"2025-08-22","datePublished":"2025-08-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
