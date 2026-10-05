---
description: The tunnel overview page in Cloudflare One now displays all replicas and supports streaming logs from multiple replicas at the same time.
title: Stream logs from multiple replicas of Cloudflare Tunnel simultaneously
image: https://developers.cloudflare.com/changelog/post/2026-03-20-tunnel-replica-overview-and-multi-log-streaming/og.png?v=91b2f70f25ce044c
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

March 20, 2026

## Stream logs from multiple replicas of Cloudflare Tunnel simultaneously

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-03-20-tunnel-replica-overview-and-multi-log-streaming/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

In the Cloudflare One dashboard, the overview page for a specific Cloudflare Tunnel now shows all [replicas](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/) of that tunnel and supports streaming logs from multiple replicas at once.

![View replicas and stream logs from multiple connectors](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=1040,format=webp/_astro/tunnel-multiconn.DEOEaLlu.gif)

Previously, you could only stream logs from one replica at a time. With this update:

- **Replicas on the tunnel overview** — All active replicas for the selected tunnel now appear on that tunnel's overview page under **Connectors**. Select any replica to stream its logs.
- **Multi-connector log streaming** — Stream logs from multiple replicas simultaneously, making it easier to correlate events across your infrastructure during debugging or incident response. To try it out, log in to [Cloudflare One ↗︎](https://one.dash.cloudflare.com/) and go to **Networks** > **Connectors** > **Cloudflare Tunnels**. Select **View logs** next to the tunnel you want to monitor.

For more information, refer to [Tunnel log streams](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/) and [Deploy replicas](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/configure-tunnels/tunnel-availability/deploy-replicas/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-03-20-tunnel-replica-overview-and-multi-log-streaming/#page","headline":"Stream logs from multiple replicas of Cloudflare Tunnel simultaneously","description":"The tunnel overview page in Cloudflare One now displays all replicas and supports streaming logs from multiple replicas at the same time.","url":"https://developers.cloudflare.com/changelog/post/2026-03-20-tunnel-replica-overview-and-multi-log-streaming/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-03-20-tunnel-replica-overview-and-multi-log-streaming/og.png?v=91b2f70f25ce044c","dateModified":"2026-03-20","datePublished":"2026-03-20","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
