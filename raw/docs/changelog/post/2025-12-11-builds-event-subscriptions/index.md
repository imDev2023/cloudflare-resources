---
description: Use Queue Event Subscriptions to receive Workers Builds events and send notifications to Slack or any destination.
title: Get notified when your Workers builds succeed or fail
image: https://developers.cloudflare.com/changelog/post/2025-12-11-builds-event-subscriptions/og.png?v=848cb543d3c304b3
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 9, 2026

## Get notified when your Workers builds succeed or fail

[Workers](https://developers.cloudflare.com/workers/) [Queues](https://developers.cloudflare.com/queues/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-11-builds-event-subscriptions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now receive notifications when your Workers' builds start, succeed, fail, or get cancelled using [Event Subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/).

[Workers Builds](https://developers.cloudflare.com/workers/ci-cd/builds/) publishes events to a [Queue](https://developers.cloudflare.com/queues/) that your Worker can read messages from, and then send notifications wherever you need — Slack, Discord, email, or any webhook endpoint.

You can deploy [this Worker ↗︎](https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template) to your own Cloudflare account to send build notifications to Slack:

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template)

The template includes:

- Build status with Preview/Live URLs for successful deployments
- Inline error messages for failed builds
- Branch, commit hash, and author name

![Slack notifications showing build events](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1700,height=1088,format=webp/_astro/builds-notifications-slack.rcRiU95L.png)

For setup instructions, refer to the [template README ↗︎](https://github.com/cloudflare/templates/tree/main/workers-builds-notifications-template#readme) or the [Event Subscriptions documentation](https://developers.cloudflare.com/queues/event-subscriptions/manage-event-subscriptions/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-11-builds-event-subscriptions/#page","headline":"Get notified when your Workers builds succeed or fail","description":"Use Queue Event Subscriptions to receive Workers Builds events and send notifications to Slack or any destination.","url":"https://developers.cloudflare.com/changelog/post/2025-12-11-builds-event-subscriptions/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-11-builds-event-subscriptions/og.png?v=848cb543d3c304b3","dateModified":"2026-01-09","datePublished":"2026-01-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
