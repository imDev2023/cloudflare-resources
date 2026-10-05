---
description: Organization Super Administrators can now view organization-level audit logs directly in the Cloudflare dashboard.
title: Audit Logs v2 — Organization-level audit logs in Cloudflare dashboard
image: https://developers.cloudflare.com/changelog/post/2026-06-24-audit-logs-v2-organization-dashboard-ui/og.png?v=5d035e466c04902e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 24, 2026

## Audit Logs v2 — Organization-level audit logs in Cloudflare dashboard

[Audit Logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-06-24-audit-logs-v2-organization-dashboard-ui/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now, as an [Organization](https://developers.cloudflare.com/fundamentals/organizations/) Super Administrator, view organization-level [audit logs](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/) in the Cloudflare dashboard, in addition to the existing [API access](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/#organization-activity-logs).

Organization audit logs help you monitor activity across your organization. You can see who performed an action, what changed, when it happened, how it was performed, and whether it succeeded or failed.

You can filter and search logs by actor, action, result, resource, request details, and timestamp. Use these logs to troubleshoot changes, investigate unexpected access, and support security or compliance workflows.

![Organization audit logs in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3450,height=1738,format=webp/_astro/Audit_logs_v2_organization_dashboard.De-uwPva.png)

If you are viewing account-level audit logs and the account belongs to an organization where you are an Organization Super Administrator, select **View Organization Audit Logs** to open the parent organization's audit logs.

![View Organization Audit Logs button](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=3456,height=510,format=webp/_astro/Audit_logs_v2_view_organization_button.Ch7CaBB-.png)

To get started, go to **Organizations**, select your organization, then go to **Manage Organization** > **Audit Logs**.

For more information, refer to the [Audit Logs documentation](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-06-24-audit-logs-v2-organization-dashboard-ui/#page","headline":"Audit Logs v2 — Organization-level audit logs in Cloudflare dashboard","description":"Organization Super Administrators can now view organization-level audit logs directly in the Cloudflare dashboard.","url":"https://developers.cloudflare.com/changelog/post/2026-06-24-audit-logs-v2-organization-dashboard-ui/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-06-24-audit-logs-v2-organization-dashboard-ui/og.png?v=5d035e466c04902e","dateModified":"2026-06-24","datePublished":"2026-06-24","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
