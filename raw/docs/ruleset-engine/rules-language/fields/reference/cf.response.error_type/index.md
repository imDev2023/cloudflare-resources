---
description: A string with the type of error in the response being returned.
title: cf.response.error_type
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# cf.response.error\_type

`cf.response.error_type``String`

A string with the type of error in the response being returned.

The default value is an empty string (`""`).

The available values are the following:

- `"managed_challenge"`
- `"iuam"`
- `"legacy_challenge"`
- `"ip_ban"`
- `"waf"`
- `"5xx"`
- `"1xxx"`
- `"always_online"`
- `"country_challenge"`
- `"ratelimit"`

You can use this field to customize the response for a specific type of error (for example, all 1XXX errors or all WAF block actions).

**Note**: This field is only available in [Response Header Transform Rules](https://developers.cloudflare.com/rules/transform/response-header-modification/) and [Custom Errors](https://developers.cloudflare.com/rules/custom-errors/).

Categories:
- Response
