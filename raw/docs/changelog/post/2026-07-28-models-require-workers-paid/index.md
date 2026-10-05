---
description: Kimi K2.6, Kimi K2.7 Code, and GLM-5.2 are no longer available on the Workers Free plan.
title: Select models now require the Workers Paid plan
image: https://developers.cloudflare.com/changelog/post/2026-07-28-models-require-workers-paid/og.png?v=86dd129bab48a04c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 28, 2026

## Select models now require the Workers Paid plan

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-28-models-require-workers-paid/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We are limiting Workers Free plan access to a few resource-intensive models so we can prioritize capacity for the broader Workers AI user base. This helps everyone get a more reliable inference experience, with fewer `429` and `3040` (Out of Capacity) errors.

The following models now require the [Workers Paid plan](https://developers.cloudflare.com/workers/platform/pricing/#workers):

- [`@cf/moonshotai/kimi-k2.6`](https://developers.cloudflare.com/workers-ai/models/kimi-k2.6/)
- [`@cf/moonshotai/kimi-k2.7-code`](https://developers.cloudflare.com/workers-ai/models/kimi-k2.7-code/)
- [`@cf/zai-org/glm-5.2`](https://developers.cloudflare.com/workers-ai/models/glm-5.2/)

On the Workers Free plan, requests to these models now return a `403` HTTP error ([internal error `5035`](https://developers.cloudflare.com/workers-ai/platform/errors/)) prompting you to upgrade. The Workers Paid plan starts at $5 per month and still includes the 10,000 free Neurons per day allocation, with usage beyond that billed at each [model's pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

Many models remain available on the Workers Free plan, including:

- [`@cf/zai-org/glm-4.7-flash`](https://developers.cloudflare.com/workers-ai/models/glm-4.7-flash/)
- [`@cf/google/gemma-4-26b-a4b-it`](https://developers.cloudflare.com/workers-ai/models/gemma-4-26b-a4b-it/)
- [`@cf/nvidia/nemotron-3-120b-a12b`](https://developers.cloudflare.com/workers-ai/models/nemotron-3-120b-a12b/)

For the full list, refer to the [Workers AI model catalog](https://developers.cloudflare.com/workers-ai/models/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-28-models-require-workers-paid/#page","headline":"Select models now require the Workers Paid plan","description":"Kimi K2.6, Kimi K2.7 Code, and GLM-5.2 are no longer available on the Workers Free plan.","url":"https://developers.cloudflare.com/changelog/post/2026-07-28-models-require-workers-paid/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-28-models-require-workers-paid/og.png?v=86dd129bab48a04c","dateModified":"2026-07-28","datePublished":"2026-07-28","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
