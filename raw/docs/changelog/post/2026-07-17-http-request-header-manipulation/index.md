---
description: Add, overwrite, or delete HTTP request headers in Allow policies.
title: New header control options for Gateway HTTP policies
image: https://developers.cloudflare.com/changelog/post/2026-07-17-http-request-header-manipulation/og.png?v=94317ff70010640c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 17, 2026

## New header control options for Gateway HTTP policies

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-17-http-request-header-manipulation/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare Gateway now supports advanced header control on [Allow policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/#allow). Administrators can add, overwrite, or delete headers on matching requests using static values or dynamic variables.

#### Header operations

Gateway HTTP policies using the Allow action support three operations in `rule_settings`:

| Operation | API field | Behavior |
| --- | --- | --- |
| Add | `add_headers` | Appends a value to the header. Existing values are preserved. |
| Overwrite | `set_headers` | Replaces the header value. Creates the header if it does not exist. |
| Delete | `delete_headers` | Removes the header from the request. |

Gateway applies operations in order: delete, then overwrite, then add.

#### Dynamic variables

Header values can include dynamic variables using the `@{...}` syntax. Gateway resolves variables at request time from identity, device, and network context.

| Variable | Description |
| --- | --- |
| `@{identity.email}` | User email from the identity provider |
| `@{identity.name}` | User display name from the identity provider |
| `@{identity.id}` | Cloudflare identity UUID |
| `@{identity.groups}` | Identity provider group memberships |
| `@{identity.SAML}` | SAML attributes (if configured) |
| `@{identity.OIDC}` | OIDC claims (if configured) |
| `@{source.ip}` | Source IP of the connection |
| `@{destination.ip}` | Destination IP of the request |
| `@{device.id}` | Cloudflare One Client device UUID |
| `@{device.posture}` | Device posture check results (JSON string) |

You can mix static text and dynamic variables in a single header value. For example, `user-@{identity.email}` resolves to `user-jdoe@example.com`.

For more information, refer to [Custom headers](https://developers.cloudflare.com/cloudflare-one/traffic-policies/http-policies/tenant-control/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-17-http-request-header-manipulation/#page","headline":"New header control options for Gateway HTTP policies","description":"Add, overwrite, or delete HTTP request headers in Allow policies.","url":"https://developers.cloudflare.com/changelog/post/2026-07-17-http-request-header-manipulation/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-17-http-request-header-manipulation/og.png?v=94317ff70010640c","dateModified":"2026-07-17","datePublished":"2026-07-17","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
