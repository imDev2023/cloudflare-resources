---
description: "Specify R2 Buckets to add to your environment as follows:"
title: R2
image: https://developers.cloudflare.com/workers/testing/miniflare/storage/r2/og.png?v=4db980a2ba80aab2
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/workers/llms.txt  
> Use this file to discover all available pages before exploring further.

# R2

Last updated Jan 28, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/workers/testing/miniflare/storage/r2/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

- [R2 Reference](https://developers.cloudflare.com/r2/api/workers/workers-api-reference/)

## Buckets

Specify R2 Buckets to add to your environment as follows:

```js
const mf = new Miniflare({
	r2Buckets: ["BUCKET1", "BUCKET2"],
});
```

## Manipulating Outside Workers

For testing, it can be useful to put/get data from R2 storage outside a worker. You can do this with the `getR2Bucket` method:

```js
import { Miniflare } from "miniflare";

const mf = new Miniflare({
	modules: true,
	script: `
  export default {
    async fetch(request, env, ctx) {
      const object = await env.BUCKET.get("count");
      const value = parseInt(await object.text()) + 1;
      await env.BUCKET.put("count", value.toString());
      return new Response(value.toString());
    }
  }
  `,
	r2Buckets: ["BUCKET"],
});

const bucket = await mf.getR2Bucket("BUCKET");
await bucket.put("count", "1");

const res = await mf.dispatchFetch("http://localhost:8787/");
console.log(await res.text()); // 2
console.log(await (await bucket.get("count")).text()); // 2
```
