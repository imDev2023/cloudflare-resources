---
title: Queues
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Queues

##### [List Queues](https://developers.cloudflare.com/api/resources/queues/methods/list)

GET/accounts/{account\_id}/queues

##### [Get Queue](https://developers.cloudflare.com/api/resources/queues/methods/get)

GET/accounts/{account\_id}/queues/{queue\_id}

##### [Get Queue Metrics](https://developers.cloudflare.com/api/resources/queues/methods/get_metrics)

GET/accounts/{account\_id}/queues/{queue\_id}/metrics

##### [Create Queue](https://developers.cloudflare.com/api/resources/queues/methods/create)

POST/accounts/{account\_id}/queues

##### [Update Queue](https://developers.cloudflare.com/api/resources/queues/methods/update)

PUT/accounts/{account\_id}/queues/{queue\_id}

##### [Update Queue](https://developers.cloudflare.com/api/resources/queues/methods/edit)

PATCH/accounts/{account\_id}/queues/{queue\_id}

##### [Delete Queue](https://developers.cloudflare.com/api/resources/queues/methods/delete)

DELETE/accounts/{account\_id}/queues/{queue\_id}

##### ModelsExpand Collapse

<details>

<summary>

Queue object {consumers, consumers\_total\_count, created\_on, 7 more }

</summary>

<details>

<summary>

consumers: optional array of <a href="https://developers.cloudflare.com/api/resources/queues#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)">Consumer</a>

</summary>

One of the following:

<details>

<summary>

Worker object {consumer\_id, created\_on, dead\_letter\_queue, 4 more }

</summary>

consumer\_id: optional string

A Resource identifier.

maxLength32

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20consumer_id">Link to this property</a>

created\_on: optional string

formatdate-time

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20created_on">Link to this property</a>

dead\_letter\_queue: optional string

Name of the dead letter queue, or empty string if not configured

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20dead_letter_queue">Link to this property</a>

queue\_name: optional string

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20queue_name">Link to this property</a>

script\_name: optional string

Name of a Worker

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20script_name">Link to this property</a>

<details>

<summary>

settings: optional object {batch\_size, max\_concurrency, max\_retries, 2 more }

</summary>

batch\_size: optional number

The maximum number of messages to include in a batch.

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20settings%20%3E%20(property)%20batch_size">Link to this property</a>

max\_concurrency: optional number

Maximum number of concurrent consumers that may consume from this Queue. Set to <code>null</code> to automatically opt in to the platform’s maximum (recommended).

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20settings%20%3E%20(property)%20max_concurrency">Link to this property</a>

max\_retries: optional number

The maximum number of retries

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20settings%20%3E%20(property)%20max_retries">Link to this property</a>

max\_wait\_time\_ms: optional number

The number of milliseconds to wait for a batch to fill up before attempting to deliver it

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20settings%20%3E%20(property)%20max_wait_time_ms">Link to this property</a>

retry\_delay: optional number

The number of seconds to delay before making the message available for another attempt.

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20settings%20%3E%20(property)%20retry_delay">Link to this property</a>

</details>

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20settings">Link to this property</a>

type: optional "worker"

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

HTTPPull object {consumer\_id, created\_on, dead\_letter\_queue, 3 more }

</summary>

consumer\_id: optional string

A Resource identifier.

maxLength32

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20consumer_id">Link to this property</a>

created\_on: optional string

formatdate-time

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20created_on">Link to this property</a>

dead\_letter\_queue: optional string

Name of the dead letter queue, or empty string if not configured

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20dead_letter_queue">Link to this property</a>

queue\_name: optional string

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20queue_name">Link to this property</a>

<details>

<summary>

settings: optional object {batch\_size, max\_retries, retry\_delay, visibility\_timeout\_ms }

</summary>

batch\_size: optional number

The maximum number of messages to include in a batch.

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20settings%20%3E%20(property)%20batch_size">Link to this property</a>

max\_retries: optional number

The maximum number of retries

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20settings%20%3E%20(property)%20max_retries">Link to this property</a>

retry\_delay: optional number

The number of seconds to delay before making the message available for another attempt.

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20settings%20%3E%20(property)%20retry_delay">Link to this property</a>

visibility\_timeout\_ms: optional number

The number of milliseconds that a message is exclusively leased. After the timeout, the message becomes available for another attempt.

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20settings%20%3E%20(property)%20visibility_timeout_ms">Link to this property</a>

</details>

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20settings">Link to this property</a>

type: optional "http\_pull"

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20queues%20%3E%20(model)%20queue%20%3E%20(schema)%20%3E%20(property)%20consumers">Link to this property</a>

consumers\_total\_count: optional number

<a href="#(resource)%20queues%20%3E%20(model)%20queue%20%3E%20(schema)%20%3E%20(property)%20consumers_total_count">Link to this property</a>

created\_on: optional string

<a href="#(resource)%20queues%20%3E%20(model)%20queue%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

<details>

