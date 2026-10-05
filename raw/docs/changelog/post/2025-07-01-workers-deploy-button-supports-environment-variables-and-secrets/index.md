---
description: Worker environment variables, secrets, and Secrets Store secrets can now be used in Workers templates
title: Deploy to Cloudflare buttons now support Worker environment variables, secrets, and Secrets Store secrets
image: https://developers.cloudflare.com/changelog/post/2025-07-01-workers-deploy-button-supports-environment-variables-and-secrets/og.png?v=1e07c3c63519b6d7
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 29, 2025

## Deploy to Cloudflare buttons now support Worker environment variables, secrets, and Secrets Store secrets

[Workers](https://developers.cloudflare.com/workers/) [Secrets Store](https://developers.cloudflare.com/secrets-store/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-01-workers-deploy-button-supports-environment-variables-and-secrets/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Any template which uses [Worker environment variables](https://developers.cloudflare.com/workers/configuration/environment-variables/), [secrets](https://developers.cloudflare.com/workers/configuration/secrets/), or [Secrets Store secrets](https://developers.cloudflare.com/secrets-store/) can now be deployed using a [Deploy to Cloudflare button](https://developers.cloudflare.com/workers/platform/deploy-buttons/).

Define environment variables and secrets store bindings in your Wrangler configuration file as normal:

```jsonc
{
  "name": "my-worker",
  "main": "./src/index.ts",
	// Set this to today's date
	"compatibility_date": "2026-10-05",
  "vars": {
    "API_HOST": "https://example.com",
  },
	"secrets_store_secrets": [
		{
			"binding": "API_KEY",
			"store_id": "demo",
			"secret_name": "api-key"
		}
	]
}
```

```toml
name = "my-worker"
main = "./src/index.ts"
# Set this to today's date
compatibility_date = "2026-10-05"

[vars]
API_HOST = "https://example.com"

[[secrets_store_secrets]]
binding = "API_KEY"
store_id = "demo"
secret_name = "api-key"
```

Add secrets to a `.dev.vars.example` or `.env.example` file:

*.dev.vars.exampleini*

```ini
COOKIE_SIGNING_KEY=my-secret # comment
```

And optionally, you can add a description for these bindings in your template's `package.json` to help users understand how to configure each value:

*package.jsonjson*

```json
{
	"name": "my-worker",
	"private": true,
	"cloudflare": {
		"bindings": {
			"API_KEY": {
				"description": "Select your company's API key for connecting to the example service."
			},
			"COOKIE_SIGNING_KEY": {
				"description": "Generate a random string using `openssl rand -hex 32`."
			}
		}
	}
}
```

These secrets and environment variables will be presented to users in the dashboard as they deploy this template, allowing them to configure each value. Additional information about creating templates and Deploy to Cloudflare buttons can be found in [our documentation](https://developers.cloudflare.com/workers/platform/deploy-buttons/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-01-workers-deploy-button-supports-environment-variables-and-secrets/#page","headline":"Deploy to Cloudflare buttons now support Worker environment variables, secrets, and Secrets Store secrets","description":"Worker environment variables, secrets, and Secrets Store secrets can now be used in Workers templates","url":"https://developers.cloudflare.com/changelog/post/2025-07-01-workers-deploy-button-supports-environment-variables-and-secrets/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-07-01-workers-deploy-button-supports-environment-variables-and-secrets/og.png?v=1e07c3c63519b6d7","dateModified":"2025-07-29","datePublished":"2025-07-29","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
