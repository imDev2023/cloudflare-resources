---
description: Members with the API Token Provisioning role can now create their Account API tokens.
title: Account members can self-serve create Account API tokens
image: https://developers.cloudflare.com/changelog/post/2026-10-01-account-api-token-provisioning/og.png?v=7ce27d3df20e03ee
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 1, 2026

## Account members can self-serve create Account API tokens

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-10-01-account-api-token-provisioning/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Account API token creation is no longer limited to Super Administrators. Members with the **API Token Provisioning** role can now create Account API tokens via the Dashboard, API, Terraform, or CF CLI, making it easier for developers and platform teams to provision credentials without depending on a Super Administrator for Account API Token Provisioning.

![Creating an Account API Token via CF CLI](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1540,height=818,format=webp/_astro/2026-10-01-account-api-token-provisioning.Dn0G5DUa.png)

#### What's new

- **Delegated creation**: Members with the **API Token Provisioning** role can create Account API tokens from the dashboard. Administrators can grant this role through the dashboard, API, or Terraform.
- **OAuth support for token creation**: OAuth clients that request the `account_api_tokens:create` scope, starting with Cloudflare CLI, can create Account API tokens.
- **Account API token permissions limited to the creator’s access at creation time**: Members can only create an Account API Token using the permissions they already have. For OAuth-created tokens, permissions are also limited to the scopes granted during authorization.
- **Creator attribution and visibility**: Account API tokens now include creator metadata. Super Administrators and Administrators can view all Account API tokens in an account, while members with the **API Token Provisioning** role can only view tokens they created.

For more information, refer to [Account API tokens](https://developers.cloudflare.com/fundamentals/api/get-started/account-owned-tokens/), [Create tokens via API](https://developers.cloudflare.com/fundamentals/api/how-to/create-via-api/), and [Roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-10-01-account-api-token-provisioning/#page","headline":"Account members can self-serve create Account API tokens","description":"Members with the API Token Provisioning role can now create their Account API tokens.","url":"https://developers.cloudflare.com/changelog/post/2026-10-01-account-api-token-provisioning/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-10-01-account-api-token-provisioning/og.png?v=7ce27d3df20e03ee","dateModified":"2026-10-01","datePublished":"2026-10-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
