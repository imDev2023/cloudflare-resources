---
description: sandbox.watch() returns an SSE stream of filesystem change events using native inotify, enabling real-time detection of file create, modify, delete, and move operations.
title: Real-time file watching in Sandboxes
image: https://developers.cloudflare.com/changelog/post/2026-03-03-sandbox-watch-file-events/og.png?v=8e616329f6228f7a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 3, 2026

## Real-time file watching in Sandboxes

[Agents](https://developers.cloudflare.com/agents/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-03-sandbox-watch-file-events/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Sandboxes](https://developers.cloudflare.com/sandbox/) now support real-time filesystem watching via `sandbox.watch()`. The method returns a [Server-Sent Events ↗︎](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events) stream backed by native inotify, so your Worker receives `create`, `modify`, `delete`, and `move` events as they happen inside the container.

#### `sandbox.watch(path, options)`

Pass a directory path and optional filters. The returned stream is a standard `ReadableStream` you can proxy directly to a browser client or consume server-side.

```js
// Stream events to a browser client
const stream = await sandbox.watch("/workspace/src", {
	recursive: true,
	include: ["*.ts", "*.js"],
});

return new Response(stream, {
	headers: { "Content-Type": "text/event-stream" },
});
```

```ts
// Stream events to a browser client
const stream = await sandbox.watch("/workspace/src", {
	recursive: true,
	include: ["*.ts", "*.js"],
});

return new Response(stream, {
	headers: { "Content-Type": "text/event-stream" },
});
```

#### Server-side consumption with `parseSSEStream`

Use `parseSSEStream` to iterate over events inside a Worker without forwarding them to a client.

```js
import { parseSSEStream } from "@cloudflare/sandbox";

const stream = await sandbox.watch("/workspace/src", { recursive: true });

for await (const event of parseSSEStream(stream)) {
	console.log(event.type, event.path);
}
```

```ts
import { parseSSEStream } from "@cloudflare/sandbox";
import type { FileWatchSSEEvent } from "@cloudflare/sandbox";

const stream = await sandbox.watch("/workspace/src", { recursive: true });

for await (const event of parseSSEStream<FileWatchSSEEvent>(stream)) {
	console.log(event.type, event.path);
}
```

Each event includes a `type` field (`create`, `modify`, `delete`, or `move`) and the affected `path`. Move events also include a `from` field with the original path.

#### Options

| Option | Type | Description |
| --- | --- | --- |
| `recursive` | `boolean` | Watch subdirectories. Defaults to `false`. |
| `include` | `string[]` | Glob patterns to filter events. Omit to receive all events. |

#### Upgrade

To update to the latest version:

```sh
npm i @cloudflare/sandbox@latest
```

For full API details, refer to the [Sandbox file watching reference](https://developers.cloudflare.com/sandbox/api/file-watching/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-03-sandbox-watch-file-events/#page","headline":"Real-time file watching in Sandboxes","description":"sandbox.watch() returns an SSE stream of filesystem change events using native inotify, enabling real-time detection of file create, modify, delete, and move operations.","url":"https://developers.cloudflare.com/changelog/post/2026-03-03-sandbox-watch-file-events/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-03-sandbox-watch-file-events/og.png?v=8e616329f6228f7a","dateModified":"2026-03-03","datePublished":"2026-03-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
