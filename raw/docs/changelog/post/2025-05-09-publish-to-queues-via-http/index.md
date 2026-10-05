---
description: You can now publish messages to Cloudflare Queues from any HTTP client.
title: Publish messages to Queues directly via HTTP
image: https://developers.cloudflare.com/changelog/post/2025-05-09-publish-to-queues-via-http/og.png?v=2c3988615066762c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 9, 2025

## Publish messages to Queues directly via HTTP

[Queues](https://developers.cloudflare.com/queues/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-09-publish-to-queues-via-http/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now publish messages to [Cloudflare Queues](https://developers.cloudflare.com/queues/) directly via HTTP from any service or programming language that supports sending HTTP requests. Previously, publishing to queues was only possible from within [Cloudflare Workers](https://developers.cloudflare.com/workers/). You can already consume from queues via Workers or [HTTP pull consumers](https://developers.cloudflare.com/queues/configuration/pull-consumers/), and now publishing is just as flexible.

Publishing via HTTP requires a [Cloudflare API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with `Queues Edit` permissions for authentication. Here's a simple example:

```bash
curl "https://api.cloudflare.com/client/v4/accounts/<account_id>/queues/<queue_id>/messages" \
  -X POST \
  -H 'Authorization: Bearer <api_token>' \
  --data '{ "body": { "greeting": "hello", "timestamp":  "2025-07-24T12:00:00Z"} }'
```

You can also use our [SDKs](https://developers.cloudflare.com/fundamentals/api/reference/sdks/) for TypeScript, Python, and Go.

To get started with HTTP publishing, check out our [step-by-step example](https://developers.cloudflare.com/queues/examples/publish-to-a-queue-via-http/) and the full API documentation in our [API reference](https://developers.cloudflare.com/api/resources/queues/subresources/messages/methods/push/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-09-publish-to-queues-via-http/#page","headline":"Publish messages to Queues directly via HTTP","description":"You can now publish messages to Cloudflare Queues from any HTTP client.","url":"https://developers.cloudflare.com/changelog/post/2025-05-09-publish-to-queues-via-http/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-09-publish-to-queues-via-http/og.png?v=2c3988615066762c","dateModified":"2025-05-09","datePublished":"2025-05-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
