---
title: Datasets
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Logs](https://developers.cloudflare.com/api/resources/logs)

[Log Explorer](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Datasets

##### [List account or zone datasets](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/list)

GET/{accounts\_or\_zones}/{account\_or\_zone\_id}/logs/explorer/datasets

##### [Get an account or zone dataset](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/get)

GET/{accounts\_or\_zones}/{account\_or\_zone\_id}/logs/explorer/datasets/{dataset\_id}

##### [Create an account or zone dataset](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/create)

POST/{accounts\_or\_zones}/{account\_or\_zone\_id}/logs/explorer/datasets

##### [Update an account or zone dataset](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/update)

PUT/{accounts\_or\_zones}/{account\_or\_zone\_id}/logs/explorer/datasets/{dataset\_id}

##### [Delete an account or zone dataset](https://developers.cloudflare.com/api/resources/logs/subresources/log_explorer/subresources/datasets/methods/delete)

DELETE/{accounts\_or\_zones}/{account\_or\_zone\_id}/logs/explorer/datasets/{dataset\_id}

##### ModelsExpand Collapse

<details>

<summary>

CreateRequest object {dataset, fields, filter, filter\_attack\_traffic }

</summary>

dataset: string

Dataset type name to create (e.g. <code>http_requests</code>).

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20create_request%20%3E%20(schema)%20%3E%20(property)%20dataset">Link to this property</a>

<details>

<summary>

fields: optional array of object {enabled, name }

Controls which fields the API ingests. Defaults to all available fields when absent.

</summary>

enabled: boolean

Whether the API includes this field in log ingest.

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20create_request%20%3E%20(schema)%20%3E%20(property)%20fields%20%3E%20(items)%20%3E%20(property)%20enabled">Link to this property</a>

name: string

Field name in lowercase.

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20create_request%20%3E%20(schema)%20%3E%20(property)%20fields%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20create_request%20%3E%20(schema)%20%3E%20(property)%20fields">Link to this property</a>

filter: optional string

Optional Logpush filter predicate to restrict which events are ingested. See <a href="https://developers.cloudflare.com/logs/reference/filters/">Logpush filters</a> for syntax and examples.

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20create_request%20%3E%20(schema)%20%3E%20(property)%20filter">Link to this property</a>

filter\_attack\_traffic: optional boolean

Whether to filter attack traffic from the Logpush job. Defaults to <code>true</code> for supported datasets when omitted. Supported datasets are <code>http_requests</code>, <code>firewall_events</code>, and <code>network_analytics_logs</code>.

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20create_request%20%3E%20(schema)%20%3E%20(property)%20filter_attack_traffic">Link to this property</a>

</details>

[Link to this property](<#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20create_request%20%3E%20(schema)>)

<details>

<summary>

Dataset object {created\_at, dataset, dataset\_id, 8 more }

A Log Explorer dataset summary. List endpoints return this type and omit field configuration; use the single-dataset endpoint to retrieve it.

</summary>

created\_at: string

RFC3339 timestamp recording when the API created this dataset.

formatdate-time

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

dataset: string

Dataset type name (e.g. <code>http_requests</code>).

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20dataset">Link to this property</a>

dataset\_id: string

Unique dataset ID.

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20dataset_id">Link to this property</a>

deletion\_protection: boolean

Whether deletion is blocked. Set to <code>false</code> before deleting the dataset.

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20deletion_protection">Link to this property</a>

enabled: boolean

Whether log ingest is currently active for this dataset.

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

fields: array of object {enabled, name }

The field configuration for this dataset.

</summary>

enabled: boolean

Whether the API includes this field in log ingest.

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20fields%20%3E%20(items)%20%3E%20(property)%20enabled">Link to this property</a>

name: string

Field name in lowercase.

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20fields%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20fields">Link to this property</a>

object\_id: string

Public ID of the account or zone that owns this dataset.

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20object_id">Link to this property</a>

<details>

<summary>

object\_type: "account"or "zone"

Whether this dataset belongs to an account or a zone.

</summary>

One of the following:

"account"

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20object_type%20%3E%20(member)%200">Link to this property</a>

"zone"

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20object_type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20object_type">Link to this property</a>

updated\_at: string

RFC3339 timestamp recording when the API last updated this dataset.

formatdate-time

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

filter: optional string

The Logpush filter predicate applied to this dataset. Omitted when no filter is set.

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20filter">Link to this property</a>

filter\_attack\_traffic: optional boolean

Whether the Logpush job filters attack traffic. Omitted for datasets that do not support this option.

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)%20%3E%20(property)%20filter_attack_traffic">Link to this property</a>

</details>

[Link to this property](<#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset%20%3E%20(schema)>)

<details>

<summary>

DatasetSummary object {created\_at, dataset, dataset\_id, 5 more }

A Log Explorer dataset summary. List endpoints return this type and omit field configuration; use the single-dataset endpoint to retrieve it.

</summary>

created\_at: string

RFC3339 timestamp recording when the API created this dataset.

formatdate-time

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset_summary%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

dataset: string

Dataset type name (e.g. <code>http_requests</code>).

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset_summary%20%3E%20(schema)%20%3E%20(property)%20dataset">Link to this property</a>

dataset\_id: string

Unique dataset ID.

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset_summary%20%3E%20(schema)%20%3E%20(property)%20dataset_id">Link to this property</a>

deletion\_protection: boolean

Whether deletion is blocked. Set to <code>false</code> before deleting the dataset.

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset_summary%20%3E%20(schema)%20%3E%20(property)%20deletion_protection">Link to this property</a>

enabled: boolean

Whether log ingest is currently active for this dataset.

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset_summary%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

object\_id: string

Public ID of the account or zone that owns this dataset.

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset_summary%20%3E%20(schema)%20%3E%20(property)%20object_id">Link to this property</a>

<details>

<summary>

object\_type: "account"or "zone"

Whether this dataset belongs to an account or a zone.

</summary>

One of the following:

"account"

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset_summary%20%3E%20(schema)%20%3E%20(property)%20object_type%20%3E%20(member)%200">Link to this property</a>

"zone"

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset_summary%20%3E%20(schema)%20%3E%20(property)%20object_type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset_summary%20%3E%20(schema)%20%3E%20(property)%20object_type">Link to this property</a>

updated\_at: string

RFC3339 timestamp recording when the API last updated this dataset.

formatdate-time

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset_summary%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20dataset_summary%20%3E%20(schema)>)

<details>

<summary>

UpdateRequest object {enabled, deletion\_protection, fields, 2 more }

</summary>

enabled: boolean

Whether to enable or disable log ingest for this dataset.

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20update_request%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

deletion\_protection: optional boolean

Set to <code>false</code> to allow deletion of this dataset.

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20update_request%20%3E%20(schema)%20%3E%20(property)%20deletion_protection">Link to this property</a>

<details>

<summary>

fields: optional array of object {enabled, name }

Controls which fields the API ingests after the update. Defaults to all available fields when absent.

</summary>

enabled: boolean

Whether the API includes this field in log ingest.

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20update_request%20%3E%20(schema)%20%3E%20(property)%20fields%20%3E%20(items)%20%3E%20(property)%20enabled">Link to this property</a>

name: string

Field name in lowercase.

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20update_request%20%3E%20(schema)%20%3E%20(property)%20fields%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20update_request%20%3E%20(schema)%20%3E%20(property)%20fields">Link to this property</a>

filter: optional string

Optional Logpush filter predicate to restrict which events are ingested. If omitted, the existing filter is left unchanged. Set to an empty string (<code>""</code>) to clear the filter. Otherwise, replaces the dataset’s filter entirely. See <a href="https://developers.cloudflare.com/logs/reference/filters/">Logpush filters</a> for syntax and examples.

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20update_request%20%3E%20(schema)%20%3E%20(property)%20filter">Link to this property</a>

filter\_attack\_traffic: optional boolean

Whether to filter attack traffic from the Logpush job. If omitted, the existing setting is left unchanged. Supported datasets are <code>http_requests</code>, <code>firewall_events</code>, and <code>network_analytics_logs</code>.

<a href="#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20update_request%20%3E%20(schema)%20%3E%20(property)%20filter_attack_traffic">Link to this property</a>

</details>

[Link to this property](<#(resource)%20logs.log_explorer.datasets%20%3E%20(model)%20update_request%20%3E%20(schema)>)

#### DatasetsAvailable

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