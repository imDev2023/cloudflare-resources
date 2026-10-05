---
title: Instances
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Workflows](https://developers.cloudflare.com/api/resources/workflows)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Instances

##### [List of workflow instances](https://developers.cloudflare.com/api/resources/workflows/subresources/instances/methods/list)

GET/accounts/{account\_id}/workflows/{workflow\_name}/instances

##### [Get logs and status from instance](https://developers.cloudflare.com/api/resources/workflows/subresources/instances/methods/get)

GET/accounts/{account\_id}/workflows/{workflow\_name}/instances/{instance\_id}

##### [Create a new workflow instance](https://developers.cloudflare.com/api/resources/workflows/subresources/instances/methods/create)

POST/accounts/{account\_id}/workflows/{workflow\_name}/instances

##### [Batch create new Workflow instances](https://developers.cloudflare.com/api/resources/workflows/subresources/instances/methods/bulk)

POST/accounts/{account\_id}/workflows/{workflow\_name}/instances/batch

##### [Get full step output from instance](https://developers.cloudflare.com/api/resources/workflows/subresources/instances/methods/step)

GET/accounts/{account\_id}/workflows/{workflow\_name}/instances/{instance\_id}/step

##### ModelsExpand Collapse

<details>

<summary>

InstanceListResponse object {id, created\_on, ended\_on, 6 more }

</summary>

id: string

maxLength100

minLength1

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_on: string

formatdate-time

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

ended\_on: string

formatdate-time

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)%20%3E%20(property)%20ended_on">Link to this property</a>

modified\_on: string

formatdate-time

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

started\_on: string

formatdate-time

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)%20%3E%20(property)%20started_on">Link to this property</a>

<details>

<summary>

status: "queued"or "running"or "paused"or 6 more

</summary>

One of the following:

"queued"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"running"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"paused"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"errored"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"terminated"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"complete"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

"waitingForPause"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%206">Link to this property</a>

"waiting"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%207">Link to this property</a>

"rollingBack"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%208">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

version\_id: string

formatuuid

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)%20%3E%20(property)%20version_id">Link to this property</a>

workflow\_id: string

formatuuid

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)%20%3E%20(property)%20workflow_id">Link to this property</a>

<details>

<summary>

trigger\_source: optional "unknown"or "api"or "binding"or 2 more

</summary>

One of the following:

"unknown"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)%20%3E%20(property)%20trigger_source%20%3E%20(member)%200">Link to this property</a>

"api"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)%20%3E%20(property)%20trigger_source%20%3E%20(member)%201">Link to this property</a>

"binding"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)%20%3E%20(property)%20trigger_source%20%3E%20(member)%202">Link to this property</a>

"event"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)%20%3E%20(property)%20trigger_source%20%3E%20(member)%203">Link to this property</a>

"cron"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)%20%3E%20(property)%20trigger_source%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)%20%3E%20(property)%20trigger_source">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workflows.instances%20%3E%20(model)%20instance_list_response%20%3E%20(schema)>)

<details>

<summary>

InstanceGetResponse object {end, error, output, 11 more }

</summary>

end: string

formatdate-time

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20end">Link to this property</a>

<details>

<summary>

error: object {message, name }

</summary>

message: string

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20error%20%3E%20(property)%20message">Link to this property</a>

name: string

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20error%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20error">Link to this property</a>

<details>

<summary>

output: stringor number

</summary>

One of the following:

string

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20output%20%3E%20(variant)%200">Link to this property</a>

number

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20output%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20output">Link to this property</a>

params: unknown

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20params">Link to this property</a>

queued: string

formatdate-time

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20queued">Link to this property</a>

<details>

<summary>

rollback: object {error, outcome }

</summary>

<details>

<summary>

error: object {message, name }

</summary>

message: string

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20rollback%20%3E%20(property)%20error%20%3E%20(property)%20message">Link to this property</a>

name: string

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20rollback%20%3E%20(property)%20error%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20rollback%20%3E%20(property)%20error">Link to this property</a>

<details>

<summary>

outcome: "complete"or "failed"

</summary>

One of the following:

"complete"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20rollback%20%3E%20(property)%20outcome%20%3E%20(member)%200">Link to this property</a>

"failed"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20rollback%20%3E%20(property)%20outcome%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20rollback%20%3E%20(property)%20outcome">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20rollback">Link to this property</a>

start: string

formatdate-time

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20start">Link to this property</a>

<details>

<summary>

status: "queued"or "running"or "paused"or 6 more

</summary>

One of the following:

"queued"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"running"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"paused"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"errored"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"terminated"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"complete"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

"waitingForPause"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%206">Link to this property</a>

"waiting"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%207">Link to this property</a>

