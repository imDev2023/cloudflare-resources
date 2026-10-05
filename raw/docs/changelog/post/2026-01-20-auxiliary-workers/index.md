---
description: Auxiliary Workers are now fully supported when using full-stack frameworks with the Cloudflare Vite plugin
title: Use auxiliary Workers alongside full-stack frameworks
image: https://developers.cloudflare.com/changelog/post/2026-01-20-auxiliary-workers/og.png?v=9bafe247debf5c60
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 20, 2026

## Use auxiliary Workers alongside full-stack frameworks

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-20-auxiliary-workers/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Auxiliary Workers are now fully supported when using full-stack frameworks, such as [React Router](https://developers.cloudflare.com/workers/framework-guides/web-apps/react-router/) and [TanStack Start](https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/), that integrate with the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/reference/api/). They are included alongside the framework's build output in the build output directory. Note that this feature requires Vite 7 or above.

Auxiliary Workers are additional Workers that can be called via [service bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/service-bindings/) from your main (entry) Worker. They are defined in the plugin config, as in the example below:

*vite.config.tsts*

```ts
import { defineConfig } from "vite";
import { tanstackStart } from "@tanstack/react-start/plugin/vite";
import { cloudflare } from "@cloudflare/vite-plugin";

export default defineConfig({
	plugins: [
		tanstackStart(),
		cloudflare({
			viteEnvironment: { name: "ssr" },
			auxiliaryWorkers: [{ configPath: "./wrangler.aux.jsonc" }],
		}),
	],
});
```

See the Vite plugin [API docs](https://developers.cloudflare.com/workers/vite-plugin/reference/api/) for more info.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-20-auxiliary-workers/#page","headline":"Use auxiliary Workers alongside full-stack frameworks","description":"Auxiliary Workers are now fully supported when using full-stack frameworks with the Cloudflare Vite plugin","url":"https://developers.cloudflare.com/changelog/post/2026-01-20-auxiliary-workers/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-20-auxiliary-workers/og.png?v=9bafe247debf5c60","dateModified":"2026-01-20","datePublished":"2026-01-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
