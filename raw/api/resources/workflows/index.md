---
title: Workflows
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Workflows

##### [List all Workflows](https://developers.cloudflare.com/api/resources/workflows/methods/list)

GET/accounts/{account\_id}/workflows

##### [Get Workflow details](https://developers.cloudflare.com/api/resources/workflows/methods/get)

GET/accounts/{account\_id}/workflows/{workflow\_name}

##### [Create/modify Workflow](https://developers.cloudflare.com/api/resources/workflows/methods/update)

PUT/accounts/{account\_id}/workflows/{workflow\_name}

##### [Deletes a Workflow](https://developers.cloudflare.com/api/resources/workflows/methods/delete)

DELETE/accounts/{account\_id}/workflows/{workflow\_name}

##### ModelsExpand Collapse

<details>

<summary>

WorkflowListResponse object {id, class\_name, created\_on, 7 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

class\_name: string

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_list_response%20%3E%20(schema)%20%3E%20(property)%20class_name">Link to this property</a>

created\_on: string

formatdate-time

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_list_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

instances: map\[number]

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_list_response%20%3E%20(schema)%20%3E%20(property)%20instances">Link to this property</a>

modified\_on: string

formatdate-time

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_list_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

name: string

maxLength64

minLength1

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_list_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

script\_name: string

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_list_response%20%3E%20(schema)%20%3E%20(property)%20script_name">Link to this property</a>

triggered\_on: string

formatdate-time

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_list_response%20%3E%20(schema)%20%3E%20(property)%20triggered_on">Link to this property</a>

<details>

<summary>

schedules: optional array of object {cron, next\_instance }

</summary>

cron: string

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_list_response%20%3E%20(schema)%20%3E%20(property)%20schedules%20%3E%20(items)%20%3E%20(property)%20cron">Link to this property</a>

next\_instance: string

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_list_response%20%3E%20(schema)%20%3E%20(property)%20schedules%20%3E%20(items)%20%3E%20(property)%20next_instance">Link to this property</a>

</details>

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_list_response%20%3E%20(schema)%20%3E%20(property)%20schedules">Link to this property</a>

script\_deleted: optional boolean

Whether the bound Worker was deleted, leaving this Workflow inactive.

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_list_response%20%3E%20(schema)%20%3E%20(property)%20script_deleted">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workflows%20%3E%20(model)%20workflow_list_response%20%3E%20(schema)>)

<details>

<summary>

WorkflowGetResponse object {id, class\_name, created\_on, 7 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

class\_name: string

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_get_response%20%3E%20(schema)%20%3E%20(property)%20class_name">Link to this property</a>

created\_on: string

formatdate-time

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_get_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

instances: map\[number]

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_get_response%20%3E%20(schema)%20%3E%20(property)%20instances">Link to this property</a>

modified\_on: string

formatdate-time

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_get_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

name: string

maxLength64

minLength1

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

script\_name: string

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_get_response%20%3E%20(schema)%20%3E%20(property)%20script_name">Link to this property</a>

triggered\_on: string

formatdate-time

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_get_response%20%3E%20(schema)%20%3E%20(property)%20triggered_on">Link to this property</a>

<details>

<summary>

schedules: optional array of object {cron, next\_instance }

</summary>

cron: string

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_get_response%20%3E%20(schema)%20%3E%20(property)%20schedules%20%3E%20(items)%20%3E%20(property)%20cron">Link to this property</a>

next\_instance: string

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_get_response%20%3E%20(schema)%20%3E%20(property)%20schedules%20%3E%20(items)%20%3E%20(property)%20next_instance">Link to this property</a>

</details>

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_get_response%20%3E%20(schema)%20%3E%20(property)%20schedules">Link to this property</a>

script\_deleted: optional boolean

Whether the bound Worker was deleted, leaving this Workflow inactive.

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_get_response%20%3E%20(schema)%20%3E%20(property)%20script_deleted">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workflows%20%3E%20(model)%20workflow_get_response%20%3E%20(schema)>)

<details>

<summary>

WorkflowUpdateResponse object {id, class\_name, created\_on, 7 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_update_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

class\_name: string

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_update_response%20%3E%20(schema)%20%3E%20(property)%20class_name">Link to this property</a>

created\_on: string

formatdate-time

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_update_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

is\_deleted: number

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_update_response%20%3E%20(schema)%20%3E%20(property)%20is_deleted">Link to this property</a>

modified\_on: string

formatdate-time

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

name: string

maxLength64

minLength1

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_update_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

script\_name: string

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_update_response%20%3E%20(schema)%20%3E%20(property)%20script_name">Link to this property</a>

terminator\_running: number

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_update_response%20%3E%20(schema)%20%3E%20(property)%20terminator_running">Link to this property</a>

triggered\_on: string

formatdate-time

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_update_response%20%3E%20(schema)%20%3E%20(property)%20triggered_on">Link to this property</a>

version\_id: string

formatuuid

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_update_response%20%3E%20(schema)%20%3E%20(property)%20version_id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workflows%20%3E%20(model)%20workflow_update_response%20%3E%20(schema)>)

<details>

<summary>

WorkflowDeleteResponse object {status, success }

</summary>

status: "ok"

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_delete_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

success: boolean

<a href="#(resource)%20workflows%20%3E%20(model)%20workflow_delete_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workflows%20%3E%20(model)%20workflow_delete_response%20%3E%20(schema)>)

#### WorkflowsInstances

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

#### WorkflowsInstancesStatus

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

#### WorkflowsInstancesEvents

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

#### WorkflowsVersions

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