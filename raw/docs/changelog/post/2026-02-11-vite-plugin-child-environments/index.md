---
description: The Cloudflare Vite plugin now integrates seamlessly with `@vitejs/plugin-rsc`
title: Improved React Server Components support in the Cloudflare Vite plugin
image: https://developers.cloudflare.com/changelog/post/2026-02-11-vite-plugin-child-environments/og.png?v=cefa24cdd5acc946
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 11, 2026

## Improved React Server Components support in the Cloudflare Vite plugin

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-11-vite-plugin-child-environments/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The Cloudflare Vite plugin now integrates seamlessly [@vitejs/plugin-rsc ↗︎](https://github.com/vitejs/vite-plugin-react/tree/main/packages/plugin-rsc), the official Vite plugin for [React Server Components ↗︎](https://react.dev/reference/rsc/server-components).

A `childEnvironments` option has been added to the plugin config to enable using multiple environments within a single Worker. The parent environment can then import modules from a child environment in order to access a separate module graph. For a typical RSC use case, the plugin might be configured as in the following example:

*vite.config.tsts*

```ts
export default defineConfig({
	plugins: [
		cloudflare({
			viteEnvironment: {
				name: "rsc",
				childEnvironments: ["ssr"],
			},
		}),
	],
});
```

`@vitejs/plugin-rsc` provides the lower level functionality that frameworks, such as [React Router ↗︎](https://reactrouter.com/how-to/react-server-components), build upon. The GitHub repository includes a [basic Cloudflare example ↗︎](https://github.com/vitejs/vite-plugin-react/tree/f066114c3e6bf18f5209ff3d3ef6bf1ab46d3866/packages/plugin-rsc/examples/starter-cf-single).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-11-vite-plugin-child-environments/#page","headline":"Improved React Server Components support in the Cloudflare Vite plugin","description":"The Cloudflare Vite plugin now integrates seamlessly with @vitejs/plugin-rsc","url":"https://developers.cloudflare.com/changelog/post/2026-02-11-vite-plugin-child-environments/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-11-vite-plugin-child-environments/og.png?v=cefa24cdd5acc946","dateModified":"2026-02-11","datePublished":"2026-02-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