<summary>

jurisdiction: optional "eu"or "us"or "fedramp"

</summary>

One of the following:

"eu"

<a href="#(resource)%20queues%20%3E%20(model)%20queue%20%3E%20(schema)%20%3E%20(property)%20jurisdiction%20%3E%20(member)%200">Link to this property</a>

"us"

<a href="#(resource)%20queues%20%3E%20(model)%20queue%20%3E%20(schema)%20%3E%20(property)%20jurisdiction%20%3E%20(member)%201">Link to this property</a>

"fedramp"

<a href="#(resource)%20queues%20%3E%20(model)%20queue%20%3E%20(schema)%20%3E%20(property)%20jurisdiction%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20queues%20%3E%20(model)%20queue%20%3E%20(schema)%20%3E%20(property)%20jurisdiction">Link to this property</a>

modified\_on: optional string

<a href="#(resource)%20queues%20%3E%20(model)%20queue%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

<details>

<summary>

producers: optional array of object {script, type } or object {bucket\_name, type }

</summary>

One of the following:

<details>

<summary>

MqWorkerProducer object {script, type }

</summary>

script: optional string

<a href="#(resource)%20queues%20%3E%20(model)%20queue%20%3E%20(schema)%20%3E%20(property)%20producers%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20script">Link to this property</a>

type: optional "worker"

<a href="#(resource)%20queues%20%3E%20(model)%20queue%20%3E%20(schema)%20%3E%20(property)%20producers%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues%20%3E%20(model)%20queue%20%3E%20(schema)%20%3E%20(property)%20producers%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

MqR2Producer object {bucket\_name, type }

</summary>

bucket\_name: optional string

<a href="#(resource)%20queues%20%3E%20(model)%20queue%20%3E%20(schema)%20%3E%20(property)%20producers%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20bucket_name">Link to this property</a>

type: optional "r2\_bucket"

<a href="#(resource)%20queues%20%3E%20(model)%20queue%20%3E%20(schema)%20%3E%20(property)%20producers%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues%20%3E%20(model)%20queue%20%3E%20(schema)%20%3E%20(property)%20producers%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20queues%20%3E%20(model)%20queue%20%3E%20(schema)%20%3E%20(property)%20producers">Link to this property</a>

producers\_total\_count: optional number

<a href="#(resource)%20queues%20%3E%20(model)%20queue%20%3E%20(schema)%20%3E%20(property)%20producers_total_count">Link to this property</a>

queue\_id: optional string

<a href="#(resource)%20queues%20%3E%20(model)%20queue%20%3E%20(schema)%20%3E%20(property)%20queue_id">Link to this property</a>

queue\_name: optional string

<a href="#(resource)%20queues%20%3E%20(model)%20queue%20%3E%20(schema)%20%3E%20(property)%20queue_name">Link to this property</a>

<details>

<summary>

settings: optional object {delivery\_delay, delivery\_paused, message\_retention\_period }

</summary>

delivery\_delay: optional number

Number of seconds to delay delivery of all messages to consumers.

<a href="#(resource)%20queues%20%3E%20(model)%20queue%20%3E%20(schema)%20%3E%20(property)%20settings%20%3E%20(property)%20delivery_delay">Link to this property</a>

delivery\_paused: optional boolean

Indicates if message delivery to consumers is currently paused.

<a href="#(resource)%20queues%20%3E%20(model)%20queue%20%3E%20(schema)%20%3E%20(property)%20settings%20%3E%20(property)%20delivery_paused">Link to this property</a>

message\_retention\_period: optional number

Number of seconds after which an unconsumed message will be delayed.

<a href="#(resource)%20queues%20%3E%20(model)%20queue%20%3E%20(schema)%20%3E%20(property)%20settings%20%3E%20(property)%20message_retention_period">Link to this property</a>

</details>

<a href="#(resource)%20queues%20%3E%20(model)%20queue%20%3E%20(schema)%20%3E%20(property)%20settings">Link to this property</a>

</details>

