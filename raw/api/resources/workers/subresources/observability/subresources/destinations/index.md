---
title: Destinations
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Workers](https://developers.cloudflare.com/api/resources/workers)

[Observability](https://developers.cloudflare.com/api/resources/workers/subresources/observability)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Destinations

##### [Get Destinations](https://developers.cloudflare.com/api/resources/workers/subresources/observability/subresources/destinations/methods/list)

GET/accounts/{account\_id}/workers/observability/destinations

##### [Create Destination](https://developers.cloudflare.com/api/resources/workers/subresources/observability/subresources/destinations/methods/create)

POST/accounts/{account\_id}/workers/observability/destinations

##### [Update Destination](https://developers.cloudflare.com/api/resources/workers/subresources/observability/subresources/destinations/methods/update)

PATCH/accounts/{account\_id}/workers/observability/destinations/{slug}

##### [Delete Destination](https://developers.cloudflare.com/api/resources/workers/subresources/observability/subresources/destinations/methods/delete)

DELETE/accounts/{account\_id}/workers/observability/destinations/{slug}

##### ModelsExpand Collapse

<details>

<summary>

DestinationListResponse object {configuration, enabled, name, 2 more }

</summary>

<details>

<summary>

configuration: object {destination\_conf, headers, jobStatus, 3 more }

</summary>

destination\_conf: string

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_list_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20destination_conf">Link to this property</a>

headers: map\[string]

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_list_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20headers">Link to this property</a>

<details>

<summary>

jobStatus: object {error\_message, last\_complete, last\_error }

</summary>

error\_message: string

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_list_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20jobStatus%20%3E%20(property)%20error_message">Link to this property</a>

last\_complete: string

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_list_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20jobStatus%20%3E%20(property)%20last_complete">Link to this property</a>

last\_error: string

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_list_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20jobStatus%20%3E%20(property)%20last_error">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_list_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20jobStatus">Link to this property</a>

<details>

<summary>

logpushDataset: "opentelemetry-traces"or "opentelemetry-logs"or "opentelemetry-metrics"

</summary>

One of the following:

"opentelemetry-traces"

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_list_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20logpushDataset%20%3E%20(member)%200">Link to this property</a>

"opentelemetry-logs"

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_list_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20logpushDataset%20%3E%20(member)%201">Link to this property</a>

"opentelemetry-metrics"

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_list_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20logpushDataset%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_list_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20logpushDataset">Link to this property</a>

type: "logpush"

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_list_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20type">Link to this property</a>

url: string

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_list_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20url">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_list_response%20%3E%20(schema)%20%3E%20(property)%20configuration">Link to this property</a>

enabled: boolean

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_list_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

name: string

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_list_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

scripts: array of string

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_list_response%20%3E%20(schema)%20%3E%20(property)%20scripts">Link to this property</a>

slug: string

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_list_response%20%3E%20(schema)%20%3E%20(property)%20slug">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_list_response%20%3E%20(schema)>)

<details>

<summary>

DestinationCreateResponse object {configuration, enabled, name, 2 more }

</summary>

<details>

<summary>

configuration: object {destination\_conf, logpushDataset, logpushJob, 2 more }

</summary>

destination\_conf: string

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_create_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20destination_conf">Link to this property</a>

<details>

<summary>

logpushDataset: "opentelemetry-traces"or "opentelemetry-logs"or "opentelemetry-metrics"

</summary>

One of the following:

"opentelemetry-traces"

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_create_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20logpushDataset%20%3E%20(member)%200">Link to this property</a>

"opentelemetry-logs"

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_create_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20logpushDataset%20%3E%20(member)%201">Link to this property</a>

"opentelemetry-metrics"

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_create_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20logpushDataset%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_create_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20logpushDataset">Link to this property</a>

logpushJob: number

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_create_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20logpushJob">Link to this property</a>

type: "logpush"

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_create_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20type">Link to this property</a>

url: string

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_create_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20url">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_create_response%20%3E%20(schema)%20%3E%20(property)%20configuration">Link to this property</a>

enabled: boolean

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_create_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

name: string

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

scripts: array of string

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_create_response%20%3E%20(schema)%20%3E%20(property)%20scripts">Link to this property</a>

slug: string

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_create_response%20%3E%20(schema)%20%3E%20(property)%20slug">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_create_response%20%3E%20(schema)>)

<details>

<summary>

DestinationUpdateResponse object {configuration, enabled, name, 2 more }

</summary>

<details>

<summary>

configuration: object {destination\_conf, logpushDataset, logpushJob, 2 more }

</summary>

destination\_conf: string

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_update_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20destination_conf">Link to this property</a>

<details>

<summary>

logpushDataset: "opentelemetry-traces"or "opentelemetry-logs"or "opentelemetry-metrics"

</summary>

One of the following:

"opentelemetry-traces"

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_update_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20logpushDataset%20%3E%20(member)%200">Link to this property</a>

"opentelemetry-logs"

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_update_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20logpushDataset%20%3E%20(member)%201">Link to this property</a>

"opentelemetry-metrics"

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_update_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20logpushDataset%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_update_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20logpushDataset">Link to this property</a>

logpushJob: number

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_update_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20logpushJob">Link to this property</a>

type: "logpush"

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_update_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20type">Link to this property</a>

url: string

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_update_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20url">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_update_response%20%3E%20(schema)%20%3E%20(property)%20configuration">Link to this property</a>

enabled: boolean

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_update_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

name: string

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_update_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

scripts: array of string

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_update_response%20%3E%20(schema)%20%3E%20(property)%20scripts">Link to this property</a>

slug: string

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_update_response%20%3E%20(schema)%20%3E%20(property)%20slug">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_update_response%20%3E%20(schema)>)

<details>

<summary>

DestinationDeleteResponse object {configuration, enabled, name, 2 more }

</summary>

<details>

<summary>

configuration: object {destination\_conf, logpushDataset, logpushJob, 2 more }

</summary>

destination\_conf: string

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_delete_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20destination_conf">Link to this property</a>

<details>

<summary>

logpushDataset: "opentelemetry-traces"or "opentelemetry-logs"or "opentelemetry-metrics"

</summary>

One of the following:

"opentelemetry-traces"

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_delete_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20logpushDataset%20%3E%20(member)%200">Link to this property</a>

"opentelemetry-logs"

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_delete_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20logpushDataset%20%3E%20(member)%201">Link to this property</a>

"opentelemetry-metrics"

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_delete_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20logpushDataset%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_delete_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20logpushDataset">Link to this property</a>

logpushJob: number

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_delete_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20logpushJob">Link to this property</a>

type: "logpush"

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_delete_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20type">Link to this property</a>

url: string

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_delete_response%20%3E%20(schema)%20%3E%20(property)%20configuration%20%3E%20(property)%20url">Link to this property</a>

</details>

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_delete_response%20%3E%20(schema)%20%3E%20(property)%20configuration">Link to this property</a>

enabled: boolean

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_delete_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

name: string

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_delete_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

scripts: array of string

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_delete_response%20%3E%20(schema)%20%3E%20(property)%20scripts">Link to this property</a>

slug: string

<a href="#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_delete_response%20%3E%20(schema)%20%3E%20(property)%20slug">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.observability.destinations%20%3E%20(model)%20destination_delete_response%20%3E%20(schema)>)