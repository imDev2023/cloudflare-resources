---
description: Expanded Certificate Transparency (CT) log insights in Cloudflare Radar, including inclusion activity and growth rate
title: Expanded CT log activity insights on Cloudflare Radar
image: https://developers.cloudflare.com/changelog/post/2025-10-09-radar-ct-log-activity-insights/og.png?v=e1e854f916618aae
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

October 9, 2025

## Expanded CT log activity insights on Cloudflare Radar

[Radar](https://developers.cloudflare.com/radar/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-10-09-radar-ct-log-activity-insights/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

[**Radar**](https://developers.cloudflare.com/radar/) has expanded its Certificate Transparency (CT) log insights with new stats that provide greater visibility into log activity:

- **Log growth rate**: The average throughput of the CT log over the past 7 days, measured in certificates per hour.
- **Included certificate count**: The total number of certificates already included in this CT log.
- **Eligible-for-inclusion certificate count**: The number of certificates eligible for inclusion in this log but not yet included. This metric is based on certificates signed by trusted root CAs within the log’s accepted date range.
- **Last update**: The timestamp of the most recent update to the CT log.

These new statistics have been added to the response of the [Get Certificate Log Details](https://developers.cloudflare.com/api/resources/radar/subresources/ct/subresources/logs/methods/get/) API endpoint, and are displayed on the [CT log information page ↗︎](https://radar.cloudflare.com/certificate-transparency/log/nimbus2025#log-activity).

![Screenshot of the CT log activity card on the CT log information page](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1598,height=441,format=webp/_astro/ct-log-activity.GHD-K7Mk.png)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-10-09-radar-ct-log-activity-insights/#page","headline":"Expanded CT log activity insights on Cloudflare Radar","description":"Expanded Certificate Transparency (CT) log insights in Cloudflare Radar, including inclusion activity and growth rate","url":"https://developers.cloudflare.com/changelog/post/2025-10-09-radar-ct-log-activity-insights/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-10-09-radar-ct-log-activity-insights/og.png?v=e1e854f916618aae","dateModified":"2025-10-09","datePublished":"2025-10-09","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
