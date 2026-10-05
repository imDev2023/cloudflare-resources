---
description: Browser Isolation policies support granular RBAC through Gateway account-level and resource-scoped roles.
title: Role-based access control for Browser Isolation policies
image: https://developers.cloudflare.com/changelog/post/2026-09-30-browser-isolation-rbac/og.png?v=bf3672b5ab7f8583
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 30, 2026

## Role-based access control for Browser Isolation policies

[Browser Isolation](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/) [Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-30-browser-isolation-rbac/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Isolation policies](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/) support role-based access control (RBAC). Because isolation policies are Gateway HTTP policies with the *Isolate* action, Gateway's account-level and resource-scoped roles apply to them directly.

Use the `Zero Trust HTTP Policies Admin` account-level role to grant access to all HTTP policies in the account. You can also assign a [resource-scoped role](https://developers.cloudflare.com/cloudflare-one/traffic-policies/granular-permissions/) to let a team member manage a specific isolation policy without exposing other Gateway resources.

[Policy settings](https://developers.cloudflare.com/cloudflare-one/remote-browser-isolation/isolation-policies/#policy-settings) such as copy/paste, file download/upload, keyboard, and printing are part of the policy object and follow the same permissions.

For setup instructions, refer to [Granular permissions for Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/granular-permissions/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-30-browser-isolation-rbac/#page","headline":"Role-based access control for Browser Isolation policies","description":"Browser Isolation policies support granular RBAC through Gateway account-level and resource-scoped roles.","url":"https://developers.cloudflare.com/changelog/post/2026-09-30-browser-isolation-rbac/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-30-browser-isolation-rbac/og.png?v=bf3672b5ab7f8583","dateModified":"2026-09-30","datePublished":"2026-09-30","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
