---
description: R2 Dashboard experience gets new updates
title: R2 Dashboard experience gets new updates
image: https://developers.cloudflare.com/changelog/post/2025-05-01-r2-dashboard-updates/og.png?v=0a00cf0183b3216b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

May 1, 2025

## R2 Dashboard experience gets new updates

[R2](https://developers.cloudflare.com/r2/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-05-01-r2-dashboard-updates/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

We're excited to announce several improvements to the [Cloudflare R2](https://developers.cloudflare.com/r2/) dashboard experience that make managing your object storage easier and more intuitive:

![Cloudflare R2 Dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2286,height=1600,format=webp/_astro/r2-dashboard-updates.B7WXxzMk.png)

#### All-new settings page

We've redesigned the bucket settings page, giving you a centralized location to manage all your bucket configurations in one place.

#### Improved navigation and sharing

- Deeplink support for prefix directories: Navigate through your bucket hierarchy without losing your state. Your browser's back button now works as expected, and you can share direct links to specific prefix directories with teammates.
- Objects as clickable links: Objects are now proper links that you can copy or `CMD + Click` to open in a new tab.

#### Clearer public access controls

- Renamed "r2.dev domain" to "Public Development URL" for better clarity when exposing bucket contents for non-production workloads.
- Public Access status now clearly displays "Enabled" when your bucket is exposed to the internet (via Public Development URL or Custom Domains).

We've also made numerous other usability improvements across the board to make your R2 experience smoother and more productive.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-05-01-r2-dashboard-updates/#page","headline":"R2 Dashboard experience gets new updates","description":"R2 Dashboard experience gets new updates","url":"https://developers.cloudflare.com/changelog/post/2025-05-01-r2-dashboard-updates/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-05-01-r2-dashboard-updates/og.png?v=0a00cf0183b3216b","dateModified":"2025-05-01","datePublished":"2025-05-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
