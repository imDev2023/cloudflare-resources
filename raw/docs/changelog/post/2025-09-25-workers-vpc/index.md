---
description: Access private resources in your VPC from Cloudflare Workers
title: Announcing Workers VPC Services (Beta)
image: https://developers.cloudflare.com/changelog/post/2025-09-25-workers-vpc/og.png?v=19a504c698937fff
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 5, 2025

## Announcing Workers VPC Services (Beta)

[Workers VPC](https://developers.cloudflare.com/workers-vpc/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-25-workers-vpc/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

**Workers VPC Services** is now available, enabling your Workers to securely access resources in your private networks, without having to expose them on the public Internet.

#### What's new

- **VPC Services**: Create secure connections to internal APIs, databases, and services using familiar Worker binding syntax
- **Multi-cloud Support**: Connect to resources in private networks in any external cloud (AWS, Azure, GCP, etc.) or on-premise using Cloudflare Tunnels

```js
export default {
	async fetch(request, env, ctx) {
		// Perform application logic in Workers here

		// Sample call to an internal API running on ECS in AWS using the binding
		const response = await env.AWS_VPC_ECS_API.fetch("https://internal-host.example.com");

		// Additional application logic in Workers
		return new Response();
	},
};
```

#### Getting started

Set up a Cloudflare Tunnel, create a VPC Service, add service bindings to your Worker, and access private resources securely. [Refer to the documentation](https://developers.cloudflare.com/workers-vpc/) to get started.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-25-workers-vpc/#page","headline":"Announcing Workers VPC Services (Beta)","description":"Access private resources in your VPC from Cloudflare Workers","url":"https://developers.cloudflare.com/changelog/post/2025-09-25-workers-vpc/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-25-workers-vpc/og.png?v=19a504c698937fff","dateModified":"2025-11-05","datePublished":"2025-11-05","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
