---
description: Two new fields expose QUIC round-trip time and connection delivery rate, completing the set of L4 transport telemetry available in rule expressions.
title: New QUIC RTT and delivery rate fields
image: https://developers.cloudflare.com/changelog/post/2026-04-01-quic-rtt-delivery-rate-fields/og.png?v=21b905fdfd443e37
---

[Skip to content](#main-content)

[View RSS feeds](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/) [ Subscribe to RSS](https://developers.cloudflare.com/changelog/rss/index.xml)

[Back to all posts](https://developers.cloudflare.com/changelog)

April 1, 2026

## New QUIC RTT and delivery rate fields

[Rules](https://developers.cloudflare.com/rules/)

Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/changelog/post/2026-04-01-quic-rtt-delivery-rate-fields/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Two new fields are now available in rule expressions that surface Layer 4 transport telemetry from the client connection. Together with the existing [`cf.timings.client_tcp_rtt_msec`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/) field, these fields give you a complete picture of connection quality for both TCP and QUIC traffic — enabling transport-aware rules without requiring any client-side changes.

Previously, QUIC RTT and delivery rate data was only available via the `Server-Timing: cfL4` response header. These new fields make the same data available directly in rule expressions, so you can use them in Transform Rules, WAF Custom Rules, and other phases that support dynamic fields.

#### New fields

| Field | Type | Description |
| --- | --- | --- |
| `cf.timings.client_quic_rtt_msec` | Integer | The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds. Only populated for QUIC (HTTP/3) connections. Returns `0` for TCP connections. |
| `cf.edge.l4.delivery_rate` | Integer | The most recent data delivery rate estimate for the client connection, in bytes per second. Returns `0` when L4 statistics are not available for the request. |

#### Example: Route slow connections to a lightweight origin

Use a request header transform rule to tag requests from high-latency connections, so your origin can serve a lighter page variant:

**Rule expression:**

```txt
cf.timings.client_tcp_rtt_msec > 200 or cf.timings.client_quic_rtt_msec > 200
```

**Header modifications:**

| Operation | Header name | Value |
| --- | --- | --- |
| Set | `X-High-Latency` | `true` |

#### Example: Match low-bandwidth connections

```txt
cf.edge.l4.delivery_rate > 0 and cf.edge.l4.delivery_rate < 100000
```

For more information, refer to [Request Header Transform Rules](https://developers.cloudflare.com/rules/transform/request-header-modification/) and the [fields reference](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/).

```json
{"@context":"https://schema.org","@type":"BlogPosting","@id":"https://developers.cloudflare.com/changelog/post/2026-04-01-quic-rtt-delivery-rate-fields/#page","headline":"New QUIC RTT and delivery rate fields","description":"Two new fields expose QUIC round-trip time and connection delivery rate, completing the set of L4 transport telemetry available in rule expressions.","url":"https://developers.cloudflare.com/changelog/post/2026-04-01-quic-rtt-delivery-rate-fields/","inLanguage":"en","image":"https://developers.cloudflare.com/changelog/post/2026-04-01-quic-rtt-delivery-rate-fields/og.png?v=21b905fdfd443e37","dateModified":"2026-04-01","datePublished":"2026-04-01","publisher":{"@type":"Organization","name":"Cloudflare","description":"One platform for your apps, agents, and workforce. Build, secure, and scale without managing infrastructure","url":"https://www.cloudflare.com/","sameAs":["https://github.com/cloudflare","https://www.linkedin.com/company/cloudflare","https://x.com/cloudflare"],"logo":{"@type":"ImageObject","url":"https://developers.cloudflare.com/logo.svg"},"address":{"@type":"PostalAddress","streetAddress":"101 Townsend St","addressLocality":"San Francisco","addressRegion":"CA","postalCode":"94107","addressCountry":"US"},"contactPoint":[{"@type":"ContactPoint","contactType":"Customer Support","url":"https://support.cloudflare.com/","availableLanguage":["English"]},{"@type":"ContactPoint","contactType":"Sales","url":"https://www.cloudflare.com/contact/","availableLanguage":["English"]}]},"isPartOf":{"@type":"WebSite","@id":"https://developers.cloudflare.com/#website","name":"Cloudflare Docs","url":"https://developers.cloudflare.com/"}}
```
