---
description: The time spent processing a request within the Cloudflare global network in milliseconds.
title: cf.timings.edge_msec
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.timings.edge\_msec

`cf.timings.edge_msec``Integer`

The time spent processing a request within the Cloudflare global network in milliseconds.

The value corresponds to the time interval between when the Cloudflare edge server accepted the HTTP request headers for processing and just before the HTTP response headers were available to be sent to the client.

The value does not include:

- The time spent forwarding the request to the origin server (refer to [`cf.timings.origin_ttfb_msec`](https://developers.cloudflare.com/ruleset-engine/rules-language/fields/reference/cf.timings.origin_ttfb_msec/)).
- The network transfer time to the client.

Example value:

```txt
28
```

Example usage:

```txt
# Matches requests where Cloudflare's edge processing time was greater than 500 milliseconds
cf.timings.edge_msec > 500
```

Categories:
- Request
