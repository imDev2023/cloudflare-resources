---
description: All users can now create and manage scheduled DNS policies directly from the Cloudflare One dashboard.
title: Schedule DNS policies from the UI
image: https://developers.cloudflare.com/changelog/post/2025-10-20-schedule-dns-policies-from-the-ui/og.png?v=fcc6956d2c3378be
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 20, 2025

## Schedule DNS policies from the UI

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-policies/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-20-schedule-dns-policies-from-the-ui/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Admins can now create [scheduled DNS policies](https://developers.cloudflare.com/cloudflare-one/traffic-policies/dns-policies/timed-policies/) directly from the Zero Trust dashboard, without using the API. You can configure policies to be active during specific, recurring times, such as blocking social media during business hours or gaming sites on school nights.

- **Preset Schedules**: Use built-in templates for common scenarios like Business Hours, School Days, Weekends, and more.
- **Custom Schedules**: Define your own schedule with specific days and up to three non-overlapping time ranges per day.
- **Timezone Control**: Choose to enforce a schedule in a specific timezone (for example, US Eastern) or based on the local time of each user.
- **Combined with Duration**: Policies can have both a schedule and a duration. If both are set, the duration's expiration takes precedence.

You can see the flow in the demo GIF:

![Schedule DNS policies demo](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1053,height=879,format=webp/_astro/gateway-dns-scheduled-policies-ui.Cf4l1OTE.gif)

This update makes time-based DNS policies accessible to all Gateway customers, removing the technical barrier of the API.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-20-schedule-dns-policies-from-the-ui/#page","headline":"Schedule DNS policies from the UI","description":"All users can now create and manage scheduled DNS policies directly from the Cloudflare One dashboard.","url":"https://developers.cloudflare.com/changelog/post/2025-10-20-schedule-dns-policies-from-the-ui/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-20-schedule-dns-policies-from-the-ui/og.png?v=fcc6956d2c3378be","dateModified":"2025-10-20","datePublished":"2025-10-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
