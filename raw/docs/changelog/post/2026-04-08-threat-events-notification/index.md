---
description: You can now subscribe to automated notifications for your saved views in Threat Events
title: Real-time alerts and daily digests for Threat Events
image: https://developers.cloudflare.com/changelog/post/2026-04-08-threat-events-notification/og.png?v=f866398ebda20eb0
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 8, 2026

## Real-time alerts and daily digests for Threat Events

[Security Center](https://developers.cloudflare.com/security-center/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-08-threat-events-notification/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

You can now automate your threat monitoring by setting up custom alerts in your saved views. Instead of manually checking the dashboard for updates, you can subscribe to notifications that trigger whenever new data matches your specific filter sets, like new activity associated to a particular threat actor or spikes in activity within your industry.

#### Stay ahead of emerging threats

By linking your saved views to the Cloudflare Notifications Center, you can ensure the right information reaches your team at the right time.

- **Immediate Alerts**: receive real-time notifications the moment a critical event is detected that matches your saved criteria. This is essential for high-priority monitoring, such as tracking active campaigns from specific APT groups.
- **Daily Digests**: opt for a summarized report delivered once a day. This is ideal for maintaining situational awareness of broader trends, like regional activity shifts or industry-wide threat landscapes, without cluttering your inbox.

![Threat Events notifications](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2630,height=1424,format=webp/_astro/threat-events-notifications.3Fl8LGOn.png)

#### How to get started

To set up an alert, go to **Application Security** > **Threat Intelligence** > **Threat Events**. From there:

1. Choose your datasets and apply your desired filters and select **Save View** (or select an existing one).
2. Open the **Manage Saved Views** menu.
3. Select **Add Alert** next to your chosen view to configure your notification preferences in the Cloudflare dashboard.

For more technical details on configuring notifications, refer to the [Threat Events documentation](https://developers.cloudflare.com/security-center/cloudforce-one/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-08-threat-events-notification/#page","headline":"Real-time alerts and daily digests for Threat Events","description":"You can now subscribe to automated notifications for your saved views in Threat Events","url":"https://developers.cloudflare.com/changelog/post/2026-04-08-threat-events-notification/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-08-threat-events-notification/og.png?v=f866398ebda20eb0","dateModified":"2026-04-08","datePublished":"2026-04-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
