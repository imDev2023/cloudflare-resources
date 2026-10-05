---
description: "Use new observability on Stream Live Inputs to better understand broadcast-side health and performance, now easily available in Dash and programmatically via GraphQL.\n"
title: Introducing observability and metrics for Stream Live Inputs
image: https://developers.cloudflare.com/changelog/post/2025-08-08-stream-live-observability/og.png?v=36bb6daebe840742
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 8, 2025

## Introducing observability and metrics for Stream Live Inputs

[Stream](https://developers.cloudflare.com/stream/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-08-08-stream-live-observability/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

New information about broadcast metrics and events is now available in [Cloudflare Stream](https://developers.cloudflare.com/stream/) in the Live Input details of the Dashboard.

![Live Input details showing metrics](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1382,height=907,format=webp/_astro/2025-08-05-live-input-metrics.B31Z3RGB.png)

You can now easily understand broadcast-side health and performance with new observability, which can help when troubleshooting common issues, particularly for new customers who are just getting started, and platform customers who may have limited visibility into how their end-users configure their encoders.

To get started, start a live stream ([just getting started?](https://developers.cloudflare.com/stream/examples/obs-from-scratch/)), then visit the Live Input details page in Dash.

See our new live [Troubleshooting](https://developers.cloudflare.com/stream/stream-live/troubleshooting/) guide to learn what these metrics mean and how to use them to address common broadcast issues.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-08-08-stream-live-observability/#page","headline":"Introducing observability and metrics for Stream Live Inputs","description":"Use new observability on Stream Live Inputs to better understand broadcast-side health and performance, now easily available in Dash and programmatically via GraphQL.","url":"https://developers.cloudflare.com/changelog/post/2025-08-08-stream-live-observability/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-08-08-stream-live-observability/og.png?v=36bb6daebe840742","dateModified":"2025-08-08","datePublished":"2025-08-08","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
