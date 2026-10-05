---
description: The ISO 3166-2 code for the first-level region associated with the IP address.
title: ip.src.subdivision_1_iso_code
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# ip.src.subdivision\_1\_iso\_code

`ip.src.subdivision_1_iso_code``String`

The ISO 3166-2 code for the first-level region associated with the IP address.

When the actual value is not available, this field contains an empty string.

Requires a Cloudflare Business or Enterprise plan.

For more information on the ISO 3166-2 standard and the available regions, refer to [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) on Wikipedia.

This field has the same value as the `ip.geoip.subdivision_1_iso_code` field, which is deprecated. The `ip.geoip.subdivision_1_iso_code` field is still available for new and existing rules, but you should use the `ip.src.subdivision_1_iso_code` field instead.

*GeoIP is the registered trademark of MaxMind, Inc.*

Example value:

```txt
"GB-ENG"
```

Categories:
- Request
- Geolocation
