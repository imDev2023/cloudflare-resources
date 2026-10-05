---
description: Scope a Cloudflare API token to selected Flagship apps instead of every app in the account.
title: Create app-scoped API tokens for Flagship
image: https://developers.cloudflare.com/changelog/post/2026-08-26-app-scoped-tokens/og.png?v=f8c9ecc1eccd97b6
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 26, 2026

## Create app-scoped API tokens for Flagship

[Flagship](https://developers.cloudflare.com/flagship/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-26-app-scoped-tokens/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now create **app-scoped API tokens** for [Flagship](https://developers.cloudflare.com/flagship/). These tokens grant access only to the Flagship apps you select, instead of every app in the account.

When you create a custom token, open the resource dropdown (it defaults to **Entire Account**) and select **Specified Flagship apps**. Then choose the app and a **Flagship App** permission: Evaluate, Read, or Write. Account-wide Flagship Evaluate, Read, and Write permissions still exist when you need access to every app.

Use app-scoped tokens in trusted server-side environments, such as Wrangler, CI, or a backend service that should only touch one app.

To create a token, refer to [API tokens](https://developers.cloudflare.com/flagship/api-tokens/) or [open the app-scoped token form ↗︎](https://dash.cloudflare.com/?to=/:account/api-tokens&permissionGroupKeys=%5B%7B%22key%22:%22flagship_app%22,%22type%22:%22evaluate%22%7D%5D&scope=specified_flagship_app) in the dashboard.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-26-app-scoped-tokens/#page","headline":"Create app-scoped API tokens for Flagship","description":"Scope a Cloudflare API token to selected Flagship apps instead of every app in the account.","url":"https://developers.cloudflare.com/changelog/post/2026-08-26-app-scoped-tokens/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-26-app-scoped-tokens/og.png?v=f8c9ecc1eccd97b6","dateModified":"2026-08-26","datePublished":"2026-08-26","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
