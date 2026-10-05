---
description: Exclude identified DDoS attack traffic from supported Logpush datasets before delivery.
title: Filter DDoS attack traffic from Logpush jobs
image: https://developers.cloudflare.com/changelog/post/2026-09-18-filter-ddos-attack-traffic/og.png?v=6d0c1122a2eeef3e
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 18, 2026

## Filter DDoS attack traffic from Logpush jobs

[Logpush](https://developers.cloudflare.com/logs/logpush/) [Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-09-18-filter-ddos-attack-traffic/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Logpush jobs can now exclude identified distributed denial-of-service (DDoS) attack traffic. This option reduces attack traffic in delivered logs.

It supports the `http_requests`, `firewall_events`, and `network_analytics_logs` datasets.

In the dashboard, select **Exclude DDoS attack traffic** under **Advanced Options**. With the API, add this field to a job request:

```json
{
	"filter_attack_traffic": true
}
```

For more information, refer to [API configuration](https://developers.cloudflare.com/logs/logpush/logpush-job/api-configuration/#ddos-attack-traffic).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-09-18-filter-ddos-attack-traffic/#page","headline":"Filter DDoS attack traffic from Logpush jobs","description":"Exclude identified DDoS attack traffic from supported Logpush datasets before delivery.","url":"https://developers.cloudflare.com/changelog/post/2026-09-18-filter-ddos-attack-traffic/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-09-18-filter-ddos-attack-traffic/og.png?v=6d0c1122a2eeef3e","dateModified":"2026-09-18","datePublished":"2026-09-18","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
