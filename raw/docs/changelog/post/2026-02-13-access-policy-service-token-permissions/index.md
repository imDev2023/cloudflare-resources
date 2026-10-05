---
description: New resource-scoped roles allow administrators to grant permissions to specific Access policies and service tokens.
title: Fine-grained permissions for Access policies and service tokens
image: https://developers.cloudflare.com/changelog/post/2026-02-13-access-policy-service-token-permissions/og.png?v=dbf16a19826cb3ff
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

February 13, 2026

## Fine-grained permissions for Access policies and service tokens

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/) [Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-02-13-access-policy-service-token-permissions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Fine-grained permissions for **Access policies** and **Access service tokens** are available. These new resource-scoped roles expand the existing RBAC model, enabling administrators to grant permissions scoped to individual resources.

#### New roles

- **Cloudflare Access policy admin**: Can edit a specific [Access policy](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) in an account.
- **Cloudflare Access service token admin**: Can edit a specific [Access service token](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/) in an account.

These roles complement the existing resource-scoped roles for Access applications, identity providers, and infrastructure targets.

For more information:

- [Resource-scoped roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/#resource-scoped-roles)
- [Role scopes](https://developers.cloudflare.com/fundamentals/manage-members/scope/)

Note

Resource-scoped roles is currently in beta.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-02-13-access-policy-service-token-permissions/#page","headline":"Fine-grained permissions for Access policies and service tokens","description":"New resource-scoped roles allow administrators to grant permissions to specific Access policies and service tokens.","url":"https://developers.cloudflare.com/changelog/post/2026-02-13-access-policy-service-token-permissions/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-02-13-access-policy-service-token-permissions/og.png?v=dbf16a19826cb3ff","dateModified":"2026-02-13","datePublished":"2026-02-13","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
