---
title: Account Custom Nameservers
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Account Custom Nameservers

##### [List Account Custom Nameservers](https://developers.cloudflare.com/api/resources/custom_nameservers/methods/get)

GET/accounts/{account\_id}/custom\_ns

##### [Add Account Custom Nameserver](https://developers.cloudflare.com/api/resources/custom_nameservers/methods/create)

POST/accounts/{account\_id}/custom\_ns

##### [Delete Account Custom Nameserver](https://developers.cloudflare.com/api/resources/custom_nameservers/methods/delete)

DELETE/accounts/{account\_id}/custom\_ns/{custom\_ns\_id}

##### ModelsExpand Collapse

<details>

<summary>

CustomNameserver object {dns\_records, ns\_name, status, 2 more }

A single account custom nameserver.

</summary>

<details>

<summary>

dns\_records: array of object {type, value }

A and AAAA records associated with the nameserver.

</summary>

<details>

<summary>

type: optional "A"or "AAAA"

DNS record type.

</summary>

One of the following:

"A"

<a href="#(resource)%20custom_nameservers%20%3E%20(model)%20custom_nameserver%20%3E%20(schema)%20%3E%20(property)%20dns_records%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"AAAA"

<a href="#(resource)%20custom_nameservers%20%3E%20(model)%20custom_nameserver%20%3E%20(schema)%20%3E%20(property)%20dns_records%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20custom_nameservers%20%3E%20(model)%20custom_nameserver%20%3E%20(schema)%20%3E%20(property)%20dns_records%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

value: optional string

DNS record contents (an IPv4 or IPv6 address).

<a href="#(resource)%20custom_nameservers%20%3E%20(model)%20custom_nameserver%20%3E%20(schema)%20%3E%20(property)%20dns_records%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20custom_nameservers%20%3E%20(model)%20custom_nameserver%20%3E%20(schema)%20%3E%20(property)%20dns_records">Link to this property</a>

ns\_name: string

The FQDN of the name server.

formathostname

<a href="#(resource)%20custom_nameservers%20%3E%20(model)%20custom_nameserver%20%3E%20(schema)%20%3E%20(property)%20ns_name">Link to this property</a>

<details>

<summary>

Deprecatedstatus: "moved"or "pending"or "verified"

Verification status of the nameserver.

</summary>

One of the following:

"moved"

<a href="#(resource)%20custom_nameservers%20%3E%20(model)%20custom_nameserver%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending"

<a href="#(resource)%20custom_nameservers%20%3E%20(model)%20custom_nameserver%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"verified"

<a href="#(resource)%20custom_nameservers%20%3E%20(model)%20custom_nameserver%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20custom_nameservers%20%3E%20(model)%20custom_nameserver%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

zone\_tag: string

Identifier.

maxLength32

<a href="#(resource)%20custom_nameservers%20%3E%20(model)%20custom_nameserver%20%3E%20(schema)%20%3E%20(property)%20zone_tag">Link to this property</a>

ns\_set: optional number

The number of the set that this name server belongs to.

maximum5

minimum1

<a href="#(resource)%20custom_nameservers%20%3E%20(model)%20custom_nameserver%20%3E%20(schema)%20%3E%20(property)%20ns_set">Link to this property</a>

</details>

[Link to this property](<#(resource)%20custom_nameservers%20%3E%20(model)%20custom_nameserver%20%3E%20(schema)>)

CustomNameserverDeleteResponse = string

Unused

[Link to this property](<#(resource)%20custom_nameservers%20%3E%20(model)%20custom_nameserver_delete_response%20%3E%20(schema)>)