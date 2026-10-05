---
description: With upgraded limits to [all free and paid plans](https://www.cloudflare.com/plans/), you can now extend the benefits of Cloudflare to more end customers via [Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/) and deploy more account level variables through [Cloudflare Secrets Store](https://developers.cloudflare.com/secrets-store/).
title: Increased limits for Cloudflare for SaaS and Secrets Store free and Pay-as-you-go plans
image: https://developers.cloudflare.com/changelog/post/2025-05-19-paygo-updates/og.png?v=38e0a8691574e7f4
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 27, 2025

## Increased limits for Cloudflare for SaaS and Secrets Store free and Pay-as-you-go plans

[SSL/TLS](https://developers.cloudflare.com/ssl/) [Cloudflare for SaaS](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/) [Secrets Store](https://developers.cloudflare.com/secrets-store/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-19-paygo-updates/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

With upgraded limits to [all free and paid plans ↗︎](https://www.cloudflare.com/plans/), you can now scale more easily with [Cloudflare for SaaS ↗︎](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/) and [Secrets Store ↗︎](https://developers.cloudflare.com/secrets-store/).

[Cloudflare for SaaS ↗︎](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/) allows you to extend the benefits of Cloudflare to your customers via their own custom or vanity domains. Now, the [limit for custom hostnames ↗︎](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/plans/) on a Cloudflare for SaaS Pay-as-you-go plan has been **raised from 5,000 custom hostnames to 50,000 custom hostnames.**

With custom origin server -- previously an enterprise-only feature -- you can route traffic from one or more custom hostnames somewhere other than your default proxy fallback. [Custom origin server ↗︎](https://developers.cloudflare.com/cloudflare-for-platforms/cloudflare-for-saas/start/advanced-settings/custom-origin/) is now available to Cloudflare for SaaS customers on Free, Pro, and Business plans.

You can enable custom origin server on a per-custom hostname basis [via the API ↗︎](https://developers.cloudflare.com/api/resources/custom_hostnames/methods/edit/) or the UI:

![Import repo or choose template](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1896,height=1636,format=webp/_astro/custom-origin-server.B-BXcG-1.png)

Currently [in beta with a Workers integration ↗︎](https://blog.cloudflare.com/secrets-store-beta/), [Cloudflare Secrets Store ↗︎](https://developers.cloudflare.com/secrets-store/) allows you to store, manage, and deploy account level secrets from a secure, centralized platform your [Cloudflare Workers ↗︎](https://developers.cloudflare.com/workers/). Now, you can create and deploy **100 secrets per account**. Try it out [in the dashboard ↗︎](http://dash.cloudflare.com/?to=/:account/secrets-store), with [Wrangler ↗︎](https://developers.cloudflare.com/secrets-store/integrations/workers/), or [via the API ↗︎](https://developers.cloudflare.com/api/resources/secrets_store/) today.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-19-paygo-updates/#page","headline":"Increased limits for Cloudflare for SaaS and Secrets Store free and Pay-as-you-go plans","description":"With upgraded limits to all free and paid plans, you can now extend the benefits of Cloudflare to more end customers via Cloudflare for SaaS and deploy more account level variables through Cloudflare Secrets Store.","url":"https://developers.cloudflare.com/changelog/post/2025-05-19-paygo-updates/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-19-paygo-updates/og.png?v=38e0a8691574e7f4","dateModified":"2025-05-27","datePublished":"2025-05-27","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
