---
description: TanStack Start can now be used with the Cloudflare Vite plugin
title: Build TanStack Start apps with the Cloudflare Vite plugin
image: https://developers.cloudflare.com/changelog/post/2025-10-24-tanstack-start/og.png?v=cee1359ff37bfa32
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 24, 2025

## Build TanStack Start apps with the Cloudflare Vite plugin

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-24-tanstack-start/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/) now supports [TanStack Start ↗︎](https://tanstack.com/start/) apps. Get started with new or existing projects.

#### New projects

Create a new TanStack Start project that uses the Cloudflare Vite plugin via the `create-cloudflare` CLI:

npmyarnpnpm

```
npm create cloudflare@latest -- my-tanstack-start-app --framework=tanstack-start
```

```
yarn create cloudflare my-tanstack-start-app --framework=tanstack-start
```

```
pnpm create cloudflare@latest my-tanstack-start-app --framework=tanstack-start
```

#### Existing projects

Migrate an existing TanStack Start project to use the Cloudflare Vite plugin:

1. Install `@cloudflare/vite-plugin` and `wrangler`

npmyarnpnpmbun

```
npm i -D @cloudflare/vite-plugin wrangler
```

```
yarn add -D @cloudflare/vite-plugin wrangler
```

```
pnpm add -D @cloudflare/vite-plugin wrangler
```

```
bun add -d @cloudflare/vite-plugin wrangler
```

2. Add the Cloudflare plugin to your Vite config

*vite.config.tsts*

```ts
import { defineConfig } from "vite";
import { tanstackStart } from "@tanstack/react-start/plugin/vite";
import viteReact from "@vitejs/plugin-react";
import { cloudflare } from "@cloudflare/vite-plugin";

export default defineConfig({
	plugins: [
		cloudflare({ viteEnvironment: { name: "ssr" } }),
		tanstackStart(),
		viteReact(),
	],
});
```

3. Add your Worker config file

```jsonc
{
	"$schema": "./node_modules/wrangler/config-schema.json",
	"name": "my-tanstack-start-app",
	// Set this to today's date
	"compatibility_date": "2026-10-05",
	"compatibility_flags": [
		"nodejs_compat"
	],
	"main": "@tanstack/react-start/server-entry"
}
```

```toml
"$schema" = "./node_modules/wrangler/config-schema.json"
name = "my-tanstack-start-app"
# Set this to today's date
compatibility_date = "2026-10-05"
compatibility_flags = [ "nodejs_compat" ]
main = "@tanstack/react-start/server-entry"
```

4. Modify the scripts in your `package.json`

*package.jsonjson*

```json
{
	"scripts": {
		"dev": "vite dev",
		"build": "vite build && tsc --noEmit",
		"start": "node .output/server/index.mjs",
		"preview": "vite preview",
		"deploy": "npm run build && wrangler deploy",
		"cf-typegen": "wrangler types"
	}
}
```

See the [TanStack Start framework guide](https://developers.cloudflare.com/workers/framework-guides/web-apps/tanstack-start/) for more info.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-24-tanstack-start/#page","headline":"Build TanStack Start apps with the Cloudflare Vite plugin","description":"TanStack Start can now be used with the Cloudflare Vite plugin","url":"https://developers.cloudflare.com/changelog/post/2025-10-24-tanstack-start/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-24-tanstack-start/og.png?v=cee1359ff37bfa32","dateModified":"2025-10-24","datePublished":"2025-10-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
