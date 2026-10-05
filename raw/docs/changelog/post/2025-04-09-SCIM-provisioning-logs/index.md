---
description: View all user and group updates, creation and deletion events made via SCIM across all of your IdP instances in one place
title: Cloudflare Zero Trust SCIM User and Group Provisioning Logs
image: https://developers.cloudflare.com/changelog/post/2025-04-09-SCIM-provisioning-logs/og.png?v=40922867278b429b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 9, 2025

## Cloudflare Zero Trust SCIM User and Group Provisioning Logs

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-04-09-SCIM-provisioning-logs/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Cloudflare Zero Trust SCIM provisioning](https://developers.cloudflare.com/cloudflare-one/team-and-resources/users/scim) now has a full audit log of all create, update and delete event from any SCIM Enabled IdP. The [SCIM logs](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/scim-logs/) support filtering by IdP, Event type, Result and many more fields. This will help with debugging user and group update issues and questions.

SCIM logs can be found on the Zero Trust Dashboard under **Logs** -> **SCIM provisioning**.

![Example SCIM Logs](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2318,height=1060,format=webp/_astro/example-scim-log.Bv5Zqckh.png)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-04-09-SCIM-provisioning-logs/#page","headline":"Cloudflare Zero Trust SCIM User and Group Provisioning Logs","description":"View all user and group updates, creation and deletion events made via SCIM across all of your IdP instances in one place","url":"https://developers.cloudflare.com/changelog/post/2025-04-09-SCIM-provisioning-logs/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-04-09-SCIM-provisioning-logs/og.png?v=40922867278b429b","dateModified":"2025-04-09","datePublished":"2025-04-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
