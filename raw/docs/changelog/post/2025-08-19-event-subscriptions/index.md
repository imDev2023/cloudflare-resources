---
description: Subscribe to events from Cloudflare services to build custom workflows, integrations, and logic.
title: Subscribe to events from Cloudflare services with Queues
image: https://developers.cloudflare.com/changelog/post/2025-08-19-event-subscriptions/og.png?v=07ee9e0f086dd414
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 19, 2025

## Subscribe to events from Cloudflare services with Queues

[Queues](https://developers.cloudflare.com/queues/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-19-event-subscriptions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now subscribe to events from other Cloudflare services (for example, [Workers KV](https://developers.cloudflare.com/kv/), [Workers AI](https://developers.cloudflare.com/workers-ai), [Workers](https://developers.cloudflare.com/workers)) and consume those events via [Queues](https://developers.cloudflare.com/queues/), allowing you to build custom workflows, integrations, and logic in response to account activity.

![Event subscriptions architecture](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=924,height=403,format=webp/_astro/queues-event-subscriptions.3aVidnXJ.png)

Event subscriptions allow you to receive messages when events occur across your Cloudflare account. Cloudflare products can publish structured events to a queue, which you can then consume with [Workers](https://developers.cloudflare.com/workers/) or [pull via HTTP from anywhere](https://developers.cloudflare.com/queues/configuration/pull-consumers/).

To create a subscription, use the dashboard or [Wrangler](https://developers.cloudflare.com/workers/wrangler/commands/queues/#queues-subscription-create):

```bash
npx wrangler queues subscription create my-queue --source r2 --events bucket.created
```

An event is a structured record of something happening in your Cloudflare account – like a Workers AI batch request being queued, a Worker build completing, or an R2 bucket being created. Events follow a consistent structure:

*Example R2 bucket created eventjson*

```json
{
  "type": "cf.r2.bucket.created",
  "source": {
    "type": "r2"
  },
  "payload": {
    "name": "my-bucket",
    "location": "WNAM"
  },
  "metadata": {
    "accountId": "f9f79265f388666de8122cfb508d7776",
    "eventTimestamp": "2025-07-28T10:30:00Z"
  }
}
```

Current [event sources](https://developers.cloudflare.com/queues/event-subscriptions/events-schemas/) include [R2](https://developers.cloudflare.com/r2/), [Workers KV](https://developers.cloudflare.com/kv/), [Workers AI](https://developers.cloudflare.com/workers-ai/), [Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/), [Vectorize](https://developers.cloudflare.com/vectorize/), [Super Slurper](https://developers.cloudflare.com/r2/data-migration/super-slurper/), and [Workflows](https://developers.cloudflare.com/workflows/). More sources and events are on the way.

For more information on event subscriptions, available events, and how to get started, refer to our [documentation](https://developers.cloudflare.com/queues/event-subscriptions/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-19-event-subscriptions/#page","headline":"Subscribe to events from Cloudflare services with Queues","description":"Subscribe to events from Cloudflare services to build custom workflows, integrations, and logic.","url":"https://developers.cloudflare.com/changelog/post/2025-08-19-event-subscriptions/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-19-event-subscriptions/og.png?v=07ee9e0f086dd414","dateModified":"2025-08-19","datePublished":"2025-08-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
