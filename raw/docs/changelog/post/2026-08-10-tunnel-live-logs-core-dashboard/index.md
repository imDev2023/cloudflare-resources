---
description: The Tunnel detail view in the Cloudflare dashboard now supports real-time log streaming, including multi-connector aggregated streaming with filtering.
title: Stream live logs from Cloudflare Tunnel in the dashboard
image: https://developers.cloudflare.com/changelog/post/2026-08-10-tunnel-live-logs-core-dashboard/og.png?v=5d2114f6ea4b37d4
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

August 10, 2026

## Stream live logs from Cloudflare Tunnel in the dashboard

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) [Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-08-10-tunnel-live-logs-core-dashboard/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Real-time Tunnel log streaming is now available in the Cloudflare dashboard under **Networking** > **Tunnels**. This brings the same live debugging capability previously only available in the Cloudflare One dashboard, including multi-connector aggregated streaming for high-availability deployments.

![Stream live logs from a tunnel in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1800,height=948,format=webp/_astro/tunnel-live-logs-core-dashboard.Dtm7Jg51.gif)

In the tunnel detail view, a new **Live logs** tab lets you:

- **Stream logs from single or multiple connectors** — In [highly available](https://developers.cloudflare.com/tunnel/configuration/#replicas-and-high-availability) deployments with multiple `cloudflared` replicas, logs from all connectors are merged into a single stream grouped by hostname, making it easy to identify which host machine produced each log entry.
- **Filter by log level, event type, and HTTP method** — Narrow the stream to only the events you care about (HTTP, TCP, UDP, or `cloudflared` internal), at any log level.

[Go to **Tunnels** ↗](https://dash.cloudflare.com/?to=/:account/tunnels)

For more information, refer to [Tunnel observability](https://developers.cloudflare.com/tunnel/observability/#remote-log-streaming) and [Tunnel log streams](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/monitor-tunnels/logs/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-08-10-tunnel-live-logs-core-dashboard/#page","headline":"Stream live logs from Cloudflare Tunnel in the dashboard","description":"The Tunnel detail view in the Cloudflare dashboard now supports real-time log streaming, including multi-connector aggregated streaming with filtering.","url":"https://developers.cloudflare.com/changelog/post/2026-08-10-tunnel-live-logs-core-dashboard/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-08-10-tunnel-live-logs-core-dashboard/og.png?v=5d2114f6ea4b37d4","dateModified":"2026-08-10","datePublished":"2026-08-10","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
