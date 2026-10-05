---
description: Improved Python Worker cold start performance
title: Python cold start improvements
image: https://developers.cloudflare.com/changelog/post/2025-12-08-python-cold-start-improvements/og.png?v=4649dba5f0acc63b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 8, 2025

## Python cold start improvements

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-08-python-cold-start-improvements/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Python Workers now feature improved cold start performance, reducing initialization time for new Worker instances. This improvement is particularly noticeable for Workers with larger dependency sets or complex initialization logic.

Every time you deploy a Python Worker, a memory snapshot is captured after the top level of the Worker is executed. This snapshot captures all imports, including package imports that are often costly to load. The memory snapshot is loaded when the Worker is first started, avoiding the need to reload the Python runtime and all dependencies on each cold start.

We set up a benchmark that imports common packages ([httpx ↗︎](https://www.python-httpx.org/), [fastapi ↗︎](https://fastapi.tiangolo.com/) and [pydantic ↗︎](https://docs.pydantic.dev/latest/)) to see how Python Workers stack up against other platforms:

| Platform | Mean Cold Start (ms) |
| --- | --- |
| Cloudflare Python Workers | 1027 |
| AWS Lambda | 2502 |
| Google Cloud Run | 3069 |

These benchmarks run continuously. You can view the results and the methodology on our [benchmark page ↗︎](https://cold.edgeworker.net).

In additional testing, we have found that without any memory snapshot, the cold start for this benchmark takes around 10 seconds, so this change improves cold start performance by roughly a factor of 10.

To get started with Python Workers, check out our [Python Workers overview](https://developers.cloudflare.com/workers/languages/python/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-08-python-cold-start-improvements/#page","headline":"Python cold start improvements","description":"Improved Python Worker cold start performance","url":"https://developers.cloudflare.com/changelog/post/2025-12-08-python-cold-start-improvements/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-08-python-cold-start-improvements/og.png?v=4649dba5f0acc63b","dateModified":"2025-12-08","datePublished":"2025-12-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
