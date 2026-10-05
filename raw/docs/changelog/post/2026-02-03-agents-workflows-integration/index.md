---
description: The Agents SDK v0.3.7 introduces first-class Cloudflare Workflows integration, synchronous setState() with validation hooks, fixed-interval scheduling with scheduleEvery(), and callable system improvements.
title: "Agents SDK v0.3.7: Workflows integration, synchronous state, and scheduleEvery()"
image: https://developers.cloudflare.com/changelog/post/2026-02-03-agents-workflows-integration/og.png?v=a2baf92d792ee91b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 3, 2026

## Agents SDK v0.3.7: Workflows integration, synchronous state, and scheduleEvery()

[Agents](https://developers.cloudflare.com/agents/) [Workflows](https://developers.cloudflare.com/workflows/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-03-agents-workflows-integration/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The latest release of the [Agents SDK ↗︎](https://github.com/cloudflare/agents) brings first-class support for [Cloudflare Workflows](https://developers.cloudflare.com/workflows/), synchronous state management, and new scheduling capabilities.

#### Cloudflare Workflows integration

Agents excel at real-time communication and state management. Workflows excel at durable execution. Together, they enable powerful patterns where Agents handle WebSocket connections while Workflows handle long-running tasks, retries, and human-in-the-loop flows.

Use the new `AgentWorkflow` class to define workflows with typed access to your Agent:

```js
import { AgentWorkflow } from "agents/workflows";

export class ProcessingWorkflow extends AgentWorkflow {
	async run(event, step) {
		// Call Agent methods via RPC
		await this.agent.updateStatus(event.payload.taskId, "processing");

		// Non-durable: progress reporting to clients
		await this.reportProgress({ step: "process", percent: 0.5 });
		this.broadcastToClients({ type: "update", taskId: event.payload.taskId });

		// Durable via step: idempotent, won't repeat on retry
		await step.mergeAgentState({ taskProgress: 0.5 });

		const result = await step.do("process", async () => {
			return processData(event.payload.data);
		});

		await step.reportComplete(result);
		return result;
	}
}
```

```ts
import { AgentWorkflow } from "agents/workflows";
import type { AgentWorkflowEvent, AgentWorkflowStep } from "agents/workflows";

export class ProcessingWorkflow extends AgentWorkflow<MyAgent, TaskParams> {
	async run(event: AgentWorkflowEvent<TaskParams>, step: AgentWorkflowStep) {
		// Call Agent methods via RPC
		await this.agent.updateStatus(event.payload.taskId, "processing");

		// Non-durable: progress reporting to clients
		await this.reportProgress({ step: "process", percent: 0.5 });
		this.broadcastToClients({ type: "update", taskId: event.payload.taskId });

		// Durable via step: idempotent, won't repeat on retry
		await step.mergeAgentState({ taskProgress: 0.5 });

		const result = await step.do("process", async () => {
			return processData(event.payload.data);
		});

		await step.reportComplete(result);
		return result;
	}
}
```

Start workflows from your Agent with `runWorkflow()` and handle lifecycle events:

```js
export class MyAgent extends Agent {
	async startTask(taskId, data) {
		const instanceId = await this.runWorkflow("PROCESSING_WORKFLOW", {
			taskId,
			data,
		});
		return { instanceId };
	}

	async onWorkflowProgress(workflowName, instanceId, progress) {
		this.broadcast(JSON.stringify({ type: "progress", progress }));
	}

	async onWorkflowComplete(workflowName, instanceId, result) {
		console.log(`Workflow ${instanceId} completed`);
	}

	async onWorkflowError(workflowName, instanceId, error) {
		console.error(`Workflow ${instanceId} failed:`, error);
	}
}
```

```ts
export class MyAgent extends Agent {
	async startTask(taskId: string, data: string) {
		const instanceId = await this.runWorkflow("PROCESSING_WORKFLOW", {
			taskId,
			data,
		});
		return { instanceId };
	}

	async onWorkflowProgress(
		workflowName: string,
		instanceId: string,
		progress: unknown,
	) {
		this.broadcast(JSON.stringify({ type: "progress", progress }));
	}

	async onWorkflowComplete(
		workflowName: string,
		instanceId: string,
		result?: unknown,
	) {
		console.log(`Workflow ${instanceId} completed`);
	}

	async onWorkflowError(
		workflowName: string,
		instanceId: string,
		error: unknown,
	) {
		console.error(`Workflow ${instanceId} failed:`, error);
	}
}
```

Key workflow methods on your Agent:

- `runWorkflow(workflowName, params, options?)` — Start a workflow with optional metadata
- `getWorkflow(workflowId)` / `getWorkflows(criteria?)` — Query workflows with cursor-based pagination
- `approveWorkflow(workflowId)` / `rejectWorkflow(workflowId)` — Human-in-the-loop approval flows
- `pauseWorkflow()`, `resumeWorkflow()`, `terminateWorkflow()` — Workflow control

#### Synchronous setState()

State updates are now synchronous with a new `validateStateChange()` validation hook:

```js
export class MyAgent extends Agent {
	validateStateChange(oldState, newState) {
		// Return false to reject the change
		if (newState.count < 0) return false;
		// Return modified state to transform
		return { ...newState, lastUpdated: Date.now() };
	}
}
```

```ts
export class MyAgent extends Agent<Env, State> {
	validateStateChange(oldState: State, newState: State): State | false {
		// Return false to reject the change
		if (newState.count < 0) return false;
		// Return modified state to transform
		return { ...newState, lastUpdated: Date.now() };
	}
}
```

#### scheduleEvery() for recurring tasks

The new `scheduleEvery()` method enables fixed-interval recurring tasks with built-in overlap prevention:

```js
// Run every 5 minutes
await this.scheduleEvery("syncData", 5 * 60 * 1000, { source: "api" });
```

```ts
// Run every 5 minutes
await this.scheduleEvery("syncData", 5 * 60 * 1000, { source: "api" });
```

#### Callable system improvements

- **Client-side RPC timeout** — Set timeouts on callable method invocations
- **`StreamingResponse.error(message)`** — Graceful stream error signaling
- **`getCallableMethods()`** — Introspection API for discovering callable methods
- **Connection close handling** — Pending calls are automatically rejected on disconnect

```js
await agent.call("method", [args], {
	timeout: 5000,
	stream: { onChunk, onDone, onError },
});
```

```ts
await agent.call("method", [args], {
	timeout: 5000,
	stream: { onChunk, onDone, onError },
});
```

#### Email and routing enhancements

**Secure email reply routing** — Email replies are now secured with HMAC-SHA256 signed headers, preventing unauthorized routing of emails to agent instances.

**Routing improvements:**

- `basePath` option to bypass default URL construction for custom routing
- Server-sent identity — Agents send `name` and `agent` type on connect
- New `onIdentity` and `onIdentityChange` callbacks on the client

```js
const agent = useAgent({
	basePath: "user",
	onIdentity: (name, agentType) => console.log(`Connected to ${name}`),
});
```

```ts
const agent = useAgent({
	basePath: "user",
	onIdentity: (name, agentType) => console.log(`Connected to ${name}`),
});
```

#### Upgrade

To update to the latest version:

```sh
npm i agents@latest
```

For the complete Workflows API reference and patterns, see [Run Workflows](https://developers.cloudflare.com/agents/runtime/execution/run-workflows/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-03-agents-workflows-integration/#page","headline":"Agents SDK v0.3.7: Workflows integration, synchronous state, and scheduleEvery()","description":"The Agents SDK v0.3.7 introduces first-class Cloudflare Workflows integration, synchronous setState() with validation hooks, fixed-interval scheduling with scheduleEvery(), and callable system improvements.","url":"https://developers.cloudflare.com/changelog/post/2026-02-03-agents-workflows-integration/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-03-agents-workflows-integration/og.png?v=a2baf92d792ee91b","dateModified":"2026-02-03","datePublished":"2026-02-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
