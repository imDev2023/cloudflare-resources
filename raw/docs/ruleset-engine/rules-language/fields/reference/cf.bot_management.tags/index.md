---
description: Provides the tags associated with bot traffic.
title: cf.bot_management.tags
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.bot\_management.tags

`cf.bot_management.tags``Array<String>`

Provides the tags associated with bot traffic.

Use this field to match requests associated with a specific bot tag.

Requires a Cloudflare Enterprise plan with [Bot Management](https://developers.cloudflare.com/bots/plans/bm-subscription/) enabled.

Example usage:

```txt
any(cf.bot_management.tags[*] eq "API")
```

Categories:
- Request
- Bots
