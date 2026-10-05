---
description: Wrangler now collects npm dependency information at deploy time and includes it in upload metadata for supply chain visibility.
title: Send npm package dependency metadata with Worker uploads
image: https://developers.cloudflare.com/changelog/post/2026-07-07-wrangler-deploy-upload-dependencies-metadata/og.png?v=3bd89c43f3c4501e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 9, 2026

## Send npm package dependency metadata with Worker uploads

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-07-wrangler-deploy-upload-dependencies-metadata/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Wrangler now collects npm package dependency information from your project's `package.json` during [`wrangler deploy`](https://developers.cloudflare.com/workers/wrangler/commands/general/#deploy) and [`wrangler versions upload`](https://developers.cloudflare.com/workers/wrangler/commands/general/#upload), and includes it in the upload metadata sent to the Cloudflare API. This data, each dependency's name, declared version range, and exact installed version, enables dependency analytics and future supply chain security features such as vulnerability alerting.

To opt out, set [`dependencies_instrumentation.enabled`](https://developers.cloudflare.com/workers/wrangler/configuration/#top-level-only-keys) to `false` in your Wrangler configuration file:

```jsonc
{
	"dependencies_instrumentation": {
		"enabled": false
	}
}
```

```toml
[dependencies_instrumentation]
enabled = false
```

For more details, refer to [Wrangler configuration](https://developers.cloudflare.com/workers/wrangler/configuration/#top-level-only-keys).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-07-wrangler-deploy-upload-dependencies-metadata/#page","headline":"Send npm package dependency metadata with Worker uploads","description":"Wrangler now collects npm dependency information at deploy time and includes it in upload metadata for supply chain visibility.","url":"https://developers.cloudflare.com/changelog/post/2026-07-07-wrangler-deploy-upload-dependencies-metadata/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-07-wrangler-deploy-upload-dependencies-metadata/og.png?v=3bd89c43f3c4501e","dateModified":"2026-07-09","datePublished":"2026-07-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
