---
description: Build long-running, reliable and durable applications on Cloudflare Workers
title: Workflows is now in open beta
image: https://developers.cloudflare.com/changelog/post/2024-10-24-workflows-beta/og.png?v=0a2b4533310d9933
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 24, 2024

## Workflows is now in open beta

[Workers](https://developers.cloudflare.com/workers/) [Workflows](https://developers.cloudflare.com/workflows/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2024-10-24-workflows-beta/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Workflows is now in open beta, and available to any developer a free or paid Workers plan.

Workflows allow you to build multi-step applications that can automatically retry, persist state and run for minutes, hours, days, or weeks. Workflows introduces a programming model that makes it easier to build reliable, long-running tasks, observe as they progress, and programmatically trigger instances based on events across your services.

#### Get started

You can get started with Workflows by [following our get started guide](https://developers.cloudflare.com/workflows/get-started/guide/) and/or using `npm create cloudflare` to pull down the starter project:

```sh
npm create cloudflare@latest workflows-starter -- --template "cloudflare/workflows-starter"
```

You can open the `src/index.ts` file, extend it, and use `wrangler deploy` to deploy your first Workflow. From there, you can:

- Learn the [Workflows API](https://developers.cloudflare.com/workflows/build/workers-api/)
- [Trigger Workflows](https://developers.cloudflare.com/workflows/build/trigger-workflows/) via your Workers apps.
- Understand the [Rules of Workflows](https://developers.cloudflare.com/workflows/build/rules-of-workflows/) and how to adopt best practices

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2024-10-24-workflows-beta/#page","headline":"Workflows is now in open beta","description":"Build long-running, reliable and durable applications on Cloudflare Workers","url":"https://developers.cloudflare.com/changelog/post/2024-10-24-workflows-beta/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2024-10-24-workflows-beta/og.png?v=0a2b4533310d9933","dateModified":"2024-10-24","datePublished":"2024-10-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
