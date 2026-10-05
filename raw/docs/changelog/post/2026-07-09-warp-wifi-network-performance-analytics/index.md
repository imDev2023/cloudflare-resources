---
description: Diagnose Cloudflare One Client device connectivity with Wi-Fi signal, traffic, and device health metrics
title: Wi-Fi signal and network performance analytics for Cloudflare One Client devices
image: https://developers.cloudflare.com/changelog/post/2026-07-09-warp-wifi-network-performance-analytics/og.png?v=6b80324effdde39b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 9, 2026

## Wi-Fi signal and network performance analytics for Cloudflare One Client devices

[Digital Experience Monitoring](https://developers.cloudflare.com/cloudflare-one/insights/dex/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-09-warp-wifi-network-performance-analytics/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[Digital Experience Monitoring (DEX)](https://developers.cloudflare.com/cloudflare-one/insights/dex/) provides visibility into device, network, and application performance across your Cloudflare SASE deployment.

The **Device Monitoring** page now analyzes hardware and network data between a Cloudflare One Client device and Cloudflare's edge, so you can diagnose connectivity and performance issues. Previously, this data was only available in raw DEX Device State Event logs, which required you to build your own analytics to interpret it.

![Device Monitoring summary with connection status, connection mode, Wi-Fi signal strength, traffic performance, and device health](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1652,height=664,format=webp/_astro/dex-device-monitoring-summary.CBxeSd6b.png)

A summary at the top of the page shows the health of each category at a glance, using **Good**, **Fair**, and **Poor** labels:

- **Connection** — connection status, Cloudflare One Client mode, and tunnel type over time
- **Wi-Fi signal strength** — signal measured in dBm over time, with thresholds that flag a weak signal
- **Traffic performance** — upstream and downstream performance, including network throughput on the active interface
- **Device health** — hardware metrics such as CPU, memory, and disk

![Wi-Fi signal strength and network throughput charts on the Device Monitoring page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1666,height=732,format=webp/_astro/dex-device-monitoring-wifi-network.CoEBznAm.png)

You can filter by category and adjust the time range to correlate a device's metrics with a user's reported issue.

These analytics are available to all Cloudflare One customers at no additional cost.

To learn more, refer to the [DEX monitoring documentation](https://developers.cloudflare.com/cloudflare-one/insights/dex/monitoring/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-09-warp-wifi-network-performance-analytics/#page","headline":"Wi-Fi signal and network performance analytics for Cloudflare One Client devices","description":"Diagnose Cloudflare One Client device connectivity with Wi-Fi signal, traffic, and device health metrics","url":"https://developers.cloudflare.com/changelog/post/2026-07-09-warp-wifi-network-performance-analytics/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-09-warp-wifi-network-performance-analytics/og.png?v=6b80324effdde39b","dateModified":"2026-07-09","datePublished":"2026-07-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
