---
description: Receive outbound transactional email lifecycle events on a queue by subscribing per sending domain.
title: Subscribe to Email Sending events with Queues
image: https://developers.cloudflare.com/changelog/post/2026-07-15-event-subscriptions/og.png?v=f8d15d49313d80f0
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 15, 2026

## Subscribe to Email Sending events with Queues

[Email Service](https://developers.cloudflare.com/email-service/) [Queues](https://developers.cloudflare.com/queues/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-15-event-subscriptions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now subscribe to **[Email Sending](https://developers.cloudflare.com/email-service/api/send-emails/) events** through [Queues event subscriptions](https://developers.cloudflare.com/queues/event-subscriptions/) and receive outbound transactional email lifecycle events on a queue. Each subscription is scoped to one sending domain — either the zone apex, such as `example.com`, or a verified sending subdomain, such as `send.example.com`.

Six event types are published: `message.delivered`, `message.deferred`, `message.bounced`, `message.failed`, `message.rejected`, and `message.complained`. Use them to track deliverability, react to bounces and complaints, and drive suppression or retry logic. Email Routing events are not published on this source.

Each event includes the message details, delivery status, and SMTP response:

```json
{
	"type": "cf.email.sending.message.delivered",
	"source": {
		"type": "email.sending",
		"zoneId": "023e105f4ecef8ad9ca31a8372d0c353",
		"domain": "example.com"
	},
	"payload": {
		"messageId": "0101018f7d0c4d9a-msg-deadbeef",
		"recipient": "user@example.net",
		"terminal": true,
		"delivery": {
			"status": "delivered",
			"smtpStatusCode": "250"
		}
	}
}
```

Refer to [Event subscriptions](https://developers.cloudflare.com/email-service/platform/event-subscriptions/) to see all event types and example payloads.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-15-event-subscriptions/#page","headline":"Subscribe to Email Sending events with Queues","description":"Receive outbound transactional email lifecycle events on a queue by subscribing per sending domain.","url":"https://developers.cloudflare.com/changelog/post/2026-07-15-event-subscriptions/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-15-event-subscriptions/og.png?v=f8d15d49313d80f0","dateModified":"2026-07-15","datePublished":"2026-07-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
