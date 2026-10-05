---
description: NetFlow export from Magic WAN Connector for breakout traffic monitoring
title: Breakout traffic visibility via NetFlow
image: https://developers.cloudflare.com/changelog/post/2025-12-31-connector-breakout-traffic-netflow/og.png?v=38ef44dc87409ba5
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

December 31, 2025

## Breakout traffic visibility via NetFlow

[Cloudflare One Appliance](https://developers.cloudflare.com/cloudflare-wan/configuration/appliance/) [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) [Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2025-12-31-connector-breakout-traffic-netflow/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Magic WAN Connector now exports NetFlow data for breakout traffic to Magic Network Monitoring (MNM), providing visibility into traffic that bypasses Cloudflare's security filtering.

This feature allows you to:

- Monitor breakout traffic statistics in the Cloudflare dashboard.
- View traffic patterns for applications configured to bypass Cloudflare.
- Maintain visibility across all traffic passing through your Magic WAN Connector.

For more information, refer to [NetFlow statistics](https://developers.cloudflare.com/cloudflare-wan/analytics/netflow-analytics/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2025-12-31-connector-breakout-traffic-netflow/#page","headline":"Breakout traffic visibility via NetFlow","description":"NetFlow export from Magic WAN Connector for breakout traffic monitoring","url":"https://developers.cloudflare.com/changelog/post/2025-12-31-connector-breakout-traffic-netflow/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2025-12-31-connector-breakout-traffic-netflow/og.png?v=38ef44dc87409ba5","dateModified":"2025-12-31","datePublished":"2025-12-31","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
