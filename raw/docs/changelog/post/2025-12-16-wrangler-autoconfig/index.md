---
description: Our new autoconfig feature makes deploying your web app to Cloudflare Workers as simple as running a single command.
title: Configure your framework for Cloudflare automatically
image: https://developers.cloudflare.com/changelog/post/2025-12-16-wrangler-autoconfig/og.png?v=982bd029d3ae6bbc
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 16, 2025

## Configure your framework for Cloudflare automatically

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-16-wrangler-autoconfig/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Wrangler now supports automatic configuration for popular web frameworks in experimental mode, making it even easier to deploy to Cloudflare Workers.

Previously, if you wanted to deploy an application using a popular web framework like Next.js or Astro, you had to follow tutorials to set up your application for deployment to Cloudflare Workers. This usually involved creating a Wrangler file, installing adapters, or changing configuration options.

Now `wrangler deploy` does this for you. Starting with Wrangler 4.55, you can use `npx wrangler deploy --x-autoconfig` in the directory of any web application using one of the supported frameworks. Wrangler will then proceed to configure and deploy it to your Cloudflare account.

You can also configure your application without deploying it by using the new `npx wrangler setup` command. This enables you to easily review what changes we are making so your application is ready for Cloudflare Workers.

The following application frameworks are supported starting today:

- Next.js
- Astro
- Nuxt
- TanStack Start
- SolidStart
- React Router
- SvelteKit
- Docusaurus
- Qwik
- Analog

Automatic configuration also supports static sites by detecting the assets directory and build command. From a single index.html file to the output of a generator like Jekyll or Hugo, you can just run `npx wrangler deploy --x-autoconfig` to upload to Cloudflare.

We're really excited to bring you automatic configuration so you can do more with Workers. Please let us know if you run into challenges using this experimentally. We’ve opened a [GitHub discussion ↗︎](https://github.com/cloudflare/workers-sdk/discussions/11667) and would love to hear your feedback.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-16-wrangler-autoconfig/#page","headline":"Configure your framework for Cloudflare automatically","description":"Our new autoconfig feature makes deploying your web app to Cloudflare Workers as simple as running a single command.","url":"https://developers.cloudflare.com/changelog/post/2025-12-16-wrangler-autoconfig/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-16-wrangler-autoconfig/og.png?v=982bd029d3ae6bbc","dateModified":"2025-12-16","datePublished":"2025-12-16","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
