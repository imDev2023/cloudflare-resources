---
description: Members with resource-scoped Access roles can list only the applications, policies, service tokens, and identity providers they can manage.
title: Access resource lists now support resource-scoped roles
image: https://developers.cloudflare.com/changelog/post/2026-08-19-granular-permissions-resource-lists/og.png?v=0ffabf2030dd4024
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 19, 2026

## Access resource lists now support resource-scoped roles

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/) [Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-19-granular-permissions-resource-lists/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Members with only resource-scoped Access roles can now open Access resource list pages in the Cloudflare dashboard and call list endpoints in the API. They no longer need an additional account-scoped read-only role to list resources.

The dashboard and API return only resources included in the member's permission policy scopes. Filtering applies to Access applications, policies, service tokens, and identity providers. This allows administrators to delegate specific Access resources without granting account-wide visibility. Previously, the dashboard blocked these list pages and API list requests returned `403` responses.

For members with the Cloudflare Access App Admin role, policy lists include policies attached directly to the selected application. Reusable policies appear only when the member has the Cloudflare Access Policy Admin role for those policies.

For role definitions and assignment details, refer to [Resource-scoped roles](https://developers.cloudflare.com/fundamentals/manage-members/roles/#resource-scoped-roles) and [Role scopes](https://developers.cloudflare.com/fundamentals/manage-members/scope/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-19-granular-permissions-resource-lists/#page","headline":"Access resource lists now support resource-scoped roles","description":"Members with resource-scoped Access roles can list only the applications, policies, service tokens, and identity providers they can manage.","url":"https://developers.cloudflare.com/changelog/post/2026-08-19-granular-permissions-resource-lists/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-19-granular-permissions-resource-lists/og.png?v=0ffabf2030dd4024","dateModified":"2026-08-19","datePublished":"2026-08-19","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
