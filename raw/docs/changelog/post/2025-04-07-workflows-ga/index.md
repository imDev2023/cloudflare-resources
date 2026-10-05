---
description: Workflows is now GA - ship Workflows that you can rely on in production.
title: Workflows is now Generally Available
image: https://developers.cloudflare.com/changelog/post/2025-04-07-workflows-ga/og.png?v=bf84f5e520244a95
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 7, 2025

## Workflows is now Generally Available

[Workflows](https://developers.cloudflare.com/workflows/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-07-workflows-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Workflows](https://developers.cloudflare.com/workflows/) is now *Generally Available* (or "GA"): in short, it's ready for production workloads. Alongside marking Workflows as GA, we've introduced a number of changes during the beta period, including:

- A new `waitForEvent` API that allows a Workflow to wait for an event to occur before continuing execution.
- Increased concurrency: you can [run up to 4,500 Workflow instances](https://developers.cloudflare.com/changelog/2025-02-25-workflows-concurrency-increased/) concurrently — and this will continue to grow.
- Improved observability, including new CPU time metrics that allow you to better understand which Workflow instances are consuming the most resources and/or contributing to your bill.
- Support for `vitest` for testing Workflows locally and in CI/CD pipelines.

Workflows also supports the new [increased CPU limits](https://developers.cloudflare.com/changelog/2025-03-25-higher-cpu-limits/) that apply to Workers, allowing you to run more CPU-intensive tasks (up to 5 minutes of CPU time per instance), not including the time spent waiting on network calls, AI models, or other I/O bound tasks.

#### Human-in-the-loop

The new `step.waitForEvent` API allows a Workflow instance to wait on events and data, enabling human-in-the-the-loop interactions, such as approving or rejecting a request, directly handling webhooks from other systems, or pushing event data to a Workflow while it's running.

Because Workflows are just code, you can conditionally execute code based on the result of a `waitForEvent` call, and/or call `waitForEvent` multiple times in a single Workflow based on what the Workflow needs.

For example, if you wanted to implement a human-in-the-loop approval process, you could use `waitForEvent` to wait for a user to approve or reject a request, and then conditionally execute code based on the result.

```js
import {
	WorkflowEntrypoint,
	WorkflowStep,
	WorkflowEvent,
} from "cloudflare:workers";

export class MyWorkflow extends WorkflowEntrypoint {
	async run(event, step) {
		// Other steps in your Workflow
		let stripeEvent = await step.waitForEvent(
			"receive invoice paid webhook from Stripe",
			{ type: "stripe-webhook", timeout: "1 hour" },
		);
		// Rest of your Workflow
	}
}
```

```ts
import { WorkflowEntrypoint, WorkflowStep, WorkflowEvent } from "cloudflare:workers";

export class MyWorkflow extends WorkflowEntrypoint<Env, Params> {
	async run(event: WorkflowEvent<Params>, step: WorkflowStep) {
		// Other steps in your Workflow
		let stripeEvent = await step.waitForEvent<IncomingStripeWebhook>("receive invoice paid webhook from Stripe", { type: "stripe-webhook", timeout: "1 hour" })
		// Rest of your Workflow
	}
}
```

You can then send a Workflow an event from an external service via HTTP or from within a Worker using the [Workers API](https://developers.cloudflare.com/workflows/build/workers-api/) for Workflows:

```js
export default {
	async fetch(req, env) {
		const instanceId = new URL(req.url).searchParams.get("instanceId");
		const webhookPayload = await req.json();

		let instance = await env.MY_WORKFLOW.get(instanceId);
		// Send our event, with `type` matching the event type defined in
		// our step.waitForEvent call
		await instance.sendEvent({
			type: "stripe-webhook",
			payload: webhookPayload,
		});

		return Response.json({
			status: await instance.status(),
		});
	},
};
```

```ts
export default {
  async fetch(req: Request, env: Env) {
    const instanceId = new URL(req.url).searchParams.get("instanceId")
    const webhookPayload = await req.json<Payload>()

    let instance = await env.MY_WORKFLOW.get(instanceId);
    // Send our event, with `type` matching the event type defined in
    // our step.waitForEvent call
    await instance.sendEvent({type: "stripe-webhook", payload: webhookPayload})

    return Response.json({
      status: await instance.status(),
    });
  },
};
```

Read the [GA announcement blog ↗︎](https://blog.cloudflare.com/workflows-is-now-generally-available/) to learn more about what landed as part of the Workflows GA.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-07-workflows-ga/#page","headline":"Workflows is now Generally Available","description":"Workflows is now GA - ship Workflows that you can rely on in production.","url":"https://developers.cloudflare.com/changelog/post/2025-04-07-workflows-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-07-workflows-ga/og.png?v=bf84f5e520244a95","dateModified":"2025-04-07","datePublished":"2025-04-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
