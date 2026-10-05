---
description: The 16-bit or 32-bit integer representing the Autonomous System (AS) number associated with the client IP address.
title: ip.src.asnum
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# ip.src.asnum

`ip.src.asnum``Number`

The 16-bit or 32-bit integer representing the Autonomous System (AS) number associated with the client IP address.

This field has the same value as the `ip.geoip.asnum` field, which is deprecated. The `ip.geoip.asnum` field is still available for new and existing rules, but you should use the `ip.src.asnum` field instead.

*GeoIP is the registered trademark of MaxMind, Inc.*

Categories:
- Request
- Geolocation
