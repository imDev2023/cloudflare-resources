---
title: Jobs
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[R2](https://developers.cloudflare.com/api/resources/r2)

[Super Slurper](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Jobs

##### [List jobs](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/subresources/jobs/methods/list)

GET/accounts/{account\_id}/slurper/jobs

##### [Get job details](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/subresources/jobs/methods/get)

GET/accounts/{account\_id}/slurper/jobs/{job\_id}

##### [Create a job](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/subresources/jobs/methods/create)

POST/accounts/{account\_id}/slurper/jobs

##### [Abort all jobs](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/subresources/jobs/methods/abort_all)

PUT/accounts/{account\_id}/slurper/jobs/abortAll

##### [Abort a job](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/subresources/jobs/methods/abort)

PUT/accounts/{account\_id}/slurper/jobs/{job\_id}/abort

##### [Pause a job](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/subresources/jobs/methods/pause)

PUT/accounts/{account\_id}/slurper/jobs/{job\_id}/pause

##### [Get job progress](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/subresources/jobs/methods/progress)

GET/accounts/{account\_id}/slurper/jobs/{job\_id}/progress

##### [Resume a job](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/subresources/jobs/methods/resume)

PUT/accounts/{account\_id}/slurper/jobs/{job\_id}/resume

##### ModelsExpand Collapse

<details>

<summary>

JobListResponse object {id, createdAt, finishedAt, 4 more }

</summary>

id: optional string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

createdAt: optional string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20createdAt">Link to this property</a>

finishedAt: optional string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20finishedAt">Link to this property</a>

overwrite: optional boolean

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20overwrite">Link to this property</a>

<details>

<summary>

source: optional object {bucket, endpoint, keys, 2 more } or object {bucket, keys, pathPrefix, vendor } or object {bucket, jurisdiction, keys, 2 more }

</summary>

One of the following:

<details>

<summary>

S3SourceResponseSchema object {bucket, endpoint, keys, 2 more }

</summary>

bucket: optional string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20bucket">Link to this property</a>

endpoint: optional string

formaturi

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20endpoint">Link to this property</a>

keys: optional array of string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20keys">Link to this property</a>

pathPrefix: optional string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20pathPrefix">Link to this property</a>

vendor: optional "s3"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20vendor">Link to this property</a>

</details>

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

GcsSourceResponseSchema object {bucket, keys, pathPrefix, vendor }

</summary>

bucket: optional string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20bucket">Link to this property</a>

keys: optional array of string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20keys">Link to this property</a>

pathPrefix: optional string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20pathPrefix">Link to this property</a>

vendor: optional "gcs"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20vendor">Link to this property</a>

</details>

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

R2SourceResponseSchema object {bucket, jurisdiction, keys, 2 more }

</summary>

bucket: optional string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20bucket">Link to this property</a>

<details>

<summary>

jurisdiction: optional "default"or "eu"or "us"or "fedramp"

</summary>

One of the following:

"default"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20jurisdiction%20%3E%20(member)%200">Link to this property</a>

"eu"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20jurisdiction%20%3E%20(member)%201">Link to this property</a>

"us"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20jurisdiction%20%3E%20(member)%202">Link to this property</a>

"fedramp"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20jurisdiction%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20jurisdiction">Link to this property</a>

keys: optional array of string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20keys">Link to this property</a>

pathPrefix: optional string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20pathPrefix">Link to this property</a>

vendor: optional <a href="https://developers.cloudflare.com/api/resources/r2#(resource)%20r2.buckets.sippy%20%3E%20(model)%20provider%20%3E%20(schema)">Provider</a>

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20vendor">Link to this property</a>

</details>

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202">Link to this property</a>

</details>

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

<details>

<summary>

status: optional "running"or "paused"or "aborted"or "completed"

</summary>

One of the following:

"running"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"paused"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"aborted"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"completed"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

target: optional object {bucket, jurisdiction, vendor }

</summary>

bucket: optional string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20target%20%3E%20(property)%20bucket">Link to this property</a>

<details>

<summary>

jurisdiction: optional "default"or "eu"or "us"or "fedramp"

</summary>

One of the following:

"default"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20target%20%3E%20(property)%20jurisdiction%20%3E%20(member)%200">Link to this property</a>

"eu"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20target%20%3E%20(property)%20jurisdiction%20%3E%20(member)%201">Link to this property</a>

"us"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20target%20%3E%20(property)%20jurisdiction%20%3E%20(member)%202">Link to this property</a>

"fedramp"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20target%20%3E%20(property)%20jurisdiction%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20target%20%3E%20(property)%20jurisdiction">Link to this property</a>

vendor: optional <a href="https://developers.cloudflare.com/api/resources/r2#(resource)%20r2.buckets.sippy%20%3E%20(model)%20provider%20%3E%20(schema)">Provider</a>

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20target%20%3E%20(property)%20vendor">Link to this property</a>

</details>

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

</details>

[Link to this property](<#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_list_response%20%3E%20(schema)>)

<details>

<summary>

JobGetResponse object {id, createdAt, finishedAt, 4 more }

</summary>

id: optional string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

createdAt: optional string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20createdAt">Link to this property</a>

finishedAt: optional string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20finishedAt">Link to this property</a>

overwrite: optional boolean

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20overwrite">Link to this property</a>

<details>

<summary>

source: optional object {bucket, endpoint, keys, 2 more } or object {bucket, keys, pathPrefix, vendor } or object {bucket, jurisdiction, keys, 2 more }

</summary>

One of the following:

<details>

<summary>

S3SourceResponseSchema object {bucket, endpoint, keys, 2 more }

</summary>

bucket: optional string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20bucket">Link to this property</a>

endpoint: optional string

formaturi

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20endpoint">Link to this property</a>

keys: optional array of string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20keys">Link to this property</a>

pathPrefix: optional string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20pathPrefix">Link to this property</a>

vendor: optional "s3"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20vendor">Link to this property</a>

</details>

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

GcsSourceResponseSchema object {bucket, keys, pathPrefix, vendor }

</summary>

bucket: optional string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20bucket">Link to this property</a>

keys: optional array of string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20keys">Link to this property</a>

pathPrefix: optional string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20pathPrefix">Link to this property</a>

vendor: optional "gcs"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20vendor">Link to this property</a>

</details>

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

R2SourceResponseSchema object {bucket, jurisdiction, keys, 2 more }

</summary>

bucket: optional string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20bucket">Link to this property</a>

<details>

<summary>

jurisdiction: optional "default"or "eu"or "us"or "fedramp"

</summary>

One of the following:

"default"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20jurisdiction%20%3E%20(member)%200">Link to this property</a>

"eu"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20jurisdiction%20%3E%20(member)%201">Link to this property</a>

"us"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20jurisdiction%20%3E%20(member)%202">Link to this property</a>

"fedramp"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20jurisdiction%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20jurisdiction">Link to this property</a>

keys: optional array of string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20keys">Link to this property</a>

pathPrefix: optional string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20pathPrefix">Link to this property</a>

vendor: optional <a href="https://developers.cloudflare.com/api/resources/r2#(resource)%20r2.buckets.sippy%20%3E%20(model)%20provider%20%3E%20(schema)">Provider</a>

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20vendor">Link to this property</a>

</details>

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202">Link to this property</a>

</details>

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

<details>

<summary>

status: optional "running"or "paused"or "aborted"or "completed"

</summary>

One of the following:

"running"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"paused"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"aborted"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"completed"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

target: optional object {bucket, jurisdiction, vendor }

</summary>

bucket: optional string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20target%20%3E%20(property)%20bucket">Link to this property</a>

<details>

<summary>

jurisdiction: optional "default"or "eu"or "us"or "fedramp"

</summary>

One of the following:

"default"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20target%20%3E%20(property)%20jurisdiction%20%3E%20(member)%200">Link to this property</a>

"eu"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20target%20%3E%20(property)%20jurisdiction%20%3E%20(member)%201">Link to this property</a>

"us"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20target%20%3E%20(property)%20jurisdiction%20%3E%20(member)%202">Link to this property</a>

"fedramp"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20target%20%3E%20(property)%20jurisdiction%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20target%20%3E%20(property)%20jurisdiction">Link to this property</a>

vendor: optional <a href="https://developers.cloudflare.com/api/resources/r2#(resource)%20r2.buckets.sippy%20%3E%20(model)%20provider%20%3E%20(schema)">Provider</a>

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20target%20%3E%20(property)%20vendor">Link to this property</a>

</details>

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)%20%3E%20(property)%20target">Link to this property</a>

</details>

[Link to this property](<#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_get_response%20%3E%20(schema)>)

<details>

<summary>

JobCreateResponse object {id }

</summary>

id: optional string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)>)

JobAbortAllResponse = string

[Link to this property](<#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_abort_all_response%20%3E%20(schema)>)

JobAbortResponse = string

[Link to this property](<#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_abort_response%20%3E%20(schema)>)

JobPauseResponse = string

[Link to this property](<#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_pause_response%20%3E%20(schema)>)

<details>

<summary>

JobProgressResponse object {id, createdAt, failedObjects, 4 more }

</summary>

id: optional string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_progress_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

createdAt: optional string

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_progress_response%20%3E%20(schema)%20%3E%20(property)%20createdAt">Link to this property</a>

failedObjects: optional number

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_progress_response%20%3E%20(schema)%20%3E%20(property)%20failedObjects">Link to this property</a>

objects: optional number

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_progress_response%20%3E%20(schema)%20%3E%20(property)%20objects">Link to this property</a>

skippedObjects: optional number

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_progress_response%20%3E%20(schema)%20%3E%20(property)%20skippedObjects">Link to this property</a>

<details>

<summary>

status: optional "running"or "paused"or "aborted"or "completed"

</summary>

One of the following:

"running"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_progress_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"paused"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_progress_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"aborted"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_progress_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"completed"

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_progress_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_progress_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

transferredObjects: optional number

<a href="#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_progress_response%20%3E%20(schema)%20%3E%20(property)%20transferredObjects">Link to this property</a>

</details>

[Link to this property](<#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_progress_response%20%3E%20(schema)>)

JobResumeResponse = string

[Link to this property](<#(resource)%20r2.super_slurper.jobs%20%3E%20(model)%20job_resume_response%20%3E%20(schema)>)

#### JobsLogs

##### [Get job logs](https://developers.cloudflare.com/api/resources/r2/subresources/super_slurper/subresources/jobs/subresources/logs/methods/list)

GET/accounts/{account\_id}/slurper/jobs/{job\_id}/logs

##### ModelsExpand Collapse

<details>

<summary>

LogListResponse object {createdAt, job, logType, 2 more }

</summary>

createdAt: optional string

<a href="#(resource)%20r2.super_slurper.jobs.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20createdAt">Link to this property</a>

job: optional string

<a href="#(resource)%20r2.super_slurper.jobs.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20job">Link to this property</a>

<details>

<summary>

logType: optional "migrationStart"or "migrationComplete"or "migrationAbort"or 12 more

</summary>

One of the following:

"migrationStart"

<a href="#(resource)%20r2.super_slurper.jobs.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20logType%20%3E%20(member)%200">Link to this property</a>

"migrationComplete"

<a href="#(resource)%20r2.super_slurper.jobs.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20logType%20%3E%20(member)%201">Link to this property</a>

"migrationAbort"

<a href="#(resource)%20r2.super_slurper.jobs.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20logType%20%3E%20(member)%202">Link to this property</a>

"migrationError"

<a href="#(resource)%20r2.super_slurper.jobs.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20logType%20%3E%20(member)%203">Link to this property</a>

"migrationPause"

<a href="#(resource)%20r2.super_slurper.jobs.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20logType%20%3E%20(member)%204">Link to this property</a>

"migrationResume"

<a href="#(resource)%20r2.super_slurper.jobs.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20logType%20%3E%20(member)%205">Link to this property</a>

"migrationErrorFailedContinuation"

<a href="#(resource)%20r2.super_slurper.jobs.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20logType%20%3E%20(member)%206">Link to this property</a>

"importErrorRetryExhaustion"

<a href="#(resource)%20r2.super_slurper.jobs.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20logType%20%3E%20(member)%207">Link to this property</a>

"importSkippedStorageClass"

<a href="#(resource)%20r2.super_slurper.jobs.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20logType%20%3E%20(member)%208">Link to this property</a>

"importSkippedOversized"

<a href="#(resource)%20r2.super_slurper.jobs.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20logType%20%3E%20(member)%209">Link to this property</a>

"importSkippedEmptyObject"

<a href="#(resource)%20r2.super_slurper.jobs.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20logType%20%3E%20(member)%2010">Link to this property</a>

"importSkippedUnsupportedContentType"

<a href="#(resource)%20r2.super_slurper.jobs.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20logType%20%3E%20(member)%2011">Link to this property</a>

"importSkippedExcludedContentType"

<a href="#(resource)%20r2.super_slurper.jobs.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20logType%20%3E%20(member)%2012">Link to this property</a>

"importSkippedInvalidMedia"

<a href="#(resource)%20r2.super_slurper.jobs.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20logType%20%3E%20(member)%2013">Link to this property</a>

"importSkippedRequiresRetrieval"

<a href="#(resource)%20r2.super_slurper.jobs.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20logType%20%3E%20(member)%2014">Link to this property</a>

</details>

<a href="#(resource)%20r2.super_slurper.jobs.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20logType">Link to this property</a>

message: optional string

<a href="#(resource)%20r2.super_slurper.jobs.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20message">Link to this property</a>

objectKey: optional string

<a href="#(resource)%20r2.super_slurper.jobs.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)%20%3E%20(property)%20objectKey">Link to this property</a>

</details>

[Link to this property](<#(resource)%20r2.super_slurper.jobs.logs%20%3E%20(model)%20log_list_response%20%3E%20(schema)>)