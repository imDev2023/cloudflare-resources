---
description: Whether the request originates from a country in the European Union (EU).
title: ip.src.is_in_european_union
image: https://developers.cloudflare.com/og-docs.png
---

[Skip to content](#main-content)

# ip.src.is\_in\_european\_union

`ip.src.is_in_european_union``Boolean`

Whether the request originates from a country in the European Union (EU).

Requires a Cloudflare Business or Enterprise plan.

Countries in the EU (from geolocation data):

| Country code | Country name |
| --- | --- |
| `AT` | Austria |
| `AX` | Åland Islands |
| `BE` | Belgium |
| `BG` | Bulgaria |
| `CY` | Cyprus |
| `CZ` | Czechia |
| `DE` | Germany |
| `DK` | Denmark |
| `EE` | Estonia |
| `ES` | Spain |
| `FI` | Finland |
| `FR` | France |
| `GF` | French Guiana |
| `GP` | Guadeloupe |
| `GR` | Greece |
| `HR` | Croatia |
| `HU` | Hungary |
| `IE` | Ireland |
| `IT` | Italy |
| `LT` | Lithuania |
| `LU` | Luxembourg |
| `LV` | Latvia |
| `MF` | Saint Martin |
| `MQ` | Martinique |
| `MT` | Malta |
| `NL` | The Netherlands |
| `PL` | Poland |
| `PT` | Portugal |
| `RE` | Réunion |
| `RO` | Romania |
| `SE` | Sweden |
| `SI` | Slovenia |
| `SK` | Slovakia |
| `YT` | Mayotte |

This field has the same value as the `ip.geoip.is_in_european_union` field, which is deprecated. The `ip.geoip.is_in_european_union` field is still available for new and existing rules, but you should use the `ip.src.is_in_european_union` field instead.

*GeoIP is the registered trademark of MaxMind, Inc.*

Categories:
- Request
- Geolocation
