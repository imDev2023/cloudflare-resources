---
description: Three new properties on request.cf expose client connection RTT and delivery rate, enabling transport-aware logic in Workers without client-side changes.
title: New L4 transport telemetry fields in Workers
image: https://developers.cloudflare.com/changelog/post/2026-04-01-l4-transport-telemetry-fields/og.png?v=61c92484e81a46e1
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 1, 2026

## New L4 transport telemetry fields in Workers

[Workers](https://developers.cloudflare.com/workers/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-01-l4-transport-telemetry-fields/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Three new properties are now available on `request.cf` in Workers that expose Layer 4 transport telemetry from the client connection. These properties let your Worker make decisions based on real-time connection quality signals — such as round-trip time and data delivery rate — without requiring any client-side changes.

Previously, this telemetry was only available via the `Server-Timing: cfL4` response header. These new properties surface the same data directly in the Workers runtime, so you can use it for routing, logging, or response customization.

#### New properties

| Property | Type | Description |
| --- | --- | --- |
| `clientTcpRtt` | number \| undefined | The smoothed TCP round-trip time (RTT) between Cloudflare and the client in milliseconds. Only present for TCP connections (HTTP/1, HTTP/2). For example, `22`. |
| `clientQuicRtt` | number \| undefined | The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds. Only present for QUIC connections (HTTP/3). For example, `42`. |
| `edgeL4` | Object \| undefined | Layer 4 transport statistics. Contains `deliveryRate` (number) — the most recent data delivery rate estimate for the connection, in bytes per second. For example, `123456`. |

#### Example: Log connection quality metrics

```js
export default {
  async fetch(request) {
    const cf = request.cf;

    const rtt = cf.clientTcpRtt ?? cf.clientQuicRtt ?? 0;
    const deliveryRate = cf.edgeL4?.deliveryRate ?? 0;
    const transport = cf.clientTcpRtt ? "TCP" : "QUIC";

    console.log(`Transport: ${transport}, RTT: ${rtt}ms, Delivery rate: ${deliveryRate} B/s`);

    const headers = new Headers(request.headers);
    headers.set("X-Client-RTT", String(rtt));
    headers.set("X-Delivery-Rate", String(deliveryRate));

    return fetch(new Request(request, { headers }));
  },
};
```

For more information, refer to [Workers Runtime APIs: Request](https://developers.cloudflare.com/workers/runtime-apis/request/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-01-l4-transport-telemetry-fields/#page","headline":"New L4 transport telemetry fields in Workers","description":"Three new properties on request.cf expose client connection RTT and delivery rate, enabling transport-aware logic in Workers without client-side changes.","url":"https://developers.cloudflare.com/changelog/post/2026-04-01-l4-transport-telemetry-fields/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-01-l4-transport-telemetry-fields/og.png?v=61c92484e81a46e1","dateModified":"2026-04-01","datePublished":"2026-04-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
