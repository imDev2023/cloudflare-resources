---
description: An agent runtime that dynamically orchestrates between isolates and containers, giving every agent a virtual filesystem and execution environment.
title: "Preview: @cloudflare/computer agent runtime"
image: https://developers.cloudflare.com/changelog/post/2026-08-03-cloudflare-computer/og.png?v=d8caed5a2ff9775e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 3, 2026

## Preview: @cloudflare/computer agent runtime

[Agents](https://developers.cloudflare.com/agents/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-03-cloudflare-computer/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We're releasing an early preview of [`@cloudflare/computer` ↗︎](https://github.com/cloudflare/computer), an open-source agent runtime that gives every agent its own computer. The runtime dynamically orchestrates between fast, efficient isolates and full Linux containers, so the agent always runs on the right compute primitive for the task at hand.

`@cloudflare/computer` provides a virtual filesystem backed by SQLite, which you can populate from cloud storage, source control, or any files you choose. Agents can read, write, and edit files, run shell commands, and interact with Git repositories. All operations are gated, audited, and observed.

Install the package via npm:

```sh
npm install @cloudflare/computer
```

Instantiate a `Workspace` inside any Durable Object to give your agent a filesystem and execution runtime:

```ts
import { Workspace } from "@cloudflare/computer";

export class Agent {
	workspace = new Workspace({
		storage: this.ctx.storage,
	});
}
```

Several execution backends are included or you can write your own:

- **Isolate runtime** — fast, horizontally scalable execution via `just-bash` and Dynamic Workers, ideal for file manipulation and data processing.
- **Container runtime** — full Linux environment via Cloudflare Containers, mounted through FUSE, for tasks that need native binaries, package managers, or a complete userland.

The AI SDK-compatible toolkit provides common agent tools (`read`, `write`, `edit`, `ls`, `exec`) and guides the model to choose the appropriate backend for each task.

For more examples, including a step-by-step tutorial, visit the [`@cloudflare/computer` repository ↗︎](https://github.com/cloudflare/computer).

Read the announcement blog post for more details: [Your agent needs a computer, not a container ↗︎](https://blog.cloudflare.com/cloudflare-computer/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-03-cloudflare-computer/#page","headline":"Preview: @cloudflare/computer agent runtime","description":"An agent runtime that dynamically orchestrates between isolates and containers, giving every agent a virtual filesystem and execution environment.","url":"https://developers.cloudflare.com/changelog/post/2026-08-03-cloudflare-computer/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-03-cloudflare-computer/og.png?v=d8caed5a2ff9775e","dateModified":"2026-08-03","datePublished":"2026-08-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
