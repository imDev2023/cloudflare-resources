---
description: Workers now support up to 5 minutes of CPU time per request. Allowing more CPU-intensive workloads.
title: Run Workers for up to 5 minutes of CPU-time
image: https://developers.cloudflare.com/changelog/post/2025-03-25-higher-cpu-limits/og.png?v=7c437d85dc3a7c64
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 26, 2025

## Run Workers for up to 5 minutes of CPU-time

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-25-higher-cpu-limits/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now run a Worker for up to 5 minutes of CPU time for each request.

Previously, each Workers request ran for a maximum of 30 seconds of CPU time — that is the time that a Worker is actually performing a task (we still allowed unlimited wall-clock time, in case you were waiting on slow resources). This meant that some compute-intensive tasks were impossible to do with a Worker. For instance, you might want to take the cryptographic hash of a large file from R2. If this computation ran for over 30 seconds, the Worker request would have timed out.

By default, Workers are still limited to 30 seconds of CPU time. This protects developers from incurring accidental cost due to buggy code.

By changing the `cpu_ms` value in your Wrangler configuration, you can opt in to any value up to 300,000 (5 minutes).

```jsonc
{
	// ...rest of your configuration...
	"limits": {
		"cpu_ms": 300000,
	},
	// ...rest of your configuration...
}
```

```toml
[limits]
cpu_ms = 300_000
```

Note

CPU time is the amount of time the CPU actually spends doing work during a given request. If a Worker's request makes a sub-request and waits for that request to come back before doing additional work, this time spent waiting **is not** counted towards CPU time.

Worker requests could run for more than 30 seconds of total time prior to this change — only CPU time was limited.

For more information on the updates limits, see the documentation on [Wrangler configuration for `cpu_ms`](https://developers.cloudflare.com/workers/wrangler/configuration/#limits) and on [Workers CPU time limits](https://developers.cloudflare.com/workers/platform/limits/#cpu-time).

For building long-running tasks on Cloudflare, we also recommend checking out [Workflows](https://developers.cloudflare.com/workflows/) and [Queues](https://developers.cloudflare.com/queues/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-25-higher-cpu-limits/#page","headline":"Run Workers for up to 5 minutes of CPU-time","description":"Workers now support up to 5 minutes of CPU time per request. Allowing more CPU-intensive workloads.","url":"https://developers.cloudflare.com/changelog/post/2025-03-25-higher-cpu-limits/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-03-25-higher-cpu-limits/og.png?v=7c437d85dc3a7c64","dateModified":"2025-03-26","datePublished":"2025-03-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
