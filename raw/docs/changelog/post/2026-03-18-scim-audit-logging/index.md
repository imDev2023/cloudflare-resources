---
description: Track user and group provisioning events from your identity provider.
title: SCIM audit logging Support
image: https://developers.cloudflare.com/changelog/post/2026-03-18-scim-audit-logging/og.png?v=ec9ce0ef31db81b3
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 18, 2026

## SCIM audit logging Support

[Cloudflare Fundamentals](https://developers.cloudflare.com/fundamentals/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-18-scim-audit-logging/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare dashboard SCIM provisioning operations are now captured in [Audit Logs v2](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/), giving you visibility into user and group changes made by your identity provider.

![SCIM audit logging](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2556,height=1332,format=webp/_astro/2026-03-18-scim-audit-logging.DPKMiE8X.png)

**Logged actions:**

| Action Type | Description |
| --- | --- |
| Create SCIM User | User provisioned from IdP |
| Replace SCIM User | User fully replaced (PUT) |
| Update SCIM User | User attributes modified (PATCH) |
| Delete SCIM User | Member deprovisioned |
| Create SCIM Group | Group provisioned from IdP |
| Update SCIM Group | Group membership or attributes modified |
| Delete SCIM Group | Group deprovisioned |

For more details, refer to the [Audit Logs v2 documentation](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-18-scim-audit-logging/#page","headline":"SCIM audit logging Support","description":"Track user and group provisioning events from your identity provider.","url":"https://developers.cloudflare.com/changelog/post/2026-03-18-scim-audit-logging/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-18-scim-audit-logging/og.png?v=ec9ce0ef31db81b3","dateModified":"2026-03-18","datePublished":"2026-03-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
