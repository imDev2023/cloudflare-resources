---
description: Persist point-in-time container filesystem with snapshot APIs in public beta.
title: Snapshot and restore Container filesystem
image: https://developers.cloudflare.com/changelog/post/2026-09-30-snapshots/og.png?v=3d369698fe1a01e8
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 30, 2026

## Snapshot and restore Container filesystem

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-30-snapshots/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Containers](https://developers.cloudflare.com/containers/) now support snapshot APIs in public beta for saving and restoring point-in-time filesystem state. Create a snapshot first, then pass it back to `start()` to restore files after container sleep, restart, or handoff to another Durable Object.

Use `snapshotContainer()` through the [Durable Object Container API](https://developers.cloudflare.com/containers/api/durable-object-container/) to capture the full container filesystem. Create a snapshot from a running Container, store its handle, and pass that handle to `start()` when you restore it later:

*src/index.jsjs*

```js
import { DurableObject } from "cloudflare:workers";

export class MyDurableObject extends DurableObject {
	async saveSnapshot() {
		// Create a snapshot from the running Container.
		const containerSnapshot = await this.ctx.container.snapshotContainer({});

		await this.ctx.storage.put("containerSnapshot", containerSnapshot);
	}

	async restoreSnapshot() {
		// Restore the saved snapshot later.
		const containerSnapshot = await this.ctx.storage.get("containerSnapshot");

		if (!containerSnapshot) {
			return;
		}

		this.ctx.container.start({ containerSnapshot, enableInternet: false });
	}
}
```

*src/index.tsts*

```ts
import { DurableObject } from "cloudflare:workers";

export class MyDurableObject extends DurableObject {
	async saveSnapshot() {
		// Create a snapshot from the running Container.
		const containerSnapshot = await this.ctx.container.snapshotContainer({});

		await this.ctx.storage.put("containerSnapshot", containerSnapshot);
	}

	async restoreSnapshot() {
		// Restore the saved snapshot later.
		const containerSnapshot =
			await this.ctx.storage.get<ContainerSnapshot>("containerSnapshot");

		if (!containerSnapshot) {
			return;
		}

		this.ctx.container.start({ containerSnapshot, enableInternet: false });
	}
}
```

Snapshots are only supported for Container applications that use the [`durable_object` scheduling policy](https://developers.cloudflare.com/containers/configuration/scheduling-policy/#use-the-durable-object-scheduling-policy). Snapshots are immutable, so create a new snapshot to persist filesystem changes made after a restore.

For more information, refer to [Snapshots](https://developers.cloudflare.com/containers/guides/snapshots/) and the [Durable Object Container API](https://developers.cloudflare.com/containers/api/durable-object-container/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-30-snapshots/#page","headline":"Snapshot and restore Container filesystem","description":"Persist point-in-time container filesystem with snapshot APIs in public beta.","url":"https://developers.cloudflare.com/changelog/post/2026-09-30-snapshots/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-30-snapshots/og.png?v=3d369698fe1a01e8","dateModified":"2026-09-30","datePublished":"2026-09-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
