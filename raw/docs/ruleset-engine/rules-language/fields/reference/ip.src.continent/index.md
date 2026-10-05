---
description: The continent code associated with the client IP address.
title: ip.src.continent
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# ip.src.continent

`ip.src.continent``String`

The continent code associated with the client IP address.

Values:

- `"AF"`: Africa
- `"AN"`: Antarctica
- `"AS"`: Asia
- `"EU"`: Europe
- `"NA"`: North America
- `"OC"`: Oceania
- `"SA"`: South America
- `"T1"`: Tor network

This field has the same value as the `ip.geoip.continent` field, which is deprecated. The `ip.geoip.continent` field is still available for new and existing rules, but you should use the `ip.src.continent` field instead.

*GeoIP is the registered trademark of MaxMind, Inc.*

Categories:
- Request
- Geolocation