"rollingBack"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%208">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

step\_count: number

maximum9007199254740991

minimum-9007199254740991

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20step_count">Link to this property</a>

<details>

<summary>

steps: array of object {attempts, config, end, 5 more } or object {end, error, finished, 3 more } or object {trigger, type } or object {end, error, finished, 5 more }

</summary>

One of the following:

<details>

<summary>

object {attempts, config, end, 5 more }

</summary>

<details>

<summary>

attempts: array of object {end, error, start, success }

</summary>

end: string

formatdate-time

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20attempts%20%3E%20(items)%20%3E%20(property)%20end">Link to this property</a>

<details>

<summary>

error: object {message, name }

</summary>

message: string

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20attempts%20%3E%20(items)%20%3E%20(property)%20error%20%3E%20(property)%20message">Link to this property</a>

name: string

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20attempts%20%3E%20(items)%20%3E%20(property)%20error%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20attempts%20%3E%20(items)%20%3E%20(property)%20error">Link to this property</a>

start: string

formatdate-time

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20attempts%20%3E%20(items)%20%3E%20(property)%20start">Link to this property</a>

success: boolean

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20attempts%20%3E%20(items)%20%3E%20(property)%20success">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20attempts">Link to this property</a>

<details>

<summary>

config: object {retries, timeout, sensitive }

</summary>

<details>

<summary>

retries: object {delay, limit, backoff }

</summary>

<details>

<summary>

delay: stringor number

Specifies the delay duration. The value ‘\[dynamic]’ means that a user-supplied function computes the delay.

</summary>

One of the following:

string

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20config%20%3E%20(property)%20retries%20%3E%20(property)%20delay%20%3E%20(variant)%200">Link to this property</a>

number

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20config%20%3E%20(property)%20retries%20%3E%20(property)%20delay%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20config%20%3E%20(property)%20retries%20%3E%20(property)%20delay">Link to this property</a>

limit: number

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20config%20%3E%20(property)%20retries%20%3E%20(property)%20limit">Link to this property</a>

<details>

<summary>

backoff: optional "constant"or "linear"or "exponential"

</summary>

One of the following:

"constant"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20config%20%3E%20(property)%20retries%20%3E%20(property)%20backoff%20%3E%20(member)%200">Link to this property</a>

"linear"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20config%20%3E%20(property)%20retries%20%3E%20(property)%20backoff%20%3E%20(member)%201">Link to this property</a>

"exponential"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20config%20%3E%20(property)%20retries%20%3E%20(property)%20backoff%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20config%20%3E%20(property)%20retries%20%3E%20(property)%20backoff">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20config%20%3E%20(property)%20retries">Link to this property</a>

<details>

<summary>

timeout: stringor number

Specifies the timeout duration.

</summary>

One of the following:

string

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20config%20%3E%20(property)%20timeout%20%3E%20(variant)%200">Link to this property</a>

number

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20config%20%3E%20(property)%20timeout%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20config%20%3E%20(property)%20timeout">Link to this property</a>

sensitive: optional "output"

When set to ‘output’, step output is redacted from log and step output responses.

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20config%20%3E%20(property)%20sensitive">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20config">Link to this property</a>

end: string

formatdate-time

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20end">Link to this property</a>

name: string

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20name">Link to this property</a>

output: string

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20output">Link to this property</a>

start: string

formatdate-time

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20start">Link to this property</a>

success: boolean

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20success">Link to this property</a>

<details>

<summary>

type: "step"or "rollback"

</summary>

One of the following:

"step"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"rollback"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {end, error, finished, 3 more }

</summary>

end: string

formatdate-time

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20end">Link to this property</a>

<details>

<summary>

error: object {message, name }

</summary>

message: string

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20error%20%3E%20(property)%20message">Link to this property</a>

name: string

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20error%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20error">Link to this property</a>

finished: boolean

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20finished">Link to this property</a>

name: string

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20name">Link to this property</a>

start: string

formatdate-time

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20start">Link to this property</a>

type: "sleep"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

object {trigger, type }

</summary>

<details>

<summary>

trigger: object {source }

</summary>

source: string

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20trigger%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20trigger">Link to this property</a>

type: "termination"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

object {end, error, finished, 5 more }

</summary>

end: string

formatdate-time

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20end">Link to this property</a>

<details>

<summary>

error: object {message, name }

</summary>

message: string

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20error%20%3E%20(property)%20message">Link to this property</a>

name: string

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20error%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20error">Link to this property</a>

finished: boolean

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20finished">Link to this property</a>

name: string

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20name">Link to this property</a>

start: string

formatdate-time

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20start">Link to this property</a>

type: "waitForEvent"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

