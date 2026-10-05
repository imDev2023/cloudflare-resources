---
description: New environment variables allow CI/CD pipelines to programmatically access deployment information
title: Capture Wrangler command output in structured format
image: https://developers.cloudflare.com/changelog/post/2025-11-03-wrangler-output-file/og.png?v=46609c30cadebd55
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

November 3, 2025

## Capture Wrangler command output in structured format

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-11-03-wrangler-output-file/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now capture Wrangler command output in a structured [ND-JSON ↗︎](https://github.com/ndjson/ndjson-spec) format by setting the [`WRANGLER_OUTPUT_FILE_PATH`](https://developers.cloudflare.com/workers/wrangler/system-environment-variables/#supported-environment-variables) or [`WRANGLER_OUTPUT_FILE_DIRECTORY`](https://developers.cloudflare.com/workers/wrangler/system-environment-variables/#supported-environment-variables) environment variables. This feature is particularly useful for CI/CD pipelines and automation tools that need programmatic access to deployment information such as worker names, version IDs, deployment URLs, and error details. Commands that support this feature include [`wrangler deploy`](https://developers.cloudflare.com/workers/wrangler/commands/#deploy), [`wrangler versions upload`](https://developers.cloudflare.com/workers/wrangler/commands/#versions), [`wrangler versions deploy`](https://developers.cloudflare.com/workers/wrangler/commands/#versions), and [`wrangler pages deploy`](https://developers.cloudflare.com/workers/wrangler/commands/#deploy-1).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-11-03-wrangler-output-file/#page","headline":"Capture Wrangler command output in structured format","description":"New environment variables allow CI/CD pipelines to programmatically access deployment information","url":"https://developers.cloudflare.com/changelog/post/2025-11-03-wrangler-output-file/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-11-03-wrangler-output-file/og.png?v=46609c30cadebd55","dateModified":"2025-11-03","datePublished":"2025-11-03","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
