---
description: A global score from 1–99 that combines the score of each WAF attack vector into a single score.
title: cf.waf.score
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.waf.score

`cf.waf.score``Number`

A global score from 1–99 that combines the score of each WAF attack vector into a single score.

The special score `100` indicates that Cloudflare did not score the request.

This is the standard [WAF attack score](https://developers.cloudflare.com/waf/detections/attack-score/) to detect variants of attack patterns.

Requires a Cloudflare Enterprise plan. You must also enable [attack score detection](https://developers.cloudflare.com/waf/detections/attack-score/).

Categories:
- Request
