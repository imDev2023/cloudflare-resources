---
description: New Worker binding methods, enhancing integration capabilities for developers.
title: AI Gateway Introduces New Worker Binding Methods
image: https://developers.cloudflare.com/changelog/post/2025-01-26-worker-binding-methods/og.png?v=8111652167c03a2e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 30, 2025

## AI Gateway Introduces New Worker Binding Methods

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-01-26-worker-binding-methods/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We have released new [Workers bindings API methods](https://developers.cloudflare.com/ai-gateway/usage/worker-binding-methods/), allowing you to connect Workers applications to AI Gateway directly. These methods simplify how Workers calls AI services behind your AI Gateway configurations, removing the need to use the REST API and manually authenticate.

To add an AI binding to your Worker, include the following in your [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/):

![Add an AI binding to your Worker.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=754,height=135,format=webp/_astro/add-binding.BoYTiyon.png)

With the new AI Gateway binding methods, you can now:

- Send feedback and update metadata with `patchLog`.
- Retrieve detailed log information using `getLog`.
- Execute [universal requests](https://developers.cloudflare.com/ai-gateway/usage/universal/) to any AI Gateway provider with `run`.

For example, to send feedback and update metadata using `patchLog`:

![Send feedback and update metadata using patchLog:](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=736,height=235,format=webp/_astro/send-feedback.BGRzKmd9.png)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-01-26-worker-binding-methods/#page","headline":"AI Gateway Introduces New Worker Binding Methods","description":"New Worker binding methods, enhancing integration capabilities for developers.","url":"https://developers.cloudflare.com/changelog/post/2025-01-26-worker-binding-methods/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-01-26-worker-binding-methods/og.png?v=8111652167c03a2e","dateModified":"2025-01-30","datePublished":"2025-01-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
