---
description: The attack score class of the current request, based on the WAF attack score.
title: cf.waf.score.class
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.waf.score.class

`cf.waf.score.class``String`

The attack score class of the current request, based on the WAF attack score.

Can have one of the following values: `attack`, `likely_attack`, `likely_clean`, `clean`.

Requires a Cloudflare Business plan or above. You must also enable [attack score detection](https://developers.cloudflare.com/waf/detections/attack-score/).

Categories:
- Request
