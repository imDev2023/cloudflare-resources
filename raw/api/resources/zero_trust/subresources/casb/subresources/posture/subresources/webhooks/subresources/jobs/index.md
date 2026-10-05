---
title: Jobs
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[Casb](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb)

[Posture](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture)

[Webhooks](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/webhooks)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Jobs

##### [Create webhook jobs](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/posture/subresources/webhooks/subresources/jobs/methods/create)

POST/accounts/{account\_id}/data-security/posture/webhooks/jobs

##### ModelsExpand Collapse

<details>

<summary>

JobCreateResponse object {created, failed }

</summary>

<details>

<summary>

created: array of object {id, asset\_data, created\_at, 9 more }

Successfully created webhook jobs.

</summary>

id: string

Unique identifier for the webhook job.

formatuuid

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

asset\_data: map\[unknown]

Asset data associated with this webhook job.

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20asset_data">Link to this property</a>

created\_at: string

When the webhook job was created.

formatdate-time

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

integration\_id: string

ID of the integration.

formatuuid

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20integration_id">Link to this property</a>

last\_updated\_at: string

When the webhook job was last updated.

formatdate-time

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20last_updated_at">Link to this property</a>

<details>

<summary>

parameters: object {finding\_instance\_id }

Parameters for a webhook job.

</summary>

finding\_instance\_id: string

ID of the finding instance.

formatuuid

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20parameters%20%3E%20(property)%20finding_instance_id">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20parameters">Link to this property</a>

<details>

<summary>

status: "pending"or "processing"or "completed"or "failed"

Status of a webhook job.

</summary>

One of the following:

"pending"

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"processing"

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"completed"

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"failed"

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

triggered\_by\_actor: "user"or "account\_token"

Type of actor that triggered the webhook job.

</summary>

One of the following:

"user"

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20triggered_by_actor%20%3E%20(member)%200">Link to this property</a>

"account\_token"

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20triggered_by_actor%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20triggered_by_actor">Link to this property</a>

triggered\_by\_id: string

ID of the actor that triggered the job.

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20triggered_by_id">Link to this property</a>

webhook\_id: string

ID of the webhook configuration.

formatuuid

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20webhook_id">Link to this property</a>

failure\_details: optional map\[unknown]

Additional details about the failure.

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20failure_details">Link to this property</a>

<details>

<summary>

failure\_reason: optional "Permission Denied"or "Integration Unavailable"or "Service Temporarily Unavailable"or "System Error"

Reason for webhook job failure.

</summary>

One of the following:

"Permission Denied"

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20failure_reason%20%3E%20(member)%200">Link to this property</a>

"Integration Unavailable"

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20failure_reason%20%3E%20(member)%201">Link to this property</a>

"Service Temporarily Unavailable"

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20failure_reason%20%3E%20(member)%202">Link to this property</a>

"System Error"

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20failure_reason%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created%20%3E%20(items)%20%3E%20(property)%20failure_reason">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

<details>

<summary>

failed: array of object {error, finding\_instance\_id, webhook\_id }

Failed webhook job creation attempts.

</summary>

error: string

Error message describing the failure.

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20failed%20%3E%20(items)%20%3E%20(property)%20error">Link to this property</a>

finding\_instance\_id: string

ID of the finding instance that failed to create a webhook job.

formatuuid

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20failed%20%3E%20(items)%20%3E%20(property)%20finding_instance_id">Link to this property</a>

webhook\_id: string

ID of the webhook configuration.

formatuuid

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20failed%20%3E%20(items)%20%3E%20(property)%20webhook_id">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)%20%3E%20(property)%20failed">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.casb.posture.webhooks.jobs%20%3E%20(model)%20job_create_response%20%3E%20(schema)>)