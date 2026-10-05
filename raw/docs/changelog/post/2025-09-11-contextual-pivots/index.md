---
description: Log Search now lets you pivot directly to related Cloudflare tools and documentation for faster investigations and actions.
title: Contextual pivots
image: https://developers.cloudflare.com/changelog/post/2025-09-11-contextual-pivots/og.png?v=41c7b6ddddf40860
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

September 11, 2025

## Contextual pivots

[Log Explorer](https://developers.cloudflare.com/log-explorer/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-09-11-contextual-pivots/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Directly from [Log Search](https://developers.cloudflare.com/log-explorer/log-search/) results, customers can pivot to other parts of the Cloudflare dashboard to immediately take action as a result of their investigation.

From the `http_requests` or `fw_events` dataset results, right click on an IP Address or JA3 Fingerprint to pivot to the Investigate portal to lookup the reputation of an IP address or JA3 fingerprint.

![Investigate IP address](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1038,height=486,format=webp/_astro/investigate-ip-address.BMVSMzDi.png)

Easily learn about error codes by linking directly to our documentation from the **EdgeResponseStatus** or **OriginResponseStatus** fields.

![View documentation](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1186,height=476,format=webp/_astro/view-documentation.Cem5QgeO.png)

From the `gateway_http` dataset, click on a **policyid** to link directly to the Zero Trust dashboard to review or make changes to a specific Gateway policy.

![View policy](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1274,height=498,format=webp/_astro/policyid.CVjEdahj.png)

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-09-11-contextual-pivots/#page","headline":"Contextual pivots","description":"Log Search now lets you pivot directly to related Cloudflare tools and documentation for faster investigations and actions.","url":"https://developers.cloudflare.com/changelog/post/2025-09-11-contextual-pivots/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-09-11-contextual-pivots/og.png?v=41c7b6ddddf40860","dateModified":"2025-09-11","datePublished":"2025-09-11","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
