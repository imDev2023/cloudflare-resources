---
description: Cloudy summaries for Access and Gateway Logs
title: Cloudy summaries for Access and Gateway Logs
image: https://developers.cloudflare.com/changelog/post/2025-07-07-cloudy-summaries-access-gateway/og.png?v=d8633e3ce11379bb
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 7, 2025

## Cloudy summaries for Access and Gateway Logs

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-07-07-cloudy-summaries-access-gateway/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudy, Cloudflare's AI Agent, will now automatically summarize your [Access](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/access-authentication-logs/) and [Gateway](https://developers.cloudflare.com/cloudflare-one/insights/logs/dashboard-logs/gateway-logs/) block logs.

In the log itself, Cloudy will summarize what occurred and why. This will be helpful for quick troubleshooting and issue correlation.

![Cloudy AI summarizes a log](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=512,height=472,format=webp/_astro/cloudy-explanation.oFZR6cXa.png)

If you have feedback about the Cloudy summary - good or bad - you can provide that right from the summary itself.

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-07-07-cloudy-summaries-access-gateway/#page","headline":"Cloudy summaries for Access and Gateway Logs","description":"Cloudy summaries for Access and Gateway Logs","url":"https://developers.cloudflare.com/changelog/post/2025-07-07-cloudy-summaries-access-gateway/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-07-07-cloudy-summaries-access-gateway/og.png?v=d8633e3ce11379bb","dateModified":"2025-07-07","datePublished":"2025-07-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
