---
description: The round-trip time (RTT) between the Cloudflare global network and the origin server in milliseconds.
title: cf.timings.origin_ttfb_msec
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.timings.origin\_ttfb\_msec

`cf.timings.origin_ttfb_msec``Integer`

The round-trip time (RTT) between the Cloudflare global network and the origin server in milliseconds.

This field provides insight into origin server latency. It represents the Time to First Byte (TTFB) from the perspective of the Cloudflare edge server.

This metric includes both the network RTT and the time the origin server spent handling the request.

If the request was served from the Cloudflare CDN cache and the origin server was not reached, the value of this field will be `0`.

Example value:

```txt
150
```

Example usage:

```txt
# Matches requests where the origin response time (TTFB) was greater than 2 seconds:
cf.timings.origin_ttfb_msec > 2000
```

Categories:
- Request
