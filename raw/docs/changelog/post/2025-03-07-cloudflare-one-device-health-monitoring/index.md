---
description: Monitor device health metrics directly from the Cloudflare One agent
title: Cloudflare One Agent now supports Endpoint Monitoring
image: https://developers.cloudflare.com/changelog/post/2025-03-07-cloudflare-one-device-health-monitoring/og.png?v=bd2f0fe454370c53
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 7, 2025

## Cloudflare One Agent now supports Endpoint Monitoring

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-03-07-cloudflare-one-device-health-monitoring/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Digital Experience Monitoring (DEX)](https://developers.cloudflare.com/cloudflare-one/insights/dex/) provides visibility into device, network, and application performance across your Cloudflare SASE deployment. The latest release of the Cloudflare One agent (v2025.1.861) now includes device endpoint monitoring capabilities to provide deeper visibility into end-user device performance which can be analyzed directly from the dashboard.

Device health metrics are now automatically collected, allowing administrators to:

- View the last network a user was connected to
- Monitor CPU and RAM utilization on devices
- Identify resource-intensive processes running on endpoints

![Device endpoint monitoring dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1226,height=675,format=webp/_astro/cloudflare-one-agent-health-monitoring.XXtiRuOp.gif)

This feature complements existing DEX features like [synthetic application monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/) and [network path visualization](https://developers.cloudflare.com/cloudflare-one/insights/dex/tests/traceroute/), creating a comprehensive troubleshooting workflow that connects application performance with device state.

For more details refer to our [DEX](https://developers.cloudflare.com/cloudflare-one/insights/dex/) documentation.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-03-07-cloudflare-one-device-health-monitoring/#page","headline":"Cloudflare One Agent now supports Endpoint Monitoring","description":"Monitor device health metrics directly from the Cloudflare One agent","url":"https://developers.cloudflare.com/changelog/post/2025-03-07-cloudflare-one-device-health-monitoring/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-03-07-cloudflare-one-device-health-monitoring/og.png?v=bd2f0fe454370c53","dateModified":"2025-03-07","datePublished":"2025-03-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
