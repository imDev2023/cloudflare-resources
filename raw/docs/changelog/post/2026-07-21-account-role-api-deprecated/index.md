---
description: Account Role API is deprecated in favor of the Permission Group API.
title: Account Role API deprecated
image: https://developers.cloudflare.com/changelog/post/2026-07-21-account-role-api-deprecated/og.png?v=5f69ea9739d34d79
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 21, 2026

## Account Role API deprecated

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-21-account-role-api-deprecated/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The [Account Roles API](https://developers.cloudflare.com/api/resources/accounts/subresources/roles/) is deprecated and is being replaced by the [Permission Groups API](https://developers.cloudflare.com/api/resources/iam/subresources/permission_groups/). An end of life date has not yet been established.

#### What you need to do

Review the [Permission Groups API](https://developers.cloudflare.com/api/resources/iam/subresources/permission_groups/) documentation; the response schema differs from the legacy Roles response.

#### Highlights

- Integrations migrating to the Permission Groups API must obtain Permission Group IDs from that API and use them in the Account Members API policies request shape. Integrations that persist legacy Role IDs will need to remap their assignments.
- The legacy `Role` response includes a top-level `description` and a `permissions` object keyed by resource type with edit/read flags.
- The `PermissionGroup` response replaces those with a `meta` object containing `label` and `scopes`. Individual permissions are not returned as part of the permission group.
- The new API supports the [API Token](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) authorization scheme. The legacy Email + API Key authorization schema is provided for backwards compatibility.

For more information, refer to [API deprecations](https://developers.cloudflare.com/fundamentals/api/reference/deprecations/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-21-account-role-api-deprecated/#page","headline":"Account Role API deprecated","description":"Account Role API is deprecated in favor of the Permission Group API.","url":"https://developers.cloudflare.com/changelog/post/2026-07-21-account-role-api-deprecated/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-21-account-role-api-deprecated/og.png?v=5f69ea9739d34d79","dateModified":"2026-07-21","datePublished":"2026-07-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
