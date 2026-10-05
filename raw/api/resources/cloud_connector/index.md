---
title: Cloud Connector
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Cloud Connector

#### Cloud ConnectorRules

##### [Rules](https://developers.cloudflare.com/api/resources/cloud_connector/subresources/rules/methods/list)

GET/zones/{zone\_id}/cloud\_connector/rules

##### [Put Rules](https://developers.cloudflare.com/api/resources/cloud_connector/subresources/rules/methods/update)

PUT/zones/{zone\_id}/cloud\_connector/rules

##### ModelsExpand Collapse

<details>

<summary>

RuleListResponse object {id, description, enabled, 3 more }

</summary>

id: optional string

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

description: optional string

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

expression: optional string

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

<details>

<summary>

parameters: optional object {host }

Parameters of Cloud Connector Rule

</summary>

host: optional string

Host to perform Cloud Connection to

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20host">Link to this property</a>

</details>

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20parameters">Link to this property</a>

<details>

<summary>

provider: optional "aws\_s3"or "cloudflare\_r2"or "gcp\_storage"or 2 more

Cloud Provider type

</summary>

One of the following:

"aws\_s3"

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20provider%20%3E%20(member)%200">Link to this property</a>

"cloudflare\_r2"

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20provider%20%3E%20(member)%201">Link to this property</a>

"gcp\_storage"

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20provider%20%3E%20(member)%202">Link to this property</a>

"azure\_storage"

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20provider%20%3E%20(member)%203">Link to this property</a>

"oci\_storage"

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20provider%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20provider">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)>)

<details>

<summary>

RuleUpdateResponse object {id, description, enabled, 3 more }

</summary>

id: optional string

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

description: optional string

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

expression: optional string

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

<details>

<summary>

parameters: optional object {host }

Parameters of Cloud Connector Rule

</summary>

host: optional string

Host to perform Cloud Connection to

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20parameters%20%3E%20(property)%20host">Link to this property</a>

</details>

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20parameters">Link to this property</a>

<details>

<summary>

provider: optional "aws\_s3"or "cloudflare\_r2"or "gcp\_storage"or 2 more

Cloud Provider type

</summary>

One of the following:

"aws\_s3"

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20provider%20%3E%20(member)%200">Link to this property</a>

"cloudflare\_r2"

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20provider%20%3E%20(member)%201">Link to this property</a>

"gcp\_storage"

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20provider%20%3E%20(member)%202">Link to this property</a>

"azure\_storage"

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20provider%20%3E%20(member)%203">Link to this property</a>

"oci\_storage"

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20provider%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20provider">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloud_connector.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)>)