---
title: Account
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[DNS](https://developers.cloudflare.com/api/resources/dns)

[Settings](https://developers.cloudflare.com/api/resources/dns/subresources/settings)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Account

##### [Show DNS Settings](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/methods/get)

GET/accounts/{account\_id}/dns\_settings

##### [Update DNS Settings](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/methods/edit)

PATCH/accounts/{account\_id}/dns\_settings

##### ModelsExpand Collapse

<details>

<summary>

AccountGetResponse object {zone\_defaults, enforce\_dns\_only }

</summary>

<details>

<summary>

zone\_defaults: object {flatten\_all\_cnames, foundation\_dns, internal\_dns, 6 more }

Default settings for new zones created in this account.

</summary>

flatten\_all\_cnames: boolean

Whether to flatten all CNAME records in the zone. Note that, due to DNS limitations, a CNAME record at the zone apex will always be flattened.

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20flatten_all_cnames">Link to this property</a>

Deprecatedfoundation\_dns: boolean

foundation\_dns is deprecated. Use nameservers.type: cloudflare.advanced to turn on Advanced Nameservers and cloudflare.standard to turn it off. This field will be removed in a future API version.

Deprecated. Use nameservers.type to configure Advanced Nameservers.

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20foundation_dns">Link to this property</a>

<details>

<summary>

internal\_dns: object {reference\_zone\_id }

Settings for this internal zone.

</summary>

reference\_zone\_id: optional string

The ID of the zone to fallback to.

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20internal_dns%20%3E%20(property)%20reference_zone_id">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20internal_dns">Link to this property</a>

multi\_provider: boolean

Whether to enable multi-provider DNS, which causes Cloudflare to activate the zone even when non-Cloudflare NS records exist, and to respect NS records at the zone apex during outbound zone transfers.

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20multi_provider">Link to this property</a>

<details>

<summary>

nameservers: object {type }

Settings determining the nameservers through which the zone should be available.

</summary>

<details>

<summary>

type: "cloudflare.standard"or "cloudflare.advanced"or "cloudflare.standard.random"or 2 more

Nameserver type

</summary>

One of the following:

"cloudflare.standard"

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20nameservers%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"cloudflare.advanced"

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20nameservers%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"cloudflare.standard.random"

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20nameservers%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"custom.account"

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20nameservers%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"custom.tenant"

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20nameservers%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20nameservers%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20nameservers">Link to this property</a>

ns\_ttl: number

The time to live (TTL) of the zone’s nameserver (NS) records.

maximum86400

minimum30

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20ns_ttl">Link to this property</a>

secondary\_overrides: boolean

Allows a Secondary DNS zone to use (proxied) override records and CNAME flattening at the zone apex.

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20secondary_overrides">Link to this property</a>

<details>

<summary>

soa: object {expire, min\_ttl, mname, 4 more }

Components of the zone’s SOA record.

</summary>

expire: optional number

Time in seconds of being unable to query the primary server after which secondary servers should stop serving the zone.

maximum2419200

minimum86400

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20soa%20%3E%20(property)%20expire">Link to this property</a>

min\_ttl: optional number

The time to live (TTL) for negative caching of records within the zone.

maximum86400

minimum60

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20soa%20%3E%20(property)%20min_ttl">Link to this property</a>

mname: optional string

The primary nameserver, which may be used for outbound zone transfers. If null, a Cloudflare-assigned value will be used.

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20soa%20%3E%20(property)%20mname">Link to this property</a>

refresh: optional number

Time in seconds after which secondary servers should re-check the SOA record to see if the zone has been updated.

maximum86400

minimum600

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20soa%20%3E%20(property)%20refresh">Link to this property</a>

retry: optional number

Time in seconds after which secondary servers should retry queries after the primary server was unresponsive.

maximum86400

minimum600

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20soa%20%3E%20(property)%20retry">Link to this property</a>

rname: optional string

The email address of the zone administrator, with the first label representing the local part of the email address.

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20soa%20%3E%20(property)%20rname">Link to this property</a>

ttl: optional number

The time to live (TTL) of the SOA record itself.

maximum86400

minimum300

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20soa%20%3E%20(property)%20ttl">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20soa">Link to this property</a>

<details>

<summary>

zone\_mode: "standard"or "cdn\_only"or "dns\_only"

Whether the zone mode is a regular or CDN/DNS only zone.

</summary>

One of the following:

"standard"

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20zone_mode%20%3E%20(member)%200">Link to this property</a>

"cdn\_only"

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20zone_mode%20%3E%20(member)%201">Link to this property</a>

"dns\_only"

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20zone_mode%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20zone_mode">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults">Link to this property</a>

enforce\_dns\_only: optional boolean

When enabled, forces all proxied DNS records in the account to behave as DNS-only at the edge, regardless of each record’s individual proxy setting. Note that this account-level override does not modify the records themselves; it only affects how they are served at the edge. See more on <a href="https://developers.cloudflare.com/dns/proxy-status/enforce-dns-only">Enforce DNS-only</a>.

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)%20%3E%20(property)%20enforce_dns_only">Link to this property</a>

</details>

[Link to this property](<#(resource)%20dns.settings.account%20%3E%20(model)%20account_get_response%20%3E%20(schema)>)

<details>

<summary>

AccountEditResponse object {zone\_defaults, enforce\_dns\_only }

</summary>

<details>

<summary>

zone\_defaults: object {flatten\_all\_cnames, foundation\_dns, internal\_dns, 6 more }

Default settings for new zones created in this account.

</summary>

flatten\_all\_cnames: boolean

Whether to flatten all CNAME records in the zone. Note that, due to DNS limitations, a CNAME record at the zone apex will always be flattened.

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20flatten_all_cnames">Link to this property</a>

Deprecatedfoundation\_dns: boolean

foundation\_dns is deprecated. Use nameservers.type: cloudflare.advanced to turn on Advanced Nameservers and cloudflare.standard to turn it off. This field will be removed in a future API version.

Deprecated. Use nameservers.type to configure Advanced Nameservers.

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20foundation_dns">Link to this property</a>

<details>

<summary>

internal\_dns: object {reference\_zone\_id }

Settings for this internal zone.

</summary>

reference\_zone\_id: optional string

The ID of the zone to fallback to.

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20internal_dns%20%3E%20(property)%20reference_zone_id">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20internal_dns">Link to this property</a>

multi\_provider: boolean

Whether to enable multi-provider DNS, which causes Cloudflare to activate the zone even when non-Cloudflare NS records exist, and to respect NS records at the zone apex during outbound zone transfers.

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20multi_provider">Link to this property</a>

<details>

<summary>

nameservers: object {type }

Settings determining the nameservers through which the zone should be available.

</summary>

<details>

<summary>

type: "cloudflare.standard"or "cloudflare.advanced"or "cloudflare.standard.random"or 2 more

Nameserver type

</summary>

One of the following:

"cloudflare.standard"

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20nameservers%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"cloudflare.advanced"

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20nameservers%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"cloudflare.standard.random"

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20nameservers%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"custom.account"

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20nameservers%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"custom.tenant"

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20nameservers%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20nameservers%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20nameservers">Link to this property</a>

ns\_ttl: number

The time to live (TTL) of the zone’s nameserver (NS) records.

maximum86400

minimum30

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20ns_ttl">Link to this property</a>

secondary\_overrides: boolean

Allows a Secondary DNS zone to use (proxied) override records and CNAME flattening at the zone apex.

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20secondary_overrides">Link to this property</a>

<details>

<summary>

soa: object {expire, min\_ttl, mname, 4 more }

Components of the zone’s SOA record.

</summary>

expire: optional number

Time in seconds of being unable to query the primary server after which secondary servers should stop serving the zone.

maximum2419200

minimum86400

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20soa%20%3E%20(property)%20expire">Link to this property</a>

min\_ttl: optional number

The time to live (TTL) for negative caching of records within the zone.

maximum86400

minimum60

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20soa%20%3E%20(property)%20min_ttl">Link to this property</a>

mname: optional string

The primary nameserver, which may be used for outbound zone transfers. If null, a Cloudflare-assigned value will be used.

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20soa%20%3E%20(property)%20mname">Link to this property</a>

refresh: optional number

Time in seconds after which secondary servers should re-check the SOA record to see if the zone has been updated.

maximum86400

minimum600

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20soa%20%3E%20(property)%20refresh">Link to this property</a>

retry: optional number

Time in seconds after which secondary servers should retry queries after the primary server was unresponsive.

maximum86400

minimum600

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20soa%20%3E%20(property)%20retry">Link to this property</a>

rname: optional string

The email address of the zone administrator, with the first label representing the local part of the email address.

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20soa%20%3E%20(property)%20rname">Link to this property</a>

ttl: optional number

The time to live (TTL) of the SOA record itself.

maximum86400

minimum300

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20soa%20%3E%20(property)%20ttl">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20soa">Link to this property</a>

<details>

<summary>

zone\_mode: "standard"or "cdn\_only"or "dns\_only"

Whether the zone mode is a regular or CDN/DNS only zone.

</summary>

One of the following:

"standard"

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20zone_mode%20%3E%20(member)%200">Link to this property</a>

"cdn\_only"

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20zone_mode%20%3E%20(member)%201">Link to this property</a>

"dns\_only"

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20zone_mode%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults%20%3E%20(property)%20zone_mode">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_defaults">Link to this property</a>

enforce\_dns\_only: optional boolean

When enabled, forces all proxied DNS records in the account to behave as DNS-only at the edge, regardless of each record’s individual proxy setting. Note that this account-level override does not modify the records themselves; it only affects how they are served at the edge. See more on <a href="https://developers.cloudflare.com/dns/proxy-status/enforce-dns-only">Enforce DNS-only</a>.

<a href="#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)%20%3E%20(property)%20enforce_dns_only">Link to this property</a>

</details>

[Link to this property](<#(resource)%20dns.settings.account%20%3E%20(model)%20account_edit_response%20%3E%20(schema)>)

#### AccountNameserver Sets

##### [List Custom Nameserver Sets](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/subresources/nameserver_sets/methods/list)

GET/accounts/{account\_id}/dns\_settings/nameserver\_sets

##### [Get Custom Nameserver Set](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/subresources/nameserver_sets/methods/get)

GET/accounts/{account\_id}/dns\_settings/nameserver\_sets/{nameserver\_set\_id}

##### [Create Custom Nameserver Set](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/subresources/nameserver_sets/methods/create)

POST/accounts/{account\_id}/dns\_settings/nameserver\_sets

##### [Delete Custom Nameserver Set](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/subresources/nameserver_sets/methods/delete)

DELETE/accounts/{account\_id}/dns\_settings/nameserver\_sets/{nameserver\_set\_id}

##### ModelsExpand Collapse

<details>

<summary>

NameserverSetListResponse = object {id, advanced, created\_on, 2 more } or object {id, advanced, created\_on, 2 more }

</summary>

One of the following:

<details>

<summary>

DNSSettingsNameserverSetStandardResponse object {id, advanced, created\_on, 2 more }

</summary>

id: string

Identifier for a nameserver set.

maxLength32

minLength32

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20id">Link to this property</a>

advanced: false

Whether the nameserver set uses Advanced anycast groups.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20advanced">Link to this property</a>

created\_on: string

When the nameserver set was created.

formatdate-time

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20created_on">Link to this property</a>

ip\_set: number

Selects the account-specific IP set that supplies the nameserver addresses. The account’s entitlement determines the maximum value. Nameserver sets with the same <code>ip_set</code> and <code>advanced</code> value may reuse addresses; otherwise, they use disjoint address groups.

formatint64

minimum1

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20ip_set">Link to this property</a>

<details>

<summary>

nameservers: array of object {ipv4, ipv6, name }

</summary>

ipv4: array of string

IPv4 addresses assigned to the nameserver.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv4">Link to this property</a>

ipv6: array of string

IPv6 addresses assigned to the nameserver.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv6">Link to this property</a>

name: string

A unique lowercase Punycode nameserver name within the set.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20nameservers">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

DNSSettingsNameserverSetAdvancedResponse object {id, advanced, created\_on, 2 more }

</summary>

id: string

Identifier for a nameserver set.

maxLength32

minLength32

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20id">Link to this property</a>

advanced: true

Whether the nameserver set uses Advanced anycast groups.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20advanced">Link to this property</a>

created\_on: string

When the nameserver set was created.

formatdate-time

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20created_on">Link to this property</a>

ip\_set: number

Selects the account-specific IP set that supplies the nameserver addresses. The account’s entitlement determines the maximum value. Nameserver sets with the same <code>ip_set</code> and <code>advanced</code> value may reuse addresses; otherwise, they use disjoint address groups.

formatint64

minimum1

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20ip_set">Link to this property</a>

<details>

<summary>

nameservers: array of object {ipv4, ipv4\_groups, ipv6, 2 more }

</summary>

ipv4: array of string

IPv4 addresses assigned to the nameserver.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv4">Link to this property</a>

<details>

<summary>

ipv4\_groups: array of "a"or "b"or "c"

Advanced anycast group for each address in the corresponding address array. Entries have the same order as, and correspond one-to-one with, the addresses.

</summary>

One of the following:

"a"

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv4_groups%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"b"

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv4_groups%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"c"

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv4_groups%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv4_groups">Link to this property</a>

ipv6: array of string

IPv6 addresses assigned to the nameserver.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv6">Link to this property</a>

<details>

<summary>

ipv6\_groups: array of "a"or "b"or "c"

Advanced anycast group for each address in the corresponding address array. Entries have the same order as, and correspond one-to-one with, the addresses.

</summary>

One of the following:

"a"

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv6_groups%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"b"

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv6_groups%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"c"

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv6_groups%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv6_groups">Link to this property</a>

name: string

A unique lowercase Punycode nameserver name within the set.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_list_response%20%3E%20(schema)>)

<details>

<summary>

NameserverSetGetResponse = object {id, advanced, created\_on, 2 more } or object {id, advanced, created\_on, 2 more }

</summary>

One of the following:

<details>

<summary>

DNSSettingsNameserverSetStandardResponse object {id, advanced, created\_on, 2 more }

</summary>

id: string

Identifier for a nameserver set.

maxLength32

minLength32

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20id">Link to this property</a>

advanced: false

Whether the nameserver set uses Advanced anycast groups.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20advanced">Link to this property</a>

created\_on: string

When the nameserver set was created.

formatdate-time

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20created_on">Link to this property</a>

ip\_set: number

Selects the account-specific IP set that supplies the nameserver addresses. The account’s entitlement determines the maximum value. Nameserver sets with the same <code>ip_set</code> and <code>advanced</code> value may reuse addresses; otherwise, they use disjoint address groups.

formatint64

minimum1

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20ip_set">Link to this property</a>

<details>

<summary>

nameservers: array of object {ipv4, ipv6, name }

</summary>

ipv4: array of string

IPv4 addresses assigned to the nameserver.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv4">Link to this property</a>

ipv6: array of string

IPv6 addresses assigned to the nameserver.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv6">Link to this property</a>

name: string

A unique lowercase Punycode nameserver name within the set.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20nameservers">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

DNSSettingsNameserverSetAdvancedResponse object {id, advanced, created\_on, 2 more }

</summary>

id: string

Identifier for a nameserver set.

maxLength32

minLength32

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20id">Link to this property</a>

advanced: true

Whether the nameserver set uses Advanced anycast groups.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20advanced">Link to this property</a>

created\_on: string

When the nameserver set was created.

formatdate-time

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20created_on">Link to this property</a>

ip\_set: number

Selects the account-specific IP set that supplies the nameserver addresses. The account’s entitlement determines the maximum value. Nameserver sets with the same <code>ip_set</code> and <code>advanced</code> value may reuse addresses; otherwise, they use disjoint address groups.

formatint64

minimum1

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20ip_set">Link to this property</a>

<details>

<summary>

nameservers: array of object {ipv4, ipv4\_groups, ipv6, 2 more }

</summary>

ipv4: array of string

IPv4 addresses assigned to the nameserver.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv4">Link to this property</a>

<details>

<summary>

ipv4\_groups: array of "a"or "b"or "c"

Advanced anycast group for each address in the corresponding address array. Entries have the same order as, and correspond one-to-one with, the addresses.

</summary>

One of the following:

"a"

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv4_groups%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"b"

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv4_groups%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"c"

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv4_groups%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv4_groups">Link to this property</a>

ipv6: array of string

IPv6 addresses assigned to the nameserver.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv6">Link to this property</a>

<details>

<summary>

ipv6\_groups: array of "a"or "b"or "c"

Advanced anycast group for each address in the corresponding address array. Entries have the same order as, and correspond one-to-one with, the addresses.

</summary>

One of the following:

"a"

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv6_groups%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"b"

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv6_groups%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"c"

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv6_groups%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv6_groups">Link to this property</a>

name: string

A unique lowercase Punycode nameserver name within the set.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_get_response%20%3E%20(schema)>)

<details>

<summary>

NameserverSetCreateResponse = object {id, advanced, created\_on, 2 more } or object {id, advanced, created\_on, 2 more }

</summary>

One of the following:

<details>

<summary>

DNSSettingsNameserverSetStandardResponse object {id, advanced, created\_on, 2 more }

</summary>

id: string

Identifier for a nameserver set.

maxLength32

minLength32

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20id">Link to this property</a>

advanced: false

Whether the nameserver set uses Advanced anycast groups.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20advanced">Link to this property</a>

created\_on: string

When the nameserver set was created.

formatdate-time

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20created_on">Link to this property</a>

ip\_set: number

Selects the account-specific IP set that supplies the nameserver addresses. The account’s entitlement determines the maximum value. Nameserver sets with the same <code>ip_set</code> and <code>advanced</code> value may reuse addresses; otherwise, they use disjoint address groups.

formatint64

minimum1

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20ip_set">Link to this property</a>

<details>

<summary>

nameservers: array of object {ipv4, ipv6, name }

</summary>

ipv4: array of string

IPv4 addresses assigned to the nameserver.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv4">Link to this property</a>

ipv6: array of string

IPv6 addresses assigned to the nameserver.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv6">Link to this property</a>

name: string

A unique lowercase Punycode nameserver name within the set.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20nameservers">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

DNSSettingsNameserverSetAdvancedResponse object {id, advanced, created\_on, 2 more }

</summary>

id: string

Identifier for a nameserver set.

maxLength32

minLength32

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20id">Link to this property</a>

advanced: true

Whether the nameserver set uses Advanced anycast groups.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20advanced">Link to this property</a>

created\_on: string

When the nameserver set was created.

formatdate-time

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20created_on">Link to this property</a>

ip\_set: number

Selects the account-specific IP set that supplies the nameserver addresses. The account’s entitlement determines the maximum value. Nameserver sets with the same <code>ip_set</code> and <code>advanced</code> value may reuse addresses; otherwise, they use disjoint address groups.

formatint64

minimum1

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20ip_set">Link to this property</a>

<details>

<summary>

nameservers: array of object {ipv4, ipv4\_groups, ipv6, 2 more }

</summary>

ipv4: array of string

IPv4 addresses assigned to the nameserver.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv4">Link to this property</a>

<details>

<summary>

ipv4\_groups: array of "a"or "b"or "c"

Advanced anycast group for each address in the corresponding address array. Entries have the same order as, and correspond one-to-one with, the addresses.

</summary>

One of the following:

"a"

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv4_groups%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"b"

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv4_groups%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"c"

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv4_groups%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv4_groups">Link to this property</a>

ipv6: array of string

IPv6 addresses assigned to the nameserver.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv6">Link to this property</a>

<details>

<summary>

ipv6\_groups: array of "a"or "b"or "c"

Advanced anycast group for each address in the corresponding address array. Entries have the same order as, and correspond one-to-one with, the addresses.

</summary>

One of the following:

"a"

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv6_groups%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"b"

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv6_groups%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"c"

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv6_groups%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20ipv6_groups">Link to this property</a>

name: string

A unique lowercase Punycode nameserver name within the set.

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20nameservers">Link to this property</a>

</details>

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_create_response%20%3E%20(schema)>)

