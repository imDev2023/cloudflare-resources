---
title: Bulks
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Intel](https://developers.cloudflare.com/api/resources/intel)

[Domains](https://developers.cloudflare.com/api/resources/intel/subresources/domains)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Bulks

##### [Get Multiple Domain Details](https://developers.cloudflare.com/api/resources/intel/subresources/domains/subresources/bulks/methods/get)

GET/accounts/{account\_id}/intel/domain/bulk

##### ModelsExpand Collapse

<details>

<summary>

BulkGetResponse = array of object {additional\_information, application, content\_categories, 7 more }

</summary>

<details>

<summary>

additional\_information: optional object {suspected\_malware\_family }

Additional information related to the host name.

</summary>

suspected\_malware\_family: optional string

Suspected DGA malware family.

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20additional_information%20%3E%20(property)%20suspected_malware_family">Link to this property</a>

</details>

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20additional_information">Link to this property</a>

<details>

<summary>

application: optional object {id, name }

Application that the hostname belongs to.

</summary>

id: optional number

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20application%20%3E%20(property)%20id">Link to this property</a>

name: optional string

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20application%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20application">Link to this property</a>

<details>

<summary>

content\_categories: optional array of object {id, name, super\_category\_id }

</summary>

id: optional number

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20content_categories%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

name: optional string

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20content_categories%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

super\_category\_id: optional number

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20content_categories%20%3E%20(items)%20%3E%20(property)%20super_category_id">Link to this property</a>

</details>

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20content_categories">Link to this property</a>

domain: optional string

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20domain">Link to this property</a>

<details>

<summary>

inherited\_content\_categories: optional array of object {id, name, super\_category\_id }

</summary>

id: optional number

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20inherited_content_categories%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

name: optional string

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20inherited_content_categories%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

super\_category\_id: optional number

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20inherited_content_categories%20%3E%20(items)%20%3E%20(property)%20super_category_id">Link to this property</a>

</details>

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20inherited_content_categories">Link to this property</a>

inherited\_from: optional string

Domain from which <code>inherited_content_categories</code> and <code>inherited_risk_types</code> are inherited, if applicable.

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20inherited_from">Link to this property</a>

<details>

<summary>

inherited\_risk\_types: optional array of object {id, name, super\_category\_id }

</summary>

id: optional number

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20inherited_risk_types%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

name: optional string

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20inherited_risk_types%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

super\_category\_id: optional number

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20inherited_risk_types%20%3E%20(items)%20%3E%20(property)%20super_category_id">Link to this property</a>

</details>

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20inherited_risk_types">Link to this property</a>

popularity\_rank: optional number

Global Cloudflare 100k ranking for the last 30 days, if available for the hostname. The top ranked domain is 1, the lowest ranked domain is 100,000.

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20popularity_rank">Link to this property</a>

risk\_score: optional number

Hostname risk score, which is a value between 0 (lowest risk) to 1 (highest risk).

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20risk_score">Link to this property</a>

<details>

<summary>

risk\_types: optional array of object {id, name, super\_category\_id }

</summary>

id: optional number

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20risk_types%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

name: optional string

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20risk_types%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

super\_category\_id: optional number

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20risk_types%20%3E%20(items)%20%3E%20(property)%20super_category_id">Link to this property</a>

</details>

<a href="#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20risk_types">Link to this property</a>

</details>

[Link to this property](<#(resource)%20intel.domains.bulks%20%3E%20(model)%20bulk_get_response%20%3E%20(schema)>)