---
description: The durable_object scheduling policy gives each Durable Object control of Container configuration.
title: New scheduling policy for Containers to configure image and instance from Durable Objects
image: https://developers.cloudflare.com/changelog/post/2026-09-30-durable-object-scheduling-policy/og.png?v=c282df86d1714143
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 30, 2026

## New scheduling policy for Containers to configure image and instance from Durable Objects

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-30-durable-object-scheduling-policy/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Containers](https://developers.cloudflare.com/containers/) now support the `durable_object` scheduling policy in public beta. This policy lets a Durable Object select the image and instance size for a Container at runtime instead of using one centrally managed configuration for the application.

To use custom images, configure the policy and one or more named images in Wrangler:

```jsonc
{
	"containers": [
		{
			"class_name": "AgentComputer",
			"scheduling_policy": "durable_object",
			"images": {
				"base": {
					"dockerfile": "./container/Dockerfile",
				},
			},
		},
	],
}
```

```toml
[[containers]]
class_name = "AgentComputer"
scheduling_policy = "durable_object"

[containers.images.base]
dockerfile = "./container/Dockerfile"
```

Wrangler prepares each image and exposes its immutable reference through `ctx.container.images`. Supply that reference and an instance size when you start the Container:

*src/index.jsjs*

```js
this.ctx.container.start({
	image: this.ctx.container.images.base,
	enableInternet: false,
	instance: "standard-2",
});
```

*src/index.tsts*

```ts
this.ctx.container.start({
	image: this.ctx.container.images.base,
	enableInternet: false,
	instance: "standard-2",
});
```

The `durable_object` policy also supports the new [`cloudflare/debian-trixie` Cloudflare-managed image](https://developers.cloudflare.com/containers/guides/image-management/#use-the-cloudflare-managed-image), which includes Node.js 24.20.0 on Debian Trixie slim. Start it directly without configuring a named image.

Durable Object-managed Container instances have independent lifecycles and do not participate in application-wide image rollouts.

For configuration, runtime sizing, snapshots, and update behavior, refer to [Scheduling Policies](https://developers.cloudflare.com/containers/configuration/scheduling-policy/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-30-durable-object-scheduling-policy/#page","headline":"New scheduling policy for Containers to configure image and instance from Durable Objects","description":"The durable_object scheduling policy gives each Durable Object control of Container configuration.","url":"https://developers.cloudflare.com/changelog/post/2026-09-30-durable-object-scheduling-policy/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-30-durable-object-scheduling-policy/og.png?v=c282df86d1714143","dateModified":"2026-09-30","datePublished":"2026-09-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
