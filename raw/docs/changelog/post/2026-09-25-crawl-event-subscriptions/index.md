---
description: Receive crawl lifecycle events through Cloudflare Queues.
title: Subscribe to Browser Run crawl events
image: https://developers.cloudflare.com/changelog/post/2026-09-25-crawl-event-subscriptions/og.png?v=b554776c08c16fc5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 25, 2026

## Subscribe to Browser Run crawl events

[Browser Run](https://developers.cloudflare.com/browser-run/) [Queues](https://developers.cloudflare.com/queues/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-25-crawl-event-subscriptions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Browser Run crawl jobs](https://developers.cloudflare.com/browser-run/quick-actions/crawl-endpoint/) can publish lifecycle events to [Cloudflare Queues](https://developers.cloudflare.com/queues/). Subscribe to started, updated, and finished events to track progress or trigger downstream processing without polling.

To create an account-level subscription, run the following command:

npmyarnpnpm

```
npx wrangler queues subscription create <QUEUE_NAME> --source browserRun --events crawl.started,crawl.updated,crawl.finished
```

```
yarn wrangler queues subscription create <QUEUE_NAME> --source browserRun --events crawl.started,crawl.updated,crawl.finished
```

```
pnpm wrangler queues subscription create <QUEUE_NAME> --source browserRun --events crawl.started,crawl.updated,crawl.finished
```

For payload examples, refer to the [Browser Run event schemas](https://developers.cloudflare.com/queues/event-subscriptions/events-schemas/#browser-run).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-25-crawl-event-subscriptions/#page","headline":"Subscribe to Browser Run crawl events","description":"Receive crawl lifecycle events through Cloudflare Queues.","url":"https://developers.cloudflare.com/changelog/post/2026-09-25-crawl-event-subscriptions/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-25-crawl-event-subscriptions/og.png?v=b554776c08c16fc5","dateModified":"2026-09-25","datePublished":"2026-09-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
