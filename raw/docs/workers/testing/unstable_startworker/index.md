---
description: Write integration tests using Wrangler's `unstable_startWorker()` API
title: Wrangler's unstable_startWorker()
image: https://developers.cloudflare.com/workers/testing/unstable_startworker/og.png?v=6cc034095c06ffa5
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/workers/llms.txt  
> Use this file to discover all available pages before exploring further.

# Wrangler's unstable\_startWorker()

Last updated Jul 27, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/workers/testing/unstable_startworker/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Caution

`unstable_startWorker()` is deprecated. Cloudflare recommends using the [`createTestHarness()`](https://developers.cloudflare.com/workers/testing/test-harness/) API, which provides a harness specifically designed for integration testing.

The [`unstable_startWorker()`](https://developers.cloudflare.com/workers/wrangler/api/#unstable_startworker) API exposes the internals of the Wrangler dev server, and allows you to customize how it runs. Compared to using [Miniflare directly for testing](https://developers.cloudflare.com/workers/testing/miniflare/writing-tests/), you can pass in a Wrangler configuration file, and it will automatically load the configuration for you.

This example uses `node:test`, but should apply to any testing framework:

```ts
import assert from "node:assert";
import test, { after, before, describe } from "node:test";
import { unstable_startWorker } from "wrangler";

describe("worker", () => {
	let worker;

	before(async () => {
		worker = await unstable_startWorker({ config: "wrangler.json" });
	});

	test("hello world", async () => {
		assert.strictEqual(
			await (await worker.fetch("http://example.com")).text(),
			"Hello world",
		);
	});

	after(async () => {
		await worker.dispose();
	});
});
```
