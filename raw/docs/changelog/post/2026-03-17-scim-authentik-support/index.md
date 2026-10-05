---
description: Provision users and groups to the Cloudflare Dashboard using Authentik as your identity provider.
title: SCIM provisioning for Authentik is now Generally Available
image: https://developers.cloudflare.com/changelog/post/2026-03-17-scim-authentik-support/og.png?v=1a236e9f2f39d4eb
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 18, 2026

## SCIM provisioning for Authentik is now Generally Available

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-17-scim-authentik-support/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare dashboard SCIM provisioning now supports [Authentik ↗︎](https://goauthentik.io/) as an identity provider, joining Okta and Microsoft Entra ID as explicitly supported providers.

Customers can now sync users and group information from Authentik to Cloudflare, apply Permission Policies to those groups, and manage the lifecycle of users & groups directly from your Authentik Identity Provider.

Note

SCIM provisioning for the Cloudflare dashboard is available to Enterprise customers. You must be a Super Administrator to complete the initial setup.

For more information:

- [SCIM provisioning overview](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/)
- [Provision with Authentik](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/authentik/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-17-scim-authentik-support/#page","headline":"SCIM provisioning for Authentik is now Generally Available","description":"Provision users and groups to the Cloudflare Dashboard using Authentik as your identity provider.","url":"https://developers.cloudflare.com/changelog/post/2026-03-17-scim-authentik-support/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-17-scim-authentik-support/og.png?v=1a236e9f2f39d4eb","dateModified":"2026-03-18","datePublished":"2026-03-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
