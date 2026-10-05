---
description: See the change history for any resource in Audit Logs, with a side-by-side diff of what changed between entries.
title: Audit Logs v2 — Resource History
image: https://developers.cloudflare.com/changelog/post/2026-07-27-audit-logs-v2-resource-history/og.png?v=370444149e8ba4fd
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 27, 2026

## Audit Logs v2 — Resource History

[Audit Logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-27-audit-logs-v2-resource-history/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Audit Logs v2 now includes **Resource History**. For any audit log entry, you can see the sequence of previous changes to the same resource and view a side-by-side diff of what was modified.

Resource History uses the audit log entries you already have. There is no additional configuration, no backend recapture, and no changes to how audit logs are generated.

![Resource History in Audit Logs v2](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1578,height=840,format=webp/_astro/Audit_logs_v2_resource_history.tpxHc9ML.png)

**Dashboard:**

1. Go to **Manage Account** > **Audit Logs**.
2. Open any audit log entry.
3. Select the **History** tab to see the full history for that resource.
4. Select any earlier entry to see a side-by-side diff of the fields that changed between it and the current entry.

**API:**

Use the History endpoint to retrieve the change history for any audit log entry:

```txt
GET https://api.cloudflare.com/client/v4/accounts/{account_id}/logs/audit/{id}/history
```

The endpoint is also available for organization-scoped audit logs at `/organizations/{organization_id}/logs/audit/{id}/history`.

For more information, refer to the [Resource History documentation](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/#resource-history).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-27-audit-logs-v2-resource-history/#page","headline":"Audit Logs v2 — Resource History","description":"See the change history for any resource in Audit Logs, with a side-by-side diff of what changed between entries.","url":"https://developers.cloudflare.com/changelog/post/2026-07-27-audit-logs-v2-resource-history/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-27-audit-logs-v2-resource-history/og.png?v=370444149e8ba4fd","dateModified":"2026-07-27","datePublished":"2026-07-27","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
