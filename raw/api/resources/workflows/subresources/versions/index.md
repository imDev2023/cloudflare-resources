---
title: Versions
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Workflows](https://developers.cloudflare.com/api/resources/workflows)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Versions

##### [List deployed Workflow versions](https://developers.cloudflare.com/api/resources/workflows/subresources/versions/methods/list)

GET/accounts/{account\_id}/workflows/{workflow\_name}/versions

##### [Get Workflow version details](https://developers.cloudflare.com/api/resources/workflows/subresources/versions/methods/get)

GET/accounts/{account\_id}/workflows/{workflow\_name}/versions/{version\_id}

##### [Get Workflow version graph](https://developers.cloudflare.com/api/resources/workflows/subresources/versions/methods/graph)

GET/accounts/{account\_id}/workflows/{workflow\_name}/versions/{version\_id}/graph

##### ModelsExpand Collapse

<details>

<summary>

VersionListResponse object {id, class\_name, created\_on, 7 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

class\_name: string

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20class_name">Link to this property</a>

created\_on: string

formatdate-time

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

has\_dag: boolean

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20has_dag">Link to this property</a>

<details>

<summary>

language: "javascript"or "python"

The programming language of the workflow implementation.

</summary>

One of the following:

"javascript"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20language%20%3E%20(member)%200">Link to this property</a>

"python"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20language%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20language">Link to this property</a>

modified\_on: string

formatdate-time

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

workflow\_id: string

formatuuid

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20workflow_id">Link to this property</a>

<details>

<summary>

concurrency: optional object {limit }

</summary>

limit: optional number

Maximum number of instances of this workflow that can run concurrently. Additional instances are queued and started as running instances complete. Must not exceed the account concurrency limit.

maximum9007199254740991

minimum1

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20concurrency%20%3E%20(property)%20limit">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20concurrency">Link to this property</a>

<details>

<summary>

default\_retention: optional object {error\_retention, success\_retention }

</summary>

error\_retention: optional number

Default error retention in milliseconds.

maximum9007199254740991

minimum-9007199254740991

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20default_retention%20%3E%20(property)%20error_retention">Link to this property</a>

success\_retention: optional number

Default success retention in milliseconds.

maximum9007199254740991

minimum-9007199254740991

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20default_retention%20%3E%20(property)%20success_retention">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20default_retention">Link to this property</a>

<details>

<summary>

limits: optional object {steps }

</summary>

steps: optional number

maximum9007199254740991

minimum1

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20limits%20%3E%20(property)%20steps">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20limits">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workflows.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)>)

<details>

<summary>

VersionGetResponse object {id, class\_name, created\_on, 7 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

class\_name: string

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20class_name">Link to this property</a>

created\_on: string

formatdate-time

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

has\_dag: boolean

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20has_dag">Link to this property</a>

<details>

<summary>

language: "javascript"or "python"

The programming language of the workflow implementation.

</summary>

One of the following:

"javascript"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20language%20%3E%20(member)%200">Link to this property</a>

"python"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20language%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20language">Link to this property</a>

modified\_on: string

formatdate-time

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

workflow\_id: string

formatuuid

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20workflow_id">Link to this property</a>

<details>

<summary>

concurrency: optional object {limit }

</summary>

limit: optional number

Maximum number of instances of this workflow that can run concurrently. Additional instances are queued and started as running instances complete. Must not exceed the account concurrency limit.

maximum9007199254740991

minimum1

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20concurrency%20%3E%20(property)%20limit">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20concurrency">Link to this property</a>

<details>

<summary>

default\_retention: optional object {error\_retention, success\_retention }

</summary>

error\_retention: optional number

Default error retention in milliseconds.

maximum9007199254740991

minimum-9007199254740991

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20default_retention%20%3E%20(property)%20error_retention">Link to this property</a>

success\_retention: optional number

Default success retention in milliseconds.

maximum9007199254740991

minimum-9007199254740991

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20default_retention%20%3E%20(property)%20success_retention">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20default_retention">Link to this property</a>

<details>

<summary>

limits: optional object {steps }

</summary>

steps: optional number

maximum9007199254740991

minimum1

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20limits%20%3E%20(property)%20steps">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20limits">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workflows.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)>)

<details>

<summary>

