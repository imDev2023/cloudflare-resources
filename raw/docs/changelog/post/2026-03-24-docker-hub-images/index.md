---
description: Use public and private Docker Hub images
title: Use Docker Hub images with Containers
image: https://developers.cloudflare.com/changelog/post/2026-03-24-docker-hub-images/og.png?v=bcc89ca6b08a11da
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 24, 2026

## Use Docker Hub images with Containers

[Containers](https://developers.cloudflare.com/containers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-24-docker-hub-images/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Containers now support [Docker Hub ↗︎](https://hub.docker.com/) images. You can use a fully qualified Docker Hub image reference in your [Wrangler configuration ↗︎](https://developers.cloudflare.com/workers/wrangler/configuration/#containers) instead of first pushing the image to Cloudflare Registry.

```jsonc
{
	"containers": [
		{
			// Example: docker.io/cloudflare/sandbox:0.7.18
			"image": "docker.io/<NAMESPACE>/<REPOSITORY>:<TAG>",
		},
	],
}
```

```toml
[[containers]]
image = "docker.io/<NAMESPACE>/<REPOSITORY>:<TAG>"
```

Containers also support private Docker Hub images. To configure credentials, refer to [Use private Docker Hub images](https://developers.cloudflare.com/containers/guides/image-management/#use-private-docker-hub-images).

For more information, refer to [Image management](https://developers.cloudflare.com/containers/guides/image-management/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-24-docker-hub-images/#page","headline":"Use Docker Hub images with Containers","description":"Use public and private Docker Hub images","url":"https://developers.cloudflare.com/changelog/post/2026-03-24-docker-hub-images/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-24-docker-hub-images/og.png?v=bcc89ca6b08a11da","dateModified":"2026-03-24","datePublished":"2026-03-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
