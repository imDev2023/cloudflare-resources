---
description: Push per-connection WebSocket close reason, close source, and session metadata to any Logpush destination.
title: New WebSocket Analytics Logpush dataset
image: https://developers.cloudflare.com/changelog/post/2026-07-07-websocket-analytics-dataset/og.png?v=1a234d0df2f39f66
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

July 7, 2026

## New WebSocket Analytics Logpush dataset

[Logs](https://developers.cloudflare.com/logs/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-07-07-websocket-analytics-dataset/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Enterprise customers can now push per-connection WebSocket analytics to any [Logpush destination](https://developers.cloudflare.com/logs/logpush/logpush-job/enable-destinations/) using the new `websocket_analytics` dataset. Each log record is emitted when a WebSocket connection closes and includes fields that were previously only available to Cloudflare engineers via internal tooling.

Key fields include:

- **`ConnectionCloseReason`** — why the connection ended: `peerReset`, `peerNoError`, `timedOut`, `upstreamReset`, `protocolViolation`, `unspecifiedError`, or `none`.
- **`ConnectionCloseSource`** — which side initiated the close: `upstream`, `downstream`, `me`, or `both`.
- **`ConnectionTransportCloseCode`** — the TLS alert code or TCP-level close code for additional precision.
- **`RayID`** — correlate WebSocket connection events with your existing HTTP Request logs.

The dataset also includes directional byte counts (`BytesSentClient`, `BytesReceivedClient`, `BytesSentOrigin`, `BytesReceivedOrigin`), connection timestamps, client IP, colo code, and request metadata from the original WebSocket upgrade.

This data lets you build alerts on connection close patterns — for example, detecting spikes in TCP resets (`ConnectionCloseReason == "peerReset"`) grouped by host and data center — directly in your existing log analysis tools.

For the full list of available fields, refer to [WebSocket Analytics](https://developers.cloudflare.com/logs/logpush/logpush-job/datasets/zone/websocket_analytics/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-07-07-websocket-analytics-dataset/#page","headline":"New WebSocket Analytics Logpush dataset","description":"Push per-connection WebSocket close reason, close source, and session metadata to any Logpush destination.","url":"https://developers.cloudflare.com/changelog/post/2026-07-07-websocket-analytics-dataset/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-07-07-websocket-analytics-dataset/og.png?v=1a234d0df2f39f66","dateModified":"2026-07-07","datePublished":"2026-07-07","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
