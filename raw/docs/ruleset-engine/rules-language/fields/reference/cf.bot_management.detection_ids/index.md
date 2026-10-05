---
description: List of IDs that correlate to the Bot Management heuristic detections made on a request.
title: cf.bot_management.detection_ids
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.bot\_management.detection\_ids

`cf.bot_management.detection_ids``Array<Number>`

List of IDs that correlate to the Bot Management heuristic detections made on a request.

Use this field to explicitly match a specific heuristic or to exclude a heuristic in a rule. You can have multiple heuristic detections on the same request.

Requires a Cloudflare Enterprise plan with [Bot Management](https://developers.cloudflare.com/bots/plans/bm-subscription/) enabled.

Example usage:

```txt
any(cf.bot_management.detection_ids[*] eq 33554817)
```

Categories:
- Request
- Bots