[Link to this property](<#(resource)%20queues%20%3E%20(model)%20queue%20%3E%20(schema)>)

<details>

<summary>

QueueGetMetricsResponse object {backlog\_bytes, backlog\_count, oldest\_message\_timestamp\_ms }

Best-effort metrics for the queue. Values may be approximate due to the distributed nature of queues.

</summary>

backlog\_bytes: number

The size in bytes of unacknowledged messages in the queue.

<a href="#(resource)%20queues%20%3E%20(model)%20queue_get_metrics_response%20%3E%20(schema)%20%3E%20(property)%20backlog_bytes">Link to this property</a>

backlog\_count: number

The number of unacknowledged messages in the queue.

<a href="#(resource)%20queues%20%3E%20(model)%20queue_get_metrics_response%20%3E%20(schema)%20%3E%20(property)%20backlog_count">Link to this property</a>

oldest\_message\_timestamp\_ms: number

Unix timestamp in milliseconds of the oldest unacknowledged message in the queue. Returns 0 if unknown.

<a href="#(resource)%20queues%20%3E%20(model)%20queue_get_metrics_response%20%3E%20(schema)%20%3E%20(property)%20oldest_message_timestamp_ms">Link to this property</a>

</details>

[Link to this property](<#(resource)%20queues%20%3E%20(model)%20queue_get_metrics_response%20%3E%20(schema)>)

<details>

<summary>

QueueDeleteResponse object {errors, messages, success }

</summary>

<details>

<summary>

errors: optional array of <a href="https://developers.cloudflare.com/api/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_info%20%3E%20(schema)">ResponseInfo</a> { code, message, documentation\_url, source }

minLength1

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

<a href="#(resource)%20queues%20%3E%20(model)%20queue_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

messages: optional array of string

<a href="#(resource)%20queues%20%3E%20(model)%20queue_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages">Link to this property</a>

success: optional true

Indicates if the API call was successful or not.

<a href="#(resource)%20queues%20%3E%20(model)%20queue_delete_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20queues%20%3E%20(model)%20queue_delete_response%20%3E%20(schema)>)

#### QueuesMessages

##### [Push Message](https://developers.cloudflare.com/api/resources/queues/subresources/messages/methods/push)

POST/accounts/{account\_id}/queues/{queue\_id}/messages

##### [Acknowledge + Retry Queue Messages](https://developers.cloudflare.com/api/resources/queues/subresources/messages/methods/ack)

POST/accounts/{account\_id}/queues/{queue\_id}/messages/ack

##### [Pull Queue Messages](https://developers.cloudflare.com/api/resources/queues/subresources/messages/methods/pull)

POST/accounts/{account\_id}/queues/{queue\_id}/messages/pull

##### [Push Message Batch](https://developers.cloudflare.com/api/resources/queues/subresources/messages/methods/bulk_push)

POST/accounts/{account\_id}/queues/{queue\_id}/messages/batch

##### [Peek Queue Messages](https://developers.cloudflare.com/api/resources/queues/subresources/messages/methods/peek)

POST/accounts/{account\_id}/queues/{queue\_id}/messages/peek

##### [Purge Peeked Queue Messages](https://developers.cloudflare.com/api/resources/queues/subresources/messages/methods/purge)

POST/accounts/{account\_id}/queues/{queue\_id}/messages/purge

##### ModelsExpand Collapse

<details>

<summary>

MessagePushResponse object {metadata }

</summary>

<details>

<summary>

metadata: optional object {metrics }

</summary>

<details>

<summary>

metrics: optional object {backlog\_bytes, backlog\_count, oldest\_message\_timestamp\_ms }

Best-effort metrics for the queue. Values may be approximate due to the distributed nature of queues.

</summary>

backlog\_bytes: number

The size in bytes of unacknowledged messages in the queue.

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_push_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20metrics%20%3E%20(property)%20backlog_bytes">Link to this property</a>

backlog\_count: number

The number of unacknowledged messages in the queue.

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_push_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20metrics%20%3E%20(property)%20backlog_count">Link to this property</a>

oldest\_message\_timestamp\_ms: number

Unix timestamp in milliseconds of the oldest unacknowledged message in the queue. Returns 0 if unknown.

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_push_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20metrics%20%3E%20(property)%20oldest_message_timestamp_ms">Link to this property</a>

</details>

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_push_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20metrics">Link to this property</a>

</details>

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_push_response%20%3E%20(schema)%20%3E%20(property)%20metadata">Link to this property</a>

</details>

[Link to this property](<#(resource)%20queues.messages%20%3E%20(model)%20message_push_response%20%3E%20(schema)>)

<details>

<summary>

MessageAckResponse object {ackCount, retryCount, warnings }

</summary>

ackCount: optional number

The number of messages that were succesfully acknowledged.

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_ack_response%20%3E%20(schema)%20%3E%20(property)%20ackCount">Link to this property</a>

retryCount: optional number

The number of messages that were succesfully retried.

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_ack_response%20%3E%20(schema)%20%3E%20(property)%20retryCount">Link to this property</a>

warnings: optional map\[string]

Map of lease IDs to warning messages encountered during acknowledgement.

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_ack_response%20%3E%20(schema)%20%3E%20(property)%20warnings">Link to this property</a>

</details>

[Link to this property](<#(resource)%20queues.messages%20%3E%20(model)%20message_ack_response%20%3E%20(schema)>)

<details>

<summary>

MessagePullResponse object {message\_backlog\_count, messages, metadata }

</summary>

message\_backlog\_count: optional number

The number of unacknowledged messages in the queue.

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_pull_response%20%3E%20(schema)%20%3E%20(property)%20message_backlog_count">Link to this property</a>

<details>

<summary>

messages: optional array of object {id, attempts, body, 3 more }

</summary>

id: optional string

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_pull_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

attempts: optional number

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_pull_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20attempts">Link to this property</a>

body: optional string

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_pull_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20body">Link to this property</a>

lease\_id: optional string

An ID that represents an “in-flight” message that has been pulled from a Queue. You must hold on to this ID and use it to acknowledge this message.

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_pull_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20lease_id">Link to this property</a>

metadata: optional unknown

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_pull_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20metadata">Link to this property</a>

timestamp\_ms: optional number

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_pull_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20timestamp_ms">Link to this property</a>

</details>

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_pull_response%20%3E%20(schema)%20%3E%20(property)%20messages">Link to this property</a>

<details>

<summary>

metadata: optional object {metrics }

</summary>

<details>

<summary>

metrics: optional object {backlog\_bytes, backlog\_count, oldest\_message\_timestamp\_ms }

Best-effort metrics for the queue. Values may be approximate due to the distributed nature of queues.

</summary>

backlog\_bytes: number

The size in bytes of unacknowledged messages in the queue.

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_pull_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20metrics%20%3E%20(property)%20backlog_bytes">Link to this property</a>

backlog\_count: number

The number of unacknowledged messages in the queue.

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_pull_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20metrics%20%3E%20(property)%20backlog_count">Link to this property</a>

oldest\_message\_timestamp\_ms: number

Unix timestamp in milliseconds of the oldest unacknowledged message in the queue. Returns 0 if unknown.

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_pull_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20metrics%20%3E%20(property)%20oldest_message_timestamp_ms">Link to this property</a>

</details>

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_pull_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20metrics">Link to this property</a>

</details>

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_pull_response%20%3E%20(schema)%20%3E%20(property)%20metadata">Link to this property</a>

</details>

[Link to this property](<#(resource)%20queues.messages%20%3E%20(model)%20message_pull_response%20%3E%20(schema)>)

<details>

<summary>

MessageBulkPushResponse object {metadata }

</summary>

<details>

<summary>

metadata: optional object {metrics }

</summary>

<details>

<summary>

metrics: optional object {backlog\_bytes, backlog\_count, oldest\_message\_timestamp\_ms }

Best-effort metrics for the queue. Values may be approximate due to the distributed nature of queues.

</summary>

backlog\_bytes: number

The size in bytes of unacknowledged messages in the queue.

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_bulk_push_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20metrics%20%3E%20(property)%20backlog_bytes">Link to this property</a>

backlog\_count: number

The number of unacknowledged messages in the queue.

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_bulk_push_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20metrics%20%3E%20(property)%20backlog_count">Link to this property</a>

oldest\_message\_timestamp\_ms: number

Unix timestamp in milliseconds of the oldest unacknowledged message in the queue. Returns 0 if unknown.

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_bulk_push_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20metrics%20%3E%20(property)%20oldest_message_timestamp_ms">Link to this property</a>

</details>

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_bulk_push_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20metrics">Link to this property</a>

</details>

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_bulk_push_response%20%3E%20(schema)%20%3E%20(property)%20metadata">Link to this property</a>

</details>

[Link to this property](<#(resource)%20queues.messages%20%3E%20(model)%20message_bulk_push_response%20%3E%20(schema)>)

<details>

<summary>

MessagePeekResponse object {messages }

</summary>

<details>

<summary>

messages: optional array of object {id, attempts, body, 3 more }

</summary>

id: optional string

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_peek_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

attempts: optional number

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_peek_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20attempts">Link to this property</a>

body: optional string

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_peek_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20body">Link to this property</a>

metadata: optional unknown

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_peek_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20metadata">Link to this property</a>

ref: optional string

An opaque reference to a peeked message. You must hold on to this value and use it to purge the message.

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_peek_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20ref">Link to this property</a>

timestamp\_ms: optional number

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_peek_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20timestamp_ms">Link to this property</a>

</details>

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_peek_response%20%3E%20(schema)%20%3E%20(property)%20messages">Link to this property</a>

</details>

[Link to this property](<#(resource)%20queues.messages%20%3E%20(model)%20message_peek_response%20%3E%20(schema)>)

<details>

<summary>

MessagePurgeResponse object {errors, warnings }

</summary>

<details>

<summary>

errors: optional array of object {message }

Errors encountered while purging messages.

</summary>

message: optional string

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_purge_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

</details>

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_purge_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

warnings: optional map\[string]

Map of refs to warning messages encountered during purge.

<a href="#(resource)%20queues.messages%20%3E%20(model)%20message_purge_response%20%3E%20(schema)%20%3E%20(property)%20warnings">Link to this property</a>

</details>

[Link to this property](<#(resource)%20queues.messages%20%3E%20(model)%20message_purge_response%20%3E%20(schema)>)

#### QueuesPurge

##### [Get Queue Purge Status](https://developers.cloudflare.com/api/resources/queues/subresources/purge/methods/status)

GET/accounts/{account\_id}/queues/{queue\_id}/purge

##### [Purge Queue](https://developers.cloudflare.com/api/resources/queues/subresources/purge/methods/start)

POST/accounts/{account\_id}/queues/{queue\_id}/purge

##### ModelsExpand Collapse

<details>

<summary>

PurgeStatusResponse object {completed, started\_at }

</summary>

completed: optional string

Indicates if the last purge operation completed successfully.

<a href="#(resource)%20queues.purge%20%3E%20(model)%20purge_status_response%20%3E%20(schema)%20%3E%20(property)%20completed">Link to this property</a>

started\_at: optional string

Timestamp when the last purge operation started.

<a href="#(resource)%20queues.purge%20%3E%20(model)%20purge_status_response%20%3E%20(schema)%20%3E%20(property)%20started_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20queues.purge%20%3E%20(model)%20purge_status_response%20%3E%20(schema)>)

#### QueuesConsumers

##### [List Queue Consumers](https://developers.cloudflare.com/api/resources/queues/subresources/consumers/methods/list)

GET/accounts/{account\_id}/queues/{queue\_id}/consumers

##### [Get Queue Consumer](https://developers.cloudflare.com/api/resources/queues/subresources/consumers/methods/get)

GET/accounts/{account\_id}/queues/{queue\_id}/consumers/{consumer\_id}

##### [Create a Queue Consumer](https://developers.cloudflare.com/api/resources/queues/subresources/consumers/methods/create)

POST/accounts/{account\_id}/queues/{queue\_id}/consumers

##### [Update Queue Consumer](https://developers.cloudflare.com/api/resources/queues/subresources/consumers/methods/update)

PUT/accounts/{account\_id}/queues/{queue\_id}/consumers/{consumer\_id}

##### [Delete Queue Consumer](https://developers.cloudflare.com/api/resources/queues/subresources/consumers/methods/delete)

DELETE/accounts/{account\_id}/queues/{queue\_id}/consumers/{consumer\_id}

##### ModelsExpand Collapse

<details>

<summary>

Consumer = object {consumer\_id, created\_on, dead\_letter\_queue, 4 more } or object {consumer\_id, created\_on, dead\_letter\_queue, 3 more }

Response body representing a consumer

</summary>

One of the following:

<details>

<summary>

Worker object {consumer\_id, created\_on, dead\_letter\_queue, 4 more }

</summary>

consumer\_id: optional string

A Resource identifier.

maxLength32

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20consumer_id">Link to this property</a>

created\_on: optional string

formatdate-time

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20created_on">Link to this property</a>

dead\_letter\_queue: optional string

Name of the dead letter queue, or empty string if not configured

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20dead_letter_queue">Link to this property</a>

queue\_name: optional string

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20queue_name">Link to this property</a>

script\_name: optional string

Name of a Worker

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20script_name">Link to this property</a>

<details>

<summary>

settings: optional object {batch\_size, max\_concurrency, max\_retries, 2 more }

</summary>

batch\_size: optional number

The maximum number of messages to include in a batch.

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20settings%20%3E%20(property)%20batch_size">Link to this property</a>

max\_concurrency: optional number

Maximum number of concurrent consumers that may consume from this Queue. Set to <code>null</code> to automatically opt in to the platform’s maximum (recommended).

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20settings%20%3E%20(property)%20max_concurrency">Link to this property</a>

max\_retries: optional number

The maximum number of retries

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20settings%20%3E%20(property)%20max_retries">Link to this property</a>

max\_wait\_time\_ms: optional number

The number of milliseconds to wait for a batch to fill up before attempting to deliver it

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20settings%20%3E%20(property)%20max_wait_time_ms">Link to this property</a>

retry\_delay: optional number

The number of seconds to delay before making the message available for another attempt.

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20settings%20%3E%20(property)%20retry_delay">Link to this property</a>

</details>

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20settings">Link to this property</a>

type: optional "worker"

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

HTTPPull object {consumer\_id, created\_on, dead\_letter\_queue, 3 more }

</summary>

consumer\_id: optional string

A Resource identifier.

maxLength32

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20consumer_id">Link to this property</a>

created\_on: optional string

formatdate-time

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20created_on">Link to this property</a>

dead\_letter\_queue: optional string

Name of the dead letter queue, or empty string if not configured

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20dead_letter_queue">Link to this property</a>

queue\_name: optional string

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20queue_name">Link to this property</a>

<details>

<summary>

settings: optional object {batch\_size, max\_retries, retry\_delay, visibility\_timeout\_ms }

</summary>

batch\_size: optional number

The maximum number of messages to include in a batch.

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20settings%20%3E%20(property)%20batch_size">Link to this property</a>

max\_retries: optional number

The maximum number of retries

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20settings%20%3E%20(property)%20max_retries">Link to this property</a>

retry\_delay: optional number

The number of seconds to delay before making the message available for another attempt.

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20settings%20%3E%20(property)%20retry_delay">Link to this property</a>

visibility\_timeout\_ms: optional number

The number of milliseconds that a message is exclusively leased. After the timeout, the message becomes available for another attempt.

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20settings%20%3E%20(property)%20visibility_timeout_ms">Link to this property</a>

</details>

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20settings">Link to this property</a>

type: optional "http\_pull"

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20queues.consumers%20%3E%20(model)%20consumer%20%3E%20(schema)>)

<details>

<summary>

ConsumerDeleteResponse object {errors, messages, success }

</summary>

<details>

<summary>

errors: optional array of <a href="https://developers.cloudflare.com/api/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_info%20%3E%20(schema)">ResponseInfo</a> { code, message, documentation\_url, source }

minLength1

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

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

messages: optional array of string

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages">Link to this property</a>

success: optional true

Indicates if the API call was successful or not.

<a href="#(resource)%20queues.consumers%20%3E%20(model)%20consumer_delete_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20queues.consumers%20%3E%20(model)%20consumer_delete_response%20%3E%20(schema)>)

#### QueuesSubscriptions

##### [List Event Subscriptions](https://developers.cloudflare.com/api/resources/queues/subresources/subscriptions/methods/list)

GET/accounts/{account\_id}/event\_subscriptions/subscriptions

##### [Get Event Subscription](https://developers.cloudflare.com/api/resources/queues/subresources/subscriptions/methods/get)

GET/accounts/{account\_id}/event\_subscriptions/subscriptions/{subscription\_id}

##### [Create Event Subscription](https://developers.cloudflare.com/api/resources/queues/subresources/subscriptions/methods/create)

POST/accounts/{account\_id}/event\_subscriptions/subscriptions

##### [Update Event Subscription](https://developers.cloudflare.com/api/resources/queues/subresources/subscriptions/methods/update)

PATCH/accounts/{account\_id}/event\_subscriptions/subscriptions/{subscription\_id}

##### [Delete Event Subscription](https://developers.cloudflare.com/api/resources/queues/subresources/subscriptions/methods/delete)

DELETE/accounts/{account\_id}/event\_subscriptions/subscriptions/{subscription\_id}

##### ModelsExpand Collapse

<details>

<summary>

SubscriptionListResponse object {id, created\_at, destination, 5 more }

</summary>

id: string

Unique identifier for the subscription

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

When the subscription was created

formatdate-time

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

destination: object {queue\_id, type }

Destination configuration for the subscription

</summary>

queue\_id: string

ID of the target queue

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20destination%20%3E%20(property)%20queue_id">Link to this property</a>

type: "queues.queue"

Type of destination

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20destination%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20destination">Link to this property</a>

enabled: boolean

Whether the subscription is active

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

events: array of string

List of event types this subscription handles

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20events">Link to this property</a>

modified\_at: string

When the subscription was last modified

formatdate-time

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

Name of the subscription

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

source: object {type } or object {type } or object {type } or 6 more

Source configuration for the subscription

</summary>

One of the following:

<details>

<summary>

MqEventSourceImages object {type }

</summary>

type: optional "images"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

MqEventSourceKV object {type }

</summary>

type: optional "kv"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

MqEventSourceR2 object {type }

</summary>

type: optional "r2"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

MqEventSourceSuperSlurper object {type }

</summary>

type: optional "superSlurper"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

MqEventSourceVectorize object {type }

</summary>

type: optional "vectorize"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

MqEventSourceWorkersAIModel object {model\_name, type }

</summary>

model\_name: optional string

Name of the Workers AI model

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%205%20%3E%20(property)%20model_name">Link to this property</a>

type: optional "workersAi.model"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%205">Link to this property</a>

<details>

<summary>

MqEventSourceWorkersBuildsWorker object {type, worker\_name }

</summary>

type: optional "workersBuilds.worker"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%206%20%3E%20(property)%20type">Link to this property</a>

worker\_name: optional string

Name of the worker

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%206%20%3E%20(property)%20worker_name">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%206">Link to this property</a>

<details>

<summary>

MqEventSourceWorkersScript object {script\_tag, type }

</summary>

script\_tag: optional string

Tag of the Worker script

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%207%20%3E%20(property)%20script_tag">Link to this property</a>

type: optional "workers.script"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%207%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%207">Link to this property</a>

<details>

<summary>

MqEventSourceWorkflowsWorkflow object {type, workflow\_name }

</summary>

type: optional "workflows.workflow"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%208%20%3E%20(property)%20type">Link to this property</a>

workflow\_name: optional string

Name of the workflow

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%208%20%3E%20(property)%20workflow_name">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%208">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

</details>

[Link to this property](<#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_list_response%20%3E%20(schema)>)

<details>

<summary>

SubscriptionGetResponse object {id, created\_at, destination, 5 more }

</summary>

id: string

Unique identifier for the subscription

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

When the subscription was created

formatdate-time

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

destination: object {queue\_id, type }

Destination configuration for the subscription

</summary>

queue\_id: string

ID of the target queue

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20destination%20%3E%20(property)%20queue_id">Link to this property</a>

type: "queues.queue"

Type of destination

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20destination%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20destination">Link to this property</a>

enabled: boolean

Whether the subscription is active

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

events: array of string

List of event types this subscription handles

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20events">Link to this property</a>

modified\_at: string

When the subscription was last modified

formatdate-time

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

Name of the subscription

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

source: object {type } or object {type } or object {type } or 6 more

Source configuration for the subscription

</summary>

One of the following:

<details>

<summary>

MqEventSourceImages object {type }

</summary>

type: optional "images"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

MqEventSourceKV object {type }

</summary>

type: optional "kv"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

MqEventSourceR2 object {type }

</summary>

type: optional "r2"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

MqEventSourceSuperSlurper object {type }

</summary>

type: optional "superSlurper"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

MqEventSourceVectorize object {type }

</summary>

type: optional "vectorize"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

MqEventSourceWorkersAIModel object {model\_name, type }

</summary>

model\_name: optional string

Name of the Workers AI model

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%205%20%3E%20(property)%20model_name">Link to this property</a>

type: optional "workersAi.model"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%205">Link to this property</a>

<details>

<summary>

MqEventSourceWorkersBuildsWorker object {type, worker\_name }

</summary>

type: optional "workersBuilds.worker"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%206%20%3E%20(property)%20type">Link to this property</a>

worker\_name: optional string

Name of the worker

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%206%20%3E%20(property)%20worker_name">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%206">Link to this property</a>

<details>

<summary>

MqEventSourceWorkersScript object {script\_tag, type }

</summary>

script\_tag: optional string

Tag of the Worker script

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%207%20%3E%20(property)%20script_tag">Link to this property</a>

type: optional "workers.script"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%207%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%207">Link to this property</a>

<details>

<summary>

MqEventSourceWorkflowsWorkflow object {type, workflow\_name }

</summary>

type: optional "workflows.workflow"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%208%20%3E%20(property)%20type">Link to this property</a>

workflow\_name: optional string

Name of the workflow

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%208%20%3E%20(property)%20workflow_name">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%208">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

</details>

[Link to this property](<#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_get_response%20%3E%20(schema)>)

<details>

<summary>

SubscriptionCreateResponse object {id, created\_at, destination, 5 more }

</summary>

id: string

Unique identifier for the subscription

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

When the subscription was created

formatdate-time

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

destination: object {queue\_id, type }

Destination configuration for the subscription

</summary>

queue\_id: string

ID of the target queue

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20destination%20%3E%20(property)%20queue_id">Link to this property</a>

type: "queues.queue"

Type of destination

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20destination%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20destination">Link to this property</a>

enabled: boolean

Whether the subscription is active

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

events: array of string

List of event types this subscription handles

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20events">Link to this property</a>

modified\_at: string

When the subscription was last modified

formatdate-time

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

Name of the subscription

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

source: object {type } or object {type } or object {type } or 6 more

Source configuration for the subscription

</summary>

One of the following:

<details>

<summary>

MqEventSourceImages object {type }

</summary>

type: optional "images"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

MqEventSourceKV object {type }

</summary>

type: optional "kv"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

MqEventSourceR2 object {type }

</summary>

type: optional "r2"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

MqEventSourceSuperSlurper object {type }

</summary>

type: optional "superSlurper"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

MqEventSourceVectorize object {type }

</summary>

type: optional "vectorize"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

MqEventSourceWorkersAIModel object {model\_name, type }

</summary>

model\_name: optional string

Name of the Workers AI model

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%205%20%3E%20(property)%20model_name">Link to this property</a>

type: optional "workersAi.model"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%205">Link to this property</a>

<details>

<summary>

MqEventSourceWorkersBuildsWorker object {type, worker\_name }

</summary>

type: optional "workersBuilds.worker"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%206%20%3E%20(property)%20type">Link to this property</a>

worker\_name: optional string

Name of the worker

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%206%20%3E%20(property)%20worker_name">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%206">Link to this property</a>

<details>

<summary>

MqEventSourceWorkersScript object {script\_tag, type }

</summary>

script\_tag: optional string

Tag of the Worker script

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%207%20%3E%20(property)%20script_tag">Link to this property</a>

type: optional "workers.script"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%207%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%207">Link to this property</a>

<details>

<summary>

MqEventSourceWorkflowsWorkflow object {type, workflow\_name }

</summary>

type: optional "workflows.workflow"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%208%20%3E%20(property)%20type">Link to this property</a>

workflow\_name: optional string

Name of the workflow

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%208%20%3E%20(property)%20workflow_name">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%208">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

</details>

[Link to this property](<#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_create_response%20%3E%20(schema)>)

<details>

<summary>

SubscriptionUpdateResponse object {id, created\_at, destination, 5 more }

</summary>

id: string

Unique identifier for the subscription

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

When the subscription was created

formatdate-time

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

destination: object {queue\_id, type }

Destination configuration for the subscription

</summary>

queue\_id: string

ID of the target queue

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20destination%20%3E%20(property)%20queue_id">Link to this property</a>

type: "queues.queue"

Type of destination

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20destination%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20destination">Link to this property</a>

enabled: boolean

Whether the subscription is active

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

events: array of string

List of event types this subscription handles

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20events">Link to this property</a>

modified\_at: string

When the subscription was last modified

formatdate-time

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

Name of the subscription

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

source: object {type } or object {type } or object {type } or 6 more

Source configuration for the subscription

</summary>

One of the following:

<details>

<summary>

MqEventSourceImages object {type }

</summary>

type: optional "images"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

MqEventSourceKV object {type }

</summary>

type: optional "kv"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

MqEventSourceR2 object {type }

</summary>

type: optional "r2"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

MqEventSourceSuperSlurper object {type }

</summary>

type: optional "superSlurper"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

MqEventSourceVectorize object {type }

</summary>

type: optional "vectorize"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

MqEventSourceWorkersAIModel object {model\_name, type }

</summary>

model\_name: optional string

Name of the Workers AI model

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%205%20%3E%20(property)%20model_name">Link to this property</a>

type: optional "workersAi.model"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%205">Link to this property</a>

<details>

<summary>

MqEventSourceWorkersBuildsWorker object {type, worker\_name }

</summary>

type: optional "workersBuilds.worker"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%206%20%3E%20(property)%20type">Link to this property</a>

worker\_name: optional string

Name of the worker

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%206%20%3E%20(property)%20worker_name">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%206">Link to this property</a>

<details>

<summary>

MqEventSourceWorkersScript object {script\_tag, type }

</summary>

script\_tag: optional string

Tag of the Worker script

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%207%20%3E%20(property)%20script_tag">Link to this property</a>

type: optional "workers.script"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%207%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%207">Link to this property</a>

<details>

<summary>

MqEventSourceWorkflowsWorkflow object {type, workflow\_name }

</summary>

type: optional "workflows.workflow"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%208%20%3E%20(property)%20type">Link to this property</a>

workflow\_name: optional string

Name of the workflow

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%208%20%3E%20(property)%20workflow_name">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%208">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

</details>

[Link to this property](<#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_update_response%20%3E%20(schema)>)

<details>

<summary>

SubscriptionDeleteResponse object {id, created\_at, destination, 5 more }

</summary>

id: string

Unique identifier for the subscription

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

When the subscription was created

formatdate-time

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

destination: object {queue\_id, type }

Destination configuration for the subscription

</summary>

queue\_id: string

ID of the target queue

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20destination%20%3E%20(property)%20queue_id">Link to this property</a>

type: "queues.queue"

Type of destination

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20destination%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20destination">Link to this property</a>

enabled: boolean

Whether the subscription is active

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

events: array of string

List of event types this subscription handles

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20events">Link to this property</a>

modified\_at: string

When the subscription was last modified

formatdate-time

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

name: string

Name of the subscription

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

source: object {type } or object {type } or object {type } or 6 more

Source configuration for the subscription

</summary>

One of the following:

<details>

<summary>

MqEventSourceImages object {type }

</summary>

type: optional "images"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

MqEventSourceKV object {type }

</summary>

type: optional "kv"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

MqEventSourceR2 object {type }

</summary>

type: optional "r2"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

MqEventSourceSuperSlurper object {type }

</summary>

type: optional "superSlurper"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

MqEventSourceVectorize object {type }

</summary>

type: optional "vectorize"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

MqEventSourceWorkersAIModel object {model\_name, type }

</summary>

model\_name: optional string

Name of the Workers AI model

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%205%20%3E%20(property)%20model_name">Link to this property</a>

type: optional "workersAi.model"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%205">Link to this property</a>

<details>

<summary>

MqEventSourceWorkersBuildsWorker object {type, worker\_name }

</summary>

type: optional "workersBuilds.worker"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%206%20%3E%20(property)%20type">Link to this property</a>

worker\_name: optional string

Name of the worker

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%206%20%3E%20(property)%20worker_name">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%206">Link to this property</a>

<details>

<summary>

MqEventSourceWorkersScript object {script\_tag, type }

</summary>

script\_tag: optional string

Tag of the Worker script

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%207%20%3E%20(property)%20script_tag">Link to this property</a>

type: optional "workers.script"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%207%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%207">Link to this property</a>

<details>

<summary>

MqEventSourceWorkflowsWorkflow object {type, workflow\_name }

</summary>

type: optional "workflows.workflow"

Type of source

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%208%20%3E%20(property)%20type">Link to this property</a>

workflow\_name: optional string

Name of the workflow

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%208%20%3E%20(property)%20workflow_name">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(variant)%208">Link to this property</a>

</details>

<a href="#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

</details>

[Link to this property](<#(resource)%20queues.subscriptions%20%3E%20(model)%20subscription_delete_response%20%3E%20(schema)>)