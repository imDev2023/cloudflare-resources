---
description: You can now grant members of your Cloudflare account read-only access to the Workers Platform.
title: Grant account members read-only access to the Workers Platform
image: https://developers.cloudflare.com/changelog/post/2025-06-16-workers-platform-admin-role/og.png?v=5449282a543b2c0e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

June 16, 2025

## Grant account members read-only access to the Workers Platform

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-06-16-workers-platform-admin-role/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now grant members of your Cloudflare account read-only access to the Workers Platform.

The new "Workers Platform (Read-only)" role grants read-only access to all products typically used as part of Cloudflare's Developer Platform, including [Workers](https://developers.cloudflare.com/workers/), [Pages](https://developers.cloudflare.com/pages/), [Durable Objects](https://developers.cloudflare.com/durable-objects/), [KV](https://developers.cloudflare.com/kv/), [R2](https://developers.cloudflare.com/r2/), Zones, [Zone Analytics](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/) and [Page Rules](https://developers.cloudflare.com/rules/). When Cloudflare introduces new products to the Workers platform, we will add additional read-only permissions to this role.

Additionally, the role previously named "Workers Admin" has been renamed to "Workers Platform Admin". This change ensures that the name more accurately reflects the permissions granted — this role has always granted access to more than just Workers — it grants read and write access to the products mentioned above, and similarly, as new products are added to the Workers platform, we will add additional read and write permissions to this role.

You can review the updated roles in the [developer docs](https://developers.cloudflare.com/fundamentals/manage-members/roles/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-06-16-workers-platform-admin-role/#page","headline":"Grant account members read-only access to the Workers Platform","description":"You can now grant members of your Cloudflare account read-only access to the Workers Platform.","url":"https://developers.cloudflare.com/changelog/post/2025-06-16-workers-platform-admin-role/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-06-16-workers-platform-admin-role/og.png?v=5449282a543b2c0e","dateModified":"2025-06-16","datePublished":"2025-06-16","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
