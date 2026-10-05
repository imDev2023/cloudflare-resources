---
description: You can now search through user and account API tokens by name in the dashboard and via the API.
title: Search API tokens by name
image: https://developers.cloudflare.com/changelog/post/2026-06-25-api-token-search/og.png?v=ee2f92859600eb22
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 25, 2026

## Search API tokens by name

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-25-api-token-search/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now search API tokens by name, making it easier to find specific tokens across large token lists without manually paginating.

#### What's new

- **Dashboard search**: Both [account API tokens ↗︎](https://dash.cloudflare.com/?to=/:account/account-api-tokens) and [user API tokens ↗︎](https://dash.cloudflare.com/profile/api-tokens) pages now include a search bar. Type a name to filter results.
- **API search support**: The [`/user/tokens`](https://developers.cloudflare.com/api/resources/user/subresources/tokens/methods/list/) and [`/accounts/{account_id}/tokens`](https://developers.cloudflare.com/api/resources/accounts/subresources/tokens/methods/list/) endpoints now accept a `name` query parameter to filter tokens by name.

For more information, refer to [Create an API token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) and [Account API tokens](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-25-api-token-search/#page","headline":"Search API tokens by name","description":"You can now search through user and account API tokens by name in the dashboard and via the API.","url":"https://developers.cloudflare.com/changelog/post/2026-06-25-api-token-search/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-25-api-token-search/og.png?v=ee2f92859600eb22","dateModified":"2026-06-25","datePublished":"2026-06-25","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
