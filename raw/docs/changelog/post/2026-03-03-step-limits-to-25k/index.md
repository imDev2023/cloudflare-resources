---
description: Each Workflow instance supports 10,000 steps by default, configurable up to 25,000 steps
title: Workflows step limit increased to 25,000 steps per instance
image: https://developers.cloudflare.com/changelog/post/2026-03-03-step-limits-to-25k/og.png?v=7634941e0ac7f488
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 3, 2026

## Workflows step limit increased to 25,000 steps per instance

[Workflows](https://developers.cloudflare.com/workflows/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-03-step-limits-to-25k/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Each Workflow on Workers Paid now supports 10,000 steps by default, configurable up to 25,000 steps in your `wrangler.jsonc` file:

```json
{
	"workflows": [
		{
			"name": "my-workflow",
			"binding": "MY_WORKFLOW",
			"class_name": "MyWorkflow",
			"limits": {
				"steps": 25000
			}
		}
	]
}
```

Previously, each instance was limited to 1,024 steps. Now, Workflows can support more complex, long-running executions without the additional complexity of recursive or child workflow calls.

Note that the maximum persisted state limit per Workflow instance remains **100 MB** for Workers Free and **1 GB** for Workers Paid. Refer to [Workflows limits](https://developers.cloudflare.com/workflows/reference/limits/) for more information.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-03-step-limits-to-25k/#page","headline":"Workflows step limit increased to 25,000 steps per instance","description":"Each Workflow instance supports 10,000 steps by default, configurable up to 25,000 steps","url":"https://developers.cloudflare.com/changelog/post/2026-03-03-step-limits-to-25k/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-03-step-limits-to-25k/og.png?v=7634941e0ac7f488","dateModified":"2026-03-03","datePublished":"2026-03-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
