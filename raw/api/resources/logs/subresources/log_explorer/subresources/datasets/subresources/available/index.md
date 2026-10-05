---
title: Available
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Logs](https://developers.cloudflare.com/api/resources/logs)

[Log Explorer](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer)

[Datasets](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Available

##### [List available account or zone datasets](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/subresources/available/methods/list)

GET/{accounts\_or\_zones}/{account\_or\_zone\_id}/logs/explorer/datasets/available

##### ModelsExpand Collapse

<details>

<summary>

AvailableDataset object {dataset, object\_type, schema, timestamp\_field }

A dataset type that the account or zone can create.

</summary>

dataset: string

Dataset type name (e.g. <code>http_requests</code>).

<a href="#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_dataset%20%3E%20(schema)%20%3E%20(property)%20dataset">Link to this property</a>

<details>

<summary>

object\_type: "account"or "zone"

Whether this dataset type is account-scoped or zone-scoped.

</summary>

One of the following:

"account"

<a href="#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_dataset%20%3E%20(schema)%20%3E%20(property)%20object_type%20%3E%20(member)%200">Link to this property</a>

"zone"

<a href="#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_dataset%20%3E%20(schema)%20%3E%20(property)%20object_type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_dataset%20%3E%20(schema)%20%3E%20(property)%20object_type">Link to this property</a>

<details>

<summary>

schema: object {properties, required, type }

JSON Schema that describes the fields this dataset exposes.

</summary>

properties: optional map\[unknown]

<a href="#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_dataset%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(property)%20properties">Link to this property</a>

required: optional array of string

<a href="#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_dataset%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(property)%20required">Link to this property</a>

type: optional "object"

<a href="#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_dataset%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_dataset%20%3E%20(schema)%20%3E%20(property)%20schema">Link to this property</a>

timestamp\_field: string

The primary timestamp field name for this dataset.

<a href="#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_dataset%20%3E%20(schema)%20%3E%20(property)%20timestamp_field">Link to this property</a>

</details>

[Link to this property](<#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_dataset%20%3E%20(schema)>)

<details>

<summary>

AvailableList object {errors, messages, success, result }

</summary>

<details>

<summary>

errors: array of <a href="https://developers.cloudflare.com/api/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_info%20%3E%20(schema)">ResponseInfo</a> { code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20%24shared%20%3E%20(model)%20response_info%20%3E%20(schema)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20%24shared%20%3E%20(model)%20response_info%20%3E%20(schema)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20%24shared%20%3E%20(model)%20response_info%20%3E%20(schema)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20%24shared%20%3E%20(model)%20response_info%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20%24shared%20%3E%20(model)%20response_info%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_list%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

messages: array of string

<a href="#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_list%20%3E%20(schema)%20%3E%20(property)%20messages">Link to this property</a>

success: boolean

<a href="#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_list%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

<details>

<summary>

result: optional array of <a href="https://developers.cloudflare.com/api/resources/logs#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_dataset%20%3E%20(schema)">AvailableDataset</a> { dataset, object\_type, schema, timestamp\_field }

</summary>

dataset: string

Dataset type name (e.g. <code>http_requests</code>).

<a href="#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_dataset%20%3E%20(schema)%20%3E%20(property)%20dataset">Link to this property</a>

<details>

<summary>

object\_type: "account"or "zone"

Whether this dataset type is account-scoped or zone-scoped.

</summary>

One of the following:

"account"

<a href="#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_dataset%20%3E%20(schema)%20%3E%20(property)%20object_type%20%3E%20(member)%200">Link to this property</a>

"zone"

<a href="#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_dataset%20%3E%20(schema)%20%3E%20(property)%20object_type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_dataset%20%3E%20(schema)%20%3E%20(property)%20object_type">Link to this property</a>

<details>

<summary>

schema: object {properties, required, type }

JSON Schema that describes the fields this dataset exposes.

</summary>

properties: optional map\[unknown]

<a href="#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_dataset%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(property)%20properties">Link to this property</a>

required: optional array of string

<a href="#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_dataset%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(property)%20required">Link to this property</a>

type: optional "object"

<a href="#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_dataset%20%3E%20(schema)%20%3E%20(property)%20schema%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_dataset%20%3E%20(schema)%20%3E%20(property)%20schema">Link to this property</a>

timestamp\_field: string

The primary timestamp field name for this dataset.

<a href="#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_dataset%20%3E%20(schema)%20%3E%20(property)%20timestamp_field">Link to this property</a>

</details>

<a href="#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_list%20%3E%20(schema)%20%3E%20(property)%20result">Link to this property</a>

</details>

[Link to this property](<#(resource)%20logs.log_explorer.datasets.available%20%3E%20(model)%20available_list%20%3E%20(schema)>)