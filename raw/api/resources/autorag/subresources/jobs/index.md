---
title: Jobs
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[AutoRAG](https://developers.cloudflare.com/api/resources/autorag)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Jobs

##### [List Jobs](https://developers.cloudflare.com/api/resources/autorag/subresources/jobs/methods/list)

Deprecated

GET/accounts/{account\_id}/autorag/rags/{id}/jobs

##### [Get a Job Details](https://developers.cloudflare.com/api/resources/autorag/subresources/jobs/methods/get)

Deprecated

GET/accounts/{account\_id}/autorag/rags/{id}/jobs/{job\_id}

##### [List Job Logs](https://developers.cloudflare.com/api/resources/autorag/subresources/jobs/methods/logs)

Deprecated

GET/accounts/{account\_id}/autorag/rags/{id}/jobs/{job\_id}/logs

##### ModelsExpand Collapse

<details>

<summary>

JobListResponse object {id, source, end\_reason, 3 more }

</summary>

id: string

<a href="#(resource)%20autorag.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

source: "user"or "schedule"

</summary>

One of the following:

"user"

<a href="#(resource)%20autorag.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"schedule"

<a href="#(resource)%20autorag.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20autorag.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

end\_reason: optional string

<a href="#(resource)%20autorag.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20end_reason">Link to this property</a>

ended\_at: optional string

<a href="#(resource)%20autorag.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20ended_at">Link to this property</a>

last\_seen\_at: optional string

<a href="#(resource)%20autorag.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20last_seen_at">Link to this property</a>

started\_at: optional string

<a href="#(resource)%20autorag.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20started_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20autorag.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)>)

<details>

<summary>

JobGetResponse object {id, source, end\_reason, 3 more }

</summary>

id: string

<a href="#(resource)%20autorag.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

source: "user"or "schedule"

</summary>

One of the following:

"user"

<a href="#(resource)%20autorag.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"schedule"

<a href="#(resource)%20autorag.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20autorag.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

end\_reason: optional string

<a href="#(resource)%20autorag.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20end_reason">Link to this property</a>

ended\_at: optional string

<a href="#(resource)%20autorag.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20ended_at">Link to this property</a>

last\_seen\_at: optional string

<a href="#(resource)%20autorag.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20last_seen_at">Link to this property</a>

started\_at: optional string

<a href="#(resource)%20autorag.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20started_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20autorag.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)>)

<details>

<summary>

JobLogsResponse = array of object {id, created\_at, message, message\_type }

</summary>

id: number

<a href="#(resource)%20autorag.jobs%20%3E%20(model)%20job_logs_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

created\_at: number

<a href="#(resource)%20autorag.jobs%20%3E%20(model)%20job_logs_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

message: string

<a href="#(resource)%20autorag.jobs%20%3E%20(model)%20job_logs_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

message\_type: number

<a href="#(resource)%20autorag.jobs%20%3E%20(model)%20job_logs_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20message_type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20autorag.jobs%20%3E%20(model)%20job_logs_response%20%3E%20(schema)>)