---
description: The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds.
title: cf.timings.client_quic_rtt_msec
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.timings.client\_quic\_rtt\_msec

`cf.timings.client_quic_rtt_msec``Integer`

The smoothed QUIC round-trip time (RTT) between Cloudflare and the client in milliseconds.

This field is only populated for QUIC (HTTP/3) connections. For TCP connections, the value is `0`.

Example value:

```txt
42
```

Example usage:

```txt
# Match requests over QUIC where the RTT exceeds 200 ms
cf.timings.client_quic_rtt_msec > 200
```

Categories:
- Request
