---
description: New version of audit logs
title: Audit logs (version 2) - Beta Release
image: https://developers.cloudflare.com/changelog/post/2025-03-27-automatic-audit-logs-beta-release/og.png?v=845c2fb1749c694b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 27, 2025

## Audit logs (version 2) - Beta Release

[Audit Logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-27-automatic-audit-logs-beta-release/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The latest version of audit logs streamlines audit logging by automatically capturing all user and system actions performed through the Cloudflare Dashboard or public APIs. This update leverages Cloudflare’s existing API Shield to generate audit logs based on OpenAPI schemas, ensuring a more consistent and automated logging process.

Availability: Audit logs (version 2) is now in Beta, with support limited to **API access**.

Use the following API endpoint to retrieve audit logs:

```js
GET https://api.cloudflare.com/client/v4/accounts/<account_id>/logs/audit?since=<date>&before=<date>
```

You can access detailed documentation for audit logs (version 2) Beta API release [here ↗︎](https://developers.cloudflare.com/api/resources/accounts/subresources/logs/subresources/audit/methods/list/).

**Key Improvements in the Beta Release:**

- **Automated & standardized logging**: Logs are now generated automatically using a standardized system, replacing manual, team-dependent logging. This ensures consistency across all Cloudflare services.
- **Expanded product coverage**: Increased audit log coverage from 75% to 95%. Key API endpoints such as `/accounts`, `/zones`, and `/organizations` are now included.
- **Granular filtering**: Logs now follow a uniform format, enabling precise filtering by actions, users, methods, and resources—allowing for faster and more efficient investigations.
- **Enhanced context and traceability**: Each log entry now includes detailed context, such as the authentication method used, the interface (API or Dashboard) through which the action was performed, and mappings to Cloudflare Ray IDs for better traceability.
- **Comprehensive activity capture**: Expanded logging to include GET requests and failed attempts, ensuring that all critical activities are recorded.

**Known Limitations in Beta**

- Error handling for the API is not implemented.
- There may be gaps or missing entries in the available audit logs.
- UI is unavailable in this Beta release.
- System-level logs and User-Activity logs are not included.

Support for these features is coming as part of the GA release later this year. For more details, including a sample audit log, check out our blog post: [Introducing Automatic Audit Logs ↗︎](https://blog.cloudflare.com/introducing-automatic-audit-logs/)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-27-automatic-audit-logs-beta-release/#page","headline":"Audit logs (version 2) - Beta Release","description":"New version of audit logs","url":"https://developers.cloudflare.com/changelog/post/2025-03-27-automatic-audit-logs-beta-release/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-03-27-automatic-audit-logs-beta-release/og.png?v=845c2fb1749c694b","dateModified":"2025-03-27","datePublished":"2025-03-27","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
