---
description: The Sandbox SDK now supports proxying WebSocket connections to container PTY sessions, enabling browser-based terminal UIs with output buffering, reconnection, and multiple isolated terminals per sandbox.
title: Interactive browser terminals in Sandboxes
image: https://developers.cloudflare.com/changelog/post/2026-02-09-pty-terminal-support/og.png?v=225add9523db5bd5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 9, 2026

## Interactive browser terminals in Sandboxes

[Agents](https://developers.cloudflare.com/agents/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-09-pty-terminal-support/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Sandbox SDK ↗︎](https://github.com/cloudflare/sandbox-sdk) now supports PTY (pseudo-terminal) passthrough, enabling browser-based terminal UIs to connect to sandbox shells via WebSocket.

#### `sandbox.terminal(request)`

The new `terminal()` method proxies a WebSocket upgrade to the container's PTY endpoint, with output buffering for replay on reconnect.

```js
// Worker: proxy WebSocket to container terminal
return sandbox.terminal(request, { cols: 80, rows: 24 });
```

```ts
// Worker: proxy WebSocket to container terminal
return sandbox.terminal(request, { cols: 80, rows: 24 });
```

#### Multiple terminals per sandbox

Each session can have its own terminal with an isolated working directory and environment, so users can run separate shells side-by-side in the same container.

```js
// Multiple isolated terminals in the same sandbox
const dev = await sandbox.getSession("dev");
return dev.terminal(request);
```

```ts
// Multiple isolated terminals in the same sandbox
const dev = await sandbox.getSession("dev");
return dev.terminal(request);
```

#### xterm.js addon

The new `@cloudflare/sandbox/xterm` export provides a `SandboxAddon` for [xterm.js ↗︎](https://xtermjs.org/) with automatic reconnection (exponential backoff + jitter), buffered output replay, and resize forwarding.

```js
import { SandboxAddon } from "@cloudflare/sandbox/xterm";

const addon = new SandboxAddon({
	getWebSocketUrl: ({ sandboxId, origin }) =>
		`${origin}/ws/terminal?id=${sandboxId}`,
	onStateChange: (state, error) => updateUI(state),
});
terminal.loadAddon(addon);
addon.connect({ sandboxId: "my-sandbox" });
```

```ts
import { SandboxAddon } from "@cloudflare/sandbox/xterm";

const addon = new SandboxAddon({
	getWebSocketUrl: ({ sandboxId, origin }) =>
		`${origin}/ws/terminal?id=${sandboxId}`,
	onStateChange: (state, error) => updateUI(state),
});
terminal.loadAddon(addon);
addon.connect({ sandboxId: "my-sandbox" });
```

#### Upgrade

To update to the latest version:

```sh
npm i @cloudflare/sandbox@latest
```

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-09-pty-terminal-support/#page","headline":"Interactive browser terminals in Sandboxes","description":"The Sandbox SDK now supports proxying WebSocket connections to container PTY sessions, enabling browser-based terminal UIs with output buffering, reconnection, and multiple isolated terminals per sandbox.","url":"https://developers.cloudflare.com/changelog/post/2026-02-09-pty-terminal-support/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-09-pty-terminal-support/og.png?v=225add9523db5bd5","dateModified":"2026-02-09","datePublished":"2026-02-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
