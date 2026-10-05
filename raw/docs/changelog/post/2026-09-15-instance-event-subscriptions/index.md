---
description: Workflow instances now support a .subscribe() method, which let Workers and applications consume events as instances run.
title: Stream Workflow instance events in your Worker or via the API with .subscribe()
image: https://developers.cloudflare.com/changelog/post/2026-09-15-instance-event-subscriptions/og.png?v=fbf5981d7f99625f
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 15, 2026

## Stream Workflow instance events in your Worker or via the API with .subscribe()

[Workflows](https://developers.cloudflare.com/workflows/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-15-instance-event-subscriptions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now stream Workflow instance events via `WorkflowInstance.subscribe()` and the `GET /subscribe` API endpoint. Workers and HTTP clients can react to [workflow](https://developers.cloudflare.com/workflows/build/events-and-parameters/) and [step](https://developers.cloudflare.com/workflows/build/step-context/#workflowstepcontext) events, including attempts, sleeps, waits, and rollbacks, without polling for instance status.

A subscription first streams the entire event history of the Workflow instance. After streaming past events, the subscription waits for new events as the instance runs. You can use `filter` to receive only specific event types or `cursor` to start a subscription at a specific event.

Use `.subscribe()` to update Workflow status in user-facing dashboards, send notifications when steps complete, or trigger follow-up work for specific events.

```js
const instance = await env.MY_WORKFLOW.get("report-123");

using subscription = await instance.subscribe();

while (true) {
	const { value, done } = await subscription.next();
	if (done) {
		break;
	}

	console.log(value.type, value);
}
```

```ts
const instance = await env.MY_WORKFLOW.get("report-123");

using subscription = await instance.subscribe();

while (true) {
	const { value, done } = await subscription.next();
	if (done) {
		break;
	}

	console.log(value.type, value);
}
```

For event types, available fields, and subscription options, refer to [Subscribe to events](https://developers.cloudflare.com/workflows/build/subscribe-to-instance-events/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-15-instance-event-subscriptions/#page","headline":"Stream Workflow instance events in your Worker or via the API with .subscribe()","description":"Workflow instances now support a .subscribe() method, which let Workers and applications consume events as instances run.","url":"https://developers.cloudflare.com/changelog/post/2026-09-15-instance-event-subscriptions/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-15-instance-event-subscriptions/og.png?v=fbf5981d7f99625f","dateModified":"2026-09-15","datePublished":"2026-09-15","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
