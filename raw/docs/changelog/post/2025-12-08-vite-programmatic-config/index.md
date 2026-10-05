---
description: The Cloudflare Vite plugin can now programmatically configure Workers without a Wrangler config file, or modify existing configuration.
title: Configure Workers programmatically using the Vite plugin
image: https://developers.cloudflare.com/changelog/post/2025-12-08-vite-programmatic-config/og.png?v=081c3d8c96f44dab
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 8, 2025

## Configure Workers programmatically using the Vite plugin

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-08-vite-programmatic-config/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/) now supports programmatic configuration of Workers without a Wrangler configuration file. You can use the `config` option to define Worker settings directly in your Vite configuration, or to modify existing configuration loaded from a Wrangler config file. This is particularly useful when integrating with other build tools or frameworks, as it allows them to control Worker configuration without needing users to manage a separate config file.

#### The `config` option

The Vite plugin's new `config` option accepts either a partial configuration object or a function that receives the current configuration and returns overrides. This option is applied after any config file is loaded, allowing the plugin to override specific values or define Worker configuration entirely in code.

#### Example usage

Setting `config` to an object to provide configuration values that merge with defaults and config file settings:

*vite.config.tsts*

```ts
import { defineConfig } from "vite";
import { cloudflare } from "@cloudflare/vite-plugin";

export default defineConfig({
	plugins: [
		cloudflare({
			config: {
				name: "my-worker",
				compatibility_flags: ["nodejs_compat"],
				send_email: [
					{
						name: "EMAIL",
					},
				],
			},
		}),
	],
});
```

Use a function to modify the existing configuration:

*vite.config.tsts*

```ts
import { defineConfig } from "vite";
import { cloudflare } from "@cloudflare/vite-plugin";
export default defineConfig({
	plugins: [
		cloudflare({
			config: (userConfig) => {
				delete userConfig.compatibility_flags;
			},
		}),
	],
});
```

Return an object with values to merge:

*vite.config.tsts*

```ts
import { defineConfig } from "vite";
import { cloudflare } from "@cloudflare/vite-plugin";

export default defineConfig({
	plugins: [
		cloudflare({
			config: (userConfig) => {
				if (!userConfig.compatibility_flags.includes("no_nodejs_compat")) {
					return { compatibility_flags: ["nodejs_compat"] };
				}
			},
		}),
	],
});
```

#### Auxiliary Workers

Auxiliary Workers also support the `config` option, enabling multi-Worker architectures without config files.

Define auxiliary Workers without config files using `config` inside the `auxiliaryWorkers` array:

*vite.config.tsts*

```ts
import { defineConfig } from "vite";
import { cloudflare } from "@cloudflare/vite-plugin";

export default defineConfig({
	plugins: [
		cloudflare({
			config: {
				name: "entry-worker",
				main: "./src/entry.ts",
				services: [{ binding: "API", service: "api-worker" }],
			},
			auxiliaryWorkers: [
				{
					config: {
						name: "api-worker",
						main: "./src/api.ts",
					},
				},
			],
		}),
	],
});
```

For more details and examples, see [Programmatic configuration](https://developers.cloudflare.com/workers/vite-plugin/reference/programmatic-configuration/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-08-vite-programmatic-config/#page","headline":"Configure Workers programmatically using the Vite plugin","description":"The Cloudflare Vite plugin can now programmatically configure Workers without a Wrangler config file, or modify existing configuration.","url":"https://developers.cloudflare.com/changelog/post/2025-12-08-vite-programmatic-config/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-08-vite-programmatic-config/og.png?v=081c3d8c96f44dab","dateModified":"2025-12-08","datePublished":"2025-12-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
