---
description: Write your first integration test for a Cloudflare Worker with createTestHarness.
title: Get started
image: https://developers.cloudflare.com/workers/testing/test-harness/get-started/og.png?v=2eb6967b7d478d0d
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/workers/llms.txt  
> Use this file to discover all available pages before exploring further.

# Get started

Last updated Jul 27, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/workers/testing/test-harness/get-started/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This guide shows how to write a basic integration test for a Worker with `createTestHarness()`. The example uses Vitest as the test runner and exercises a Worker built with Wrangler.

## Prerequisites

You need:

- A Worker project with a [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/)
- A Node.js test runner such as [Vitest ↗︎](https://vitest.dev/)
- `wrangler` installed as a development dependency

## Create a test harness

Import `createTestHarness()` from `wrangler`. Point the test harness at your Worker configuration file.

*test/index.test.jsjs*

```js
import { createTestHarness } from "wrangler";

const server = createTestHarness({
	workers: [{ configPath: "./wrangler.jsonc" }],
});
```

*test/index.test.tsts*

```ts
import { createTestHarness } from "wrangler";

const server = createTestHarness({
	workers: [{ configPath: "./wrangler.jsonc" }],
});
```

## Manage the test harness lifecycle

For simplicity, we will reuse a single server for the test suite and reset it after each test. You can also start a new server for each test if the tests do not share the same configuration.

*test/index.test.jsjs*

```js
import { afterAll, afterEach, beforeAll } from "vitest";

beforeAll(async () => {
	// Start the server before all tests
	await server.listen();
});

afterEach(async () => {
	// Recreates storage and restores the original Worker options after each test
	await server.reset();
});

afterAll(async () => {
	// Close the server after all tests
	await server.close();
});
```

*test/index.test.tsts*

```ts
import { afterAll, afterEach, beforeAll } from "vitest";

beforeAll(async () => {
	// Start the server before all tests
	await server.listen();
});

afterEach(async () => {
	// Recreates storage and restores the original Worker options after each test
	await server.reset();
});

afterAll(async () => {
	// Close the server after all tests
	await server.close();
});
```

## Write your first test

Use the [helpers](https://developers.cloudflare.com/workers/testing/test-harness/interact-with-workers/) provided by the test harness to interact with the Worker and assert its behavior. For example, you can call `server.fetch()` to send a request to the Worker and assert against its response.

*test/index.test.jsjs*

```js
import { test } from "vitest";

test("responds", async ({ expect }) => {
	const response = await server.fetch("/");
	expect(await response.text()).toBe("Hello World");
});
```

*test/index.test.tsts*

```ts
import { test } from "vitest";

test("responds", async ({ expect }) => {
	const response = await server.fetch("/");
	expect(await response.text()).toBe("Hello World");
});
```
