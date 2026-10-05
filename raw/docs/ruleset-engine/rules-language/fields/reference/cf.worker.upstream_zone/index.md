---
description: Identifies whether a request comes from a worker or not.
title: cf.worker.upstream_zone
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.worker.upstream\_zone

`cf.worker.upstream_zone``String`

Identifies whether a request comes from a worker or not.

When a request comes from a worker, this field will hold the name of the zone for that worker. Otherwise, `cf.worker.upstream_zone` is empty.

Categories:
- Request
