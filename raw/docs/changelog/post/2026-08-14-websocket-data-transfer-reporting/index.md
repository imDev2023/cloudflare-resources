---
description: HTTP Traffic Analytics and HTTP request logs now report data transfer and duration for the full WebSocket connection, not only the initial handshake.
title: WebSocket reporting now includes full connection data transfer and duration
image: https://developers.cloudflare.com/changelog/post/2026-08-14-websocket-data-transfer-reporting/og.png?v=812eaee4bba0a99b
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 14, 2026

## WebSocket reporting now includes full connection data transfer and duration

[Analytics](https://developers.cloudflare.com/analytics/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-14-websocket-data-transfer-reporting/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Cloudflare has fixed an issue affecting WebSocket data transfer and session duration reporting. HTTP Traffic Analytics and HTTP request logs now correctly report data transferred throughout a WebSocket connection and the duration of the full session. During the affected period, reporting captured only the bytes and duration of the initial `101 Switching Protocols` handshake for some WebSocket connections.

Customers with WebSocket traffic will see the correct **Data Transfer** in the dashboard and `EdgeResponseBytes` in analytics and HTTP request logs. Reported session duration now reflects the full WebSocket session rather than only the handshake. These changes restore the accounting of existing WebSocket traffic and duration. They do not indicate an increase in traffic or alter WebSocket connection behavior.

The separate [WebSocket Analytics Logpush dataset](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/websocket_analytics/) continues to provide per-connection directional byte counts, timestamps, and close details.

For more information about HTTP Traffic Analytics, refer to [Zone Analytics](https://developers.cloudflare.com/analytics/account-and-zone-analytics/zone-analytics/#http-traffic).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-14-websocket-data-transfer-reporting/#page","headline":"WebSocket reporting now includes full connection data transfer and duration","description":"HTTP Traffic Analytics and HTTP request logs now report data transfer and duration for the full WebSocket connection, not only the initial handshake.","url":"https://developers.cloudflare.com/changelog/post/2026-08-14-websocket-data-transfer-reporting/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-14-websocket-data-transfer-reporting/og.png?v=812eaee4bba0a99b","dateModified":"2026-08-14","datePublished":"2026-08-14","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
