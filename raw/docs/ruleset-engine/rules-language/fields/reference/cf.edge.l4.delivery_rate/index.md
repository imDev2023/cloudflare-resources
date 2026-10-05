---
description: The most recent data delivery rate estimate for the client connection, in bytes per second.
title: cf.edge.l4.delivery_rate
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.edge.l4.delivery\_rate

`cf.edge.l4.delivery_rate``Integer`

The most recent data delivery rate estimate for the client connection, in bytes per second.

This metric reflects the rate at which data is being successfully delivered over the connection.

Returns `0` when L4 statistics are not available for the request.

Example value:

```txt
123456
```

Example usage:

```txt
# Match requests where the delivery rate is below 100 KB/s
cf.edge.l4.delivery_rate < 100000
```

Categories:
- Request