event\_type: optional string

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20event_type">Link to this property</a>

output: optional string

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20output">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20steps">Link to this property</a>

success: boolean

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

<details>

<summary>

trigger: object {source }

</summary>

<details>

<summary>

source: "unknown"or "api"or "binding"or 2 more

</summary>

One of the following:

"unknown"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20trigger%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"api"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20trigger%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

"binding"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20trigger%20%3E%20(property)%20source%20%3E%20(member)%202">Link to this property</a>

"event"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20trigger%20%3E%20(property)%20source%20%3E%20(member)%203">Link to this property</a>

"cron"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20trigger%20%3E%20(property)%20source%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20trigger%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20trigger">Link to this property</a>

versionId: string

formatuuid

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20versionId">Link to this property</a>

<details>

<summary>

schedule: optional object {cron, scheduledTime }

</summary>

cron: string

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20schedule%20%3E%20(property)%20cron">Link to this property</a>

scheduledTime: number

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20schedule%20%3E%20(property)%20scheduledTime">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)%20%3E%20(property)%20schedule">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workflows.instances%20%3E%20(model)%20instance_get_response%20%3E%20(schema)>)

<details>

<summary>

InstanceCreateResponse object {id, status, version\_id, 2 more }

</summary>

id: string

maxLength100

minLength1

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

status: "queued"or "running"or "paused"or 6 more

</summary>

One of the following:

"queued"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"running"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"paused"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"errored"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"terminated"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"complete"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

"waitingForPause"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%206">Link to this property</a>

"waiting"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%207">Link to this property</a>

"rollingBack"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%208">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_create_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

version\_id: string

formatuuid

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_create_response%20%3E%20(schema)%20%3E%20(property)%20version_id">Link to this property</a>

workflow\_id: string

formatuuid

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_create_response%20%3E%20(schema)%20%3E%20(property)%20workflow_id">Link to this property</a>

<details>

<summary>

trigger\_source: optional "unknown"or "api"or "binding"or 2 more

</summary>

One of the following:

"unknown"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_create_response%20%3E%20(schema)%20%3E%20(property)%20trigger_source%20%3E%20(member)%200">Link to this property</a>

"api"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_create_response%20%3E%20(schema)%20%3E%20(property)%20trigger_source%20%3E%20(member)%201">Link to this property</a>

"binding"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_create_response%20%3E%20(schema)%20%3E%20(property)%20trigger_source%20%3E%20(member)%202">Link to this property</a>

"event"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_create_response%20%3E%20(schema)%20%3E%20(property)%20trigger_source%20%3E%20(member)%203">Link to this property</a>

"cron"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_create_response%20%3E%20(schema)%20%3E%20(property)%20trigger_source%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_create_response%20%3E%20(schema)%20%3E%20(property)%20trigger_source">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workflows.instances%20%3E%20(model)%20instance_create_response%20%3E%20(schema)>)

<details>

<summary>

InstanceBulkResponse object {id, status, version\_id, 2 more }

</summary>

id: string

maxLength100

minLength1

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_bulk_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

status: "queued"or "running"or "paused"or 6 more

</summary>

One of the following:

"queued"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_bulk_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"running"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_bulk_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"paused"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_bulk_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"errored"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_bulk_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"terminated"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_bulk_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"complete"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_bulk_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

"waitingForPause"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_bulk_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%206">Link to this property</a>

"waiting"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_bulk_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%207">Link to this property</a>

"rollingBack"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_bulk_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%208">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_bulk_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

version\_id: string

formatuuid

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_bulk_response%20%3E%20(schema)%20%3E%20(property)%20version_id">Link to this property</a>

workflow\_id: string

formatuuid

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_bulk_response%20%3E%20(schema)%20%3E%20(property)%20workflow_id">Link to this property</a>

<details>

<summary>

trigger\_source: optional "unknown"or "api"or "binding"or 2 more

</summary>

One of the following:

"unknown"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_bulk_response%20%3E%20(schema)%20%3E%20(property)%20trigger_source%20%3E%20(member)%200">Link to this property</a>

"api"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_bulk_response%20%3E%20(schema)%20%3E%20(property)%20trigger_source%20%3E%20(member)%201">Link to this property</a>

"binding"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_bulk_response%20%3E%20(schema)%20%3E%20(property)%20trigger_source%20%3E%20(member)%202">Link to this property</a>

"event"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_bulk_response%20%3E%20(schema)%20%3E%20(property)%20trigger_source%20%3E%20(member)%203">Link to this property</a>

"cron"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_bulk_response%20%3E%20(schema)%20%3E%20(property)%20trigger_source%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_bulk_response%20%3E%20(schema)%20%3E%20(property)%20trigger_source">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workflows.instances%20%3E%20(model)%20instance_bulk_response%20%3E%20(schema)>)

