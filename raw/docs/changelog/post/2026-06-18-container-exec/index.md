---
description: Control additional processes from the associated Durable Object.
title: exec() is now available for Containers
image: https://developers.cloudflare.com/changelog/post/2026-06-18-container-exec/og.png?v=e916b1fcd2e487d5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 18, 2026

## exec() is now available for Containers

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-18-container-exec/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

`exec()` is now available for [Containers](https://developers.cloudflare.com/containers/). Use `this.ctx.container.exec()` to start processes inside a running Container, stream standard input and output, inspect exit codes, and signal each process.

Call `exec()` from a class extending `Container`, or from another Durable Object through `this.ctx.container`. The associated Container must already be running.

This example starts the Container when needed, then reads its Node.js version:

*src/index.jsjs*

```js
import { Container } from "@cloudflare/containers";

export class MyContainer extends Container {
	async readVersion() {
		if (!this.ctx.container.running) {
			await this.start();
		}

		const process = await this.ctx.container.exec(["node", "--version"]);
		const output = await process.output();
		const decoder = new TextDecoder();

		return {
			exitCode: output.exitCode,
			stdout: decoder.decode(output.stdout),
			stderr: decoder.decode(output.stderr),
		};
	}
}
```

*src/index.tsts*

```ts
import { Container } from "@cloudflare/containers";

export class MyContainer extends Container {
	async readVersion() {
		if (!this.ctx.container.running) {
			await this.start();
		}

		const process = await this.ctx.container.exec(["node", "--version"]);
		const output = await process.output();
		const decoder = new TextDecoder();

		return {
			exitCode: output.exitCode,
			stdout: decoder.decode(output.stdout),
			stderr: decoder.decode(output.stderr),
		};
	}
}
```

The command array starts an executable directly, without an implicit shell. Invoke a shell explicitly for pipes, redirects, or variable expansion.

One RPC method can coordinate multiple `exec()` calls in one caller-to-Durable Object round trip. It can also pass byte-oriented `ReadableStream` input or return streamed output with flow control.

For options and streaming examples, refer to [Execute commands](https://developers.cloudflare.com/containers/guides/execute-commands/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-18-container-exec/#page","headline":"exec() is now available for Containers","description":"Control additional processes from the associated Durable Object.","url":"https://developers.cloudflare.com/changelog/post/2026-06-18-container-exec/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-18-container-exec/og.png?v=e916b1fcd2e487d5","dateModified":"2026-06-18","datePublished":"2026-06-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