VersionGraphResponse object {id, class\_name, created\_on, 3 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

class\_name: string

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20class_name">Link to this property</a>

created\_on: string

formatdate-time

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

<details>

<summary>

graph: object {version, workflow }

Versioned workflow graph payload.

</summary>

version: number

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20version">Link to this property</a>

<details>

<summary>

workflow: object {class\_name, functions, nodes, payload }

A parsed workflow entrypoint with its step graph.

</summary>

class\_name: string

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20class_name">Link to this property</a>

<details>

<summary>

functions: map\[object {name, nodes, type } ]

</summary>

name: string

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20functions%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

nodes: array of unknown

Child nodes (recursive).

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20functions%20%3E%20(items)%20%3E%20(property)%20nodes">Link to this property</a>

type: "function\_def"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20functions%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20functions">Link to this property</a>

<details>

<summary>

nodes: array of object {duration, name, type, 2 more } or object {config, name, nodes, 3 more } or object {name, options, type, 3 more } or 11 more

</summary>

One of the following:

<details>

<summary>

object {duration, name, type, 2 more }

</summary>

<details>

<summary>

duration: numberor string

Duration as milliseconds (number) or human-readable string.

</summary>

One of the following:

number

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20duration%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20duration%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20duration">Link to this property</a>

name: string

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20name">Link to this property</a>

type: "step\_sleep"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

resolves: optional number

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20resolves">Link to this property</a>

starts: optional number

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20starts">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {config, name, nodes, 3 more }

</summary>

<details>

<summary>

config: object {retries, timeout }

Configuration for a step (retries and timeout).

</summary>

<details>

<summary>

retries: object {backoff, delay, limit }

Retry policy for a step.

</summary>

<details>

<summary>

backoff: "constant"or "linear"or "exponential"

Backoff strategy for step retries.

</summary>

One of the following:

"constant"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20config%20%3E%20(property)%20retries%20%3E%20(property)%20backoff%20%3E%20(member)%200">Link to this property</a>

"linear"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20config%20%3E%20(property)%20retries%20%3E%20(property)%20backoff%20%3E%20(member)%201">Link to this property</a>

"exponential"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20config%20%3E%20(property)%20retries%20%3E%20(property)%20backoff%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20config%20%3E%20(property)%20retries%20%3E%20(property)%20backoff">Link to this property</a>

<details>

<summary>

delay: numberor string

Duration as milliseconds (number) or human-readable string.

</summary>

One of the following:

number

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20config%20%3E%20(property)%20retries%20%3E%20(property)%20delay%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20config%20%3E%20(property)%20retries%20%3E%20(property)%20delay%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20config%20%3E%20(property)%20retries%20%3E%20(property)%20delay">Link to this property</a>

limit: number

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20config%20%3E%20(property)%20retries%20%3E%20(property)%20limit">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20config%20%3E%20(property)%20retries">Link to this property</a>

<details>

<summary>

timeout: numberor string

Duration as milliseconds (number) or human-readable string.

</summary>

One of the following:

number

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20config%20%3E%20(property)%20timeout%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20config%20%3E%20(property)%20timeout%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20config%20%3E%20(property)%20timeout">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20config">Link to this property</a>

name: string

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20name">Link to this property</a>

nodes: array of unknown

Child nodes (recursive).

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20nodes">Link to this property</a>

type: "step\_do"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

resolves: optional number

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20resolves">Link to this property</a>

starts: optional number

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20starts">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

object {name, options, type, 3 more }

</summary>

name: string

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

options: object {event\_type, timeout }

Options for a waitForEvent step.

</summary>

event\_type: string

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20options%20%3E%20(property)%20event_type">Link to this property</a>

<details>

<summary>

timeout: numberor string

Duration as milliseconds (number) or human-readable string.

</summary>

One of the following:

number

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20options%20%3E%20(property)%20timeout%20%3E%20(variant)%200">Link to this property</a>

string

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20options%20%3E%20(property)%20timeout%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20options%20%3E%20(property)%20timeout">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20options">Link to this property</a>

type: "step\_wait\_for\_event"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

payload: optional object {type } or object {fields, type }

Shape descriptor for JSON payloads.

</summary>

One of the following:

<details>

<summary>

Type object {type }

</summary>

type: "unknown"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20payload%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20payload%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {fields, type }

</summary>

fields: map\[unknown]

Nested JsonShape fields (recursive structure).

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20payload%20%3E%20(variant)%201%20%3E%20(property)%20fields">Link to this property</a>

type: "object"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20payload%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20payload%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20payload">Link to this property</a>

resolves: optional number

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20resolves">Link to this property</a>

starts: optional number

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20starts">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

object {name, timestamp, type, 2 more }

</summary>

name: string

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20name">Link to this property</a>

timestamp: string

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20timestamp">Link to this property</a>

type: "step\_sleep\_until"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

resolves: optional number

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20resolves">Link to this property</a>

starts: optional number

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20starts">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

object {nodes, type }

</summary>

nodes: array of unknown

Child nodes (recursive).

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20nodes">Link to this property</a>

type: "loop"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

object {kind, nodes, type }

</summary>

<details>

<summary>

kind: "all"or "any"or "all\_settled"or "race"

Parallel execution strategy.

</summary>

One of the following:

"all"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20kind%20%3E%20(member)%200">Link to this property</a>

"any"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20kind%20%3E%20(member)%201">Link to this property</a>

"all\_settled"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20kind%20%3E%20(member)%202">Link to this property</a>

"race"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20kind%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20kind">Link to this property</a>

nodes: array of unknown

Child nodes (recursive).

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20nodes">Link to this property</a>

type: "parallel"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%205">Link to this property</a>

<details>

<summary>

object {catch\_block, finally\_block, try\_block, type }

</summary>

<details>

<summary>

catch\_block: object {nodes, type }

</summary>

nodes: array of unknown

Child nodes (recursive).

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20catch_block%20%3E%20(property)%20nodes">Link to this property</a>

type: "block"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20catch_block%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20catch_block">Link to this property</a>

<details>

<summary>

finally\_block: object {nodes, type }

</summary>

nodes: array of unknown

Child nodes (recursive).

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20finally_block%20%3E%20(property)%20nodes">Link to this property</a>

type: "block"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20finally_block%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20finally_block">Link to this property</a>

<details>

<summary>

try\_block: object {nodes, type }

</summary>

nodes: array of unknown

Child nodes (recursive).

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20try_block%20%3E%20(property)%20nodes">Link to this property</a>

type: "block"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20try_block%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20try_block">Link to this property</a>

type: "try"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%206">Link to this property</a>

<details>

<summary>

object {nodes, type }

</summary>

nodes: array of unknown

Child nodes (recursive).

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(property)%20nodes">Link to this property</a>

type: "block"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%207">Link to this property</a>

<details>

<summary>

object {branches, type }

</summary>

<details>

<summary>

branches: array of object {condition, nodes }

</summary>

condition: string

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20branches%20%3E%20(items)%20%3E%20(property)%20condition">Link to this property</a>

nodes: array of unknown

Child nodes (recursive).

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20branches%20%3E%20(items)%20%3E%20(property)%20nodes">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20branches">Link to this property</a>

type: "if"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%208">Link to this property</a>

<details>

<summary>

object {branches, discriminant, type }

</summary>

<details>

<summary>

branches: array of object {condition, nodes }

</summary>

condition: string

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20branches%20%3E%20(items)%20%3E%20(property)%20condition">Link to this property</a>

nodes: array of unknown

Child nodes (recursive).

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20branches%20%3E%20(items)%20%3E%20(property)%20nodes">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20branches">Link to this property</a>

discriminant: string

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20discriminant">Link to this property</a>

type: "switch"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%209">Link to this property</a>

<details>

<summary>

object {class\_name, functions, nodes, 2 more }

</summary>

class\_name: string

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20class_name">Link to this property</a>

<details>

<summary>

functions: map\[object {name, nodes, type } ]

</summary>

name: string

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20functions%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

nodes: array of unknown

Child nodes (recursive).

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20functions%20%3E%20(items)%20%3E%20(property)%20nodes">Link to this property</a>

type: "function\_def"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20functions%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20functions">Link to this property</a>

nodes: array of unknown

Child nodes (recursive).

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20nodes">Link to this property</a>

type: "start"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

payload: optional object {type } or object {fields, type }

Shape descriptor for JSON payloads.

</summary>

One of the following:

<details>

<summary>

Type object {type }

</summary>

type: "unknown"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20payload%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20payload%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {fields, type }

</summary>

fields: map\[unknown]

Nested JsonShape fields (recursive structure).

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20payload%20%3E%20(variant)%201%20%3E%20(property)%20fields">Link to this property</a>

type: "object"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20payload%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20payload%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20payload">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2010">Link to this property</a>

<details>

<summary>

object {name, type, resolves, starts }

</summary>

name: string

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20name">Link to this property</a>

type: "function\_call"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20type">Link to this property</a>

resolves: optional number

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20resolves">Link to this property</a>

starts: optional number

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20starts">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2011">Link to this property</a>

<details>

<summary>

object {name, nodes, type }

</summary>

name: string

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20name">Link to this property</a>

nodes: array of unknown

Child nodes (recursive).

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20nodes">Link to this property</a>

type: "function\_def"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2012">Link to this property</a>

<details>

<summary>

object {kind, type }

</summary>

<details>

<summary>

kind: "break"or "return"

Break or return from a loop.

</summary>

One of the following:

"break"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(property)%20kind%20%3E%20(member)%200">Link to this property</a>

"return"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(property)%20kind%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(property)%20kind">Link to this property</a>

type: "break"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes%20%3E%20(items)%20%3E%20(variant)%2013">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20nodes">Link to this property</a>

<details>

<summary>

payload: optional object {type } or object {fields, type }

Shape descriptor for JSON payloads.

</summary>

One of the following:

<details>

<summary>

Type object {type }

</summary>

type: "unknown"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20payload%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20payload%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {fields, type }

</summary>

fields: map\[unknown]

Nested JsonShape fields (recursive structure).

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20payload%20%3E%20(variant)%201%20%3E%20(property)%20fields">Link to this property</a>

type: "object"

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20payload%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20payload%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow%20%3E%20(property)%20payload">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph%20%3E%20(property)%20workflow">Link to this property</a>

</details>

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20graph">Link to this property</a>

modified\_on: string

formatdate-time

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

workflow\_id: string

formatuuid

<a href="#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)%20%3E%20(property)%20workflow_id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workflows.versions%20%3E%20(model)%20version_graph_response%20%3E%20(schema)>)