<details>

<summary>

InstanceStepResponse object {error, status, event\_type, output }

</summary>

<details>

<summary>

error: object {message, name }

Error details when status=‘errored’; null otherwise.

</summary>

message: string

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_step_response%20%3E%20(schema)%20%3E%20(property)%20error%20%3E%20(property)%20message">Link to this property</a>

name: string

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_step_response%20%3E%20(schema)%20%3E%20(property)%20error%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_step_response%20%3E%20(schema)%20%3E%20(property)%20error">Link to this property</a>

<details>

<summary>

status: "queued"or "running"or "paused"or 6 more

</summary>

One of the following:

"queued"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_step_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"running"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_step_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"paused"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_step_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"errored"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_step_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"terminated"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_step_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"complete"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_step_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

"waitingForPause"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_step_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%206">Link to this property</a>

"waiting"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_step_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%207">Link to this property</a>

"rollingBack"

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_step_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%208">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_step_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

event\_type: optional string

The event type the step is waiting on, as supplied to step.waitForEvent. Only present when type=‘waitForEvent’.

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_step_response%20%3E%20(schema)%20%3E%20(property)%20event_type">Link to this property</a>

output: optional unknown

Contains the full step output or waitForEvent payload without truncation. Uses ‘\[REDACTED]’ for sensitive outputs. Contains a value when status=‘complete’. May contain a ReadableStream when step.do returns one; the response serves stream outputs as application/octet-stream rather than JSON.

<a href="#(resource)%20workflows.instances%20%3E%20(model)%20instance_step_response%20%3E%20(schema)%20%3E%20(property)%20output">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workflows.instances%20%3E%20(model)%20instance_step_response%20%3E%20(schema)>)

#### InstancesStatus

##### [Change status of instance](https://developers.cloudflare.com/api/resources/workflows/subresources/instances/subresources/status/methods/edit)

PATCH/accounts/{account\_id}/workflows/{workflow\_name}/instances/{instance\_id}/status

##### ModelsExpand Collapse

<details>

<summary>

StatusEditResponse object {status, timestamp }

</summary>

<details>

<summary>

status: "queued"or "running"or "paused"or 6 more

</summary>

One of the following:

"queued"

<a href="#(resource)%20workflows.instances.status%20%3E%20(model)%20status_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"running"

<a href="#(resource)%20workflows.instances.status%20%3E%20(model)%20status_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"paused"

<a href="#(resource)%20workflows.instances.status%20%3E%20(model)%20status_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"errored"

<a href="#(resource)%20workflows.instances.status%20%3E%20(model)%20status_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"terminated"

<a href="#(resource)%20workflows.instances.status%20%3E%20(model)%20status_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"complete"

<a href="#(resource)%20workflows.instances.status%20%3E%20(model)%20status_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

"waitingForPause"

<a href="#(resource)%20workflows.instances.status%20%3E%20(model)%20status_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%206">Link to this property</a>

"waiting"

<a href="#(resource)%20workflows.instances.status%20%3E%20(model)%20status_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%207">Link to this property</a>

"rollingBack"

<a href="#(resource)%20workflows.instances.status%20%3E%20(model)%20status_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%208">Link to this property</a>

</details>

<a href="#(resource)%20workflows.instances.status%20%3E%20(model)%20status_edit_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

timestamp: string

Accepts ISO 8601 with no timezone offsets and in UTC.

formatdate-time

<a href="#(resource)%20workflows.instances.status%20%3E%20(model)%20status_edit_response%20%3E%20(schema)%20%3E%20(property)%20timestamp">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workflows.instances.status%20%3E%20(model)%20status_edit_response%20%3E%20(schema)>)

#### InstancesEvents

##### [Send event to instance](https://developers.cloudflare.com/api/resources/workflows/subresources/instances/subresources/events/methods/create)

POST/accounts/{account\_id}/workflows/{workflow\_name}/instances/{instance\_id}/events/{event\_type}

##### ModelsExpand Collapse

<details>

<summary>

EventCreateResponse object {instanceId, timestamp }

</summary>

instanceId: string

<a href="#(resource)%20workflows.instances.events%20%3E%20(model)%20event_create_response%20%3E%20(schema)%20%3E%20(property)%20instanceId">Link to this property</a>

timestamp: string

Accepts ISO 8601 with no timezone offsets and in UTC.

formatdate-time

<a href="#(resource)%20workflows.instances.events%20%3E%20(model)%20event_create_response%20%3E%20(schema)%20%3E%20(property)%20timestamp">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workflows.instances.events%20%3E%20(model)%20event_create_response%20%3E%20(schema)>)