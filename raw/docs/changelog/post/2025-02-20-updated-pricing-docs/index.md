---
description: Granular pricing in units and neurons
title: Workers AI updated pricing
image: https://developers.cloudflare.com/changelog/post/2025-02-20-updated-pricing-docs/og.png?v=aa563da6056584b9
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 20, 2025

## Workers AI updated pricing

[Workers AI](https://developers.cloudflare.com/workers-ai/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-02-20-updated-pricing-docs/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We've updated the Workers AI [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/) to include the latest models and how model usage maps to Neurons.

- Each model's core input format(s) (tokens, audio seconds, images, etc) now include mappings to Neurons, making it easier to understand how your included Neuron volume is consumed and how you are charged at scale
- Per-model pricing, instead of the previous bucket approach, allows us to be more flexible on how models are charged based on their size, performance and capabilities. As we optimize each model, we can then pass on savings for that model.
- You will still only pay for what you consume: Workers AI inference is serverless, and not billed by the hour.

Going forward, models will be launched with their associated Neuron costs, and we'll be updating the Workers AI dashboard and API to reflect consumption in both raw units and Neurons. Visit the [Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/) page to learn more about Workers AI pricing.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-02-20-updated-pricing-docs/#page","headline":"Workers AI updated pricing","description":"Granular pricing in units and neurons","url":"https://developers.cloudflare.com/changelog/post/2025-02-20-updated-pricing-docs/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-02-20-updated-pricing-docs/og.png?v=aa563da6056584b9","dateModified":"2025-02-20","datePublished":"2025-02-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
