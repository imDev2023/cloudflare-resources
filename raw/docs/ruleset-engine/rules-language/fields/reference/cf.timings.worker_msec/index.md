---
description: The time spent executing a Cloudflare Worker in milliseconds.
title: cf.timings.worker_msec
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.timings.worker\_msec

`cf.timings.worker_msec``Integer`

The time spent executing a Cloudflare Worker in milliseconds.

This field provides the wall-clock time that a Cloudflare Worker spent handling the request, measured in milliseconds.

Use this field to identify slow Worker executions, set up alerts for performance regressions, or add Worker execution time as a request header using Transform Rules for downstream observability.

If the request did not invoke a Worker, the value of this field will be `0`.

Example value:

```txt
12
```

Example usage:

```txt
# Matches requests where the Worker execution time exceeded 500 milliseconds
cf.timings.worker_msec > 500
```

Categories:
- Request
