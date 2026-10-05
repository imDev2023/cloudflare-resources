---
description: Three new API token permissions let you scope tokens to user session revocation and SCIM resources.
title: New granular API token permissions for Cloudflare Access
image: https://developers.cloudflare.com/changelog/post/2026-01-22-granular-api-token-permissions/og.png?v=a4a47d011b021aa5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

January 22, 2026

## New granular API token permissions for Cloudflare Access

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-01-22-granular-api-token-permissions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Three new API token permissions are available for Cloudflare Access, giving you finer-grained control when building automations and integrations:

- **Access: Organizations Revoke** — Grants the ability to [revoke user sessions](https://developers.cloudflare.com/cloudflare-one/access-controls/access-settings/session-management/#revoke-user-sessions) in a Zero Trust organization. Use this permission when you need a token that can terminate active sessions without broader write access to organization settings.
- **Access: Population Read** — Grants read access to the [SCIM users and groups](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/scim/) synced from an identity provider to Cloudflare Access. Use this permission for tokens that only need to read synced user and group data.
- **Access: Population Write** — Grants write access to the [SCIM users and groups](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/scim/) synced from an identity provider to Cloudflare Access. Use this permission for tokens that need to create or modify synced user and group data.

These permissions are scoped at the account level and can be combined with existing Access permissions.

For a full list of available permissions, refer to [API token permissions](https://developers.cloudflare.com/fundamentals/api/reference/permissions/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-01-22-granular-api-token-permissions/#page","headline":"New granular API token permissions for Cloudflare Access","description":"Three new API token permissions let you scope tokens to user session revocation and SCIM resources.","url":"https://developers.cloudflare.com/changelog/post/2026-01-22-granular-api-token-permissions/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-01-22-granular-api-token-permissions/og.png?v=a4a47d011b021aa5","dateModified":"2026-01-22","datePublished":"2026-01-22","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
