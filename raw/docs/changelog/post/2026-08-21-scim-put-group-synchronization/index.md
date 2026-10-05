---
description: Dashboard SCIM now supports replacing groups using HTTP PUT for full-state group synchronization.
title: Improved SCIM 2.0 group synchronization
image: https://developers.cloudflare.com/changelog/post/2026-08-21-scim-put-group-synchronization/og.png?v=9d89feda95fbad3a
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 21, 2026

## Improved SCIM 2.0 group synchronization

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-21-scim-put-group-synchronization/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Dashboard SCIM now supports replacing groups using HTTP `PUT`, as defined by [RFC 7644 section 3.5.1 ↗︎](https://datatracker.ietf.org/doc/html/rfc7644#section-3.5.1). This allows identity providers to synchronize a group's full state, including its display name, external ID, and members, in a single request.

**What's New**

**Group replacement via `PUT`**: Full-state group synchronization improves compatibility with identity providers that use replacement semantics and helps keep Cloudflare groups aligned with their source identity provider.

Note

SCIM provisioning for the Cloudflare dashboard is available to Enterprise customers. You must be a Super Administrator to complete the initial setup.

For more information:

- [SCIM provisioning overview](https://developers.cloudflare.com/fundamentals/account/account-security/scim-setup/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-21-scim-put-group-synchronization/#page","headline":"Improved SCIM 2.0 group synchronization","description":"Dashboard SCIM now supports replacing groups using HTTP PUT for full-state group synchronization.","url":"https://developers.cloudflare.com/changelog/post/2026-08-21-scim-put-group-synchronization/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-21-scim-put-group-synchronization/og.png?v=9d89feda95fbad3a","dateModified":"2026-08-21","datePublished":"2026-08-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
