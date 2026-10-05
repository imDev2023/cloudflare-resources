---
description: Super Administrators can now invite account members and grant scoped access to an individual Worker directly from the Workers dashboard.
title: Give teammates access to specific Workers directly from the dashboard
image: https://developers.cloudflare.com/changelog/post/2026-09-21-invite-members-to-workers/og.png?v=cbfa731907d02370
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 21, 2026

## Give teammates access to specific Workers directly from the dashboard

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-21-invite-members-to-workers/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now grant teammates scoped access to specific Workers directly from the Workers dashboard.

Go to your Worker and click **Invite**.

![Invite button on a Worker's overview page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2366,height=1134,format=webp/_astro/invite-button.BtZmWRrA.png)

Enter the teammate's email address, choose the appropriate access level, and click **Invite**.

![Dialog for inviting a teammate and choosing their access level](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=748,height=724,format=webp/_astro/invite-dialog.Bo5P-iat.png)

You can grant a user one of the following access levels:

- **Metadata Read-Only**: View settings, metrics, logs, and traces without access to Worker code or the ability to make changes.
- **Content Read-Only**: Read Worker code, settings, and observability data without the ability to modify or deploy changes.
- **Editor**: Update and deploy a Worker without the ability to delete it.
- **Admin**: Everything included with Editor, plus the ability to delete the Worker.

If the teammate is already an account member, they will receive access to the Worker immediately. If they are not an account member, Cloudflare will send them an invitation to join the account, and they will receive access to the Worker after accepting the invitation.

Only account members with the Super Administrator role can invite users from a Worker's dashboard.

For details about available roles and scopes, refer to the [Workers roles and permissions documentation](https://developers.cloudflare.com/workers/authorization/workers/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-21-invite-members-to-workers/#page","headline":"Give teammates access to specific Workers directly from the dashboard","description":"Super Administrators can now invite account members and grant scoped access to an individual Worker directly from the Workers dashboard.","url":"https://developers.cloudflare.com/changelog/post/2026-09-21-invite-members-to-workers/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-21-invite-members-to-workers/og.png?v=cbfa731907d02370","dateModified":"2026-09-21","datePublished":"2026-09-21","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
