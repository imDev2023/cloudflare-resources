---
title: Zone
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[DNS](https://developers.cloudflare.com/api/resources/dns)

[Settings](https://developers.cloudflare.com/api/resources/dns/subresources/settings)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Zone

##### [Show DNS Settings](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/zone/methods/get)

GET/zones/{zone\_id}/dns\_settings

##### [Update DNS Settings](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/zone/methods/edit)

PATCH/zones/{zone\_id}/dns\_settings

##### ModelsExpand Collapse

<details>

<summary>

ZoneGetResponse object {flatten\_all\_cnames, foundation\_dns, internal\_dns, 6 more }

</summary>

flatten\_all\_cnames: boolean

Whether to flatten all CNAME records in the zone. Note that, due to DNS limitations, a CNAME record at the zone apex will always be flattened.

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20flatten_all_cnames">Link to this property</a>

Deprecatedfoundation\_dns: boolean

foundation\_dns is deprecated. Use nameservers.type: cloudflare.advanced to turn on Advanced Nameservers and cloudflare.standard to turn it off. This field will be removed in a future API version.

Deprecated. Use nameservers.type to configure Advanced Nameservers.

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20foundation_dns">Link to this property</a>

<details>

<summary>

internal\_dns: object {reference\_zone\_id }

Settings for this internal zone.

</summary>

reference\_zone\_id: optional string

The ID of the zone to fallback to.

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20internal_dns%20%3E%20(property)%20reference_zone_id">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20internal_dns">Link to this property</a>

multi\_provider: boolean

Whether to enable multi-provider DNS, which causes Cloudflare to activate the zone even when non-Cloudflare NS records exist, and to respect NS records at the zone apex during outbound zone transfers.

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20multi_provider">Link to this property</a>

<details>

<summary>

nameservers: object {type } or object {type, ns\_set } or object {nameserver\_set\_id, type }

Controls the nameservers through which the zone is available.

</summary>

One of the following:

<details>

<summary>

DNSSettingsZoneNameserversCloudflare object {type }

</summary>

<details>

<summary>

type: "cloudflare.standard"or "cloudflare.advanced"

Nameserver type.

</summary>

One of the following:

"cloudflare.standard"

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%200%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"cloudflare.advanced"

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%200%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

DNSSettingsZoneNameserversCustomExisting object {type, ns\_set }

</summary>

<details>

<summary>

type: "custom.account"or "custom.tenant"or "custom.zone"

Nameserver type.

</summary>

One of the following:

"custom.account"

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%201%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"custom.tenant"

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%201%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"custom.zone"

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%201%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

ns\_set: optional number

Configured nameserver set number to use for this zone.

maximum5

minimum1

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%201%20%3E%20(property)%20ns_set">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

DNSSettingsZoneNameserversCustomSet object {nameserver\_set\_id, type }

</summary>

nameserver\_set\_id: string

Identifier of the account-owned Custom Nameserver Set to use for this zone.

maxLength32

minLength32

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%202%20%3E%20(property)%20nameserver_set_id">Link to this property</a>

type: "custom"

Nameserver type.

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%202">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20nameservers">Link to this property</a>

ns\_ttl: number

The time to live (TTL) of the zone’s nameserver (NS) records.

maximum86400

minimum30

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20ns_ttl">Link to this property</a>

secondary\_overrides: boolean

Allows a Secondary DNS zone to use (proxied) override records and CNAME flattening at the zone apex.

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20secondary_overrides">Link to this property</a>

<details>

<summary>

soa: object {expire, min\_ttl, mname, 4 more }

Components of the zone’s SOA record.

</summary>

expire: optional number

Time in seconds of being unable to query the primary server after which secondary servers should stop serving the zone.

maximum2419200

minimum86400

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20soa%20%3E%20(property)%20expire">Link to this property</a>

min\_ttl: optional number

The time to live (TTL) for negative caching of records within the zone.

maximum86400

minimum60

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20soa%20%3E%20(property)%20min_ttl">Link to this property</a>

mname: optional string

The primary nameserver, which may be used for outbound zone transfers. If null, a Cloudflare-assigned value will be used.

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20soa%20%3E%20(property)%20mname">Link to this property</a>

refresh: optional number

Time in seconds after which secondary servers should re-check the SOA record to see if the zone has been updated.

maximum86400

minimum600

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20soa%20%3E%20(property)%20refresh">Link to this property</a>

retry: optional number

Time in seconds after which secondary servers should retry queries after the primary server was unresponsive.

maximum86400

minimum600

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20soa%20%3E%20(property)%20retry">Link to this property</a>

rname: optional string

The email address of the zone administrator, with the first label representing the local part of the email address.

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20soa%20%3E%20(property)%20rname">Link to this property</a>

ttl: optional number

The time to live (TTL) of the SOA record itself.

maximum86400

minimum300

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20soa%20%3E%20(property)%20ttl">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20soa">Link to this property</a>

<details>

<summary>

zone\_mode: "standard"or "cdn\_only"or "dns\_only"

Whether the zone mode is a regular or CDN/DNS only zone.

</summary>

One of the following:

"standard"

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_mode%20%3E%20(member)%200">Link to this property</a>

"cdn\_only"

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_mode%20%3E%20(member)%201">Link to this property</a>

"dns\_only"

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_mode%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_mode">Link to this property</a>

</details>

[Link to this property](<#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_get_response%20%3E%20(schema)>)

<details>

<summary>

ZoneEditResponse object {flatten\_all\_cnames, foundation\_dns, internal\_dns, 6 more }

</summary>

flatten\_all\_cnames: boolean

Whether to flatten all CNAME records in the zone. Note that, due to DNS limitations, a CNAME record at the zone apex will always be flattened.

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20flatten_all_cnames">Link to this property</a>

Deprecatedfoundation\_dns: boolean

foundation\_dns is deprecated. Use nameservers.type: cloudflare.advanced to turn on Advanced Nameservers and cloudflare.standard to turn it off. This field will be removed in a future API version.

Deprecated. Use nameservers.type to configure Advanced Nameservers.

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20foundation_dns">Link to this property</a>

<details>

<summary>

internal\_dns: object {reference\_zone\_id }

Settings for this internal zone.

</summary>

reference\_zone\_id: optional string

The ID of the zone to fallback to.

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20internal_dns%20%3E%20(property)%20reference_zone_id">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20internal_dns">Link to this property</a>

multi\_provider: boolean

Whether to enable multi-provider DNS, which causes Cloudflare to activate the zone even when non-Cloudflare NS records exist, and to respect NS records at the zone apex during outbound zone transfers.

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20multi_provider">Link to this property</a>

<details>

<summary>

nameservers: object {type } or object {type, ns\_set } or object {nameserver\_set\_id, type }

Controls the nameservers through which the zone is available.

</summary>

One of the following:

<details>

<summary>

DNSSettingsZoneNameserversCloudflare object {type }

</summary>

<details>

<summary>

type: "cloudflare.standard"or "cloudflare.advanced"

Nameserver type.

</summary>

One of the following:

"cloudflare.standard"

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%200%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"cloudflare.advanced"

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%200%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

DNSSettingsZoneNameserversCustomExisting object {type, ns\_set }

</summary>

<details>

<summary>

type: "custom.account"or "custom.tenant"or "custom.zone"

Nameserver type.

</summary>

One of the following:

"custom.account"

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%201%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"custom.tenant"

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%201%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"custom.zone"

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%201%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

ns\_set: optional number

Configured nameserver set number to use for this zone.

maximum5

minimum1

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%201%20%3E%20(property)%20ns_set">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

DNSSettingsZoneNameserversCustomSet object {nameserver\_set\_id, type }

</summary>

nameserver\_set\_id: string

Identifier of the account-owned Custom Nameserver Set to use for this zone.

maxLength32

minLength32

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%202%20%3E%20(property)%20nameserver_set_id">Link to this property</a>

type: "custom"

Nameserver type.

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20nameservers%20%3E%20(variant)%202">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20nameservers">Link to this property</a>

ns\_ttl: number

The time to live (TTL) of the zone’s nameserver (NS) records.

maximum86400

minimum30

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20ns_ttl">Link to this property</a>

secondary\_overrides: boolean

Allows a Secondary DNS zone to use (proxied) override records and CNAME flattening at the zone apex.

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20secondary_overrides">Link to this property</a>

<details>

<summary>

soa: object {expire, min\_ttl, mname, 4 more }

Components of the zone’s SOA record.

</summary>

expire: optional number

Time in seconds of being unable to query the primary server after which secondary servers should stop serving the zone.

maximum2419200

minimum86400

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20soa%20%3E%20(property)%20expire">Link to this property</a>

min\_ttl: optional number

The time to live (TTL) for negative caching of records within the zone.

maximum86400

minimum60

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20soa%20%3E%20(property)%20min_ttl">Link to this property</a>

mname: optional string

The primary nameserver, which may be used for outbound zone transfers. If null, a Cloudflare-assigned value will be used.

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20soa%20%3E%20(property)%20mname">Link to this property</a>

refresh: optional number

Time in seconds after which secondary servers should re-check the SOA record to see if the zone has been updated.

maximum86400

minimum600

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20soa%20%3E%20(property)%20refresh">Link to this property</a>

retry: optional number

Time in seconds after which secondary servers should retry queries after the primary server was unresponsive.

maximum86400

minimum600

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20soa%20%3E%20(property)%20retry">Link to this property</a>

rname: optional string

The email address of the zone administrator, with the first label representing the local part of the email address.

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20soa%20%3E%20(property)%20rname">Link to this property</a>

ttl: optional number

The time to live (TTL) of the SOA record itself.

maximum86400

minimum300

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20soa%20%3E%20(property)%20ttl">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20soa">Link to this property</a>

<details>

<summary>

zone\_mode: "standard"or "cdn\_only"or "dns\_only"

Whether the zone mode is a regular or CDN/DNS only zone.

</summary>

One of the following:

"standard"

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_mode%20%3E%20(member)%200">Link to this property</a>

"cdn\_only"

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_mode%20%3E%20(member)%201">Link to this property</a>

"dns\_only"

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_mode%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_mode">Link to this property</a>

</details>

[Link to this property](<#(resource)%20dns.settings.zone%20%3E%20(model)%20zone_edit_response%20%3E%20(schema)>)