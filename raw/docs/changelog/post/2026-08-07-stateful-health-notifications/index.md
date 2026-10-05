---
description: Health notifications carry alert state, so the notification sent when a pool or endpoint recovers automatically resolves the incident opened by the earlier unhealthy notification.
title: Load Balancing health notifications now resolve automatically
image: https://developers.cloudflare.com/changelog/post/2026-08-07-stateful-health-notifications/og.png?v=5c4eff21640371da
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 7, 2026

## Load Balancing health notifications now resolve automatically

[Load Balancing](https://developers.cloudflare.com/load-balancing/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-07-stateful-health-notifications/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Load Balancing](https://developers.cloudflare.com/load-balancing/) health notifications are now stateful. When a pool or endpoint becomes unhealthy, the notification opens an incident in your alerting tool as before. When that same pool or endpoint recovers, the follow-up notification is matched to the original alert and resolves that incident automatically, so you no longer have to close it by hand.

As part of this change, Load Balancing also sends a notification when a pool or endpoint returns to a healthy state, not only when it becomes unhealthy. Expect to see recovery notifications alongside the failure notifications you already receive.

This applies to your existing Load Balancing health alerts with no configuration change, and it matches the behavior already used by [Health Checks](https://developers.cloudflare.com/health-checks/) notifications.

Two things to keep in mind:

- A recovery notification is matched to the earlier unhealthy notification for the **same pool or endpoint**. Renaming an endpoint while an incident is open prevents the match, so that incident stays open until you close it.
- If a health change cannot be classified as either healthy or unhealthy, the notification is still delivered, but without the state needed to open or resolve an incident.

Refer to [Integrate with PagerDuty](https://developers.cloudflare.com/load-balancing/additional-options/pagerduty-integration/) to learn more about routing Load Balancing health notifications to an incident management tool.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-07-stateful-health-notifications/#page","headline":"Load Balancing health notifications now resolve automatically","description":"Health notifications carry alert state, so the notification sent when a pool or endpoint recovers automatically resolves the incident opened by the earlier unhealthy notification.","url":"https://developers.cloudflare.com/changelog/post/2026-08-07-stateful-health-notifications/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-07-stateful-health-notifications/og.png?v=5c4eff21640371da","dateModified":"2026-08-07","datePublished":"2026-08-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
