---
title: DNS
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Intel](https://developers.cloudflare.com/api/resources/intel)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# DNS

##### [Get Passive DNS by IP](https://developers.cloudflare.com/api/resources/intel/subresources/dns/methods/list)

GET/accounts/{account\_id}/intel/dns

##### ModelsExpand Collapse

<details>

<summary>

DNS object {count, page, per\_page, reverse\_records }

</summary>

count: optional number

Total results returned based on your search parameters.

<a href="#(resource)%20intel.dns%20%3E%20(model)%20dns%20%3E%20(schema)%20%3E%20(property)%20count">Link to this property</a>

page: optional number

Current page within paginated list of results.

<a href="#(resource)%20intel.dns%20%3E%20(model)%20dns%20%3E%20(schema)%20%3E%20(property)%20page">Link to this property</a>

per\_page: optional number

Number of results per page of results.

<a href="#(resource)%20intel.dns%20%3E%20(model)%20dns%20%3E%20(schema)%20%3E%20(property)%20per_page">Link to this property</a>

<details>

<summary>

reverse\_records: optional array of object {first\_seen, hostname, last\_seen }

Reverse DNS look-ups observed during the time period.

</summary>

first\_seen: optional string

First seen date of the DNS record during the time period.

formatdate

<a href="#(resource)%20intel.dns%20%3E%20(model)%20dns%20%3E%20(schema)%20%3E%20(property)%20reverse_records%20%3E%20(items)%20%3E%20(property)%20first_seen">Link to this property</a>

hostname: optional string

Hostname that the IP was observed resolving to.

<a href="#(resource)%20intel.dns%20%3E%20(model)%20dns%20%3E%20(schema)%20%3E%20(property)%20reverse_records%20%3E%20(items)%20%3E%20(property)%20hostname">Link to this property</a>

last\_seen: optional string

Last seen date of the DNS record during the time period.

formatdate

<a href="#(resource)%20intel.dns%20%3E%20(model)%20dns%20%3E%20(schema)%20%3E%20(property)%20reverse_records%20%3E%20(items)%20%3E%20(property)%20last_seen">Link to this property</a>

</details>

<a href="#(resource)%20intel.dns%20%3E%20(model)%20dns%20%3E%20(schema)%20%3E%20(property)%20reverse_records">Link to this property</a>

</details>

[Link to this property](<#(resource)%20intel.dns%20%3E%20(model)%20dns%20%3E%20(schema)>)