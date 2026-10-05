---
description: Audit Logs v2 now supports organization-level audit logs.
title: Audit Logs v2 — Organization-level support
image: https://developers.cloudflare.com/changelog/post/2026-04-23-audit-logs-v2-organization-level/og.png?v=77133886a35f34b7
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 23, 2026

## Audit Logs v2 — Organization-level support

[Audit Logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-23-audit-logs-v2-organization-level/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Audit Logs v2 now supports organization-level audit logs. Org Admins can retrieve audit events for actions performed at the organization level via the Audit Logs v2 API.

To retrieve organization-level audit logs, use the following endpoint:

```bash
GET https://api.cloudflare.com/client/v4/organizations/{organization_id}/logs/audit
```

This release covers user-initiated actions performed through organization-level APIs. Audit logs for system-initiated actions, a dashboard UI, and Logpush support for organizations will be added in future releases.

Note

Organization-level audit logs are separate from account-level audit logs. Actions performed within a specific account continue to be available via the account-level Audit Logs UI, Audit Logs v2 API, and Logpush.

For more information, refer to the [Audit Logs documentation](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-23-audit-logs-v2-organization-level/#page","headline":"Audit Logs v2 — Organization-level support","description":"Audit Logs v2 now supports organization-level audit logs.","url":"https://developers.cloudflare.com/changelog/post/2026-04-23-audit-logs-v2-organization-level/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-23-audit-logs-v2-organization-level/og.png?v=77133886a35f34b7","dateModified":"2026-04-23","datePublished":"2026-04-23","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