<details>

<summary>

NameserverSetDeleteResponse object {id }

</summary>

id: string

Identifier for a nameserver set.

maxLength32

minLength32

<a href="#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20dns.settings.account.nameserver_sets%20%3E%20(model)%20nameserver_set_delete_response%20%3E%20(schema)>)

#### AccountViews

##### [List Internal DNS Views](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/subresources/views/methods/list)

GET/accounts/{account\_id}/dns\_settings/views

##### [DNS Internal View Details](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/subresources/views/methods/get)

GET/accounts/{account\_id}/dns\_settings/views/{view\_id}

##### [Create Internal DNS View](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/subresources/views/methods/create)

POST/accounts/{account\_id}/dns\_settings/views

##### [Update Internal DNS View](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/subresources/views/methods/edit)

PATCH/accounts/{account\_id}/dns\_settings/views/{view\_id}

##### [Delete Internal DNS View](https://developers.cloudflare.com/api/resources/dns/subresources/settings/subresources/account/subresources/views/methods/delete)

DELETE/accounts/{account\_id}/dns\_settings/views/{view\_id}

##### ModelsExpand Collapse

<details>

<summary>

ViewListResponse object {id, created\_time, modified\_time, 2 more }

</summary>

id: string

Identifier.

maxLength32

<a href="#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_time: string

