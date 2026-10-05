---
description: "scheduled events are automatically dispatched according to the specified cron\ntriggers:"
title: Scheduled Events
image: https://developers.cloudflare.com/workers/testing/miniflare/core/scheduled/og.png?v=832cc50000e85d43
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/workers/llms.txt  
> Use this file to discover all available pages before exploring further.

# Scheduled Events

Last updated Sep 4, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/workers/testing/miniflare/core/scheduled/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

- [`ScheduledEvent` Reference](https://developers.cloudflare.com/workers/runtime-apis/handlers/scheduled/)

## Cron Triggers

`scheduled` events are automatically dispatched according to the specified cron triggers:

```js
const mf = new Miniflare({
	crons: ["15 * * * *", "45 * * * *"],
});
```

## HTTP Triggers

Because waiting for cron triggers is annoying, you can also make HTTP requests to `/cdn-cgi/local/scheduled` to trigger `scheduled` events:

```sh
$ curl "http://localhost:8787/cdn-cgi/local/scheduled"
```

To simulate different values of `scheduledTime` and `cron` in the dispatched event, use the `time` and `cron` query parameters:

```sh
$ curl "http://localhost:8787/cdn-cgi/local/scheduled?time=1000"
$ curl "http://localhost:8787/cdn-cgi/local/scheduled?cron=*+*+*+*+*"
```

## Dispatching Events

When using the API, the `getWorker` function can be used to dispatch `scheduled` events to your Worker. This can be used for testing responses. It takes optional `scheduledTime` and `cron` parameters, which default to the current time and the empty string respectively. It will return a promise which resolves to an array containing data returned by all waited promises:

```js
import { Miniflare } from "miniflare";

const mf = new Miniflare({
	modules: true,
	script: `
  export default {
    async scheduled(controller, env, ctx) {
      const lastScheduledController = controller;
      if (controller.cron === "* * * * *") controller.noRetry();
    }
  }
  `,
});

const worker = await mf.getWorker();

let scheduledResult = await worker.scheduled({
	cron: "* * * * *",
});
console.log(scheduledResult); // { outcome: 'ok', noRetry: true }

scheduledResult = await worker.scheduled({
	scheduledTime: new Date(1000),
	cron: "30 * * * *",
});

console.log(scheduledResult); // { outcome: 'ok', noRetry: false }
```
