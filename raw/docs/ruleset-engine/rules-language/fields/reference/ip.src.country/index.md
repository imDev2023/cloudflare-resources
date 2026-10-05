---
description: The 2-letter country code in [ISO 3166-1 Alpha 2](https://www.iso.org/obp/ui/#search/code/) format.
title: ip.src.country
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# ip.src.country

`ip.src.country``String`

The 2-letter country code in [ISO 3166-1 Alpha 2](https://www.iso.org/obp/ui/#search/code/) format.

For more information on the ISO 3166-1 Alpha 2 format, refer to [ISO 3166-1 Alpha 2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) on Wikipedia.

This field has the same value as the `ip.geoip.country` field, which is deprecated. The `ip.geoip.country` field is still available for new and existing rules, but you should use the `ip.src.country` field instead.

*GeoIP is the registered trademark of MaxMind, Inc.*

Example value:

```txt
"GB"
```

Categories:
- Request
- Geolocation
