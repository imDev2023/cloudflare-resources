---
description: Declare the Workflows a Worker defines in the `exports` field of your Wrangler configuration, without adding a binding.
title: Declare Workflows in the `exports` configuration
image: https://developers.cloudflare.com/changelog/post/2026-09-24-workflow-exports/og.png?v=25a0417742b748b9
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 24, 2026

## Declare Workflows in the \`exports\` configuration

[Workflows](https://developers.cloudflare.com/workflows/) [Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-24-workflow-exports/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now declare the Workflows a Worker defines in the [`exports`](https://developers.cloudflare.com/workers/wrangler/configuration/#workflow-exports) field of your Wrangler configuration file. Previously, a Worker could only define a Workflow through a `workflows` binding, even when the Worker never called the Workflow itself.

Key each entry by the name of the class that extends `WorkflowEntrypoint`:

```jsonc
{
	"exports": {
		"MyWorkflow": {
			"type": "workflow",
			"name": "my-workflow",
			"limits": {
				"steps": 25000,
			},
			"schedules": ["0 * * * *"],
		},
	},
}
```

```toml
[exports.MyWorkflow]
type = "workflow"
name = "my-workflow"
schedules = [ "0 * * * *" ]

  [exports.MyWorkflow.limits]
  steps = 25_000
```

A `workflow` export accepts the same settings as a `workflows` binding: `limits`, `schedules`, and `default_retention`. When you run `wrangler deploy`, Wrangler creates or updates the Workflow with these settings.

You can declare a Workflow as both a binding and an export. Both declarations must use the same class, and cannot set the same setting to different values.

A `workflows` binding to a Workflow in another Worker cannot use the same `name` as a Workflow export in this Worker. Workflow names are unique per account.

Workflow exports require Wrangler 4.139.0 or above.

For more information, refer to [Declare Workflows in `exports`](https://developers.cloudflare.com/workflows/build/workers-api/#declare-workflows-in-exports).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-24-workflow-exports/#page","headline":"Declare Workflows in the `exports` configuration","description":"Declare the Workflows a Worker defines in the exports field of your Wrangler configuration, without adding a binding.","url":"https://developers.cloudflare.com/changelog/post/2026-09-24-workflow-exports/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-24-workflow-exports/og.png?v=25a0417742b748b9","dateModified":"2026-09-24","datePublished":"2026-09-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
