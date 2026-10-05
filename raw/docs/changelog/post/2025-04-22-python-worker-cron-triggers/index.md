---
description: You can now set up scheduled handlers in your Python Workers
title: Cron triggers are now supported in Python Workers
image: https://developers.cloudflare.com/changelog/post/2025-04-22-python-worker-cron-triggers/og.png?v=4ca8ae81ece3b32b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 24, 2025

## Cron triggers are now supported in Python Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-22-python-worker-cron-triggers/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now create Python Workers which are executed via a cron trigger.

This is similar to how it's done in JavaScript Workers, simply define a scheduled event listener in your Worker:

```python
from workers import handler

@handler
async def on_scheduled(event, env, ctx):
  print("cron processed")
```

Define a cron trigger configuration in your Wrangler configuration file:

```jsonc
{
	"triggers": {
		// Schedule cron triggers:
		// - At every 3rd minute
		// - At 15:00 (UTC) on first day of the month
		// - At 23:59 (UTC) on the last weekday of the month
		"crons": [
			"*/3 * * * *",
			"0 15 1 * *",
			"59 23 LW * *"
		]
	}
}
```

```toml
[triggers]
crons = [ "*/3 * * * *", "0 15 1 * *", "59 23 LW * *" ]
```

Then test your new handler by using Wrangler with the `--test-scheduled` flag and making a request to `/cdn-cgi/local/scheduled?cron=*+*+*+*+*`:

```sh
npx wrangler dev --test-scheduled

curl "http://localhost:8787/cdn-cgi/local/scheduled?cron=*+*+*+*+*"
```

Consult the [Workers Cron Triggers page](https://developers.cloudflare.com/workers/configuration/cron-triggers/) for full details on cron triggers in Workers.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-22-python-worker-cron-triggers/#page","headline":"Cron triggers are now supported in Python Workers","description":"You can now set up scheduled handlers in your Python Workers","url":"https://developers.cloudflare.com/changelog/post/2025-04-22-python-worker-cron-triggers/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-22-python-worker-cron-triggers/og.png?v=4ca8ae81ece3b32b","dateModified":"2025-04-24","datePublished":"2025-04-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
