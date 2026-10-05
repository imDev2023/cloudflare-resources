---
description: The smoothed TCP round-trip time (RTT) between Cloudflare and the client in milliseconds.
title: cf.timings.client_tcp_rtt_msec
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.timings.client\_tcp\_rtt\_msec

`cf.timings.client_tcp_rtt_msec``Number`

The smoothed TCP round-trip time (RTT) between Cloudflare and the client in milliseconds.

This field is only populated for TCP (HTTP/1, HTTP/2) connections. For QUIC connections, the value is `0`.

Example value:

```txt
20
```

Example usage:

```txt
# Match requests over TCP where the RTT exceeds 200 ms
cf.timings.client_quic_rtt_msec > 200
```

Categories:
- Request
