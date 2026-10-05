---
description: Queues now supports consuming up to 5,000 messages per second per queue over HTTP.
title: Increased limits for Queues pull consumers
image: https://developers.cloudflare.com/changelog/post/2025-04-17-pull-consumer-limits/og.png?v=6a842886223dfee4
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 17, 2025

## Increased limits for Queues pull consumers

[Queues](https://developers.cloudflare.com/queues/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-17-pull-consumer-limits/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Queues pull consumers](https://developers.cloudflare.com/queues/configuration/pull-consumers/) can now pull and acknowledge up to **5,000 messages / second per queue**. Previously, pull consumers were rate limited to 1,200 requests / 5 minutes, aggregated across all queues.

Pull consumers allow you to consume messages over HTTP from any environment—including outside of [Cloudflare Workers](https://developers.cloudflare.com/workers). They’re also useful when you need fine-grained control over how quickly messages are consumed.

To setup a new queue with a pull based consumer using [Wrangler](https://developers.cloudflare.com/workers/wrangler/), run:

*Create a queue with a pull based consumersh*

```sh
npx wrangler queues create my-queue
npx wrangler queues consumer http add my-queue
```

You can also configure a pull consumer using the [REST API](https://developers.cloudflare.com/api/resources/queues/subresources/consumers/methods/create/) or the Queues dashboard.

Once configured, you can pull messages from the queue using any HTTP client. You'll need a [Cloudflare API Token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) with `queues_read` and `queues_write` permissions. For example:

*Pull messages from a queuebash*

```bash
curl "https://api.cloudflare.com/client/v4/accounts/${CF_ACCOUNT_ID}/queues/${QUEUE_ID}/messages/pull" \
--header "Authorization: Bearer ${API_TOKEN}" \
--header "Content-Type: application/json" \
--data '{ "visibility_timeout": 10000, "batch_size": 2 }'
```

To learn more about how to acknowledge messages, pull batches at once, and setup multiple consumers, refer to the [pull consumer documentation](https://developers.cloudflare.com/queues/configuration/pull-consumers).

As always, Queues doesn't charge for data egress. Pull operations continue to be billed at the [existing rate](https://developers.cloudflare.com/queues/platform/pricing), of $0.40 / million operations. The increased limits are available now, on all new and existing queues. If you're new to Queues, [get started with the Cloudflare Queues guide](https://developers.cloudflare.com/queues/get-started).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-17-pull-consumer-limits/#page","headline":"Increased limits for Queues pull consumers","description":"Queues now supports consuming up to 5,000 messages per second per queue over HTTP.","url":"https://developers.cloudflare.com/changelog/post/2025-04-17-pull-consumer-limits/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-17-pull-consumer-limits/og.png?v=6a842886223dfee4","dateModified":"2025-04-17","datePublished":"2025-04-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
