---
description: Audit Logs v2 is now generally available
title: Audit logs (version 2) - General Availability
image: https://developers.cloudflare.com/changelog/post/2026-03-10-audit-logs-v2-ga/og.png?v=662024018ffe863d
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 10, 2026

## Audit logs (version 2) - General Availability

[Audit Logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-10-audit-logs-v2-ga/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Audit Logs v2 is now generally available to all Cloudflare customers.

![Audit Logs v2 GA](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=800,height=319,format=webp/_astro/auditlogsv2.C3pqAR33.gif)

Audit Logs v2 provides a unified and standardized system for tracking and recording all user and system actions across Cloudflare products. Built on Cloudflare's API Shield / OpenAPI gateway, logs are generated automatically without requiring manual instrumentation from individual product teams, ensuring consistency across \~95% of Cloudflare products.

**What's available at GA:**

- **Standardized logging** — Audit logs follow a consistent format across all Cloudflare products, making it easier to search, filter, and investigate activity.
- **Expanded product coverage** — \~95% of Cloudflare products covered, up from \~75% in v1.
- **Granular filtering** — Filter by actor, action type, action result, resource, raw HTTP method, zone, and more. Over 20 filter parameters available via the API.
- **Enhanced context** — Each log entry includes authentication method, interface (API or dashboard), Cloudflare Ray ID, and actor token details.
- **18-month retention** — Logs are retained for 18 months. Full history is accessible via the API or Logpush.

**Access:**

- **Dashboard**: Go to **Manage Account** > **Audit Logs**. Audit Logs v2 is shown by default.
- **API**: `GET https://api.cloudflare.com/client/v4/accounts/{account_id}/logs/audit`
- **Logpush**: Available via the `audit_logs_v2` account-scoped dataset.

**Important notes:**

- Approximately 30 days of logs from the Beta period (back to \~February 8, 2026) are available at GA. These Beta logs will expire on \~April 9, 2026. Logs generated after GA will be retained for the full 18 months. Older logs remain available in Audit Logs v1.
- The UI query window is limited to 90 days for performance reasons. Use the API or Logpush for access to the full 18-month history.
- `GET` requests (view actions) and `4xx` error responses are not logged at GA. `GET` logging will be selectively re-enabled for sensitive read operations in a future release.
- Audit Logs v1 continues to run in parallel. A deprecation timeline will be communicated separately.
- Before and after values — the ability to see what a value changed from and to — is a highly requested feature and is on our roadmap for a post-GA release. In the meantime, we recommend using Audit Logs v1 for before and after values. Audit Logs v1 will continue to run in parallel until this feature is available in v2.

For more details, refer to the [Audit Logs v2 documentation](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-10-audit-logs-v2-ga/#page","headline":"Audit logs (version 2) - General Availability","description":"Audit Logs v2 is now generally available","url":"https://developers.cloudflare.com/changelog/post/2026-03-10-audit-logs-v2-ga/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-10-audit-logs-v2-ga/og.png?v=662024018ffe863d","dateModified":"2026-03-10","datePublished":"2026-03-10","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