When the view was created.

formatdate-time

<a href="#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_list_response%20%3E%20(schema)%20%3E%20(property)%20created_time">Link to this property</a>

modified\_time: string

When the view was last modified.

formatdate-time

<a href="#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_list_response%20%3E%20(schema)%20%3E%20(property)%20modified_time">Link to this property</a>

name: string

The name of the view.

maxLength255

minLength1

<a href="#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_list_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

zones: array of string

The list of zones linked to this view.

<a href="#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_list_response%20%3E%20(schema)%20%3E%20(property)%20zones">Link to this property</a>

</details>

[Link to this property](<#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_list_response%20%3E%20(schema)>)

<details>

<summary>

ViewGetResponse object {id, created\_time, modified\_time, 2 more }

</summary>

id: string

Identifier.

maxLength32

<a href="#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_time: string

When the view was created.

formatdate-time

<a href="#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_get_response%20%3E%20(schema)%20%3E%20(property)%20created_time">Link to this property</a>

modified\_time: string

When the view was last modified.

formatdate-time

<a href="#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_get_response%20%3E%20(schema)%20%3E%20(property)%20modified_time">Link to this property</a>

name: string

The name of the view.

maxLength255

minLength1

<a href="#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

zones: array of string

The list of zones linked to this view.

<a href="#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_get_response%20%3E%20(schema)%20%3E%20(property)%20zones">Link to this property</a>

</details>

[Link to this property](<#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_get_response%20%3E%20(schema)>)

<details>

<summary>

ViewCreateResponse object {id, created\_time, modified\_time, 2 more }

</summary>

id: string

Identifier.

maxLength32

<a href="#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_time: string

When the view was created.

formatdate-time

<a href="#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_create_response%20%3E%20(schema)%20%3E%20(property)%20created_time">Link to this property</a>

modified\_time: string

When the view was last modified.

formatdate-time

<a href="#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_create_response%20%3E%20(schema)%20%3E%20(property)%20modified_time">Link to this property</a>

name: string

The name of the view.

maxLength255

minLength1

<a href="#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

zones: array of string

The list of zones linked to this view.

<a href="#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_create_response%20%3E%20(schema)%20%3E%20(property)%20zones">Link to this property</a>

</details>

[Link to this property](<#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_create_response%20%3E%20(schema)>)

<details>

<summary>

ViewEditResponse object {id, created\_time, modified\_time, 2 more }

</summary>

id: string

Identifier.

maxLength32

<a href="#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_time: string

When the view was created.

formatdate-time

<a href="#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_edit_response%20%3E%20(schema)%20%3E%20(property)%20created_time">Link to this property</a>

modified\_time: string

When the view was last modified.

formatdate-time

<a href="#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_edit_response%20%3E%20(schema)%20%3E%20(property)%20modified_time">Link to this property</a>

name: string

The name of the view.

maxLength255

minLength1

<a href="#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_edit_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

zones: array of string

The list of zones linked to this view.

<a href="#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_edit_response%20%3E%20(schema)%20%3E%20(property)%20zones">Link to this property</a>

</details>

[Link to this property](<#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_edit_response%20%3E%20(schema)>)

<details>

<summary>

ViewDeleteResponse object {id }

</summary>

id: optional string

Identifier.

maxLength32

<a href="#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20dns.settings.account.views%20%3E%20(model)%20view_delete_response%20%3E%20(schema)>)