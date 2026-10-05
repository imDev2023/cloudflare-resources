---
title: Scripts
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Workers](https://developers.cloudflare.com/api/resources/workers)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Scripts

##### [List Worker Scripts](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/methods/list)

GET/accounts/{account\_id}/workers/scripts

##### [Search Worker Scripts](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/methods/search)

GET/accounts/{account\_id}/workers/scripts-search

##### [Download Worker Script](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/methods/get)

GET/accounts/{account\_id}/workers/scripts/{script\_name}

##### [Upload Worker Module](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/methods/update)

PUT/accounts/{account\_id}/workers/scripts/{script\_name}

##### [Delete Worker](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/methods/delete)

DELETE/accounts/{account\_id}/workers/scripts/{script\_name}

##### ModelsExpand Collapse

<details>

<summary>

Script object {id, cache\_options, compatibility\_date, 20 more }

</summary>

id: optional string

The name used to identify the script.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

cache\_options: optional object {enabled, cross\_version\_cache }

Global CacheW configuration for the Worker. When caching is on, the platform provisions a <code>cloudflare.app</code> zone for the Worker. A <code>type: worker</code> entry in the <code>exports</code> map can override this value for a single entrypoint.

</summary>

enabled: boolean

Whether caching is enabled for this Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20cache_options%20%3E%20(property)%20enabled">Link to this property</a>

cross\_version\_cache: optional boolean

Whether cached responses are shared across Worker version uploads. This is independent of <code>enabled</code>. It can stay true while caching is off, so the preference survives turning caching off and back on.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20cache_options%20%3E%20(property)%20cross_version_cache">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20cache_options">Link to this property</a>

compatibility\_date: optional string

Date indicating targeted support in the Workers runtime. Backwards incompatible fixes to the runtime following this date will not affect this Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20compatibility_date">Link to this property</a>

compatibility\_flags: optional array of string

Flags that enable or disable certain features in the Workers runtime. Used to enable upcoming features or opt in or out of specific changes not included in a <code>compatibility_date</code>.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20compatibility_flags">Link to this property</a>

created\_on: optional string

When the script was created.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

etag: optional string

Hashed script content, can be used in a If-None-Match header when updating.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20etag">Link to this property</a>

<details>

<summary>

exports: optional map\[object {type, cache, state } or object {storage, type, container, state } or object {state, type } or 3 more]

Declarative exports for the Worker’s most recent version, including Durable Object classes (with their <code>storage</code> backend) and named Worker entrypoints. Tombstoned lifecycle entries are omitted, so only live exports (<code>created</code> and <code>expecting-transfer</code>) are returned.

</summary>

One of the following:

<details>

<summary>

Worker object {type, cache, state }

A named Worker entrypoint export (<code>type: worker</code>). Worker entrypoints are always live (<code>state: created</code>) and carry no storage or lifecycle fields. The optional <code>cache</code> block overrides the Worker’s global <code>cache_options.enabled</code> for this entrypoint.

</summary>

type: "worker"

Marks this entry as a Worker entrypoint export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

cache: optional object {enabled }

Cache override for this entrypoint. Overrides the Worker’s global <code>cache_options.enabled</code> for this entrypoint only.

</summary>

enabled: boolean

Whether caching is enabled for this entrypoint.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20cache%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20cache">Link to this property</a>

state: optional "created"

Live export. May be omitted; defaults to <code>created</code>.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20state">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

WorkersDurableObjectExport object {storage, type, container, state }

A live Durable Object export (<code>state: created</code>, the default). The platform auto-provisions the namespace on first deploy, matches it on subsequent deploys, and never mutates or deletes it as a side effect of a code-only change. <code>storage</code> is required; <code>renamed_to</code>, <code>transferred_to</code> and <code>transfer_from</code> are not allowed on a live entry.

</summary>

<details>

<summary>

storage: "sqlite"or "legacy-kv"

Durable Object storage backend. <code>sqlite</code> is the recommended (and only) backend for new namespaces. <code>legacy-kv</code> is accepted only for a class whose namespace already exists as KV-backed; the <code>exports</code> flow never provisions a new <code>legacy-kv</code> namespace.

</summary>

One of the following:

"sqlite"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20storage%20%3E%20(member)%200">Link to this property</a>

"legacy-kv"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20storage%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20storage">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

container: optional string

Name of the container (declared in the upload’s <code>metadata.containers</code>) that backs this Durable Object. When set, the namespace is container-enabled. Valid only on live entries.

maxLength128

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20container">Link to this property</a>

state: optional "created"

Live export. May be omitted; defaults to <code>created</code>.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20state">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

WorkersDurableObjectDeletedExport object {state, type }

A <code>deleted</code> tombstone: retires the provisioned namespace for this class and all of its data. The class must be absent from the uploaded code and no other Worker in the account may bind to the namespace, otherwise the deploy is rejected. No other fields are allowed. Deletion is irreversible.

</summary>

state: "deleted"

Tombstone that deletes the namespace.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20state">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

WorkersDurableObjectRenamedExport object {renamed\_to, state, type }

A <code>renamed</code> tombstone: rewrites the provisioned namespace’s class name from this map key to <code>renamed_to</code>. The source class may stay in code during the rollout window (an info notice is emitted). <code>storage</code>, <code>transferred_to</code> and <code>transfer_from</code> are not allowed.

</summary>

renamed\_to: string

The destination class name. Must differ from the source class (the map key) and must be declared as a live (<code>created</code>) entry in the same <code>exports</code> map. Write-only: never present in GET responses.

maxLength128

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20renamed_to">Link to this property</a>

state: "renamed"

Tombstone that renames the namespace’s class.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20state">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

WorkersDurableObjectTransferredExport object {state, transferred\_to, type }

A <code>transferred</code> tombstone (source side of a two-phase transfer): hands ownership of the provisioned namespace to another script in the same account, named by <code>transferred_to</code>. The target must have already deployed a matching <code>expecting-transfer</code> entry. The source class may stay in code during the rollout window (an info notice is emitted). <code>storage</code>, <code>renamed_to</code> and <code>transfer_from</code> are not allowed.

</summary>

state: "transferred"

Tombstone that transfers the namespace to another script.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20state">Link to this property</a>

transferred\_to: string

The destination script name. Must be in the same account and the same dispatch-namespace context (or both non-dispatch). Cross-dispatch-namespace transfers are rejected. Write-only: never present in GET responses.

maxLength128

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20transferred_to">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

WorkersDurableObjectExpectingTransferExport object {state, storage, transfer\_from, 2 more }

The target side of a two-phase transfer (<code>state: expecting-transfer</code>). Declares that this script expects to receive a namespace for this class from the <code>transfer_from</code> script. This is a live entry, not a tombstone: bindings resolve through the source’s namespace until the source commits with a <code>transferred</code> tombstone. <code>storage</code> and <code>transfer_from</code> are required; <code>renamed_to</code> and <code>transferred_to</code> are not allowed.

</summary>

state: "expecting-transfer"

Target side of a two-phase transfer.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20state">Link to this property</a>

<details>

<summary>

storage: "sqlite"or "legacy-kv"

Durable Object storage backend. <code>sqlite</code> is the recommended (and only) backend for new namespaces. <code>legacy-kv</code> is accepted only for a class whose namespace already exists as KV-backed; the <code>exports</code> flow never provisions a new <code>legacy-kv</code> namespace.

</summary>

One of the following:

"sqlite"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20storage%20%3E%20(member)%200">Link to this property</a>

"legacy-kv"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20storage%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20storage">Link to this property</a>

transfer\_from: string

The source script name to receive the namespace from. Must be in the same account and dispatch-namespace context. Present on reads for <code>expecting-transfer</code> entries.

maxLength128

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20transfer_from">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

container: optional string

Name of the container (declared in the upload’s <code>metadata.containers</code>) that backs this Durable Object once the transfer settles. Valid only on live entries.

maxLength128

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20container">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20exports">Link to this property</a>

handlers: optional array of string

The names of handlers exported as part of the default export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20handlers">Link to this property</a>

has\_assets: optional boolean

Whether a Worker contains assets.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20has_assets">Link to this property</a>

has\_modules: optional boolean

Whether a Worker contains modules.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20has_modules">Link to this property</a>

last\_deployed\_from: optional string

The client most recently used to deploy this Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20last_deployed_from">Link to this property</a>

logpush: optional boolean

Whether Logpush is turned on for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20logpush">Link to this property</a>

migration\_tag: optional string

The tag of the Durable Object migration that was most recently applied for this Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20migration_tag">Link to this property</a>

modified\_on: optional string

When the script was last modified.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

<details>

<summary>

named\_handlers: optional array of object {handlers, name }

Named exports, such as Durable Object class implementations and named entrypoints.

</summary>

handlers: optional array of string

The names of handlers exported as part of the named export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20named_handlers%20%3E%20(items)%20%3E%20(property)%20handlers">Link to this property</a>

name: optional string

The name of the export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20named_handlers%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20named_handlers">Link to this property</a>

<details>

<summary>

observability: optional object {enabled, head\_sampling\_rate, issues, 3 more }

Observability settings for the Worker.

</summary>

enabled: boolean

Whether observability is enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20enabled">Link to this property</a>

head\_sampling\_rate: optional number

The sampling rate for incoming requests. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20head_sampling_rate">Link to this property</a>

<details>

<summary>

issues: optional object {enabled }

Real-time Issues settings for the Worker.

</summary>

enabled: optional boolean

Whether real-time Issues are enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20issues%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20issues">Link to this property</a>

<details>

<summary>

logs: optional object {enabled, invocation\_logs, destinations, 2 more }

Log settings for the Worker.

</summary>

enabled: boolean

Whether logs are enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20enabled">Link to this property</a>

invocation\_logs: boolean

Whether <a href="https://developers.cloudflare.com/workers/observability/logs/workers-logs/#invocation-logs">invocation logs</a> are enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20invocation_logs">Link to this property</a>

destinations: optional array of string

A list of destinations where logs will be exported to.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20destinations">Link to this property</a>

head\_sampling\_rate: optional number

The sampling rate for logs. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20head_sampling_rate">Link to this property</a>

persist: optional boolean

Whether log persistence is enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20persist">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs">Link to this property</a>

redact\_query\_string: optional boolean

Whether query strings are removed from request URLs in logs and traces.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20redact_query_string">Link to this property</a>

<details>

<summary>

traces: optional object {destinations, enabled, head\_sampling\_rate, 2 more }

Trace settings for the Worker.

</summary>

destinations: optional array of string

A list of destinations where traces will be exported to.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20destinations">Link to this property</a>

enabled: optional boolean

Whether traces are enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20enabled">Link to this property</a>

head\_sampling\_rate: optional number

The sampling rate for traces. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20head_sampling_rate">Link to this property</a>

persist: optional boolean

Whether trace persistence is enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20persist">Link to this property</a>

<details>

<summary>

propagation\_policy: optional "authenticated"or "accept"

Controls how inbound trace context (traceparent/tracestate) headers on incoming requests are handled. “authenticated” honors inbound trace context only when accompanied by a valid trace auth token. “accept” unconditionally accepts inbound trace context. Requires the trace propagation feature to be enabled. Returns null when the trace propagation feature is not enabled for the account.

</summary>

One of the following:

"authenticated"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20propagation_policy%20%3E%20(member)%200">Link to this property</a>

"accept"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20propagation_policy%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20propagation_policy">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20observability">Link to this property</a>

<details>

<summary>

placement: optional object {mode, last\_analyzed\_at, status } or object {region, last\_analyzed\_at, status } or object {hostname, last\_analyzed\_at, status } or 5 more

Configuration for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>. Specify mode=‘smart’ for Smart Placement, or one of region/hostname/host.

</summary>

One of the following:

<details>

<summary>

object {mode, last\_analyzed\_at, status }

</summary>

mode: "smart"

Enables <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200%20%3E%20(property)%20mode">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {region, last\_analyzed\_at, status }

</summary>

region: string

Cloud region for targeted placement in format ‘provider:region’.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201%20%3E%20(property)%20region">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

object {hostname, last\_analyzed\_at, status }

</summary>

hostname: string

HTTP hostname for targeted placement.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202%20%3E%20(property)%20hostname">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

object {host, last\_analyzed\_at, status }

</summary>

host: string

TCP host and port for targeted placement.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203%20%3E%20(property)%20host">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

object {mode, region, last\_analyzed\_at, status }

</summary>

mode: "targeted"

Targeted placement mode.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20mode">Link to this property</a>

region: string

Cloud region for targeted placement in format ‘provider:region’.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20region">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

object {hostname, mode, last\_analyzed\_at, status }

</summary>

hostname: string

HTTP hostname for targeted placement.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20hostname">Link to this property</a>

mode: "targeted"

Targeted placement mode.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20mode">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205">Link to this property</a>

<details>

<summary>

object {host, mode, last\_analyzed\_at, status }

</summary>

host: string

TCP host and port for targeted placement.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20host">Link to this property</a>

mode: "targeted"

Targeted placement mode.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20mode">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206">Link to this property</a>

<details>

<summary>

object {mode, target, last\_analyzed\_at, status }

</summary>

mode: "targeted"

Targeted placement mode.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20mode">Link to this property</a>

<details>

<summary>

target: array of object {region } or object {hostname } or object {host }

Array of placement targets (currently limited to single target).

</summary>

One of the following:

<details>

<summary>

Region object {region }

</summary>

region: string

Cloud region in format ‘provider:region’.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20region">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

Hostname object {hostname }

</summary>

hostname: string

HTTP hostname for targeted placement.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20hostname">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

Host object {host }

</summary>

host: string

TCP host:port for targeted placement.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20host">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement">Link to this property</a>

<details>

<summary>

Deprecatedplacement\_mode: optional "smart"or "targeted"

Configuration for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>. Specify mode=‘smart’ for Smart Placement, or one of region/hostname/host.

</summary>

One of the following:

"smart"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement_mode%20%3E%20(member)%200">Link to this property</a>

"targeted"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement_mode%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement_mode">Link to this property</a>

<details>

<summary>

Deprecatedplacement\_status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement_status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement_status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement_status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20placement_status">Link to this property</a>

tag: optional string

The immutable ID of the script.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20tag">Link to this property</a>

tags: optional array of string

Tags associated with the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

<details>

<summary>

tail\_consumers: optional array of <a href="https://developers.cloudflare.com/api/resources/workers#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)">ConsumerScript</a> { service, environment, namespace }

List of Workers that will consume logs from the attached Worker.

</summary>

service: string

Name of Worker that is to be the consumer.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20service">Link to this property</a>

environment: optional string

Optional environment if the Worker utilizes one.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20environment">Link to this property</a>

namespace: optional string

Optional dispatch namespace the script belongs to.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20namespace">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20tail_consumers">Link to this property</a>

<details>

<summary>

usage\_model: optional "standard"or "bundled"or "unbound"

Usage model for the Worker invocations.

</summary>

One of the following:

"standard"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20usage_model%20%3E%20(member)%200">Link to this property</a>

"bundled"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20usage_model%20%3E%20(member)%201">Link to this property</a>

"unbound"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20usage_model%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)%20%3E%20(property)%20usage_model">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts%20%3E%20(model)%20script%20%3E%20(schema)>)

<details>

<summary>

ScriptSetting object {logpush, observability, tags, tail\_consumers }

</summary>

logpush: optional boolean

Whether Logpush is turned on for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)%20%3E%20(property)%20logpush">Link to this property</a>

<details>

<summary>

observability: optional object {enabled, head\_sampling\_rate, issues, 3 more }

Observability settings for the Worker.

</summary>

enabled: boolean

Whether observability is enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20enabled">Link to this property</a>

head\_sampling\_rate: optional number

The sampling rate for incoming requests. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20head_sampling_rate">Link to this property</a>

<details>

<summary>

issues: optional object {enabled }

Real-time Issues settings for the Worker.

</summary>

enabled: optional boolean

Whether real-time Issues are enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20issues%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20issues">Link to this property</a>

<details>

<summary>

logs: optional object {enabled, invocation\_logs, destinations, 2 more }

Log settings for the Worker.

</summary>

enabled: boolean

Whether logs are enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20enabled">Link to this property</a>

invocation\_logs: boolean

Whether <a href="https://developers.cloudflare.com/workers/observability/logs/workers-logs/#invocation-logs">invocation logs</a> are enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20invocation_logs">Link to this property</a>

destinations: optional array of string

A list of destinations where logs will be exported to.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20destinations">Link to this property</a>

head\_sampling\_rate: optional number

The sampling rate for logs. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20head_sampling_rate">Link to this property</a>

persist: optional boolean

Whether log persistence is enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20persist">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs">Link to this property</a>

redact\_query\_string: optional boolean

Whether query strings are removed from request URLs in logs and traces.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20redact_query_string">Link to this property</a>

<details>

<summary>

traces: optional object {destinations, enabled, head\_sampling\_rate, 2 more }

Trace settings for the Worker.

</summary>

destinations: optional array of string

A list of destinations where traces will be exported to.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20destinations">Link to this property</a>

enabled: optional boolean

Whether traces are enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20enabled">Link to this property</a>

head\_sampling\_rate: optional number

The sampling rate for traces. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20head_sampling_rate">Link to this property</a>

persist: optional boolean

Whether trace persistence is enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20persist">Link to this property</a>

<details>

<summary>

propagation\_policy: optional "authenticated"or "accept"

Controls how inbound trace context (traceparent/tracestate) headers on incoming requests are handled. “authenticated” honors inbound trace context only when accompanied by a valid trace auth token. “accept” unconditionally accepts inbound trace context. Requires the trace propagation feature to be enabled. Returns null when the trace propagation feature is not enabled for the account.

</summary>

One of the following:

"authenticated"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20propagation_policy%20%3E%20(member)%200">Link to this property</a>

"accept"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20propagation_policy%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20propagation_policy">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)%20%3E%20(property)%20observability">Link to this property</a>

tags: optional array of string

Tags associated with the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

<details>

<summary>

tail\_consumers: optional array of <a href="https://developers.cloudflare.com/api/resources/workers#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)">ConsumerScript</a> { service, environment, namespace }

List of Workers that will consume logs from the attached Worker.

</summary>

service: string

Name of Worker that is to be the consumer.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20service">Link to this property</a>

environment: optional string

Optional environment if the Worker utilizes one.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20environment">Link to this property</a>

namespace: optional string

Optional dispatch namespace the script belongs to.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20namespace">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)%20%3E%20(property)%20tail_consumers">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts%20%3E%20(model)%20script_setting%20%3E%20(schema)>)

<details>

<summary>

ScriptListResponse object {id, cache\_options, compatibility\_date, 21 more }

</summary>

id: optional string

The name used to identify the script.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

cache\_options: optional object {enabled, cross\_version\_cache }

Global CacheW configuration for the Worker. When caching is on, the platform provisions a <code>cloudflare.app</code> zone for the Worker. A <code>type: worker</code> entry in the <code>exports</code> map can override this value for a single entrypoint.

</summary>

enabled: boolean

Whether caching is enabled for this Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20cache_options%20%3E%20(property)%20enabled">Link to this property</a>

cross\_version\_cache: optional boolean

Whether cached responses are shared across Worker version uploads. This is independent of <code>enabled</code>. It can stay true while caching is off, so the preference survives turning caching off and back on.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20cache_options%20%3E%20(property)%20cross_version_cache">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20cache_options">Link to this property</a>

compatibility\_date: optional string

Date indicating targeted support in the Workers runtime. Backwards incompatible fixes to the runtime following this date will not affect this Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20compatibility_date">Link to this property</a>

compatibility\_flags: optional array of string

Flags that enable or disable certain features in the Workers runtime. Used to enable upcoming features or opt in or out of specific changes not included in a <code>compatibility_date</code>.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20compatibility_flags">Link to this property</a>

created\_on: optional string

When the script was created.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

etag: optional string

Hashed script content, can be used in a If-None-Match header when updating.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20etag">Link to this property</a>

<details>

<summary>

exports: optional map\[object {type, cache, state } or object {storage, type, container, state } or object {state, type } or 3 more]

Declarative exports for the Worker’s most recent version, including Durable Object classes (with their <code>storage</code> backend) and named Worker entrypoints. Tombstoned lifecycle entries are omitted, so only live exports (<code>created</code> and <code>expecting-transfer</code>) are returned.

</summary>

One of the following:

<details>

<summary>

Worker object {type, cache, state }

A named Worker entrypoint export (<code>type: worker</code>). Worker entrypoints are always live (<code>state: created</code>) and carry no storage or lifecycle fields. The optional <code>cache</code> block overrides the Worker’s global <code>cache_options.enabled</code> for this entrypoint.

</summary>

type: "worker"

Marks this entry as a Worker entrypoint export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

cache: optional object {enabled }

Cache override for this entrypoint. Overrides the Worker’s global <code>cache_options.enabled</code> for this entrypoint only.

</summary>

enabled: boolean

Whether caching is enabled for this entrypoint.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20cache%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20cache">Link to this property</a>

state: optional "created"

Live export. May be omitted; defaults to <code>created</code>.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20state">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

WorkersDurableObjectExport object {storage, type, container, state }

A live Durable Object export (<code>state: created</code>, the default). The platform auto-provisions the namespace on first deploy, matches it on subsequent deploys, and never mutates or deletes it as a side effect of a code-only change. <code>storage</code> is required; <code>renamed_to</code>, <code>transferred_to</code> and <code>transfer_from</code> are not allowed on a live entry.

</summary>

<details>

<summary>

storage: "sqlite"or "legacy-kv"

Durable Object storage backend. <code>sqlite</code> is the recommended (and only) backend for new namespaces. <code>legacy-kv</code> is accepted only for a class whose namespace already exists as KV-backed; the <code>exports</code> flow never provisions a new <code>legacy-kv</code> namespace.

</summary>

One of the following:

"sqlite"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20storage%20%3E%20(member)%200">Link to this property</a>

"legacy-kv"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20storage%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20storage">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

container: optional string

Name of the container (declared in the upload’s <code>metadata.containers</code>) that backs this Durable Object. When set, the namespace is container-enabled. Valid only on live entries.

maxLength128

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20container">Link to this property</a>

state: optional "created"

Live export. May be omitted; defaults to <code>created</code>.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20state">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

WorkersDurableObjectDeletedExport object {state, type }

A <code>deleted</code> tombstone: retires the provisioned namespace for this class and all of its data. The class must be absent from the uploaded code and no other Worker in the account may bind to the namespace, otherwise the deploy is rejected. No other fields are allowed. Deletion is irreversible.

</summary>

state: "deleted"

Tombstone that deletes the namespace.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20state">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

WorkersDurableObjectRenamedExport object {renamed\_to, state, type }

A <code>renamed</code> tombstone: rewrites the provisioned namespace’s class name from this map key to <code>renamed_to</code>. The source class may stay in code during the rollout window (an info notice is emitted). <code>storage</code>, <code>transferred_to</code> and <code>transfer_from</code> are not allowed.

</summary>

renamed\_to: string

The destination class name. Must differ from the source class (the map key) and must be declared as a live (<code>created</code>) entry in the same <code>exports</code> map. Write-only: never present in GET responses.

maxLength128

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20renamed_to">Link to this property</a>

state: "renamed"

Tombstone that renames the namespace’s class.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20state">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

WorkersDurableObjectTransferredExport object {state, transferred\_to, type }

A <code>transferred</code> tombstone (source side of a two-phase transfer): hands ownership of the provisioned namespace to another script in the same account, named by <code>transferred_to</code>. The target must have already deployed a matching <code>expecting-transfer</code> entry. The source class may stay in code during the rollout window (an info notice is emitted). <code>storage</code>, <code>renamed_to</code> and <code>transfer_from</code> are not allowed.

</summary>

state: "transferred"

Tombstone that transfers the namespace to another script.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20state">Link to this property</a>

transferred\_to: string

The destination script name. Must be in the same account and the same dispatch-namespace context (or both non-dispatch). Cross-dispatch-namespace transfers are rejected. Write-only: never present in GET responses.

maxLength128

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20transferred_to">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

WorkersDurableObjectExpectingTransferExport object {state, storage, transfer\_from, 2 more }

The target side of a two-phase transfer (<code>state: expecting-transfer</code>). Declares that this script expects to receive a namespace for this class from the <code>transfer_from</code> script. This is a live entry, not a tombstone: bindings resolve through the source’s namespace until the source commits with a <code>transferred</code> tombstone. <code>storage</code> and <code>transfer_from</code> are required; <code>renamed_to</code> and <code>transferred_to</code> are not allowed.

</summary>

state: "expecting-transfer"

Target side of a two-phase transfer.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20state">Link to this property</a>

<details>

<summary>

storage: "sqlite"or "legacy-kv"

Durable Object storage backend. <code>sqlite</code> is the recommended (and only) backend for new namespaces. <code>legacy-kv</code> is accepted only for a class whose namespace already exists as KV-backed; the <code>exports</code> flow never provisions a new <code>legacy-kv</code> namespace.

</summary>

One of the following:

"sqlite"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20storage%20%3E%20(member)%200">Link to this property</a>

"legacy-kv"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20storage%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20storage">Link to this property</a>

transfer\_from: string

The source script name to receive the namespace from. Must be in the same account and dispatch-namespace context. Present on reads for <code>expecting-transfer</code> entries.

maxLength128

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20transfer_from">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

container: optional string

Name of the container (declared in the upload’s <code>metadata.containers</code>) that backs this Durable Object once the transfer settles. Valid only on live entries.

maxLength128

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20container">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20exports">Link to this property</a>

handlers: optional array of string

The names of handlers exported as part of the default export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20handlers">Link to this property</a>

has\_assets: optional boolean

Whether a Worker contains assets.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20has_assets">Link to this property</a>

has\_modules: optional boolean

Whether a Worker contains modules.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20has_modules">Link to this property</a>

last\_deployed\_from: optional string

The client most recently used to deploy this Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20last_deployed_from">Link to this property</a>

logpush: optional boolean

Whether Logpush is turned on for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20logpush">Link to this property</a>

migration\_tag: optional string

The tag of the Durable Object migration that was most recently applied for this Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20migration_tag">Link to this property</a>

modified\_on: optional string

When the script was last modified.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

<details>

<summary>

named\_handlers: optional array of object {handlers, name }

Named exports, such as Durable Object class implementations and named entrypoints.

</summary>

handlers: optional array of string

The names of handlers exported as part of the named export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20named_handlers%20%3E%20(items)%20%3E%20(property)%20handlers">Link to this property</a>

name: optional string

The name of the export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20named_handlers%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20named_handlers">Link to this property</a>

<details>

<summary>

observability: optional object {enabled, head\_sampling\_rate, issues, 3 more }

Observability settings for the Worker.

</summary>

enabled: boolean

Whether observability is enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20enabled">Link to this property</a>

head\_sampling\_rate: optional number

The sampling rate for incoming requests. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20head_sampling_rate">Link to this property</a>

<details>

<summary>

issues: optional object {enabled }

Real-time Issues settings for the Worker.

</summary>

enabled: optional boolean

Whether real-time Issues are enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20issues%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20issues">Link to this property</a>

<details>

<summary>

logs: optional object {enabled, invocation\_logs, destinations, 2 more }

Log settings for the Worker.

</summary>

enabled: boolean

Whether logs are enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20enabled">Link to this property</a>

invocation\_logs: boolean

Whether <a href="https://developers.cloudflare.com/workers/observability/logs/workers-logs/#invocation-logs">invocation logs</a> are enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20invocation_logs">Link to this property</a>

destinations: optional array of string

A list of destinations where logs will be exported to.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20destinations">Link to this property</a>

head\_sampling\_rate: optional number

The sampling rate for logs. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20head_sampling_rate">Link to this property</a>

persist: optional boolean

Whether log persistence is enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20persist">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs">Link to this property</a>

redact\_query\_string: optional boolean

Whether query strings are removed from request URLs in logs and traces.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20redact_query_string">Link to this property</a>

<details>

<summary>

traces: optional object {destinations, enabled, head\_sampling\_rate, 2 more }

Trace settings for the Worker.

</summary>

destinations: optional array of string

A list of destinations where traces will be exported to.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20destinations">Link to this property</a>

enabled: optional boolean

Whether traces are enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20enabled">Link to this property</a>

head\_sampling\_rate: optional number

The sampling rate for traces. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20head_sampling_rate">Link to this property</a>

persist: optional boolean

Whether trace persistence is enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20persist">Link to this property</a>

<details>

<summary>

propagation\_policy: optional "authenticated"or "accept"

Controls how inbound trace context (traceparent/tracestate) headers on incoming requests are handled. “authenticated” honors inbound trace context only when accompanied by a valid trace auth token. “accept” unconditionally accepts inbound trace context. Requires the trace propagation feature to be enabled. Returns null when the trace propagation feature is not enabled for the account.

</summary>

One of the following:

"authenticated"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20propagation_policy%20%3E%20(member)%200">Link to this property</a>

"accept"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20propagation_policy%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20propagation_policy">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20observability">Link to this property</a>

<details>

<summary>

placement: optional object {mode, last\_analyzed\_at, status } or object {region, last\_analyzed\_at, status } or object {hostname, last\_analyzed\_at, status } or 5 more

Configuration for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>. Specify mode=‘smart’ for Smart Placement, or one of region/hostname/host.

</summary>

One of the following:

<details>

<summary>

object {mode, last\_analyzed\_at, status }

</summary>

mode: "smart"

Enables <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200%20%3E%20(property)%20mode">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {region, last\_analyzed\_at, status }

</summary>

region: string

Cloud region for targeted placement in format ‘provider:region’.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201%20%3E%20(property)%20region">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

object {hostname, last\_analyzed\_at, status }

</summary>

hostname: string

HTTP hostname for targeted placement.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202%20%3E%20(property)%20hostname">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

object {host, last\_analyzed\_at, status }

</summary>

host: string

TCP host and port for targeted placement.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203%20%3E%20(property)%20host">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

object {mode, region, last\_analyzed\_at, status }

</summary>

mode: "targeted"

Targeted placement mode.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20mode">Link to this property</a>

region: string

Cloud region for targeted placement in format ‘provider:region’.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20region">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

object {hostname, mode, last\_analyzed\_at, status }

</summary>

hostname: string

HTTP hostname for targeted placement.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20hostname">Link to this property</a>

mode: "targeted"

Targeted placement mode.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20mode">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205">Link to this property</a>

<details>

<summary>

object {host, mode, last\_analyzed\_at, status }

</summary>

host: string

TCP host and port for targeted placement.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20host">Link to this property</a>

mode: "targeted"

Targeted placement mode.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20mode">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206">Link to this property</a>

<details>

<summary>

object {mode, target, last\_analyzed\_at, status }

</summary>

mode: "targeted"

Targeted placement mode.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20mode">Link to this property</a>

<details>

<summary>

target: array of object {region } or object {hostname } or object {host }

Array of placement targets (currently limited to single target).

</summary>

One of the following:

<details>

<summary>

Region object {region }

</summary>

region: string

Cloud region in format ‘provider:region’.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20region">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

Hostname object {hostname }

</summary>

hostname: string

HTTP hostname for targeted placement.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20hostname">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

Host object {host }

</summary>

host: string

TCP host:port for targeted placement.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20host">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement">Link to this property</a>

<details>

<summary>

Deprecatedplacement\_mode: optional "smart"or "targeted"

</summary>

One of the following:

"smart"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement_mode%20%3E%20(member)%200">Link to this property</a>

"targeted"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement_mode%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement_mode">Link to this property</a>

<details>

<summary>

Deprecatedplacement\_status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement_status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement_status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement_status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20placement_status">Link to this property</a>

<details>

<summary>

routes: optional array of object {id, pattern, script }

Routes associated with the Worker.

</summary>

id: string

Identifier.

maxLength32

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

pattern: string

Pattern to match incoming requests against. <a href="https://developers.cloudflare.com/workers/configuration/routing/routes/#matching-behavior">Learn more</a>.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20pattern">Link to this property</a>

script: optional string

Name of the script to run if the route matches.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20routes%20%3E%20(items)%20%3E%20(property)%20script">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20routes">Link to this property</a>

tag: optional string

The immutable ID of the script.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20tag">Link to this property</a>

tags: optional array of string

Tags associated with the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

<details>

<summary>

tail\_consumers: optional array of <a href="https://developers.cloudflare.com/api/resources/workers#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)">ConsumerScript</a> { service, environment, namespace }

List of Workers that will consume logs from the attached Worker.

</summary>

service: string

Name of Worker that is to be the consumer.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20service">Link to this property</a>

environment: optional string

Optional environment if the Worker utilizes one.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20environment">Link to this property</a>

namespace: optional string

Optional dispatch namespace the script belongs to.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20namespace">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20tail_consumers">Link to this property</a>

<details>

<summary>

usage\_model: optional "standard"or "bundled"or "unbound"

Usage model for the Worker invocations.

</summary>

One of the following:

"standard"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20usage_model%20%3E%20(member)%200">Link to this property</a>

"bundled"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20usage_model%20%3E%20(member)%201">Link to this property</a>

"unbound"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20usage_model%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)%20%3E%20(property)%20usage_model">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts%20%3E%20(model)%20script_list_response%20%3E%20(schema)>)

<details>

<summary>

ScriptSearchResponse = array of object {id, created\_on, modified\_on, 4 more }

</summary>

id: string

Identifier.

maxLength32

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_search_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

created\_on: string

When the script was created.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_search_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20created_on">Link to this property</a>

modified\_on: string

When the script was last modified.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_search_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20modified_on">Link to this property</a>

script\_name: string

Name of the script.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_search_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20script_name">Link to this property</a>

environment\_is\_default: optional boolean

Whether the environment is the default environment.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_search_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20environment_is_default">Link to this property</a>

environment\_name: optional string

Name of the environment.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_search_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20environment_name">Link to this property</a>

service\_name: optional string

Name of the service.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_search_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20service_name">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts%20%3E%20(model)%20script_search_response%20%3E%20(schema)>)

ScriptGetResponse = string

[Link to this property](<#(resource)%20workers.scripts%20%3E%20(model)%20script_get_response%20%3E%20(schema)>)

<details>

<summary>

ScriptUpdateResponse object {startup\_time\_ms, id, cache\_options, 22 more }

</summary>

startup\_time\_ms: number

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20startup_time_ms">Link to this property</a>

id: optional string

The name used to identify the script.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

cache\_options: optional object {enabled, cross\_version\_cache }

Global CacheW configuration for the Worker. When caching is on, the platform provisions a <code>cloudflare.app</code> zone for the Worker. A <code>type: worker</code> entry in the <code>exports</code> map can override this value for a single entrypoint.

</summary>

enabled: boolean

Whether caching is enabled for this Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20cache_options%20%3E%20(property)%20enabled">Link to this property</a>

cross\_version\_cache: optional boolean

Whether cached responses are shared across Worker version uploads. This is independent of <code>enabled</code>. It can stay true while caching is off, so the preference survives turning caching off and back on.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20cache_options%20%3E%20(property)%20cross_version_cache">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20cache_options">Link to this property</a>

compatibility\_date: optional string

Date indicating targeted support in the Workers runtime. Backwards incompatible fixes to the runtime following this date will not affect this Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20compatibility_date">Link to this property</a>

compatibility\_flags: optional array of string

Flags that enable or disable certain features in the Workers runtime. Used to enable upcoming features or opt in or out of specific changes not included in a <code>compatibility_date</code>.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20compatibility_flags">Link to this property</a>

created\_on: optional string

When the script was created.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

entry\_point: optional string

The entry point for the script.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20entry_point">Link to this property</a>

etag: optional string

Hashed script content, can be used in a If-None-Match header when updating.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20etag">Link to this property</a>

<details>

<summary>

exports: optional map\[object {type, cache, state } or object {storage, type, container, state } or object {state, type } or 3 more]

Declarative exports for the Worker’s most recent version, including Durable Object classes (with their <code>storage</code> backend) and named Worker entrypoints. Tombstoned lifecycle entries are omitted, so only live exports (<code>created</code> and <code>expecting-transfer</code>) are returned.

</summary>

One of the following:

<details>

<summary>

Worker object {type, cache, state }

A named Worker entrypoint export (<code>type: worker</code>). Worker entrypoints are always live (<code>state: created</code>) and carry no storage or lifecycle fields. The optional <code>cache</code> block overrides the Worker’s global <code>cache_options.enabled</code> for this entrypoint.

</summary>

type: "worker"

Marks this entry as a Worker entrypoint export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

cache: optional object {enabled }

Cache override for this entrypoint. Overrides the Worker’s global <code>cache_options.enabled</code> for this entrypoint only.

</summary>

enabled: boolean

Whether caching is enabled for this entrypoint.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20cache%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20cache">Link to this property</a>

state: optional "created"

Live export. May be omitted; defaults to <code>created</code>.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20state">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

WorkersDurableObjectExport object {storage, type, container, state }

A live Durable Object export (<code>state: created</code>, the default). The platform auto-provisions the namespace on first deploy, matches it on subsequent deploys, and never mutates or deletes it as a side effect of a code-only change. <code>storage</code> is required; <code>renamed_to</code>, <code>transferred_to</code> and <code>transfer_from</code> are not allowed on a live entry.

</summary>

<details>

<summary>

storage: "sqlite"or "legacy-kv"

Durable Object storage backend. <code>sqlite</code> is the recommended (and only) backend for new namespaces. <code>legacy-kv</code> is accepted only for a class whose namespace already exists as KV-backed; the <code>exports</code> flow never provisions a new <code>legacy-kv</code> namespace.

</summary>

One of the following:

"sqlite"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20storage%20%3E%20(member)%200">Link to this property</a>

"legacy-kv"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20storage%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20storage">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

container: optional string

Name of the container (declared in the upload’s <code>metadata.containers</code>) that backs this Durable Object. When set, the namespace is container-enabled. Valid only on live entries.

maxLength128

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20container">Link to this property</a>

state: optional "created"

Live export. May be omitted; defaults to <code>created</code>.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20state">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

WorkersDurableObjectDeletedExport object {state, type }

A <code>deleted</code> tombstone: retires the provisioned namespace for this class and all of its data. The class must be absent from the uploaded code and no other Worker in the account may bind to the namespace, otherwise the deploy is rejected. No other fields are allowed. Deletion is irreversible.

</summary>

state: "deleted"

Tombstone that deletes the namespace.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20state">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

WorkersDurableObjectRenamedExport object {renamed\_to, state, type }

A <code>renamed</code> tombstone: rewrites the provisioned namespace’s class name from this map key to <code>renamed_to</code>. The source class may stay in code during the rollout window (an info notice is emitted). <code>storage</code>, <code>transferred_to</code> and <code>transfer_from</code> are not allowed.

</summary>

renamed\_to: string

The destination class name. Must differ from the source class (the map key) and must be declared as a live (<code>created</code>) entry in the same <code>exports</code> map. Write-only: never present in GET responses.

maxLength128

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20renamed_to">Link to this property</a>

state: "renamed"

Tombstone that renames the namespace’s class.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20state">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

WorkersDurableObjectTransferredExport object {state, transferred\_to, type }

A <code>transferred</code> tombstone (source side of a two-phase transfer): hands ownership of the provisioned namespace to another script in the same account, named by <code>transferred_to</code>. The target must have already deployed a matching <code>expecting-transfer</code> entry. The source class may stay in code during the rollout window (an info notice is emitted). <code>storage</code>, <code>renamed_to</code> and <code>transfer_from</code> are not allowed.

</summary>

state: "transferred"

Tombstone that transfers the namespace to another script.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20state">Link to this property</a>

transferred\_to: string

The destination script name. Must be in the same account and the same dispatch-namespace context (or both non-dispatch). Cross-dispatch-namespace transfers are rejected. Write-only: never present in GET responses.

maxLength128

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20transferred_to">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

WorkersDurableObjectExpectingTransferExport object {state, storage, transfer\_from, 2 more }

The target side of a two-phase transfer (<code>state: expecting-transfer</code>). Declares that this script expects to receive a namespace for this class from the <code>transfer_from</code> script. This is a live entry, not a tombstone: bindings resolve through the source’s namespace until the source commits with a <code>transferred</code> tombstone. <code>storage</code> and <code>transfer_from</code> are required; <code>renamed_to</code> and <code>transferred_to</code> are not allowed.

</summary>

state: "expecting-transfer"

Target side of a two-phase transfer.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20state">Link to this property</a>

<details>

<summary>

storage: "sqlite"or "legacy-kv"

Durable Object storage backend. <code>sqlite</code> is the recommended (and only) backend for new namespaces. <code>legacy-kv</code> is accepted only for a class whose namespace already exists as KV-backed; the <code>exports</code> flow never provisions a new <code>legacy-kv</code> namespace.

</summary>

One of the following:

"sqlite"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20storage%20%3E%20(member)%200">Link to this property</a>

"legacy-kv"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20storage%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20storage">Link to this property</a>

transfer\_from: string

The source script name to receive the namespace from. Must be in the same account and dispatch-namespace context. Present on reads for <code>expecting-transfer</code> entries.

maxLength128

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20transfer_from">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

container: optional string

Name of the container (declared in the upload’s <code>metadata.containers</code>) that backs this Durable Object once the transfer settles. Valid only on live entries.

maxLength128

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20container">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20exports">Link to this property</a>

handlers: optional array of string

The names of handlers exported as part of the default export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20handlers">Link to this property</a>

has\_assets: optional boolean

Whether a Worker contains assets.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20has_assets">Link to this property</a>

has\_modules: optional boolean

Whether a Worker contains modules.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20has_modules">Link to this property</a>

last\_deployed\_from: optional string

The client most recently used to deploy this Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20last_deployed_from">Link to this property</a>

logpush: optional boolean

Whether Logpush is turned on for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20logpush">Link to this property</a>

migration\_tag: optional string

The tag of the Durable Object migration that was most recently applied for this Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20migration_tag">Link to this property</a>

modified\_on: optional string

When the script was last modified.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

<details>

<summary>

named\_handlers: optional array of object {handlers, name }

Named exports, such as Durable Object class implementations and named entrypoints.

</summary>

handlers: optional array of string

The names of handlers exported as part of the named export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20named_handlers%20%3E%20(items)%20%3E%20(property)%20handlers">Link to this property</a>

name: optional string

The name of the export.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20named_handlers%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20named_handlers">Link to this property</a>

<details>

<summary>

observability: optional object {enabled, head\_sampling\_rate, issues, 3 more }

Observability settings for the Worker.

</summary>

enabled: boolean

Whether observability is enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20enabled">Link to this property</a>

head\_sampling\_rate: optional number

The sampling rate for incoming requests. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20head_sampling_rate">Link to this property</a>

<details>

<summary>

issues: optional object {enabled }

Real-time Issues settings for the Worker.

</summary>

enabled: optional boolean

Whether real-time Issues are enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20issues%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20issues">Link to this property</a>

<details>

<summary>

logs: optional object {enabled, invocation\_logs, destinations, 2 more }

Log settings for the Worker.

</summary>

enabled: boolean

Whether logs are enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20enabled">Link to this property</a>

invocation\_logs: boolean

Whether <a href="https://developers.cloudflare.com/workers/observability/logs/workers-logs/#invocation-logs">invocation logs</a> are enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20invocation_logs">Link to this property</a>

destinations: optional array of string

A list of destinations where logs will be exported to.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20destinations">Link to this property</a>

head\_sampling\_rate: optional number

The sampling rate for logs. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20head_sampling_rate">Link to this property</a>

persist: optional boolean

Whether log persistence is enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20persist">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs">Link to this property</a>

redact\_query\_string: optional boolean

Whether query strings are removed from request URLs in logs and traces.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20redact_query_string">Link to this property</a>

<details>

<summary>

traces: optional object {destinations, enabled, head\_sampling\_rate, 2 more }

Trace settings for the Worker.

</summary>

destinations: optional array of string

A list of destinations where traces will be exported to.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20destinations">Link to this property</a>

enabled: optional boolean

Whether traces are enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20enabled">Link to this property</a>

head\_sampling\_rate: optional number

The sampling rate for traces. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20head_sampling_rate">Link to this property</a>

persist: optional boolean

Whether trace persistence is enabled for the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20persist">Link to this property</a>

<details>

<summary>

propagation\_policy: optional "authenticated"or "accept"

Controls how inbound trace context (traceparent/tracestate) headers on incoming requests are handled. “authenticated” honors inbound trace context only when accompanied by a valid trace auth token. “accept” unconditionally accepts inbound trace context. Requires the trace propagation feature to be enabled. Returns null when the trace propagation feature is not enabled for the account.

</summary>

One of the following:

"authenticated"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20propagation_policy%20%3E%20(member)%200">Link to this property</a>

"accept"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20propagation_policy%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20propagation_policy">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20observability">Link to this property</a>

<details>

<summary>

placement: optional object {mode, last\_analyzed\_at, status } or object {region, last\_analyzed\_at, status } or object {hostname, last\_analyzed\_at, status } or 5 more

Configuration for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>. Specify mode=‘smart’ for Smart Placement, or one of region/hostname/host.

</summary>

One of the following:

<details>

<summary>

object {mode, last\_analyzed\_at, status }

</summary>

mode: "smart"

Enables <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200%20%3E%20(property)%20mode">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {region, last\_analyzed\_at, status }

</summary>

region: string

Cloud region for targeted placement in format ‘provider:region’.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201%20%3E%20(property)%20region">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

object {hostname, last\_analyzed\_at, status }

</summary>

hostname: string

HTTP hostname for targeted placement.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202%20%3E%20(property)%20hostname">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

object {host, last\_analyzed\_at, status }

</summary>

host: string

TCP host and port for targeted placement.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203%20%3E%20(property)%20host">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

object {mode, region, last\_analyzed\_at, status }

</summary>

mode: "targeted"

Targeted placement mode.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20mode">Link to this property</a>

region: string

Cloud region for targeted placement in format ‘provider:region’.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20region">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

object {hostname, mode, last\_analyzed\_at, status }

</summary>

hostname: string

HTTP hostname for targeted placement.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20hostname">Link to this property</a>

mode: "targeted"

Targeted placement mode.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20mode">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205">Link to this property</a>

<details>

<summary>

object {host, mode, last\_analyzed\_at, status }

</summary>

host: string

TCP host and port for targeted placement.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20host">Link to this property</a>

mode: "targeted"

Targeted placement mode.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20mode">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206">Link to this property</a>

<details>

<summary>

object {mode, target, last\_analyzed\_at, status }

</summary>

mode: "targeted"

Targeted placement mode.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20mode">Link to this property</a>

<details>

<summary>

target: array of object {region } or object {hostname } or object {host }

Array of placement targets (currently limited to single target).

</summary>

One of the following:

<details>

<summary>

Region object {region }

</summary>

region: string

Cloud region in format ‘provider:region’.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20region">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

Hostname object {hostname }

</summary>

hostname: string

HTTP hostname for targeted placement.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20hostname">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

Host object {host }

</summary>

host: string

TCP host:port for targeted placement.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20host">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target">Link to this property</a>

last\_analyzed\_at: optional string

The last time the script was analyzed for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

formatdate-time

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20last_analyzed_at">Link to this property</a>

<details>

<summary>

status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

Status of <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement">Link to this property</a>

<details>

<summary>

Deprecatedplacement\_mode: optional "smart"or "targeted"

</summary>

One of the following:

"smart"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement_mode%20%3E%20(member)%200">Link to this property</a>

"targeted"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement_mode%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement_mode">Link to this property</a>

<details>

<summary>

Deprecatedplacement\_status: optional "SUCCESS"or "UNSUPPORTED\_APPLICATION"or "INSUFFICIENT\_INVOCATIONS"

</summary>

One of the following:

"SUCCESS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement_status%20%3E%20(member)%200">Link to this property</a>

"UNSUPPORTED\_APPLICATION"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement_status%20%3E%20(member)%201">Link to this property</a>

"INSUFFICIENT\_INVOCATIONS"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement_status%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20placement_status">Link to this property</a>

tag: optional string

The immutable ID of the script.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20tag">Link to this property</a>

tags: optional array of string

Tags associated with the Worker.

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

<details>

<summary>

tail\_consumers: optional array of <a href="https://developers.cloudflare.com/api/resources/workers#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)">ConsumerScript</a> { service, environment, namespace }

List of Workers that will consume logs from the attached Worker.

</summary>

service: string

Name of Worker that is to be the consumer.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20service">Link to this property</a>

environment: optional string

Optional environment if the Worker utilizes one.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20environment">Link to this property</a>

namespace: optional string

Optional dispatch namespace the script belongs to.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20namespace">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20tail_consumers">Link to this property</a>

<details>

<summary>

usage\_model: optional "standard"or "bundled"or "unbound"

Usage model for the Worker invocations.

</summary>

One of the following:

"standard"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20usage_model%20%3E%20(member)%200">Link to this property</a>

"bundled"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20usage_model%20%3E%20(member)%201">Link to this property</a>

"unbound"

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20usage_model%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)%20%3E%20(property)%20usage_model">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts%20%3E%20(model)%20script_update_response%20%3E%20(schema)>)

ScriptDeleteResponse = unknown

[Link to this property](<#(resource)%20workers.scripts%20%3E%20(model)%20script_delete_response%20%3E%20(schema)>)

#### ScriptsAssets

#### ScriptsAssetsUpload

##### [Create Worker Assets Upload Session](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/assets/subresources/upload/methods/create)

POST/accounts/{account\_id}/workers/scripts/{script\_name}/assets-upload-session

##### ModelsExpand Collapse

<details>

<summary>

UploadCreateResponse object {buckets, jwt }

</summary>

buckets: optional array of array of string

The requests to make to upload assets.

<a href="#(resource)%20workers.scripts.assets.upload%20%3E%20(model)%20upload_create_response%20%3E%20(schema)%20%3E%20(property)%20buckets">Link to this property</a>

jwt: optional string

A JWT to use as authentication for uploading assets.

<a href="#(resource)%20workers.scripts.assets.upload%20%3E%20(model)%20upload_create_response%20%3E%20(schema)%20%3E%20(property)%20jwt">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.assets.upload%20%3E%20(model)%20upload_create_response%20%3E%20(schema)>)

#### ScriptsSubdomain

##### [Get Worker Script Subdomain](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/subdomain/methods/get)

GET/accounts/{account\_id}/workers/scripts/{script\_name}/subdomain

##### [Update Worker Script Subdomain](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/subdomain/methods/create)

POST/accounts/{account\_id}/workers/scripts/{script\_name}/subdomain

##### [Delete Worker Script Subdomain](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/subdomain/methods/delete)

DELETE/accounts/{account\_id}/workers/scripts/{script\_name}/subdomain

##### ModelsExpand Collapse

<details>

<summary>

SubdomainGetResponse object {enabled, previews\_enabled }

</summary>

enabled: boolean

Whether the Worker is available on the workers.dev subdomain.

<a href="#(resource)%20workers.scripts.subdomain%20%3E%20(model)%20subdomain_get_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

previews\_enabled: boolean

Whether the Worker’s Preview URLs are available on the workers.dev subdomain.

<a href="#(resource)%20workers.scripts.subdomain%20%3E%20(model)%20subdomain_get_response%20%3E%20(schema)%20%3E%20(property)%20previews_enabled">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.subdomain%20%3E%20(model)%20subdomain_get_response%20%3E%20(schema)>)

<details>

<summary>

SubdomainCreateResponse object {enabled, previews\_enabled }

</summary>

enabled: boolean

Whether the Worker is available on the workers.dev subdomain.

<a href="#(resource)%20workers.scripts.subdomain%20%3E%20(model)%20subdomain_create_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

previews\_enabled: boolean

Whether the Worker’s Preview URLs are available on the workers.dev subdomain.

<a href="#(resource)%20workers.scripts.subdomain%20%3E%20(model)%20subdomain_create_response%20%3E%20(schema)%20%3E%20(property)%20previews_enabled">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.subdomain%20%3E%20(model)%20subdomain_create_response%20%3E%20(schema)>)

<details>

<summary>

SubdomainDeleteResponse object {enabled, previews\_enabled }

</summary>

enabled: boolean

Whether the Worker is available on the workers.dev subdomain.

<a href="#(resource)%20workers.scripts.subdomain%20%3E%20(model)%20subdomain_delete_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

previews\_enabled: boolean

Whether the Worker’s Preview URLs are available on the workers.dev subdomain.

<a href="#(resource)%20workers.scripts.subdomain%20%3E%20(model)%20subdomain_delete_response%20%3E%20(schema)%20%3E%20(property)%20previews_enabled">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.subdomain%20%3E%20(model)%20subdomain_delete_response%20%3E%20(schema)>)

#### ScriptsSchedules

##### [Get Worker Script Schedules (Cron Triggers)](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/schedules/methods/get)

GET/accounts/{account\_id}/workers/scripts/{script\_name}/schedules

##### [Update Worker Script Schedules (Cron Triggers)](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/schedules/methods/update)

PUT/accounts/{account\_id}/workers/scripts/{script\_name}/schedules

##### ModelsExpand Collapse

<details>

<summary>

ScheduleGetResponse object {schedules }

</summary>

<details>

<summary>

schedules: array of object {cron, created\_on, modified\_on }

</summary>

cron: string

<a href="#(resource)%20workers.scripts.schedules%20%3E%20(model)%20schedule_get_response%20%3E%20(schema)%20%3E%20(property)%20schedules%20%3E%20(items)%20%3E%20(property)%20cron">Link to this property</a>

created\_on: optional string

<a href="#(resource)%20workers.scripts.schedules%20%3E%20(model)%20schedule_get_response%20%3E%20(schema)%20%3E%20(property)%20schedules%20%3E%20(items)%20%3E%20(property)%20created_on">Link to this property</a>

modified\_on: optional string

<a href="#(resource)%20workers.scripts.schedules%20%3E%20(model)%20schedule_get_response%20%3E%20(schema)%20%3E%20(property)%20schedules%20%3E%20(items)%20%3E%20(property)%20modified_on">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.schedules%20%3E%20(model)%20schedule_get_response%20%3E%20(schema)%20%3E%20(property)%20schedules">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.schedules%20%3E%20(model)%20schedule_get_response%20%3E%20(schema)>)

<details>

<summary>

ScheduleUpdateResponse object {schedules }

</summary>

<details>

<summary>

schedules: array of object {cron, created\_on, modified\_on }

</summary>

cron: string

<a href="#(resource)%20workers.scripts.schedules%20%3E%20(model)%20schedule_update_response%20%3E%20(schema)%20%3E%20(property)%20schedules%20%3E%20(items)%20%3E%20(property)%20cron">Link to this property</a>

created\_on: optional string

<a href="#(resource)%20workers.scripts.schedules%20%3E%20(model)%20schedule_update_response%20%3E%20(schema)%20%3E%20(property)%20schedules%20%3E%20(items)%20%3E%20(property)%20created_on">Link to this property</a>

modified\_on: optional string

<a href="#(resource)%20workers.scripts.schedules%20%3E%20(model)%20schedule_update_response%20%3E%20(schema)%20%3E%20(property)%20schedules%20%3E%20(items)%20%3E%20(property)%20modified_on">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.schedules%20%3E%20(model)%20schedule_update_response%20%3E%20(schema)%20%3E%20(property)%20schedules">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.schedules%20%3E%20(model)%20schedule_update_response%20%3E%20(schema)>)

#### ScriptsTail

##### [List Worker Tails](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/tail/methods/get)

GET/accounts/{account\_id}/workers/scripts/{script\_name}/tails

##### [Start Worker Tail](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/tail/methods/create)

POST/accounts/{account\_id}/workers/scripts/{script\_name}/tails

##### [Delete Worker Tail](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/tail/methods/delete)

DELETE/accounts/{account\_id}/workers/scripts/{script\_name}/tails/{id}

##### ModelsExpand Collapse

<details>

<summary>

ConsumerScript object {service, environment, namespace }

A reference to a script that will consume logs from the attached Worker.

</summary>

service: string

Name of Worker that is to be the consumer.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20service">Link to this property</a>

environment: optional string

Optional environment if the Worker utilizes one.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20environment">Link to this property</a>

namespace: optional string

Optional dispatch namespace the script belongs to.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20namespace">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)>)

<details>

<summary>

TailGetResponse object {id, expires\_at, url }

</summary>

id: string

Identifier.

maxLength32

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

expires\_at: string

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_get_response%20%3E%20(schema)%20%3E%20(property)%20expires_at">Link to this property</a>

url: string

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_get_response%20%3E%20(schema)%20%3E%20(property)%20url">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_get_response%20%3E%20(schema)>)

<details>

<summary>

TailCreateResponse object {id, expires\_at, url }

</summary>

id: string

Identifier.

maxLength32

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

expires\_at: string

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_create_response%20%3E%20(schema)%20%3E%20(property)%20expires_at">Link to this property</a>

url: string

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_create_response%20%3E%20(schema)%20%3E%20(property)%20url">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_create_response%20%3E%20(schema)>)

<details>

<summary>

TailDeleteResponse object {errors, messages, success }

</summary>

<details>

<summary>

errors: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

<details>

<summary>

messages: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages">Link to this property</a>

success: true

Whether the API call was successful.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.tail%20%3E%20(model)%20tail_delete_response%20%3E%20(schema)>)

#### ScriptsContent

##### [Get Worker Script Content](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/content/methods/get)

GET/accounts/{account\_id}/workers/scripts/{script\_name}/content/v2

##### [Replace Worker Script Content](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/content/methods/update)

PUT/accounts/{account\_id}/workers/scripts/{script\_name}/content

#### ScriptsSettings

##### [Get Worker Script Settings](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/settings/methods/get)

GET/accounts/{account\_id}/workers/scripts/{script\_name}/script-settings

##### [Patch Worker Script Settings](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/settings/methods/edit)

PATCH/accounts/{account\_id}/workers/scripts/{script\_name}/script-settings

#### ScriptsDeployments

##### [List Worker Deployments](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/deployments/methods/list)

GET/accounts/{account\_id}/workers/scripts/{script\_name}/deployments

##### [Create Worker Deployment](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/deployments/methods/create)

POST/accounts/{account\_id}/workers/scripts/{script\_name}/deployments

##### [Get Worker Deployment](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/deployments/methods/get)

GET/accounts/{account\_id}/workers/scripts/{script\_name}/deployments/{deployment\_id}

##### [Delete Worker Deployment](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/deployments/methods/delete)

DELETE/accounts/{account\_id}/workers/scripts/{script\_name}/deployments/{deployment\_id}

##### ModelsExpand Collapse

<details>

<summary>

Deployment object {id, created\_on, source, 4 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_on: string

formatdate-time

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

source: string

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

strategy: "percentage"

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20strategy">Link to this property</a>

<details>

<summary>

versions: array of object {percentage, version\_id }

Worker versions included in this deployment. Each object must contain a <code>version_id</code> UUID and a <code>percentage</code>; percentages across all objects must total 100. In the <code>cf</code> CLI, pass the entire array as one JSON value to <code>--versions</code>, either inline, for example <code>--versions '[{"version_id":"023e105f-2a42-4f8b-a1c1-73f6a2a30c0f","percentage":100}]'</code>, or from a JSON file with <code>--versions @versions.json</code>.

</summary>

percentage: number

Percentage of traffic served by this version.

maximum100

minimum0.01

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20versions%20%3E%20(items)%20%3E%20(property)%20percentage">Link to this property</a>

version\_id: string

Identifier of the Worker Version.

formatuuid

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20versions%20%3E%20(items)%20%3E%20(property)%20version_id">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20versions">Link to this property</a>

<details>

<summary>

annotations: optional object {"workers/message", "workers/triggered\_by" }

</summary>

"workers/message": optional string

Human-readable message about the deployment. Truncated to 1000 bytes if longer.

maxLength1000

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(property)%20workers%2Fmessage">Link to this property</a>

"workers/triggered\_by": optional string

Operation that triggered the creation of the deployment.

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(property)%20workers%2Ftriggered_by">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20annotations">Link to this property</a>

author\_email: optional string

formatemail

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20author_email">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)>)

<details>

<summary>

DeploymentListResponse object {deployments }

</summary>

<details>

<summary>

deployments: array of <a href="https://developers.cloudflare.com/api/resources/workers#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)">Deployment</a> { id, created\_on, source, 4 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

created\_on: string

formatdate-time

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20created_on">Link to this property</a>

source: string

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

strategy: "percentage"

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20strategy">Link to this property</a>

<details>

<summary>

versions: array of object {percentage, version\_id }

Worker versions included in this deployment. Each object must contain a <code>version_id</code> UUID and a <code>percentage</code>; percentages across all objects must total 100. In the <code>cf</code> CLI, pass the entire array as one JSON value to <code>--versions</code>, either inline, for example <code>--versions '[{"version_id":"023e105f-2a42-4f8b-a1c1-73f6a2a30c0f","percentage":100}]'</code>, or from a JSON file with <code>--versions @versions.json</code>.

</summary>

percentage: number

Percentage of traffic served by this version.

maximum100

minimum0.01

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20versions%20%3E%20(items)%20%3E%20(property)%20percentage">Link to this property</a>

version\_id: string

Identifier of the Worker Version.

formatuuid

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20versions%20%3E%20(items)%20%3E%20(property)%20version_id">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20versions">Link to this property</a>

<details>

<summary>

annotations: optional object {"workers/message", "workers/triggered\_by" }

</summary>

"workers/message": optional string

Human-readable message about the deployment. Truncated to 1000 bytes if longer.

maxLength1000

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(property)%20workers%2Fmessage">Link to this property</a>

"workers/triggered\_by": optional string

Operation that triggered the creation of the deployment.

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(property)%20workers%2Ftriggered_by">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20annotations">Link to this property</a>

author\_email: optional string

formatemail

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment%20%3E%20(schema)%20%3E%20(property)%20author_email">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment_list_response%20%3E%20(schema)%20%3E%20(property)%20deployments">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment_list_response%20%3E%20(schema)>)

<details>

<summary>

DeploymentDeleteResponse object {errors, messages, success }

</summary>

<details>

<summary>

errors: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment_delete_response%20%3E%20(schema)%20%3E%20(property)%20errors">Link to this property</a>

<details>

<summary>

messages: array of object {code, message, documentation\_url, source }

</summary>

code: number

minimum1000

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20code">Link to this property</a>

message: string

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

documentation\_url: optional string

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20documentation_url">Link to this property</a>

<details>

<summary>

source: optional object {pointer }

</summary>

pointer: optional string

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source%20%3E%20(property)%20pointer">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages%20%3E%20(items)%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment_delete_response%20%3E%20(schema)%20%3E%20(property)%20messages">Link to this property</a>

success: true

Whether the API call was successful.

<a href="#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment_delete_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.deployments%20%3E%20(model)%20deployment_delete_response%20%3E%20(schema)>)

#### ScriptsVersions

##### [List Versions](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/versions/methods/list)

GET/accounts/{account\_id}/workers/scripts/{script\_name}/versions

##### [Get Worker Script Version](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/versions/methods/get)

GET/accounts/{account\_id}/workers/scripts/{script\_name}/versions/{version\_id}

##### [Upload Version](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/versions/methods/create)

POST/accounts/{account\_id}/workers/scripts/{script\_name}/versions

##### ModelsExpand Collapse

<details>

<summary>

VersionListResponse object {id, metadata, number }

</summary>

id: optional string

Unique identifier for the version.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

metadata: optional object {author\_email, author\_id, created\_on, 3 more }

</summary>

author\_email: optional string

Email of the user who created the version.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20author_email">Link to this property</a>

author\_id: optional string

Identifier of the user who created the version.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20author_id">Link to this property</a>

created\_on: optional string

When the version was created.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20created_on">Link to this property</a>

hasPreview: optional boolean

Whether the version can be previewed.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20hasPreview">Link to this property</a>

modified\_on: optional string

When the version was last modified.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20modified_on">Link to this property</a>

<details>

<summary>

source: optional "unknown"or "api"or "wrangler"or 8 more

The source of the version upload.

</summary>

One of the following:

"unknown"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"api"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

"wrangler"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%202">Link to this property</a>

"terraform"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%203">Link to this property</a>

"dash"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%204">Link to this property</a>

"cf\_cli"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%205">Link to this property</a>

"dash\_template"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%206">Link to this property</a>

"integration"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%207">Link to this property</a>

"quick\_editor"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%208">Link to this property</a>

"playground"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%209">Link to this property</a>

"workersci"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%2010">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20metadata">Link to this property</a>

number: optional number

Sequential version number.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20number">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)>)

<details>

<summary>

VersionGetResponse object {resources, id, metadata, number }

</summary>

<details>

<summary>

resources: object {bindings, script, script\_runtime }

</summary>

bindings: optional

List of bindings attached to a Worker. You can find more about bindings on our docs: <a href="https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings">https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings</a>.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20bindings">Link to this property</a>

<details>

<summary>

script: optional object {etag, handlers, last\_deployed\_from, named\_handlers }

</summary>

etag: optional string

Hashed script content

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script%20%3E%20(property)%20etag">Link to this property</a>

handlers: optional array of string

The names of handlers exported as part of the default export.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script%20%3E%20(property)%20handlers">Link to this property</a>

last\_deployed\_from: optional string

The client most recently used to deploy this Worker.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script%20%3E%20(property)%20last_deployed_from">Link to this property</a>

<details>

<summary>

named\_handlers: optional array of object {handlers, name }

Named exports, such as Durable Object class implementations and named entrypoints.

</summary>

handlers: optional array of string

The names of handlers exported as part of the named export.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script%20%3E%20(property)%20named_handlers%20%3E%20(items)%20%3E%20(property)%20handlers">Link to this property</a>

name: optional string

The name of the exported class or entrypoint.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script%20%3E%20(property)%20named_handlers%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script%20%3E%20(property)%20named_handlers">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script">Link to this property</a>

<details>

<summary>

script\_runtime: optional object {compatibility\_date, compatibility\_flags, exports, 3 more }

Runtime configuration for the Worker.

</summary>

compatibility\_date: optional string

Date indicating targeted support in the Workers runtime. Backwards incompatible fixes to the runtime following this date will not affect this Worker.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20compatibility_date">Link to this property</a>

compatibility\_flags: optional array of string

Flags that enable or disable certain features in the Workers runtime.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20compatibility_flags">Link to this property</a>

<details>

<summary>

exports: optional map\[object {type, cache, state } or object {storage, type, container, state } or object {state, type } or 3 more]

Declarative exports for this version, including Durable Object classes (with their <code>storage</code> backend) and named Worker entrypoints. Tombstoned lifecycle entries are omitted, so only live exports (<code>created</code> and <code>expecting-transfer</code>) are returned.

</summary>

One of the following:

<details>

<summary>

Worker object {type, cache, state }

A named Worker entrypoint export (<code>type: worker</code>). Worker entrypoints are always live (<code>state: created</code>) and carry no storage or lifecycle fields. The optional <code>cache</code> block overrides the Worker’s global <code>cache_options.enabled</code> for this entrypoint.

</summary>

type: "worker"

Marks this entry as a Worker entrypoint export.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

cache: optional object {enabled }

Cache override for this entrypoint. Overrides the Worker’s global <code>cache_options.enabled</code> for this entrypoint only.

</summary>

enabled: boolean

Whether caching is enabled for this entrypoint.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20cache%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20cache">Link to this property</a>

state: optional "created"

Live export. May be omitted; defaults to <code>created</code>.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20state">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

WorkersDurableObjectExport object {storage, type, container, state }

A live Durable Object export (<code>state: created</code>, the default). The platform auto-provisions the namespace on first deploy, matches it on subsequent deploys, and never mutates or deletes it as a side effect of a code-only change. <code>storage</code> is required; <code>renamed_to</code>, <code>transferred_to</code> and <code>transfer_from</code> are not allowed on a live entry.

</summary>

<details>

<summary>

storage: "sqlite"or "legacy-kv"

Durable Object storage backend. <code>sqlite</code> is the recommended (and only) backend for new namespaces. <code>legacy-kv</code> is accepted only for a class whose namespace already exists as KV-backed; the <code>exports</code> flow never provisions a new <code>legacy-kv</code> namespace.

</summary>

One of the following:

"sqlite"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20storage%20%3E%20(member)%200">Link to this property</a>

"legacy-kv"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20storage%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20storage">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

container: optional string

Name of the container (declared in the upload’s <code>metadata.containers</code>) that backs this Durable Object. When set, the namespace is container-enabled. Valid only on live entries.

maxLength128

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20container">Link to this property</a>

state: optional "created"

Live export. May be omitted; defaults to <code>created</code>.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20state">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

WorkersDurableObjectDeletedExport object {state, type }

A <code>deleted</code> tombstone: retires the provisioned namespace for this class and all of its data. The class must be absent from the uploaded code and no other Worker in the account may bind to the namespace, otherwise the deploy is rejected. No other fields are allowed. Deletion is irreversible.

</summary>

state: "deleted"

Tombstone that deletes the namespace.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20state">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

WorkersDurableObjectRenamedExport object {renamed\_to, state, type }

A <code>renamed</code> tombstone: rewrites the provisioned namespace’s class name from this map key to <code>renamed_to</code>. The source class may stay in code during the rollout window (an info notice is emitted). <code>storage</code>, <code>transferred_to</code> and <code>transfer_from</code> are not allowed.

</summary>

renamed\_to: string

The destination class name. Must differ from the source class (the map key) and must be declared as a live (<code>created</code>) entry in the same <code>exports</code> map. Write-only: never present in GET responses.

maxLength128

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20renamed_to">Link to this property</a>

state: "renamed"

Tombstone that renames the namespace’s class.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20state">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

WorkersDurableObjectTransferredExport object {state, transferred\_to, type }

A <code>transferred</code> tombstone (source side of a two-phase transfer): hands ownership of the provisioned namespace to another script in the same account, named by <code>transferred_to</code>. The target must have already deployed a matching <code>expecting-transfer</code> entry. The source class may stay in code during the rollout window (an info notice is emitted). <code>storage</code>, <code>renamed_to</code> and <code>transfer_from</code> are not allowed.

</summary>

state: "transferred"

Tombstone that transfers the namespace to another script.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20state">Link to this property</a>

transferred\_to: string

The destination script name. Must be in the same account and the same dispatch-namespace context (or both non-dispatch). Cross-dispatch-namespace transfers are rejected. Write-only: never present in GET responses.

maxLength128

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20transferred_to">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

WorkersDurableObjectExpectingTransferExport object {state, storage, transfer\_from, 2 more }

The target side of a two-phase transfer (<code>state: expecting-transfer</code>). Declares that this script expects to receive a namespace for this class from the <code>transfer_from</code> script. This is a live entry, not a tombstone: bindings resolve through the source’s namespace until the source commits with a <code>transferred</code> tombstone. <code>storage</code> and <code>transfer_from</code> are required; <code>renamed_to</code> and <code>transferred_to</code> are not allowed.

</summary>

state: "expecting-transfer"

Target side of a two-phase transfer.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20state">Link to this property</a>

<details>

<summary>

storage: "sqlite"or "legacy-kv"

Durable Object storage backend. <code>sqlite</code> is the recommended (and only) backend for new namespaces. <code>legacy-kv</code> is accepted only for a class whose namespace already exists as KV-backed; the <code>exports</code> flow never provisions a new <code>legacy-kv</code> namespace.

</summary>

One of the following:

"sqlite"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20storage%20%3E%20(member)%200">Link to this property</a>

"legacy-kv"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20storage%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20storage">Link to this property</a>

transfer\_from: string

The source script name to receive the namespace from. Must be in the same account and dispatch-namespace context. Present on reads for <code>expecting-transfer</code> entries.

maxLength128

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20transfer_from">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

container: optional string

Name of the container (declared in the upload’s <code>metadata.containers</code>) that backs this Durable Object once the transfer settles. Valid only on live entries.

maxLength128

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20container">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports">Link to this property</a>

<details>

<summary>

limits: optional object {cpu\_ms }

Resource limits for the Worker.

</summary>

cpu\_ms: optional number

The amount of CPU time this Worker can use in milliseconds.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20limits%20%3E%20(property)%20cpu_ms">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20limits">Link to this property</a>

migration\_tag: optional string

The tag of the Durable Object migration that was most recently applied for this Worker.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20migration_tag">Link to this property</a>

<details>

<summary>

usage\_model: optional "bundled"or "unbound"or "standard"

Usage model for the Worker invocations.

</summary>

One of the following:

"bundled"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20usage_model%20%3E%20(member)%200">Link to this property</a>

"unbound"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20usage_model%20%3E%20(member)%201">Link to this property</a>

"standard"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20usage_model%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20usage_model">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20resources">Link to this property</a>

id: optional string

Unique identifier for the version.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

metadata: optional object {author\_email, author\_id, created\_on, 3 more }

</summary>

author\_email: optional string

Email of the user who created the version.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20author_email">Link to this property</a>

author\_id: optional string

Identifier of the user who created the version.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20author_id">Link to this property</a>

created\_on: optional string

When the version was created.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20created_on">Link to this property</a>

hasPreview: optional boolean

Whether the version can be previewed.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20hasPreview">Link to this property</a>

modified\_on: optional string

When the version was last modified.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20modified_on">Link to this property</a>

<details>

<summary>

source: optional "unknown"or "api"or "wrangler"or 8 more

The source of the version upload.

</summary>

One of the following:

"unknown"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"api"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

"wrangler"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%202">Link to this property</a>

"terraform"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%203">Link to this property</a>

"dash"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%204">Link to this property</a>

"cf\_cli"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%205">Link to this property</a>

"dash\_template"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%206">Link to this property</a>

"integration"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%207">Link to this property</a>

"quick\_editor"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%208">Link to this property</a>

"playground"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%209">Link to this property</a>

"workersci"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%2010">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20metadata">Link to this property</a>

number: optional number

Sequential version number.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20number">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)>)

<details>

<summary>

VersionCreateResponse object {resources, id, exports\_reconciliation, 3 more }

</summary>

<details>

<summary>

resources: object {bindings, script, script\_runtime }

</summary>

bindings: optional

List of bindings attached to a Worker. You can find more about bindings on our docs: <a href="https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings">https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings</a>.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20bindings">Link to this property</a>

<details>

<summary>

script: optional object {etag, handlers, last\_deployed\_from, named\_handlers }

</summary>

etag: optional string

Hashed script content

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script%20%3E%20(property)%20etag">Link to this property</a>

handlers: optional array of string

The names of handlers exported as part of the default export.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script%20%3E%20(property)%20handlers">Link to this property</a>

last\_deployed\_from: optional string

The client most recently used to deploy this Worker.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script%20%3E%20(property)%20last_deployed_from">Link to this property</a>

<details>

<summary>

named\_handlers: optional array of object {handlers, name }

Named exports, such as Durable Object class implementations and named entrypoints.

</summary>

handlers: optional array of string

The names of handlers exported as part of the named export.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script%20%3E%20(property)%20named_handlers%20%3E%20(items)%20%3E%20(property)%20handlers">Link to this property</a>

name: optional string

The name of the exported class or entrypoint.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script%20%3E%20(property)%20named_handlers%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script%20%3E%20(property)%20named_handlers">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script">Link to this property</a>

<details>

<summary>

script\_runtime: optional object {compatibility\_date, compatibility\_flags, exports, 3 more }

Runtime configuration for the Worker.

</summary>

compatibility\_date: optional string

Date indicating targeted support in the Workers runtime. Backwards incompatible fixes to the runtime following this date will not affect this Worker.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20compatibility_date">Link to this property</a>

compatibility\_flags: optional array of string

Flags that enable or disable certain features in the Workers runtime.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20compatibility_flags">Link to this property</a>

<details>

<summary>

exports: optional map\[object {type, cache, state } or object {storage, type, container, state } or object {state, type } or 3 more]

Declarative exports for this version, including Durable Object classes (with their <code>storage</code> backend) and named Worker entrypoints. Tombstoned lifecycle entries are omitted, so only live exports (<code>created</code> and <code>expecting-transfer</code>) are returned.

</summary>

One of the following:

<details>

<summary>

Worker object {type, cache, state }

A named Worker entrypoint export (<code>type: worker</code>). Worker entrypoints are always live (<code>state: created</code>) and carry no storage or lifecycle fields. The optional <code>cache</code> block overrides the Worker’s global <code>cache_options.enabled</code> for this entrypoint.

</summary>

type: "worker"

Marks this entry as a Worker entrypoint export.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

cache: optional object {enabled }

Cache override for this entrypoint. Overrides the Worker’s global <code>cache_options.enabled</code> for this entrypoint only.

</summary>

enabled: boolean

Whether caching is enabled for this entrypoint.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20cache%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20cache">Link to this property</a>

state: optional "created"

Live export. May be omitted; defaults to <code>created</code>.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20state">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

WorkersDurableObjectExport object {storage, type, container, state }

A live Durable Object export (<code>state: created</code>, the default). The platform auto-provisions the namespace on first deploy, matches it on subsequent deploys, and never mutates or deletes it as a side effect of a code-only change. <code>storage</code> is required; <code>renamed_to</code>, <code>transferred_to</code> and <code>transfer_from</code> are not allowed on a live entry.

</summary>

<details>

<summary>

storage: "sqlite"or "legacy-kv"

Durable Object storage backend. <code>sqlite</code> is the recommended (and only) backend for new namespaces. <code>legacy-kv</code> is accepted only for a class whose namespace already exists as KV-backed; the <code>exports</code> flow never provisions a new <code>legacy-kv</code> namespace.

</summary>

One of the following:

"sqlite"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20storage%20%3E%20(member)%200">Link to this property</a>

"legacy-kv"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20storage%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20storage">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

container: optional string

Name of the container (declared in the upload’s <code>metadata.containers</code>) that backs this Durable Object. When set, the namespace is container-enabled. Valid only on live entries.

maxLength128

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20container">Link to this property</a>

state: optional "created"

Live export. May be omitted; defaults to <code>created</code>.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20state">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

WorkersDurableObjectDeletedExport object {state, type }

A <code>deleted</code> tombstone: retires the provisioned namespace for this class and all of its data. The class must be absent from the uploaded code and no other Worker in the account may bind to the namespace, otherwise the deploy is rejected. No other fields are allowed. Deletion is irreversible.

</summary>

state: "deleted"

Tombstone that deletes the namespace.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20state">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

WorkersDurableObjectRenamedExport object {renamed\_to, state, type }

A <code>renamed</code> tombstone: rewrites the provisioned namespace’s class name from this map key to <code>renamed_to</code>. The source class may stay in code during the rollout window (an info notice is emitted). <code>storage</code>, <code>transferred_to</code> and <code>transfer_from</code> are not allowed.

</summary>

renamed\_to: string

The destination class name. Must differ from the source class (the map key) and must be declared as a live (<code>created</code>) entry in the same <code>exports</code> map. Write-only: never present in GET responses.

maxLength128

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20renamed_to">Link to this property</a>

state: "renamed"

Tombstone that renames the namespace’s class.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20state">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

WorkersDurableObjectTransferredExport object {state, transferred\_to, type }

A <code>transferred</code> tombstone (source side of a two-phase transfer): hands ownership of the provisioned namespace to another script in the same account, named by <code>transferred_to</code>. The target must have already deployed a matching <code>expecting-transfer</code> entry. The source class may stay in code during the rollout window (an info notice is emitted). <code>storage</code>, <code>renamed_to</code> and <code>transfer_from</code> are not allowed.

</summary>

state: "transferred"

Tombstone that transfers the namespace to another script.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20state">Link to this property</a>

transferred\_to: string

The destination script name. Must be in the same account and the same dispatch-namespace context (or both non-dispatch). Cross-dispatch-namespace transfers are rejected. Write-only: never present in GET responses.

maxLength128

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20transferred_to">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

WorkersDurableObjectExpectingTransferExport object {state, storage, transfer\_from, 2 more }

The target side of a two-phase transfer (<code>state: expecting-transfer</code>). Declares that this script expects to receive a namespace for this class from the <code>transfer_from</code> script. This is a live entry, not a tombstone: bindings resolve through the source’s namespace until the source commits with a <code>transferred</code> tombstone. <code>storage</code> and <code>transfer_from</code> are required; <code>renamed_to</code> and <code>transferred_to</code> are not allowed.

</summary>

state: "expecting-transfer"

Target side of a two-phase transfer.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20state">Link to this property</a>

<details>

<summary>

storage: "sqlite"or "legacy-kv"

Durable Object storage backend. <code>sqlite</code> is the recommended (and only) backend for new namespaces. <code>legacy-kv</code> is accepted only for a class whose namespace already exists as KV-backed; the <code>exports</code> flow never provisions a new <code>legacy-kv</code> namespace.

</summary>

One of the following:

"sqlite"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20storage%20%3E%20(member)%200">Link to this property</a>

"legacy-kv"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20storage%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20storage">Link to this property</a>

transfer\_from: string

The source script name to receive the namespace from. Must be in the same account and dispatch-namespace context. Present on reads for <code>expecting-transfer</code> entries.

maxLength128

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20transfer_from">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

container: optional string

Name of the container (declared in the upload’s <code>metadata.containers</code>) that backs this Durable Object once the transfer settles. Valid only on live entries.

maxLength128

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20container">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20exports">Link to this property</a>

<details>

<summary>

limits: optional object {cpu\_ms }

Resource limits for the Worker.

</summary>

cpu\_ms: optional number

The amount of CPU time this Worker can use in milliseconds.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20limits%20%3E%20(property)%20cpu_ms">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20limits">Link to this property</a>

migration\_tag: optional string

The tag of the Durable Object migration that was most recently applied for this Worker.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20migration_tag">Link to this property</a>

<details>

<summary>

usage\_model: optional "bundled"or "unbound"or "standard"

Usage model for the Worker invocations.

</summary>

One of the following:

"bundled"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20usage_model%20%3E%20(member)%200">Link to this property</a>

"unbound"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20usage_model%20%3E%20(member)%201">Link to this property</a>

"standard"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20usage_model%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime%20%3E%20(property)%20usage_model">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources%20%3E%20(property)%20script_runtime">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20resources">Link to this property</a>

id: optional string

Unique identifier for the version.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

exports\_reconciliation: optional object {created, deleted, info, 6 more }

Summary of the declarative exports reconciliation that ran on this upload. Populated only when the uploaded metadata included an <code>exports</code> block. Durable Object entries drive reconciliation; <code>type: worker</code> entries do not contribute to this summary.

</summary>

created: array of string

Class names for which a new namespace was provisioned.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20created">Link to this property</a>

deleted: array of string

Class names whose namespace was deleted by a <code>deleted</code> tombstone.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20deleted">Link to this property</a>

<details>

<summary>

info: array of object {class, message, scenario, 2 more }

Non-blocking info entries (stale tombstones, tombstone applied with class still in code). See <code>exports_reconciliation_info</code>.

</summary>

class: string

The class name the info entry is about.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20class">Link to this property</a>

message: string

Human-readable explanation.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

scenario: "code\_class\_not\_in\_exports"or "provisioned\_class\_missing\_from\_config"or "config\_export\_not\_in\_code"or 30 more

Stable, machine-readable tag identifying which reconciliation scenario produced an error, warning, or info entry. Clients may branch on this value instead of parsing <code>message</code>.

</summary>

One of the following:

"code\_class\_not\_in\_exports"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%200">Link to this property</a>

"provisioned\_class\_missing\_from\_config"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%201">Link to this property</a>

"config\_export\_not\_in\_code"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%202">Link to this property</a>

"config\_references\_nonexistent\_class"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%203">Link to this property</a>

"orphaned\_provisioned\_namespace"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%204">Link to this property</a>

"storage\_type\_mismatch"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%205">Link to this property</a>

"free\_tier\_requires\_sqlite"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%206">Link to this property</a>

"invalid\_export"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%207">Link to this property</a>

"tombstone\_delete\_class\_still\_in\_code"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%208">Link to this property</a>

"tombstone\_delete\_blocked\_by\_external\_bindings"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%209">Link to this property</a>

"tombstone\_renamed\_to\_occupied"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2010">Link to this property</a>

"transferred\_pending\_not\_found"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2011">Link to this property</a>

"transferred\_target\_missing"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2012">Link to this property</a>

"transferred\_target\_mismatch"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2013">Link to this property</a>

"phase\_one\_transfer\_source\_missing"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2014">Link to this property</a>

"phase\_one\_transfer\_source\_namespace\_missing"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2015">Link to this property</a>

"phase\_one\_transfer\_target\_class\_provisioned"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2016">Link to this property</a>

"phase\_one\_transfer\_after\_commit\_mismatch"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2017">Link to this property</a>

"phase\_one\_transfer\_duplicate"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2018">Link to this property</a>

"phase\_one\_transfer\_target\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2019">Link to this property</a>

"phase\_one\_transfer\_source\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2020">Link to this property</a>

"transferred\_source\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2021">Link to this property</a>

"transferred\_target\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2022">Link to this property</a>

"container\_undeclared\_reference"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2023">Link to this property</a>

"container\_class\_not\_durable\_object"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2024">Link to this property</a>

"container\_wiring\_inconsistent"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2025">Link to this property</a>

"container\_multiple\_durable\_objects"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2026">Link to this property</a>

"transfer\_container\_parity\_mismatch"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2027">Link to this property</a>

"transfer\_container\_parity\_mismatch\_on\_commit"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2028">Link to this property</a>

"tombstone\_class\_still\_in\_code"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2029">Link to this property</a>

"stale\_tombstone"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2030">Link to this property</a>

"transfer\_receive\_already\_applied"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2031">Link to this property</a>

"transfer\_receive\_cleanup\_complete"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2032">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario">Link to this property</a>

namespace\_id: optional string

The provisioned namespace the entry relates to, when applicable.

formatuuid

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20namespace_id">Link to this property</a>

referencing\_scripts: optional array of string

Other Workers in the account that still bind to the affected class. Advisory: while non-empty the tombstone is not yet safe to remove — redeploy these Workers with bindings re-pointed first.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20referencing_scripts">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info">Link to this property</a>

removable\_entries: array of string

Source class names whose tombstone entry is now stale and safe to delete from <code>exports</code> (no remaining referencing scripts).

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20removable_entries">Link to this property</a>

<details>

<summary>

renamed: array of object {from, to }

Applied <code>renamed</code> tombstones.

</summary>

from: string

The original (source) class name.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20renamed%20%3E%20(items)%20%3E%20(property)%20from">Link to this property</a>

to: string

The new class name (<code>renamed_to</code>).

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20renamed%20%3E%20(items)%20%3E%20(property)%20to">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20renamed">Link to this property</a>

<details>

<summary>

transfer\_pending: array of object {class, from }

Phase-1 transfer hints recorded on the target side.

</summary>

class: string

The target-side class name awaiting transfer.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20transfer_pending%20%3E%20(items)%20%3E%20(property)%20class">Link to this property</a>

from: string

The source script the namespace will be transferred from.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20transfer_pending%20%3E%20(items)%20%3E%20(property)%20from">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20transfer_pending">Link to this property</a>

<details>

<summary>

transferred: array of object {class, phase, to }

Committed <code>transferred</code> tombstones (phase-2).

</summary>

class: string

The source class name that was transferred.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20transferred%20%3E%20(items)%20%3E%20(property)%20class">Link to this property</a>

phase: "committed"

The transfer phase. Currently always <code>committed</code>.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20transferred%20%3E%20(items)%20%3E%20(property)%20phase">Link to this property</a>

to: string

The destination script that now owns the namespace.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20transferred%20%3E%20(items)%20%3E%20(property)%20to">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20transferred">Link to this property</a>

updated: array of string

Class names whose provisioned namespace was mutated in place.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20updated">Link to this property</a>

<details>

<summary>

warnings: array of object {class, message, scenario, namespace\_id }

Non-blocking warnings. See <code>exports_reconciliation_warning</code>.

</summary>

class: string

The class name the warning is about.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20class">Link to this property</a>

message: string

Human-readable explanation of the warning.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

scenario: "code\_class\_not\_in\_exports"or "provisioned\_class\_missing\_from\_config"or "config\_export\_not\_in\_code"or 30 more

Stable, machine-readable tag identifying which reconciliation scenario produced an error, warning, or info entry. Clients may branch on this value instead of parsing <code>message</code>.

</summary>

One of the following:

"code\_class\_not\_in\_exports"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%200">Link to this property</a>

"provisioned\_class\_missing\_from\_config"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%201">Link to this property</a>

"config\_export\_not\_in\_code"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%202">Link to this property</a>

"config\_references\_nonexistent\_class"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%203">Link to this property</a>

"orphaned\_provisioned\_namespace"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%204">Link to this property</a>

"storage\_type\_mismatch"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%205">Link to this property</a>

"free\_tier\_requires\_sqlite"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%206">Link to this property</a>

"invalid\_export"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%207">Link to this property</a>

"tombstone\_delete\_class\_still\_in\_code"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%208">Link to this property</a>

"tombstone\_delete\_blocked\_by\_external\_bindings"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%209">Link to this property</a>

"tombstone\_renamed\_to\_occupied"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2010">Link to this property</a>

"transferred\_pending\_not\_found"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2011">Link to this property</a>

"transferred\_target\_missing"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2012">Link to this property</a>

"transferred\_target\_mismatch"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2013">Link to this property</a>

"phase\_one\_transfer\_source\_missing"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2014">Link to this property</a>

"phase\_one\_transfer\_source\_namespace\_missing"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2015">Link to this property</a>

"phase\_one\_transfer\_target\_class\_provisioned"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2016">Link to this property</a>

"phase\_one\_transfer\_after\_commit\_mismatch"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2017">Link to this property</a>

"phase\_one\_transfer\_duplicate"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2018">Link to this property</a>

"phase\_one\_transfer\_target\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2019">Link to this property</a>

"phase\_one\_transfer\_source\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2020">Link to this property</a>

"transferred\_source\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2021">Link to this property</a>

"transferred\_target\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2022">Link to this property</a>

"container\_undeclared\_reference"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2023">Link to this property</a>

"container\_class\_not\_durable\_object"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2024">Link to this property</a>

"container\_wiring\_inconsistent"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2025">Link to this property</a>

"container\_multiple\_durable\_objects"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2026">Link to this property</a>

"transfer\_container\_parity\_mismatch"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2027">Link to this property</a>

"transfer\_container\_parity\_mismatch\_on\_commit"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2028">Link to this property</a>

"tombstone\_class\_still\_in\_code"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2029">Link to this property</a>

"stale\_tombstone"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2030">Link to this property</a>

"transfer\_receive\_already\_applied"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2031">Link to this property</a>

"transfer\_receive\_cleanup\_complete"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2032">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario">Link to this property</a>

namespace\_id: optional string

The provisioned namespace the warning relates to, when applicable.

formatuuid

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20namespace_id">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation">Link to this property</a>

<details>

<summary>

metadata: optional object {author\_email, author\_id, created\_on, 3 more }

</summary>

author\_email: optional string

Email of the user who created the version.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20author_email">Link to this property</a>

author\_id: optional string

Identifier of the user who created the version.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20author_id">Link to this property</a>

created\_on: optional string

When the version was created.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20created_on">Link to this property</a>

hasPreview: optional boolean

Whether the version can be previewed.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20hasPreview">Link to this property</a>

modified\_on: optional string

When the version was last modified.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20modified_on">Link to this property</a>

<details>

<summary>

source: optional "unknown"or "api"or "wrangler"or 8 more

The source of the version upload.

</summary>

One of the following:

"unknown"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"api"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

"wrangler"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%202">Link to this property</a>

"terraform"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%203">Link to this property</a>

"dash"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%204">Link to this property</a>

"cf\_cli"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%205">Link to this property</a>

"dash\_template"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%206">Link to this property</a>

"integration"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%207">Link to this property</a>

"quick\_editor"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%208">Link to this property</a>

"playground"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%209">Link to this property</a>

"workersci"

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source%20%3E%20(member)%2010">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20metadata%20%3E%20(property)%20source">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20metadata">Link to this property</a>

number: optional number

Sequential version number.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20number">Link to this property</a>

startup\_time\_ms: optional number

Time in milliseconds spent on <a href="https://developers.cloudflare.com/workers/platform/limits/#worker-startup-time">Worker startup</a>.

<a href="#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)%20%3E%20(property)%20startup_time_ms">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.versions%20%3E%20(model)%20version_create_response%20%3E%20(schema)>)

#### ScriptsSecrets

##### [List secrets bound to a Worker script](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/secrets/methods/list)

GET/accounts/{account\_id}/workers/scripts/{script\_name}/secrets

##### [Get a secret binding](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/secrets/methods/get)

GET/accounts/{account\_id}/workers/scripts/{script\_name}/secrets/{secret\_name}

##### [Add a secret to a Worker script](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/secrets/methods/update)

PUT/accounts/{account\_id}/workers/scripts/{script\_name}/secrets

##### [Delete Worker script secret](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/secrets/methods/delete)

DELETE/accounts/{account\_id}/workers/scripts/{script\_name}/secrets/{secret\_name}

##### [Patch multiple Worker script secrets](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/secrets/methods/bulk_update)

PATCH/accounts/{account\_id}/workers/scripts/{script\_name}/secrets-bulk

##### ModelsExpand Collapse

<details>

<summary>

SecretListResponse = object {name, text, type } or object {algorithm, format, name, 4 more }

A secret value accessible through a binding.

</summary>

One of the following:

<details>

<summary>

SecretText object {name, text, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20name">Link to this property</a>

text: string

The secret value to use.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20text">Link to this property</a>

type: "secret\_text"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

SecretKey object {algorithm, format, name, 4 more }

</summary>

algorithm: unknown

Algorithm-specific key parameters. <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#algorithm">Learn more</a>.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20algorithm">Link to this property</a>

<details>

<summary>

format: "raw"or "pkcs8"or "spki"or "jwk"

Data format of the key. <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#format">Learn more</a>.

</summary>

One of the following:

"raw"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%3E%20(member)%200">Link to this property</a>

"pkcs8"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%3E%20(member)%201">Link to this property</a>

"spki"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%3E%20(member)%202">Link to this property</a>

"jwk"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20format">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20name">Link to this property</a>

type: "secret\_key"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

usages: array of "encrypt"or "decrypt"or "sign"or 5 more

Allowed operations with the key. <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#keyUsages">Learn more</a>.

</summary>

One of the following:

"encrypt"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"decrypt"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"sign"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"verify"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"deriveKey"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

"deriveBits"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%205">Link to this property</a>

"wrapKey"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%206">Link to this property</a>

"unwrapKey"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages">Link to this property</a>

key\_base64: optional string

Base64-encoded key data. Required if <code>format</code> is “raw”, “pkcs8”, or “spki”.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20key_base64">Link to this property</a>

key\_jwk: optional unknown

Key data in <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#json_web_key">JSON Web Key</a> format. Required if <code>format</code> is “jwk”.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20key_jwk">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_list_response%20%3E%20(schema)>)

<details>

<summary>

SecretGetResponse = object {name, text, type } or object {algorithm, format, name, 4 more }

A secret value accessible through a binding.

</summary>

One of the following:

<details>

<summary>

SecretText object {name, text, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20name">Link to this property</a>

text: string

The secret value to use.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20text">Link to this property</a>

type: "secret\_text"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

SecretKey object {algorithm, format, name, 4 more }

</summary>

algorithm: unknown

Algorithm-specific key parameters. <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#algorithm">Learn more</a>.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20algorithm">Link to this property</a>

<details>

<summary>

format: "raw"or "pkcs8"or "spki"or "jwk"

Data format of the key. <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#format">Learn more</a>.

</summary>

One of the following:

"raw"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%3E%20(member)%200">Link to this property</a>

"pkcs8"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%3E%20(member)%201">Link to this property</a>

"spki"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%3E%20(member)%202">Link to this property</a>

"jwk"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20format">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20name">Link to this property</a>

type: "secret\_key"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

usages: array of "encrypt"or "decrypt"or "sign"or 5 more

Allowed operations with the key. <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#keyUsages">Learn more</a>.

</summary>

One of the following:

"encrypt"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"decrypt"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"sign"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"verify"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"deriveKey"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

"deriveBits"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%205">Link to this property</a>

"wrapKey"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%206">Link to this property</a>

"unwrapKey"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages">Link to this property</a>

key\_base64: optional string

Base64-encoded key data. Required if <code>format</code> is “raw”, “pkcs8”, or “spki”.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20key_base64">Link to this property</a>

key\_jwk: optional unknown

Key data in <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#json_web_key">JSON Web Key</a> format. Required if <code>format</code> is “jwk”.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20key_jwk">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_get_response%20%3E%20(schema)>)

<details>

<summary>

SecretUpdateResponse = object {name, text, type } or object {algorithm, format, name, 4 more }

A secret value accessible through a binding.

</summary>

One of the following:

<details>

<summary>

SecretText object {name, text, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20name">Link to this property</a>

text: string

The secret value to use.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20text">Link to this property</a>

type: "secret\_text"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

SecretKey object {algorithm, format, name, 4 more }

</summary>

algorithm: unknown

Algorithm-specific key parameters. <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#algorithm">Learn more</a>.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20algorithm">Link to this property</a>

<details>

<summary>

format: "raw"or "pkcs8"or "spki"or "jwk"

Data format of the key. <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#format">Learn more</a>.

</summary>

One of the following:

"raw"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%3E%20(member)%200">Link to this property</a>

"pkcs8"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%3E%20(member)%201">Link to this property</a>

"spki"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%3E%20(member)%202">Link to this property</a>

"jwk"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20format">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20name">Link to this property</a>

type: "secret\_key"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

usages: array of "encrypt"or "decrypt"or "sign"or 5 more

Allowed operations with the key. <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#keyUsages">Learn more</a>.

</summary>

One of the following:

"encrypt"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"decrypt"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"sign"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"verify"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"deriveKey"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

"deriveBits"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%205">Link to this property</a>

"wrapKey"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%206">Link to this property</a>

"unwrapKey"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20usages">Link to this property</a>

key\_base64: optional string

Base64-encoded key data. Required if <code>format</code> is “raw”, “pkcs8”, or “spki”.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20key_base64">Link to this property</a>

key\_jwk: optional unknown

Key data in <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#json_web_key">JSON Web Key</a> format. Required if <code>format</code> is “jwk”.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%201%20%3E%20(property)%20key_jwk">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_update_response%20%3E%20(schema)>)

SecretDeleteResponse = unknown

[Link to this property](<#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_delete_response%20%3E%20(schema)>)

<details>

<summary>

SecretBulkUpdateResponse = map\[object {name, text, type } or object {algorithm, format, name, 4 more } ]

Map of secret names to secret metadata for resulting secrets.

</summary>

One of the following:

<details>

<summary>

SecretText object {name, text, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20name">Link to this property</a>

text: string

The secret value to use.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20text">Link to this property</a>

type: "secret\_text"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

SecretKey object {algorithm, format, name, 4 more }

</summary>

algorithm: unknown

Algorithm-specific key parameters. <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#algorithm">Learn more</a>.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20algorithm">Link to this property</a>

<details>

<summary>

format: "raw"or "pkcs8"or "spki"or "jwk"

Data format of the key. <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#format">Learn more</a>.

</summary>

One of the following:

"raw"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%3E%20(member)%200">Link to this property</a>

"pkcs8"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%3E%20(member)%201">Link to this property</a>

"spki"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%3E%20(member)%202">Link to this property</a>

"jwk"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20format%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20format">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20name">Link to this property</a>

type: "secret\_key"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

usages: array of "encrypt"or "decrypt"or "sign"or 5 more

Allowed operations with the key. <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#keyUsages">Learn more</a>.

</summary>

One of the following:

"encrypt"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"decrypt"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"sign"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"verify"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"deriveKey"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

"deriveBits"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%205">Link to this property</a>

"wrapKey"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%206">Link to this property</a>

"unwrapKey"

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20usages">Link to this property</a>

key\_base64: optional string

Base64-encoded key data. Required if <code>format</code> is “raw”, “pkcs8”, or “spki”.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20key_base64">Link to this property</a>

key\_jwk: optional unknown

Key data in <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#json_web_key">JSON Web Key</a> format. Required if <code>format</code> is “jwk”.

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20key_jwk">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.secrets%20%3E%20(model)%20secret_bulk_update_response%20%3E%20(schema)>)

#### ScriptsScript And Version Settings

##### [Get Worker Script and Version Settings](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/script_and_version_settings/methods/get)

GET/accounts/{account\_id}/workers/scripts/{script\_name}/settings

##### [Patch Worker Script and Version Settings](https://developers.cloudflare.com/api/resources/workers/subresources/scripts/subresources/script_and_version_settings/methods/edit)

PATCH/accounts/{account\_id}/workers/scripts/{script\_name}/settings

##### ModelsExpand Collapse

<details>

<summary>

ScriptAndVersionSettingGetResponse object {annotations, bindings, cache\_options, 12 more }

</summary>

<details>

<summary>

annotations: optional object {"workers/message", "workers/tag", "workers/triggered\_by" }

Annotations for the Worker version. Annotations are not inherited across settings updates; omitting this field means the new version will have no annotations.

</summary>

"workers/message": optional string

Human-readable message about the version. Truncated to 1000 bytes if longer.

maxLength1000

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(property)%20workers%2Fmessage">Link to this property</a>

"workers/tag": optional string

User-provided identifier for the version. Maximum 100 bytes.

maxLength100

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(property)%20workers%2Ftag">Link to this property</a>

"workers/triggered\_by": optional string

Operation that triggered the creation of the version. This is read-only and set by the server.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(property)%20workers%2Ftriggered_by">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20annotations">Link to this property</a>

<details>

<summary>

bindings: optional array of object {name, type } or object {instance\_name, name, type, namespace } or object {name, namespace, type } or 35 more

List of bindings attached to a Worker. You can find more about bindings on our docs: <a href="https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings">https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings</a>.

</summary>

One of the following:

<details>

<summary>

AI object {name, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20name">Link to this property</a>

type: "ai"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

AISearch object {instance\_name, name, type, namespace }

</summary>

instance\_name: string

The user-chosen instance name. Must exist at deploy time. The worker can search, chat, update, and manage items/jobs on this instance.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20instance_name">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20name">Link to this property</a>

type: "ai\_search"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

namespace: optional string

The namespace the instance belongs to. Defaults to “default” if omitted. Customers who don’t use namespaces can simply omit this field.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20namespace">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

AISearchNamespace object {name, namespace, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20name">Link to this property</a>

namespace: string

The user-chosen namespace name. Must exist before deploy — Wrangler handles auto-creation on deploy failure (R2 bucket pattern). The “default” namespace is auto-created by config-api for new accounts. Grants full access (CRUD + search + chat) to all instances within the namespace.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20namespace">Link to this property</a>

type: "ai\_search\_namespace"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

Messaging object {name, namespace, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20name">Link to this property</a>

namespace: string

The Messaging namespace to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20namespace">Link to this property</a>

type: "messaging"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

AnalyticsEngine object {dataset, name, type }

</summary>

dataset: string

The name of the dataset to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20dataset">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20name">Link to this property</a>

type: "analytics\_engine"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

Artifacts object {name, namespace, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20name">Link to this property</a>

namespace: string

The Artifacts namespace exposed to the Worker in the Worker’s account. Must be 2-63 characters, start with an ASCII alphanumeric character, contain only ASCII alphanumeric characters, dots, underscores, and hyphens, and must not end with a hyphen. The namespace does not need to be created before binding it.

maxLength63

minLength2

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20namespace">Link to this property</a>

type: "artifacts"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%205">Link to this property</a>

<details>

<summary>

Assets object {name, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20name">Link to this property</a>

type: "assets"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%206">Link to this property</a>

<details>

<summary>

Browser object {name, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(property)%20name">Link to this property</a>

type: "browser"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%207">Link to this property</a>

<details>

<summary>

D1 object {database\_id, name, type, id }

</summary>

database\_id: string

Identifier of the D1 database to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20database_id">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20name">Link to this property</a>

type: "d1"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20type">Link to this property</a>

Deprecatedid: optional string

This property has been renamed to <code>database_id</code>.

Identifier of the D1 database to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20id">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%208">Link to this property</a>

<details>

<summary>

DataBlob object {name, part, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20name">Link to this property</a>

part: string

The name of the file containing the data content. Only accepted for <code>service worker syntax</code> Workers.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20part">Link to this property</a>

Deprecatedtype: "data\_blob"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%209">Link to this property</a>

<details>

<summary>

DispatchNamespace object {name, namespace, type, outbound }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20name">Link to this property</a>

namespace: string

The name of the dispatch namespace.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20namespace">Link to this property</a>

type: "dispatch\_namespace"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

outbound: optional object {params, worker }

Outbound worker.

</summary>

<details>

<summary>

params: optional array of object {name }

Pass information from the Dispatch Worker to the Outbound Worker through the parameters.

</summary>

name: string

Name of the parameter.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20outbound%20%3E%20(property)%20params%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20outbound%20%3E%20(property)%20params">Link to this property</a>

<details>

<summary>

worker: optional object {entrypoint, environment, service }

Outbound worker.

</summary>

entrypoint: optional string

Entrypoint to invoke on the outbound worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20outbound%20%3E%20(property)%20worker%20%3E%20(property)%20entrypoint">Link to this property</a>

environment: optional string

Environment of the outbound worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20outbound%20%3E%20(property)%20worker%20%3E%20(property)%20environment">Link to this property</a>

service: optional string

Name of the outbound worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20outbound%20%3E%20(property)%20worker%20%3E%20(property)%20service">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20outbound%20%3E%20(property)%20worker">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20outbound">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2010">Link to this property</a>

<details>

<summary>

DurableObjectNamespace object {name, type, class\_name, 4 more }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20name">Link to this property</a>

type: "durable\_object\_namespace"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20type">Link to this property</a>

class\_name: optional string

The exported class name of the Durable Object.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20class_name">Link to this property</a>

dispatch\_namespace: optional string

The dispatch namespace the Durable Object script belongs to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20dispatch_namespace">Link to this property</a>

environment: optional string

The environment of the script\_name to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20environment">Link to this property</a>

namespace\_id: optional string

Namespace identifier tag.

maxLength32

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20namespace_id">Link to this property</a>

script\_name: optional string

The script where the Durable Object is defined, if it is external to this Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20script_name">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2011">Link to this property</a>

<details>

<summary>

Hyperdrive object {id, name, type }

</summary>

id: string

Identifier of the Hyperdrive connection to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20id">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20name">Link to this property</a>

type: "hyperdrive"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2012">Link to this property</a>

<details>

<summary>

Inherit object {name, type, old\_name, version\_id }

</summary>

name: string

The name of the inherited binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(property)%20name">Link to this property</a>

type: "inherit"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(property)%20type">Link to this property</a>

old\_name: optional string

The old name of the inherited binding. If set, the binding will be renamed from <code>old_name</code> to <code>name</code> in the new version. If not set, the binding will keep the same name between versions.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(property)%20old_name">Link to this property</a>

version\_id: optional string

Identifier for the version to inherit the binding from, which can be the version ID or the literal “latest” to inherit from the latest version. Defaults to inheriting the binding from the latest version.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(property)%20version_id">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2013">Link to this property</a>

<details>

<summary>

Images object {name, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(property)%20name">Link to this property</a>

type: "images"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2014">Link to this property</a>

<details>

<summary>

Json object {json, name, type }

</summary>

json: unknown

JSON data to use.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20json">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20name">Link to this property</a>

type: "json"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2015">Link to this property</a>

<details>

<summary>

KVNamespace object {name, namespace\_id, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(property)%20name">Link to this property</a>

namespace\_id: string

Namespace identifier tag.

maxLength32

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(property)%20namespace_id">Link to this property</a>

type: "kv\_namespace"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2016">Link to this property</a>

<details>

<summary>

Media object {name, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20name">Link to this property</a>

type: "media"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2017">Link to this property</a>

<details>

<summary>

MTLSCertificate object {certificate\_id, name, type }

</summary>

certificate\_id: string

Identifier of the certificate to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(property)%20certificate_id">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(property)%20name">Link to this property</a>

type: "mtls\_certificate"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2018">Link to this property</a>

<details>

<summary>

PlainText object {name, text, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(property)%20name">Link to this property</a>

text: string

The text value to use.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(property)%20text">Link to this property</a>

type: "plain\_text"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2019">Link to this property</a>

<details>

<summary>

Pipelines object {name, pipeline, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20name">Link to this property</a>

pipeline: string

Name of the Pipeline to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20pipeline">Link to this property</a>

type: "pipelines"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2020">Link to this property</a>

<details>

<summary>

K2 object {name, stream, type }

A K2 stream binding. Available only to accounts enabled for K2.

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2021%20%3E%20(property)%20name">Link to this property</a>

stream: string

ID of a K2 stream owned by the account deploying the Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2021%20%3E%20(property)%20stream">Link to this property</a>

type: "k2"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2021%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2021">Link to this property</a>

<details>

<summary>

Queue object {name, queue\_name, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2022%20%3E%20(property)%20name">Link to this property</a>

queue\_name: string

Name of the Queue to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2022%20%3E%20(property)%20queue_name">Link to this property</a>

type: "queue"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2022%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2022">Link to this property</a>

<details>

<summary>

Ratelimit object {name, namespace\_id, simple, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2023%20%3E%20(property)%20name">Link to this property</a>

namespace\_id: string

Identifier of the rate limit namespace to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2023%20%3E%20(property)%20namespace_id">Link to this property</a>

<details>

<summary>

simple: object {limit, period, mitigation\_timeout }

The rate limit configuration.

</summary>

limit: number

The limit (requests per period).

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2023%20%3E%20(property)%20simple%20%3E%20(property)%20limit">Link to this property</a>

period: number

The period in seconds.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2023%20%3E%20(property)%20simple%20%3E%20(property)%20period">Link to this property</a>

mitigation\_timeout: optional number

Duration in seconds to apply the mitigation action after the rate limit is exceeded. Valid values are 0 (disabled), 10, or multiples of 60 up to 86400. Must be greater than or equal to the period when non-zero.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2023%20%3E%20(property)%20simple%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2023%20%3E%20(property)%20simple">Link to this property</a>

type: "ratelimit"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2023%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2023">Link to this property</a>

<details>

<summary>

R2Bucket object {bucket\_name, name, type, jurisdiction }

</summary>

bucket\_name: string

R2 bucket to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2024%20%3E%20(property)%20bucket_name">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2024%20%3E%20(property)%20name">Link to this property</a>

type: "r2\_bucket"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2024%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

jurisdiction: optional "eu"or "fedramp"or "fedramp-high"or "us"

The <a href="https://developers.cloudflare.com/r2/reference/data-location/#jurisdictional-restrictions">jurisdiction</a> of the R2 bucket.

</summary>

One of the following:

"eu"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2024%20%3E%20(property)%20jurisdiction%20%3E%20(member)%200">Link to this property</a>

"fedramp"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2024%20%3E%20(property)%20jurisdiction%20%3E%20(member)%201">Link to this property</a>

"fedramp-high"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2024%20%3E%20(property)%20jurisdiction%20%3E%20(member)%202">Link to this property</a>

"us"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2024%20%3E%20(property)%20jurisdiction%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2024%20%3E%20(property)%20jurisdiction">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2024">Link to this property</a>

<details>

<summary>

SecretText object {name, text, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2025%20%3E%20(property)%20name">Link to this property</a>

text: string

The secret value to use.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2025%20%3E%20(property)%20text">Link to this property</a>

type: "secret\_text"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2025%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2025">Link to this property</a>

<details>

<summary>

SendEmail object {name, type, allowed\_destination\_addresses, 2 more }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2026%20%3E%20(property)%20name">Link to this property</a>

type: "send\_email"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2026%20%3E%20(property)%20type">Link to this property</a>

allowed\_destination\_addresses: optional array of string

List of allowed destination addresses.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2026%20%3E%20(property)%20allowed_destination_addresses">Link to this property</a>

allowed\_sender\_addresses: optional array of string

List of allowed sender addresses.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2026%20%3E%20(property)%20allowed_sender_addresses">Link to this property</a>

destination\_address: optional string

Destination address for the email.

formatemail

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2026%20%3E%20(property)%20destination_address">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2026">Link to this property</a>

<details>

<summary>

Service object {name, service, type, 2 more }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2027%20%3E%20(property)%20name">Link to this property</a>

service: string

Name of Worker to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2027%20%3E%20(property)%20service">Link to this property</a>

type: "service"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2027%20%3E%20(property)%20type">Link to this property</a>

entrypoint: optional string

Entrypoint to invoke on the target Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2027%20%3E%20(property)%20entrypoint">Link to this property</a>

environment: optional string

Optional environment if the Worker utilizes one.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2027%20%3E%20(property)%20environment">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2027">Link to this property</a>

<details>

<summary>

TextBlob object {name, part, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2028%20%3E%20(property)%20name">Link to this property</a>

part: string

The name of the file containing the text content. Only accepted for <code>service worker syntax</code> Workers.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2028%20%3E%20(property)%20part">Link to this property</a>

Deprecatedtype: "text\_blob"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2028%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2028">Link to this property</a>

<details>

<summary>

Vectorize object {index\_name, name, type }

</summary>

index\_name: string

Name of the Vectorize index to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2029%20%3E%20(property)%20index_name">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2029%20%3E%20(property)%20name">Link to this property</a>

type: "vectorize"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2029%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2029">Link to this property</a>

<details>

<summary>

VersionMetadata object {name, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2030%20%3E%20(property)%20name">Link to this property</a>

type: "version\_metadata"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2030%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2030">Link to this property</a>

<details>

<summary>

SecretsStoreSecret object {name, secret\_name, store\_id, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2031%20%3E%20(property)%20name">Link to this property</a>

secret\_name: string

Name of the secret in the store.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2031%20%3E%20(property)%20secret_name">Link to this property</a>

store\_id: string

ID of the store containing the secret.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2031%20%3E%20(property)%20store_id">Link to this property</a>

type: "secrets\_store\_secret"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2031%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2031">Link to this property</a>

<details>

<summary>

Flagship object {app\_id, name, type }

</summary>

app\_id: string

ID of the Flagship app to bind to for feature flag evaluation.

maxLength128

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2032%20%3E%20(property)%20app_id">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2032%20%3E%20(property)%20name">Link to this property</a>

type: "flagship"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2032%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2032">Link to this property</a>

<details>

<summary>

SecretKey object {algorithm, format, name, 4 more }

</summary>

algorithm: unknown

Algorithm-specific key parameters. <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#algorithm">Learn more</a>.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20algorithm">Link to this property</a>

<details>

<summary>

format: "raw"or "pkcs8"or "spki"or "jwk"

Data format of the key. <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#format">Learn more</a>.

</summary>

One of the following:

"raw"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20format%20%3E%20(member)%200">Link to this property</a>

"pkcs8"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20format%20%3E%20(member)%201">Link to this property</a>

"spki"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20format%20%3E%20(member)%202">Link to this property</a>

"jwk"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20format%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20format">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20name">Link to this property</a>

type: "secret\_key"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

usages: array of "encrypt"or "decrypt"or "sign"or 5 more

Allowed operations with the key. <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#keyUsages">Learn more</a>.

</summary>

One of the following:

"encrypt"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"decrypt"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"sign"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"verify"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"deriveKey"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

"deriveBits"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%205">Link to this property</a>

"wrapKey"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%206">Link to this property</a>

"unwrapKey"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20usages">Link to this property</a>

key\_base64: optional string

Base64-encoded key data. Required if <code>format</code> is “raw”, “pkcs8”, or “spki”.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20key_base64">Link to this property</a>

key\_jwk: optional unknown

Key data in <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#json_web_key">JSON Web Key</a> format. Required if <code>format</code> is “jwk”.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20key_jwk">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033">Link to this property</a>

<details>

<summary>

Workflow object {name, type, workflow\_name, 2 more }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2034%20%3E%20(property)%20name">Link to this property</a>

type: "workflow"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2034%20%3E%20(property)%20type">Link to this property</a>

workflow\_name: string

Name of the Workflow to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2034%20%3E%20(property)%20workflow_name">Link to this property</a>

class\_name: optional string

Class name of the Workflow. Should only be provided if the Workflow belongs to this script.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2034%20%3E%20(property)%20class_name">Link to this property</a>

script\_name: optional string

Script name that contains the Workflow. If not provided, defaults to this script name.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2034%20%3E%20(property)%20script_name">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2034">Link to this property</a>

<details>

<summary>

WasmModule object {name, part, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2035%20%3E%20(property)%20name">Link to this property</a>

part: string

The name of the file containing the WebAssembly module content. Only accepted for <code>service worker syntax</code> Workers.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2035%20%3E%20(property)%20part">Link to this property</a>

Deprecatedtype: "wasm\_module"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2035%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2035">Link to this property</a>

<details>

<summary>

VPCService object {name, service\_id, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2036%20%3E%20(property)%20name">Link to this property</a>

service\_id: string

Identifier of the VPC service to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2036%20%3E%20(property)%20service_id">Link to this property</a>

type: "vpc\_service"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2036%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2036">Link to this property</a>

<details>

<summary>

VPCNetwork object {name, type, identity, 2 more }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2037%20%3E%20(property)%20name">Link to this property</a>

type: "vpc\_network"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2037%20%3E%20(property)%20type">Link to this property</a>

identity: optional "runtime-email-alpha"

Enables Gateway identity for the binding. Requires network\_id to be “cf1:network” and cannot be combined with tunnel\_id.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2037%20%3E%20(property)%20identity">Link to this property</a>

network\_id: optional string

Identifier of the network to bind to. Only “cf1:network” is currently supported. Mutually exclusive with tunnel\_id.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2037%20%3E%20(property)%20network_id">Link to this property</a>

tunnel\_id: optional string

UUID of the Cloudflare Tunnel to bind to. Mutually exclusive with network\_id.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2037%20%3E%20(property)%20tunnel_id">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2037">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20bindings">Link to this property</a>

<details>

<summary>

cache\_options: optional object {enabled, cross\_version\_cache }

Global CacheW configuration for the Worker. When caching is on, the platform provisions a <code>cloudflare.app</code> zone for the Worker. A <code>type: worker</code> entry in the <code>exports</code> map can override this value for a single entrypoint.

</summary>

enabled: boolean

Whether caching is enabled for this Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20cache_options%20%3E%20(property)%20enabled">Link to this property</a>

cross\_version\_cache: optional boolean

Whether cached responses are shared across Worker version uploads. This is independent of <code>enabled</code>. It can stay true while caching is off, so the preference survives turning caching off and back on.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20cache_options%20%3E%20(property)%20cross_version_cache">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20cache_options">Link to this property</a>

compatibility\_date: optional string

Date indicating targeted support in the Workers runtime. Backwards incompatible fixes to the runtime following this date will not affect this Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20compatibility_date">Link to this property</a>

compatibility\_flags: optional array of string

Flags that enable or disable certain features in the Workers runtime. Used to enable upcoming features or opt in or out of specific changes not included in a <code>compatibility_date</code>.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20compatibility_flags">Link to this property</a>

<details>

<summary>

exports: optional map\[object {type, cache, state } or object {storage, type, container, state } or object {state, type } or 3 more]

Declarative exports for the Worker. Worker entrypoint entries (<code>type: worker</code>) carry cache configuration for that entrypoint.

</summary>

One of the following:

<details>

<summary>

Worker object {type, cache, state }

A named Worker entrypoint export (<code>type: worker</code>). Worker entrypoints are always live (<code>state: created</code>) and carry no storage or lifecycle fields. The optional <code>cache</code> block overrides the Worker’s global <code>cache_options.enabled</code> for this entrypoint.

</summary>

type: "worker"

Marks this entry as a Worker entrypoint export.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

cache: optional object {enabled }

Cache override for this entrypoint. Overrides the Worker’s global <code>cache_options.enabled</code> for this entrypoint only.

</summary>

enabled: boolean

Whether caching is enabled for this entrypoint.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20cache%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20cache">Link to this property</a>

state: optional "created"

Live export. May be omitted; defaults to <code>created</code>.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20state">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

WorkersDurableObjectExport object {storage, type, container, state }

A live Durable Object export (<code>state: created</code>, the default). The platform auto-provisions the namespace on first deploy, matches it on subsequent deploys, and never mutates or deletes it as a side effect of a code-only change. <code>storage</code> is required; <code>renamed_to</code>, <code>transferred_to</code> and <code>transfer_from</code> are not allowed on a live entry.

</summary>

<details>

<summary>

storage: "sqlite"or "legacy-kv"

Durable Object storage backend. <code>sqlite</code> is the recommended (and only) backend for new namespaces. <code>legacy-kv</code> is accepted only for a class whose namespace already exists as KV-backed; the <code>exports</code> flow never provisions a new <code>legacy-kv</code> namespace.

</summary>

One of the following:

"sqlite"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20storage%20%3E%20(member)%200">Link to this property</a>

"legacy-kv"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20storage%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20storage">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

container: optional string

Name of the container (declared in the upload’s <code>metadata.containers</code>) that backs this Durable Object. When set, the namespace is container-enabled. Valid only on live entries.

maxLength128

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20container">Link to this property</a>

state: optional "created"

Live export. May be omitted; defaults to <code>created</code>.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20state">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

WorkersDurableObjectDeletedExport object {state, type }

A <code>deleted</code> tombstone: retires the provisioned namespace for this class and all of its data. The class must be absent from the uploaded code and no other Worker in the account may bind to the namespace, otherwise the deploy is rejected. No other fields are allowed. Deletion is irreversible.

</summary>

state: "deleted"

Tombstone that deletes the namespace.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20state">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

WorkersDurableObjectRenamedExport object {renamed\_to, state, type }

A <code>renamed</code> tombstone: rewrites the provisioned namespace’s class name from this map key to <code>renamed_to</code>. The source class may stay in code during the rollout window (an info notice is emitted). <code>storage</code>, <code>transferred_to</code> and <code>transfer_from</code> are not allowed.

</summary>

renamed\_to: string

The destination class name. Must differ from the source class (the map key) and must be declared as a live (<code>created</code>) entry in the same <code>exports</code> map. Write-only: never present in GET responses.

maxLength128

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20renamed_to">Link to this property</a>

state: "renamed"

Tombstone that renames the namespace’s class.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20state">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

WorkersDurableObjectTransferredExport object {state, transferred\_to, type }

A <code>transferred</code> tombstone (source side of a two-phase transfer): hands ownership of the provisioned namespace to another script in the same account, named by <code>transferred_to</code>. The target must have already deployed a matching <code>expecting-transfer</code> entry. The source class may stay in code during the rollout window (an info notice is emitted). <code>storage</code>, <code>renamed_to</code> and <code>transfer_from</code> are not allowed.

</summary>

state: "transferred"

Tombstone that transfers the namespace to another script.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20state">Link to this property</a>

transferred\_to: string

The destination script name. Must be in the same account and the same dispatch-namespace context (or both non-dispatch). Cross-dispatch-namespace transfers are rejected. Write-only: never present in GET responses.

maxLength128

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20transferred_to">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

WorkersDurableObjectExpectingTransferExport object {state, storage, transfer\_from, 2 more }

The target side of a two-phase transfer (<code>state: expecting-transfer</code>). Declares that this script expects to receive a namespace for this class from the <code>transfer_from</code> script. This is a live entry, not a tombstone: bindings resolve through the source’s namespace until the source commits with a <code>transferred</code> tombstone. <code>storage</code> and <code>transfer_from</code> are required; <code>renamed_to</code> and <code>transferred_to</code> are not allowed.

</summary>

state: "expecting-transfer"

Target side of a two-phase transfer.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20state">Link to this property</a>

<details>

<summary>

storage: "sqlite"or "legacy-kv"

Durable Object storage backend. <code>sqlite</code> is the recommended (and only) backend for new namespaces. <code>legacy-kv</code> is accepted only for a class whose namespace already exists as KV-backed; the <code>exports</code> flow never provisions a new <code>legacy-kv</code> namespace.

</summary>

One of the following:

"sqlite"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20storage%20%3E%20(member)%200">Link to this property</a>

"legacy-kv"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20storage%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20storage">Link to this property</a>

transfer\_from: string

The source script name to receive the namespace from. Must be in the same account and dispatch-namespace context. Present on reads for <code>expecting-transfer</code> entries.

maxLength128

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20transfer_from">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

container: optional string

Name of the container (declared in the upload’s <code>metadata.containers</code>) that backs this Durable Object once the transfer settles. Valid only on live entries.

maxLength128

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20container">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports">Link to this property</a>

<details>

<summary>

exports\_reconciliation: optional object {created, deleted, info, 6 more }

Summary of the declarative exports reconciliation that ran on this upload. Populated only when the uploaded metadata included an <code>exports</code> block. Durable Object entries drive reconciliation; <code>type: worker</code> entries do not contribute to this summary.

</summary>

created: array of string

Class names for which a new namespace was provisioned.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20created">Link to this property</a>

deleted: array of string

Class names whose namespace was deleted by a <code>deleted</code> tombstone.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20deleted">Link to this property</a>

<details>

<summary>

info: array of object {class, message, scenario, 2 more }

Non-blocking info entries (stale tombstones, tombstone applied with class still in code). See <code>exports_reconciliation_info</code>.

</summary>

class: string

The class name the info entry is about.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20class">Link to this property</a>

message: string

Human-readable explanation.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

scenario: "code\_class\_not\_in\_exports"or "provisioned\_class\_missing\_from\_config"or "config\_export\_not\_in\_code"or 30 more

Stable, machine-readable tag identifying which reconciliation scenario produced an error, warning, or info entry. Clients may branch on this value instead of parsing <code>message</code>.

</summary>

One of the following:

"code\_class\_not\_in\_exports"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%200">Link to this property</a>

"provisioned\_class\_missing\_from\_config"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%201">Link to this property</a>

"config\_export\_not\_in\_code"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%202">Link to this property</a>

"config\_references\_nonexistent\_class"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%203">Link to this property</a>

"orphaned\_provisioned\_namespace"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%204">Link to this property</a>

"storage\_type\_mismatch"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%205">Link to this property</a>

"free\_tier\_requires\_sqlite"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%206">Link to this property</a>

"invalid\_export"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%207">Link to this property</a>

"tombstone\_delete\_class\_still\_in\_code"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%208">Link to this property</a>

"tombstone\_delete\_blocked\_by\_external\_bindings"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%209">Link to this property</a>

"tombstone\_renamed\_to\_occupied"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2010">Link to this property</a>

"transferred\_pending\_not\_found"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2011">Link to this property</a>

"transferred\_target\_missing"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2012">Link to this property</a>

"transferred\_target\_mismatch"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2013">Link to this property</a>

"phase\_one\_transfer\_source\_missing"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2014">Link to this property</a>

"phase\_one\_transfer\_source\_namespace\_missing"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2015">Link to this property</a>

"phase\_one\_transfer\_target\_class\_provisioned"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2016">Link to this property</a>

"phase\_one\_transfer\_after\_commit\_mismatch"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2017">Link to this property</a>

"phase\_one\_transfer\_duplicate"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2018">Link to this property</a>

"phase\_one\_transfer\_target\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2019">Link to this property</a>

"phase\_one\_transfer\_source\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2020">Link to this property</a>

"transferred\_source\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2021">Link to this property</a>

"transferred\_target\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2022">Link to this property</a>

"container\_undeclared\_reference"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2023">Link to this property</a>

"container\_class\_not\_durable\_object"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2024">Link to this property</a>

"container\_wiring\_inconsistent"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2025">Link to this property</a>

"container\_multiple\_durable\_objects"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2026">Link to this property</a>

"transfer\_container\_parity\_mismatch"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2027">Link to this property</a>

"transfer\_container\_parity\_mismatch\_on\_commit"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2028">Link to this property</a>

"tombstone\_class\_still\_in\_code"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2029">Link to this property</a>

"stale\_tombstone"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2030">Link to this property</a>

"transfer\_receive\_already\_applied"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2031">Link to this property</a>

"transfer\_receive\_cleanup\_complete"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2032">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario">Link to this property</a>

namespace\_id: optional string

The provisioned namespace the entry relates to, when applicable.

formatuuid

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20namespace_id">Link to this property</a>

referencing\_scripts: optional array of string

Other Workers in the account that still bind to the affected class. Advisory: while non-empty the tombstone is not yet safe to remove — redeploy these Workers with bindings re-pointed first.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20referencing_scripts">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info">Link to this property</a>

removable\_entries: array of string

Source class names whose tombstone entry is now stale and safe to delete from <code>exports</code> (no remaining referencing scripts).

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20removable_entries">Link to this property</a>

<details>

<summary>

renamed: array of object {from, to }

Applied <code>renamed</code> tombstones.

</summary>

from: string

The original (source) class name.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20renamed%20%3E%20(items)%20%3E%20(property)%20from">Link to this property</a>

to: string

The new class name (<code>renamed_to</code>).

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20renamed%20%3E%20(items)%20%3E%20(property)%20to">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20renamed">Link to this property</a>

<details>

<summary>

transfer\_pending: array of object {class, from }

Phase-1 transfer hints recorded on the target side.

</summary>

class: string

The target-side class name awaiting transfer.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20transfer_pending%20%3E%20(items)%20%3E%20(property)%20class">Link to this property</a>

from: string

The source script the namespace will be transferred from.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20transfer_pending%20%3E%20(items)%20%3E%20(property)%20from">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20transfer_pending">Link to this property</a>

<details>

<summary>

transferred: array of object {class, phase, to }

Committed <code>transferred</code> tombstones (phase-2).

</summary>

class: string

The source class name that was transferred.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20transferred%20%3E%20(items)%20%3E%20(property)%20class">Link to this property</a>

phase: "committed"

The transfer phase. Currently always <code>committed</code>.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20transferred%20%3E%20(items)%20%3E%20(property)%20phase">Link to this property</a>

to: string

The destination script that now owns the namespace.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20transferred%20%3E%20(items)%20%3E%20(property)%20to">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20transferred">Link to this property</a>

updated: array of string

Class names whose provisioned namespace was mutated in place.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20updated">Link to this property</a>

<details>

<summary>

warnings: array of object {class, message, scenario, namespace\_id }

Non-blocking warnings. See <code>exports_reconciliation_warning</code>.

</summary>

class: string

The class name the warning is about.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20class">Link to this property</a>

message: string

Human-readable explanation of the warning.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

scenario: "code\_class\_not\_in\_exports"or "provisioned\_class\_missing\_from\_config"or "config\_export\_not\_in\_code"or 30 more

Stable, machine-readable tag identifying which reconciliation scenario produced an error, warning, or info entry. Clients may branch on this value instead of parsing <code>message</code>.

</summary>

One of the following:

"code\_class\_not\_in\_exports"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%200">Link to this property</a>

"provisioned\_class\_missing\_from\_config"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%201">Link to this property</a>

"config\_export\_not\_in\_code"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%202">Link to this property</a>

"config\_references\_nonexistent\_class"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%203">Link to this property</a>

"orphaned\_provisioned\_namespace"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%204">Link to this property</a>

"storage\_type\_mismatch"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%205">Link to this property</a>

"free\_tier\_requires\_sqlite"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%206">Link to this property</a>

"invalid\_export"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%207">Link to this property</a>

"tombstone\_delete\_class\_still\_in\_code"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%208">Link to this property</a>

"tombstone\_delete\_blocked\_by\_external\_bindings"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%209">Link to this property</a>

"tombstone\_renamed\_to\_occupied"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2010">Link to this property</a>

"transferred\_pending\_not\_found"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2011">Link to this property</a>

"transferred\_target\_missing"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2012">Link to this property</a>

"transferred\_target\_mismatch"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2013">Link to this property</a>

"phase\_one\_transfer\_source\_missing"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2014">Link to this property</a>

"phase\_one\_transfer\_source\_namespace\_missing"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2015">Link to this property</a>

"phase\_one\_transfer\_target\_class\_provisioned"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2016">Link to this property</a>

"phase\_one\_transfer\_after\_commit\_mismatch"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2017">Link to this property</a>

"phase\_one\_transfer\_duplicate"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2018">Link to this property</a>

"phase\_one\_transfer\_target\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2019">Link to this property</a>

"phase\_one\_transfer\_source\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2020">Link to this property</a>

"transferred\_source\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2021">Link to this property</a>

"transferred\_target\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2022">Link to this property</a>

"container\_undeclared\_reference"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2023">Link to this property</a>

"container\_class\_not\_durable\_object"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2024">Link to this property</a>

"container\_wiring\_inconsistent"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2025">Link to this property</a>

"container\_multiple\_durable\_objects"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2026">Link to this property</a>

"transfer\_container\_parity\_mismatch"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2027">Link to this property</a>

"transfer\_container\_parity\_mismatch\_on\_commit"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2028">Link to this property</a>

"tombstone\_class\_still\_in\_code"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2029">Link to this property</a>

"stale\_tombstone"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2030">Link to this property</a>

"transfer\_receive\_already\_applied"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2031">Link to this property</a>

"transfer\_receive\_cleanup\_complete"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2032">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario">Link to this property</a>

namespace\_id: optional string

The provisioned namespace the warning relates to, when applicable.

formatuuid

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20namespace_id">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation">Link to this property</a>

<details>

<summary>

limits: optional object {cpu\_ms, subrequests }

Limits to apply for this Worker.

</summary>

cpu\_ms: optional number

The amount of CPU time this Worker can use in milliseconds.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20limits%20%3E%20(property)%20cpu_ms">Link to this property</a>

subrequests: optional number

The number of subrequests this Worker can make per request.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20limits%20%3E%20(property)%20subrequests">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20limits">Link to this property</a>

logpush: optional boolean

Whether Logpush is turned on for the Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20logpush">Link to this property</a>

<details>

<summary>

migrations: optional <a href="https://developers.cloudflare.com/api/resources/workers#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)">SingleStepMigration</a> { deleted\_classes, new\_classes, new\_sqlite\_classes, 4 more } or object {new\_tag, old\_tag, steps }

Migrations to apply for Durable Objects associated with this Worker.

</summary>

One of the following:

<details>

<summary>

SingleStepMigration object {deleted\_classes, new\_classes, new\_sqlite\_classes, 4 more }

A single set of migrations to apply.

</summary>

deleted\_classes: optional array of string

A list of classes to delete Durable Object namespaces from.

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20deleted_classes">Link to this property</a>

new\_classes: optional array of string

A list of classes to create Durable Object namespaces from.

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20new_classes">Link to this property</a>

new\_sqlite\_classes: optional array of string

A list of classes to create Durable Object namespaces with SQLite from.

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20new_sqlite_classes">Link to this property</a>

new\_tag: optional string

Tag to set as the latest migration tag.

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20new_tag">Link to this property</a>

old\_tag: optional string

Tag used to verify against the latest migration tag for this Worker. If they don’t match, the upload is rejected.

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20old_tag">Link to this property</a>

<details>

<summary>

renamed\_classes: optional array of object {from, to }

A list of classes with Durable Object namespaces that were renamed.

</summary>

from: optional string

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20renamed_classes%20%3E%20(items)%20%3E%20(property)%20from">Link to this property</a>

to: optional string

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20renamed_classes%20%3E%20(items)%20%3E%20(property)%20to">Link to this property</a>

</details>

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20renamed_classes">Link to this property</a>

<details>

<summary>

transferred\_classes: optional array of object {from, from\_script, to }

A list of transfers for Durable Object namespaces from a different Worker and class to a class defined in this Worker.

</summary>

from: optional string

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20transferred_classes%20%3E%20(items)%20%3E%20(property)%20from">Link to this property</a>

from\_script: optional string

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20transferred_classes%20%3E%20(items)%20%3E%20(property)%20from_script">Link to this property</a>

to: optional string

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20transferred_classes%20%3E%20(items)%20%3E%20(property)%20to">Link to this property</a>

</details>

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20transferred_classes">Link to this property</a>

</details>

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

WorkersMultipleStepMigrations object {new\_tag, old\_tag, steps }

</summary>

new\_tag: optional string

Tag to set as the latest migration tag.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20migrations%20%3E%20(variant)%201%20%3E%20(property)%20new_tag">Link to this property</a>

old\_tag: optional string

Tag used to verify against the latest migration tag for this Worker. If they don’t match, the upload is rejected.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20migrations%20%3E%20(variant)%201%20%3E%20(property)%20old_tag">Link to this property</a>

<details>

<summary>

steps: optional array of <a href="https://developers.cloudflare.com/api/resources/workers#(resource)%20workers%20%3E%20(model)%20migration_step%20%3E%20(schema)">MigrationStep</a> { deleted\_classes, new\_classes, new\_sqlite\_classes, 2 more }

Migrations to apply in order.

</summary>

deleted\_classes: optional array of string

A list of classes to delete Durable Object namespaces from.

<a href="#(resource)%20workers%20%3E%20(model)%20migration_step%20%3E%20(schema)%20%3E%20(property)%20deleted_classes">Link to this property</a>

new\_classes: optional array of string

A list of classes to create Durable Object namespaces from.

<a href="#(resource)%20workers%20%3E%20(model)%20migration_step%20%3E%20(schema)%20%3E%20(property)%20new_classes">Link to this property</a>

new\_sqlite\_classes: optional array of string

A list of classes to create Durable Object namespaces with SQLite from.

<a href="#(resource)%20workers%20%3E%20(model)%20migration_step%20%3E%20(schema)%20%3E%20(property)%20new_sqlite_classes">Link to this property</a>

<details>

<summary>

renamed\_classes: optional array of object {from, to }

A list of classes with Durable Object namespaces that were renamed.

</summary>

from: optional string

<a href="#(resource)%20workers%20%3E%20(model)%20migration_step%20%3E%20(schema)%20%3E%20(property)%20renamed_classes%20%3E%20(items)%20%3E%20(property)%20from">Link to this property</a>

to: optional string

<a href="#(resource)%20workers%20%3E%20(model)%20migration_step%20%3E%20(schema)%20%3E%20(property)%20renamed_classes%20%3E%20(items)%20%3E%20(property)%20to">Link to this property</a>

</details>

<a href="#(resource)%20workers%20%3E%20(model)%20migration_step%20%3E%20(schema)%20%3E%20(property)%20renamed_classes">Link to this property</a>

<details>

<summary>

transferred\_classes: optional array of object {from, from\_script, to }

A list of transfers for Durable Object namespaces from a different Worker and class to a class defined in this Worker.

</summary>

from: optional string

<a href="#(resource)%20workers%20%3E%20(model)%20migration_step%20%3E%20(schema)%20%3E%20(property)%20transferred_classes%20%3E%20(items)%20%3E%20(property)%20from">Link to this property</a>

from\_script: optional string

<a href="#(resource)%20workers%20%3E%20(model)%20migration_step%20%3E%20(schema)%20%3E%20(property)%20transferred_classes%20%3E%20(items)%20%3E%20(property)%20from_script">Link to this property</a>

to: optional string

<a href="#(resource)%20workers%20%3E%20(model)%20migration_step%20%3E%20(schema)%20%3E%20(property)%20transferred_classes%20%3E%20(items)%20%3E%20(property)%20to">Link to this property</a>

</details>

<a href="#(resource)%20workers%20%3E%20(model)%20migration_step%20%3E%20(schema)%20%3E%20(property)%20transferred_classes">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20migrations%20%3E%20(variant)%201%20%3E%20(property)%20steps">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20migrations%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20migrations">Link to this property</a>

<details>

<summary>

observability: optional object {enabled, head\_sampling\_rate, issues, 3 more }

Observability settings for the Worker.

</summary>

enabled: boolean

Whether observability is enabled for the Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20enabled">Link to this property</a>

head\_sampling\_rate: optional number

The sampling rate for incoming requests. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20head_sampling_rate">Link to this property</a>

<details>

<summary>

issues: optional object {enabled }

Real-time Issues settings for the Worker.

</summary>

enabled: optional boolean

Whether real-time Issues are enabled for the Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20issues%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20issues">Link to this property</a>

<details>

<summary>

logs: optional object {enabled, invocation\_logs, destinations, 2 more }

Log settings for the Worker.

</summary>

enabled: boolean

Whether logs are enabled for the Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20enabled">Link to this property</a>

invocation\_logs: boolean

Whether <a href="https://developers.cloudflare.com/workers/observability/logs/workers-logs/#invocation-logs">invocation logs</a> are enabled for the Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20invocation_logs">Link to this property</a>

destinations: optional array of string

A list of destinations where logs will be exported to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20destinations">Link to this property</a>

head\_sampling\_rate: optional number

The sampling rate for logs. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20head_sampling_rate">Link to this property</a>

persist: optional boolean

Whether log persistence is enabled for the Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20persist">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs">Link to this property</a>

redact\_query\_string: optional boolean

Whether query strings are removed from request URLs in logs and traces.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20redact_query_string">Link to this property</a>

<details>

<summary>

traces: optional object {destinations, enabled, head\_sampling\_rate, 2 more }

Trace settings for the Worker.

</summary>

destinations: optional array of string

A list of destinations where traces will be exported to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20destinations">Link to this property</a>

enabled: optional boolean

Whether traces are enabled for the Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20enabled">Link to this property</a>

head\_sampling\_rate: optional number

The sampling rate for traces. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20head_sampling_rate">Link to this property</a>

persist: optional boolean

Whether trace persistence is enabled for the Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20persist">Link to this property</a>

<details>

<summary>

propagation\_policy: optional "authenticated"or "accept"

Controls how inbound trace context (traceparent/tracestate) headers on incoming requests are handled. “authenticated” honors inbound trace context only when accompanied by a valid trace auth token. “accept” unconditionally accepts inbound trace context. Requires the trace propagation feature to be enabled. Returns null when the trace propagation feature is not enabled for the account.

</summary>

One of the following:

"authenticated"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20propagation_policy%20%3E%20(member)%200">Link to this property</a>

"accept"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20propagation_policy%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20propagation_policy">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20observability">Link to this property</a>

<details>

<summary>

placement: optional object {mode } or object {region } or object {hostname } or 5 more

Configuration for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>. Specify mode=‘smart’ for Smart Placement, or one of region/hostname/host.

</summary>

One of the following:

<details>

<summary>

Mode object {mode }

</summary>

mode: "smart"

Enables <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200%20%3E%20(property)%20mode">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

Region object {region }

</summary>

region: string

Cloud region for targeted placement in format ‘provider:region’.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201%20%3E%20(property)%20region">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

Hostname object {hostname }

</summary>

hostname: string

HTTP hostname for targeted placement.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202%20%3E%20(property)%20hostname">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

Host object {host }

</summary>

host: string

TCP host and port for targeted placement.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203%20%3E%20(property)%20host">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

object {mode, region }

</summary>

mode: "targeted"

Targeted placement mode.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20mode">Link to this property</a>

region: string

Cloud region for targeted placement in format ‘provider:region’.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20region">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

object {hostname, mode }

</summary>

hostname: string

HTTP hostname for targeted placement.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20hostname">Link to this property</a>

mode: "targeted"

Targeted placement mode.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20mode">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205">Link to this property</a>

<details>

<summary>

object {host, mode }

</summary>

host: string

TCP host and port for targeted placement.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20host">Link to this property</a>

mode: "targeted"

Targeted placement mode.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20mode">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206">Link to this property</a>

<details>

<summary>

object {mode, target }

</summary>

mode: "targeted"

Targeted placement mode.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20mode">Link to this property</a>

<details>

<summary>

target: array of object {region } or object {hostname } or object {host }

Array of placement targets (currently limited to single target).

</summary>

One of the following:

<details>

<summary>

Region object {region }

</summary>

region: string

Cloud region in format ‘provider:region’.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20region">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

Hostname object {hostname }

</summary>

hostname: string

HTTP hostname for targeted placement.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20hostname">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

Host object {host }

</summary>

host: string

TCP host:port for targeted placement.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20host">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20placement">Link to this property</a>

tags: optional array of string

Tags associated with the Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

<details>

<summary>

tail\_consumers: optional array of <a href="https://developers.cloudflare.com/api/resources/workers#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)">ConsumerScript</a> { service, environment, namespace }

List of Workers that will consume logs from the attached Worker.

</summary>

service: string

Name of Worker that is to be the consumer.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20service">Link to this property</a>

environment: optional string

Optional environment if the Worker utilizes one.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20environment">Link to this property</a>

namespace: optional string

Optional dispatch namespace the script belongs to.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20namespace">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20tail_consumers">Link to this property</a>

<details>

<summary>

usage\_model: optional "standard"or "bundled"or "unbound"

Usage model for the Worker invocations.

</summary>

One of the following:

"standard"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20usage_model%20%3E%20(member)%200">Link to this property</a>

"bundled"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20usage_model%20%3E%20(member)%201">Link to this property</a>

"unbound"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20usage_model%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)%20%3E%20(property)%20usage_model">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_get_response%20%3E%20(schema)>)

<details>

<summary>

ScriptAndVersionSettingEditResponse object {annotations, bindings, cache\_options, 12 more }

</summary>

<details>

<summary>

annotations: optional object {"workers/message", "workers/tag", "workers/triggered\_by" }

Annotations for the Worker version. Annotations are not inherited across settings updates; omitting this field means the new version will have no annotations.

</summary>

"workers/message": optional string

Human-readable message about the version. Truncated to 1000 bytes if longer.

maxLength1000

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(property)%20workers%2Fmessage">Link to this property</a>

"workers/tag": optional string

User-provided identifier for the version. Maximum 100 bytes.

maxLength100

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(property)%20workers%2Ftag">Link to this property</a>

"workers/triggered\_by": optional string

Operation that triggered the creation of the version. This is read-only and set by the server.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20annotations%20%3E%20(property)%20workers%2Ftriggered_by">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20annotations">Link to this property</a>

<details>

<summary>

bindings: optional array of object {name, type } or object {instance\_name, name, type, namespace } or object {name, namespace, type } or 35 more

List of bindings attached to a Worker. You can find more about bindings on our docs: <a href="https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings">https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings</a>.

</summary>

One of the following:

<details>

<summary>

AI object {name, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20name">Link to this property</a>

type: "ai"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

AISearch object {instance\_name, name, type, namespace }

</summary>

instance\_name: string

The user-chosen instance name. Must exist at deploy time. The worker can search, chat, update, and manage items/jobs on this instance.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20instance_name">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20name">Link to this property</a>

type: "ai\_search"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

namespace: optional string

The namespace the instance belongs to. Defaults to “default” if omitted. Customers who don’t use namespaces can simply omit this field.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20namespace">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

AISearchNamespace object {name, namespace, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20name">Link to this property</a>

namespace: string

The user-chosen namespace name. Must exist before deploy — Wrangler handles auto-creation on deploy failure (R2 bucket pattern). The “default” namespace is auto-created by config-api for new accounts. Grants full access (CRUD + search + chat) to all instances within the namespace.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20namespace">Link to this property</a>

type: "ai\_search\_namespace"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

Messaging object {name, namespace, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20name">Link to this property</a>

namespace: string

The Messaging namespace to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20namespace">Link to this property</a>

type: "messaging"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

AnalyticsEngine object {dataset, name, type }

</summary>

dataset: string

The name of the dataset to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20dataset">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20name">Link to this property</a>

type: "analytics\_engine"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

Artifacts object {name, namespace, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20name">Link to this property</a>

namespace: string

The Artifacts namespace exposed to the Worker in the Worker’s account. Must be 2-63 characters, start with an ASCII alphanumeric character, contain only ASCII alphanumeric characters, dots, underscores, and hyphens, and must not end with a hyphen. The namespace does not need to be created before binding it.

maxLength63

minLength2

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20namespace">Link to this property</a>

type: "artifacts"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%205">Link to this property</a>

<details>

<summary>

Assets object {name, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20name">Link to this property</a>

type: "assets"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%206">Link to this property</a>

<details>

<summary>

Browser object {name, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(property)%20name">Link to this property</a>

type: "browser"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%207">Link to this property</a>

<details>

<summary>

D1 object {database\_id, name, type, id }

</summary>

database\_id: string

Identifier of the D1 database to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20database_id">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20name">Link to this property</a>

type: "d1"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20type">Link to this property</a>

Deprecatedid: optional string

This property has been renamed to <code>database_id</code>.

Identifier of the D1 database to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(property)%20id">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%208">Link to this property</a>

<details>

<summary>

DataBlob object {name, part, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20name">Link to this property</a>

part: string

The name of the file containing the data content. Only accepted for <code>service worker syntax</code> Workers.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20part">Link to this property</a>

Deprecatedtype: "data\_blob"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%209">Link to this property</a>

<details>

<summary>

DispatchNamespace object {name, namespace, type, outbound }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20name">Link to this property</a>

namespace: string

The name of the dispatch namespace.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20namespace">Link to this property</a>

type: "dispatch\_namespace"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

outbound: optional object {params, worker }

Outbound worker.

</summary>

<details>

<summary>

params: optional array of object {name }

Pass information from the Dispatch Worker to the Outbound Worker through the parameters.

</summary>

name: string

Name of the parameter.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20outbound%20%3E%20(property)%20params%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20outbound%20%3E%20(property)%20params">Link to this property</a>

<details>

<summary>

worker: optional object {entrypoint, environment, service }

Outbound worker.

</summary>

entrypoint: optional string

Entrypoint to invoke on the outbound worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20outbound%20%3E%20(property)%20worker%20%3E%20(property)%20entrypoint">Link to this property</a>

environment: optional string

Environment of the outbound worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20outbound%20%3E%20(property)%20worker%20%3E%20(property)%20environment">Link to this property</a>

service: optional string

Name of the outbound worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20outbound%20%3E%20(property)%20worker%20%3E%20(property)%20service">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20outbound%20%3E%20(property)%20worker">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(property)%20outbound">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2010">Link to this property</a>

<details>

<summary>

DurableObjectNamespace object {name, type, class\_name, 4 more }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20name">Link to this property</a>

type: "durable\_object\_namespace"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20type">Link to this property</a>

class\_name: optional string

The exported class name of the Durable Object.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20class_name">Link to this property</a>

dispatch\_namespace: optional string

The dispatch namespace the Durable Object script belongs to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20dispatch_namespace">Link to this property</a>

environment: optional string

The environment of the script\_name to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20environment">Link to this property</a>

namespace\_id: optional string

Namespace identifier tag.

maxLength32

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20namespace_id">Link to this property</a>

script\_name: optional string

The script where the Durable Object is defined, if it is external to this Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(property)%20script_name">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2011">Link to this property</a>

<details>

<summary>

Hyperdrive object {id, name, type }

</summary>

id: string

Identifier of the Hyperdrive connection to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20id">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20name">Link to this property</a>

type: "hyperdrive"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2012">Link to this property</a>

<details>

<summary>

Inherit object {name, type, old\_name, version\_id }

</summary>

name: string

The name of the inherited binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(property)%20name">Link to this property</a>

type: "inherit"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(property)%20type">Link to this property</a>

old\_name: optional string

The old name of the inherited binding. If set, the binding will be renamed from <code>old_name</code> to <code>name</code> in the new version. If not set, the binding will keep the same name between versions.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(property)%20old_name">Link to this property</a>

version\_id: optional string

Identifier for the version to inherit the binding from, which can be the version ID or the literal “latest” to inherit from the latest version. Defaults to inheriting the binding from the latest version.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(property)%20version_id">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2013">Link to this property</a>

<details>

<summary>

Images object {name, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(property)%20name">Link to this property</a>

type: "images"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2014">Link to this property</a>

<details>

<summary>

Json object {json, name, type }

</summary>

json: unknown

JSON data to use.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20json">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20name">Link to this property</a>

type: "json"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2015">Link to this property</a>

<details>

<summary>

KVNamespace object {name, namespace\_id, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(property)%20name">Link to this property</a>

namespace\_id: string

Namespace identifier tag.

maxLength32

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(property)%20namespace_id">Link to this property</a>

type: "kv\_namespace"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2016">Link to this property</a>

<details>

<summary>

Media object {name, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20name">Link to this property</a>

type: "media"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2017">Link to this property</a>

<details>

<summary>

MTLSCertificate object {certificate\_id, name, type }

</summary>

certificate\_id: string

Identifier of the certificate to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(property)%20certificate_id">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(property)%20name">Link to this property</a>

type: "mtls\_certificate"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2018">Link to this property</a>

<details>

<summary>

PlainText object {name, text, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(property)%20name">Link to this property</a>

text: string

The text value to use.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(property)%20text">Link to this property</a>

type: "plain\_text"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2019">Link to this property</a>

<details>

<summary>

Pipelines object {name, pipeline, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20name">Link to this property</a>

pipeline: string

Name of the Pipeline to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20pipeline">Link to this property</a>

type: "pipelines"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2020">Link to this property</a>

<details>

<summary>

K2 object {name, stream, type }

A K2 stream binding. Available only to accounts enabled for K2.

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2021%20%3E%20(property)%20name">Link to this property</a>

stream: string

ID of a K2 stream owned by the account deploying the Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2021%20%3E%20(property)%20stream">Link to this property</a>

type: "k2"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2021%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2021">Link to this property</a>

<details>

<summary>

Queue object {name, queue\_name, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2022%20%3E%20(property)%20name">Link to this property</a>

queue\_name: string

Name of the Queue to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2022%20%3E%20(property)%20queue_name">Link to this property</a>

type: "queue"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2022%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2022">Link to this property</a>

<details>

<summary>

Ratelimit object {name, namespace\_id, simple, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2023%20%3E%20(property)%20name">Link to this property</a>

namespace\_id: string

Identifier of the rate limit namespace to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2023%20%3E%20(property)%20namespace_id">Link to this property</a>

<details>

<summary>

simple: object {limit, period, mitigation\_timeout }

The rate limit configuration.

</summary>

limit: number

The limit (requests per period).

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2023%20%3E%20(property)%20simple%20%3E%20(property)%20limit">Link to this property</a>

period: number

The period in seconds.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2023%20%3E%20(property)%20simple%20%3E%20(property)%20period">Link to this property</a>

mitigation\_timeout: optional number

Duration in seconds to apply the mitigation action after the rate limit is exceeded. Valid values are 0 (disabled), 10, or multiples of 60 up to 86400. Must be greater than or equal to the period when non-zero.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2023%20%3E%20(property)%20simple%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2023%20%3E%20(property)%20simple">Link to this property</a>

type: "ratelimit"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2023%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2023">Link to this property</a>

<details>

<summary>

R2Bucket object {bucket\_name, name, type, jurisdiction }

</summary>

bucket\_name: string

R2 bucket to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2024%20%3E%20(property)%20bucket_name">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2024%20%3E%20(property)%20name">Link to this property</a>

type: "r2\_bucket"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2024%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

jurisdiction: optional "eu"or "fedramp"or "fedramp-high"or "us"

The <a href="https://developers.cloudflare.com/r2/reference/data-location/#jurisdictional-restrictions">jurisdiction</a> of the R2 bucket.

</summary>

One of the following:

"eu"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2024%20%3E%20(property)%20jurisdiction%20%3E%20(member)%200">Link to this property</a>

"fedramp"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2024%20%3E%20(property)%20jurisdiction%20%3E%20(member)%201">Link to this property</a>

"fedramp-high"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2024%20%3E%20(property)%20jurisdiction%20%3E%20(member)%202">Link to this property</a>

"us"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2024%20%3E%20(property)%20jurisdiction%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2024%20%3E%20(property)%20jurisdiction">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2024">Link to this property</a>

<details>

<summary>

SecretText object {name, text, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2025%20%3E%20(property)%20name">Link to this property</a>

text: string

The secret value to use.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2025%20%3E%20(property)%20text">Link to this property</a>

type: "secret\_text"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2025%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2025">Link to this property</a>

<details>

<summary>

SendEmail object {name, type, allowed\_destination\_addresses, 2 more }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2026%20%3E%20(property)%20name">Link to this property</a>

type: "send\_email"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2026%20%3E%20(property)%20type">Link to this property</a>

allowed\_destination\_addresses: optional array of string

List of allowed destination addresses.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2026%20%3E%20(property)%20allowed_destination_addresses">Link to this property</a>

allowed\_sender\_addresses: optional array of string

List of allowed sender addresses.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2026%20%3E%20(property)%20allowed_sender_addresses">Link to this property</a>

destination\_address: optional string

Destination address for the email.

formatemail

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2026%20%3E%20(property)%20destination_address">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2026">Link to this property</a>

<details>

<summary>

Service object {name, service, type, 2 more }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2027%20%3E%20(property)%20name">Link to this property</a>

service: string

Name of Worker to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2027%20%3E%20(property)%20service">Link to this property</a>

type: "service"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2027%20%3E%20(property)%20type">Link to this property</a>

entrypoint: optional string

Entrypoint to invoke on the target Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2027%20%3E%20(property)%20entrypoint">Link to this property</a>

environment: optional string

Optional environment if the Worker utilizes one.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2027%20%3E%20(property)%20environment">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2027">Link to this property</a>

<details>

<summary>

TextBlob object {name, part, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2028%20%3E%20(property)%20name">Link to this property</a>

part: string

The name of the file containing the text content. Only accepted for <code>service worker syntax</code> Workers.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2028%20%3E%20(property)%20part">Link to this property</a>

Deprecatedtype: "text\_blob"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2028%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2028">Link to this property</a>

<details>

<summary>

Vectorize object {index\_name, name, type }

</summary>

index\_name: string

Name of the Vectorize index to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2029%20%3E%20(property)%20index_name">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2029%20%3E%20(property)%20name">Link to this property</a>

type: "vectorize"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2029%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2029">Link to this property</a>

<details>

<summary>

VersionMetadata object {name, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2030%20%3E%20(property)%20name">Link to this property</a>

type: "version\_metadata"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2030%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2030">Link to this property</a>

<details>

<summary>

SecretsStoreSecret object {name, secret\_name, store\_id, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2031%20%3E%20(property)%20name">Link to this property</a>

secret\_name: string

Name of the secret in the store.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2031%20%3E%20(property)%20secret_name">Link to this property</a>

store\_id: string

ID of the store containing the secret.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2031%20%3E%20(property)%20store_id">Link to this property</a>

type: "secrets\_store\_secret"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2031%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2031">Link to this property</a>

<details>

<summary>

Flagship object {app\_id, name, type }

</summary>

app\_id: string

ID of the Flagship app to bind to for feature flag evaluation.

maxLength128

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2032%20%3E%20(property)%20app_id">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2032%20%3E%20(property)%20name">Link to this property</a>

type: "flagship"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2032%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2032">Link to this property</a>

<details>

<summary>

SecretKey object {algorithm, format, name, 4 more }

</summary>

algorithm: unknown

Algorithm-specific key parameters. <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#algorithm">Learn more</a>.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20algorithm">Link to this property</a>

<details>

<summary>

format: "raw"or "pkcs8"or "spki"or "jwk"

Data format of the key. <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#format">Learn more</a>.

</summary>

One of the following:

"raw"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20format%20%3E%20(member)%200">Link to this property</a>

"pkcs8"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20format%20%3E%20(member)%201">Link to this property</a>

"spki"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20format%20%3E%20(member)%202">Link to this property</a>

"jwk"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20format%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20format">Link to this property</a>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20name">Link to this property</a>

type: "secret\_key"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

usages: array of "encrypt"or "decrypt"or "sign"or 5 more

Allowed operations with the key. <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#keyUsages">Learn more</a>.

</summary>

One of the following:

"encrypt"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"decrypt"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"sign"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"verify"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"deriveKey"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

"deriveBits"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%205">Link to this property</a>

"wrapKey"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%206">Link to this property</a>

"unwrapKey"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20usages%20%3E%20(items)%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20usages">Link to this property</a>

key\_base64: optional string

Base64-encoded key data. Required if <code>format</code> is “raw”, “pkcs8”, or “spki”.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20key_base64">Link to this property</a>

key\_jwk: optional unknown

Key data in <a href="https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/importKey#json_web_key">JSON Web Key</a> format. Required if <code>format</code> is “jwk”.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033%20%3E%20(property)%20key_jwk">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2033">Link to this property</a>

<details>

<summary>

Workflow object {name, type, workflow\_name, 2 more }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2034%20%3E%20(property)%20name">Link to this property</a>

type: "workflow"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2034%20%3E%20(property)%20type">Link to this property</a>

workflow\_name: string

Name of the Workflow to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2034%20%3E%20(property)%20workflow_name">Link to this property</a>

class\_name: optional string

Class name of the Workflow. Should only be provided if the Workflow belongs to this script.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2034%20%3E%20(property)%20class_name">Link to this property</a>

script\_name: optional string

Script name that contains the Workflow. If not provided, defaults to this script name.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2034%20%3E%20(property)%20script_name">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2034">Link to this property</a>

<details>

<summary>

WasmModule object {name, part, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2035%20%3E%20(property)%20name">Link to this property</a>

part: string

The name of the file containing the WebAssembly module content. Only accepted for <code>service worker syntax</code> Workers.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2035%20%3E%20(property)%20part">Link to this property</a>

Deprecatedtype: "wasm\_module"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2035%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2035">Link to this property</a>

<details>

<summary>

VPCService object {name, service\_id, type }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2036%20%3E%20(property)%20name">Link to this property</a>

service\_id: string

Identifier of the VPC service to bind to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2036%20%3E%20(property)%20service_id">Link to this property</a>

type: "vpc\_service"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2036%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2036">Link to this property</a>

<details>

<summary>

VPCNetwork object {name, type, identity, 2 more }

</summary>

name: string

A JavaScript variable name for the binding.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2037%20%3E%20(property)%20name">Link to this property</a>

type: "vpc\_network"

The kind of resource that the binding provides.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2037%20%3E%20(property)%20type">Link to this property</a>

identity: optional "runtime-email-alpha"

Enables Gateway identity for the binding. Requires network\_id to be “cf1:network” and cannot be combined with tunnel\_id.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2037%20%3E%20(property)%20identity">Link to this property</a>

network\_id: optional string

Identifier of the network to bind to. Only “cf1:network” is currently supported. Mutually exclusive with tunnel\_id.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2037%20%3E%20(property)%20network_id">Link to this property</a>

tunnel\_id: optional string

UUID of the Cloudflare Tunnel to bind to. Mutually exclusive with network\_id.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2037%20%3E%20(property)%20tunnel_id">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings%20%3E%20(items)%20%3E%20(variant)%2037">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20bindings">Link to this property</a>

<details>

<summary>

cache\_options: optional object {enabled, cross\_version\_cache }

Global CacheW configuration for the Worker. When caching is on, the platform provisions a <code>cloudflare.app</code> zone for the Worker. A <code>type: worker</code> entry in the <code>exports</code> map can override this value for a single entrypoint.

</summary>

enabled: boolean

Whether caching is enabled for this Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20cache_options%20%3E%20(property)%20enabled">Link to this property</a>

cross\_version\_cache: optional boolean

Whether cached responses are shared across Worker version uploads. This is independent of <code>enabled</code>. It can stay true while caching is off, so the preference survives turning caching off and back on.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20cache_options%20%3E%20(property)%20cross_version_cache">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20cache_options">Link to this property</a>

compatibility\_date: optional string

Date indicating targeted support in the Workers runtime. Backwards incompatible fixes to the runtime following this date will not affect this Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20compatibility_date">Link to this property</a>

compatibility\_flags: optional array of string

Flags that enable or disable certain features in the Workers runtime. Used to enable upcoming features or opt in or out of specific changes not included in a <code>compatibility_date</code>.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20compatibility_flags">Link to this property</a>

<details>

<summary>

exports: optional map\[object {type, cache, state } or object {storage, type, container, state } or object {state, type } or 3 more]

Declarative exports for the Worker. Worker entrypoint entries (<code>type: worker</code>) carry cache configuration for that entrypoint.

</summary>

One of the following:

<details>

<summary>

Worker object {type, cache, state }

A named Worker entrypoint export (<code>type: worker</code>). Worker entrypoints are always live (<code>state: created</code>) and carry no storage or lifecycle fields. The optional <code>cache</code> block overrides the Worker’s global <code>cache_options.enabled</code> for this entrypoint.

</summary>

type: "worker"

Marks this entry as a Worker entrypoint export.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

cache: optional object {enabled }

Cache override for this entrypoint. Overrides the Worker’s global <code>cache_options.enabled</code> for this entrypoint only.

</summary>

enabled: boolean

Whether caching is enabled for this entrypoint.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20cache%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20cache">Link to this property</a>

state: optional "created"

Live export. May be omitted; defaults to <code>created</code>.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20state">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

WorkersDurableObjectExport object {storage, type, container, state }

A live Durable Object export (<code>state: created</code>, the default). The platform auto-provisions the namespace on first deploy, matches it on subsequent deploys, and never mutates or deletes it as a side effect of a code-only change. <code>storage</code> is required; <code>renamed_to</code>, <code>transferred_to</code> and <code>transfer_from</code> are not allowed on a live entry.

</summary>

<details>

<summary>

storage: "sqlite"or "legacy-kv"

Durable Object storage backend. <code>sqlite</code> is the recommended (and only) backend for new namespaces. <code>legacy-kv</code> is accepted only for a class whose namespace already exists as KV-backed; the <code>exports</code> flow never provisions a new <code>legacy-kv</code> namespace.

</summary>

One of the following:

"sqlite"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20storage%20%3E%20(member)%200">Link to this property</a>

"legacy-kv"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20storage%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20storage">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

container: optional string

Name of the container (declared in the upload’s <code>metadata.containers</code>) that backs this Durable Object. When set, the namespace is container-enabled. Valid only on live entries.

maxLength128

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20container">Link to this property</a>

state: optional "created"

Live export. May be omitted; defaults to <code>created</code>.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20state">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

WorkersDurableObjectDeletedExport object {state, type }

A <code>deleted</code> tombstone: retires the provisioned namespace for this class and all of its data. The class must be absent from the uploaded code and no other Worker in the account may bind to the namespace, otherwise the deploy is rejected. No other fields are allowed. Deletion is irreversible.

</summary>

state: "deleted"

Tombstone that deletes the namespace.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20state">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

WorkersDurableObjectRenamedExport object {renamed\_to, state, type }

A <code>renamed</code> tombstone: rewrites the provisioned namespace’s class name from this map key to <code>renamed_to</code>. The source class may stay in code during the rollout window (an info notice is emitted). <code>storage</code>, <code>transferred_to</code> and <code>transfer_from</code> are not allowed.

</summary>

renamed\_to: string

The destination class name. Must differ from the source class (the map key) and must be declared as a live (<code>created</code>) entry in the same <code>exports</code> map. Write-only: never present in GET responses.

maxLength128

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20renamed_to">Link to this property</a>

state: "renamed"

Tombstone that renames the namespace’s class.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20state">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

WorkersDurableObjectTransferredExport object {state, transferred\_to, type }

A <code>transferred</code> tombstone (source side of a two-phase transfer): hands ownership of the provisioned namespace to another script in the same account, named by <code>transferred_to</code>. The target must have already deployed a matching <code>expecting-transfer</code> entry. The source class may stay in code during the rollout window (an info notice is emitted). <code>storage</code>, <code>renamed_to</code> and <code>transfer_from</code> are not allowed.

</summary>

state: "transferred"

Tombstone that transfers the namespace to another script.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20state">Link to this property</a>

transferred\_to: string

The destination script name. Must be in the same account and the same dispatch-namespace context (or both non-dispatch). Cross-dispatch-namespace transfers are rejected. Write-only: never present in GET responses.

maxLength128

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20transferred_to">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

WorkersDurableObjectExpectingTransferExport object {state, storage, transfer\_from, 2 more }

The target side of a two-phase transfer (<code>state: expecting-transfer</code>). Declares that this script expects to receive a namespace for this class from the <code>transfer_from</code> script. This is a live entry, not a tombstone: bindings resolve through the source’s namespace until the source commits with a <code>transferred</code> tombstone. <code>storage</code> and <code>transfer_from</code> are required; <code>renamed_to</code> and <code>transferred_to</code> are not allowed.

</summary>

state: "expecting-transfer"

Target side of a two-phase transfer.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20state">Link to this property</a>

<details>

<summary>

storage: "sqlite"or "legacy-kv"

Durable Object storage backend. <code>sqlite</code> is the recommended (and only) backend for new namespaces. <code>legacy-kv</code> is accepted only for a class whose namespace already exists as KV-backed; the <code>exports</code> flow never provisions a new <code>legacy-kv</code> namespace.

</summary>

One of the following:

"sqlite"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20storage%20%3E%20(member)%200">Link to this property</a>

"legacy-kv"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20storage%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20storage">Link to this property</a>

transfer\_from: string

The source script name to receive the namespace from. Must be in the same account and dispatch-namespace context. Present on reads for <code>expecting-transfer</code> entries.

maxLength128

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20transfer_from">Link to this property</a>

type: "durable-object"

Marks this entry as a Durable Object export.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

container: optional string

Name of the container (declared in the upload’s <code>metadata.containers</code>) that backs this Durable Object once the transfer settles. Valid only on live entries.

maxLength128

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20container">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports%20%3E%20(items)%20%3E%20(variant)%205">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports">Link to this property</a>

<details>

<summary>

exports\_reconciliation: optional object {created, deleted, info, 6 more }

Summary of the declarative exports reconciliation that ran on this upload. Populated only when the uploaded metadata included an <code>exports</code> block. Durable Object entries drive reconciliation; <code>type: worker</code> entries do not contribute to this summary.

</summary>

created: array of string

Class names for which a new namespace was provisioned.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20created">Link to this property</a>

deleted: array of string

Class names whose namespace was deleted by a <code>deleted</code> tombstone.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20deleted">Link to this property</a>

<details>

<summary>

info: array of object {class, message, scenario, 2 more }

Non-blocking info entries (stale tombstones, tombstone applied with class still in code). See <code>exports_reconciliation_info</code>.

</summary>

class: string

The class name the info entry is about.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20class">Link to this property</a>

message: string

Human-readable explanation.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

scenario: "code\_class\_not\_in\_exports"or "provisioned\_class\_missing\_from\_config"or "config\_export\_not\_in\_code"or 30 more

Stable, machine-readable tag identifying which reconciliation scenario produced an error, warning, or info entry. Clients may branch on this value instead of parsing <code>message</code>.

</summary>

One of the following:

"code\_class\_not\_in\_exports"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%200">Link to this property</a>

"provisioned\_class\_missing\_from\_config"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%201">Link to this property</a>

"config\_export\_not\_in\_code"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%202">Link to this property</a>

"config\_references\_nonexistent\_class"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%203">Link to this property</a>

"orphaned\_provisioned\_namespace"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%204">Link to this property</a>

"storage\_type\_mismatch"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%205">Link to this property</a>

"free\_tier\_requires\_sqlite"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%206">Link to this property</a>

"invalid\_export"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%207">Link to this property</a>

"tombstone\_delete\_class\_still\_in\_code"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%208">Link to this property</a>

"tombstone\_delete\_blocked\_by\_external\_bindings"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%209">Link to this property</a>

"tombstone\_renamed\_to\_occupied"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2010">Link to this property</a>

"transferred\_pending\_not\_found"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2011">Link to this property</a>

"transferred\_target\_missing"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2012">Link to this property</a>

"transferred\_target\_mismatch"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2013">Link to this property</a>

"phase\_one\_transfer\_source\_missing"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2014">Link to this property</a>

"phase\_one\_transfer\_source\_namespace\_missing"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2015">Link to this property</a>

"phase\_one\_transfer\_target\_class\_provisioned"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2016">Link to this property</a>

"phase\_one\_transfer\_after\_commit\_mismatch"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2017">Link to this property</a>

"phase\_one\_transfer\_duplicate"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2018">Link to this property</a>

"phase\_one\_transfer\_target\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2019">Link to this property</a>

"phase\_one\_transfer\_source\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2020">Link to this property</a>

"transferred\_source\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2021">Link to this property</a>

"transferred\_target\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2022">Link to this property</a>

"container\_undeclared\_reference"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2023">Link to this property</a>

"container\_class\_not\_durable\_object"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2024">Link to this property</a>

"container\_wiring\_inconsistent"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2025">Link to this property</a>

"container\_multiple\_durable\_objects"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2026">Link to this property</a>

"transfer\_container\_parity\_mismatch"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2027">Link to this property</a>

"transfer\_container\_parity\_mismatch\_on\_commit"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2028">Link to this property</a>

"tombstone\_class\_still\_in\_code"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2029">Link to this property</a>

"stale\_tombstone"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2030">Link to this property</a>

"transfer\_receive\_already\_applied"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2031">Link to this property</a>

"transfer\_receive\_cleanup\_complete"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2032">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20scenario">Link to this property</a>

namespace\_id: optional string

The provisioned namespace the entry relates to, when applicable.

formatuuid

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20namespace_id">Link to this property</a>

referencing\_scripts: optional array of string

Other Workers in the account that still bind to the affected class. Advisory: while non-empty the tombstone is not yet safe to remove — redeploy these Workers with bindings re-pointed first.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info%20%3E%20(items)%20%3E%20(property)%20referencing_scripts">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20info">Link to this property</a>

removable\_entries: array of string

Source class names whose tombstone entry is now stale and safe to delete from <code>exports</code> (no remaining referencing scripts).

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20removable_entries">Link to this property</a>

<details>

<summary>

renamed: array of object {from, to }

Applied <code>renamed</code> tombstones.

</summary>

from: string

The original (source) class name.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20renamed%20%3E%20(items)%20%3E%20(property)%20from">Link to this property</a>

to: string

The new class name (<code>renamed_to</code>).

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20renamed%20%3E%20(items)%20%3E%20(property)%20to">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20renamed">Link to this property</a>

<details>

<summary>

transfer\_pending: array of object {class, from }

Phase-1 transfer hints recorded on the target side.

</summary>

class: string

The target-side class name awaiting transfer.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20transfer_pending%20%3E%20(items)%20%3E%20(property)%20class">Link to this property</a>

from: string

The source script the namespace will be transferred from.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20transfer_pending%20%3E%20(items)%20%3E%20(property)%20from">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20transfer_pending">Link to this property</a>

<details>

<summary>

transferred: array of object {class, phase, to }

Committed <code>transferred</code> tombstones (phase-2).

</summary>

class: string

The source class name that was transferred.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20transferred%20%3E%20(items)%20%3E%20(property)%20class">Link to this property</a>

phase: "committed"

The transfer phase. Currently always <code>committed</code>.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20transferred%20%3E%20(items)%20%3E%20(property)%20phase">Link to this property</a>

to: string

The destination script that now owns the namespace.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20transferred%20%3E%20(items)%20%3E%20(property)%20to">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20transferred">Link to this property</a>

updated: array of string

Class names whose provisioned namespace was mutated in place.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20updated">Link to this property</a>

<details>

<summary>

warnings: array of object {class, message, scenario, namespace\_id }

Non-blocking warnings. See <code>exports_reconciliation_warning</code>.

</summary>

class: string

The class name the warning is about.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20class">Link to this property</a>

message: string

Human-readable explanation of the warning.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

<details>

<summary>

scenario: "code\_class\_not\_in\_exports"or "provisioned\_class\_missing\_from\_config"or "config\_export\_not\_in\_code"or 30 more

Stable, machine-readable tag identifying which reconciliation scenario produced an error, warning, or info entry. Clients may branch on this value instead of parsing <code>message</code>.

</summary>

One of the following:

"code\_class\_not\_in\_exports"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%200">Link to this property</a>

"provisioned\_class\_missing\_from\_config"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%201">Link to this property</a>

"config\_export\_not\_in\_code"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%202">Link to this property</a>

"config\_references\_nonexistent\_class"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%203">Link to this property</a>

"orphaned\_provisioned\_namespace"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%204">Link to this property</a>

"storage\_type\_mismatch"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%205">Link to this property</a>

"free\_tier\_requires\_sqlite"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%206">Link to this property</a>

"invalid\_export"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%207">Link to this property</a>

"tombstone\_delete\_class\_still\_in\_code"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%208">Link to this property</a>

"tombstone\_delete\_blocked\_by\_external\_bindings"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%209">Link to this property</a>

"tombstone\_renamed\_to\_occupied"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2010">Link to this property</a>

"transferred\_pending\_not\_found"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2011">Link to this property</a>

"transferred\_target\_missing"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2012">Link to this property</a>

"transferred\_target\_mismatch"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2013">Link to this property</a>

"phase\_one\_transfer\_source\_missing"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2014">Link to this property</a>

"phase\_one\_transfer\_source\_namespace\_missing"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2015">Link to this property</a>

"phase\_one\_transfer\_target\_class\_provisioned"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2016">Link to this property</a>

"phase\_one\_transfer\_after\_commit\_mismatch"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2017">Link to this property</a>

"phase\_one\_transfer\_duplicate"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2018">Link to this property</a>

"phase\_one\_transfer\_target\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2019">Link to this property</a>

"phase\_one\_transfer\_source\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2020">Link to this property</a>

"transferred\_source\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2021">Link to this property</a>

"transferred\_target\_in\_dispatch\_namespace"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2022">Link to this property</a>

"container\_undeclared\_reference"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2023">Link to this property</a>

"container\_class\_not\_durable\_object"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2024">Link to this property</a>

"container\_wiring\_inconsistent"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2025">Link to this property</a>

"container\_multiple\_durable\_objects"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2026">Link to this property</a>

"transfer\_container\_parity\_mismatch"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2027">Link to this property</a>

"transfer\_container\_parity\_mismatch\_on\_commit"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2028">Link to this property</a>

"tombstone\_class\_still\_in\_code"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2029">Link to this property</a>

"stale\_tombstone"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2030">Link to this property</a>

"transfer\_receive\_already\_applied"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2031">Link to this property</a>

"transfer\_receive\_cleanup\_complete"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario%20%3E%20(member)%2032">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20scenario">Link to this property</a>

namespace\_id: optional string

The provisioned namespace the warning relates to, when applicable.

formatuuid

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings%20%3E%20(items)%20%3E%20(property)%20namespace_id">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation%20%3E%20(property)%20warnings">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20exports_reconciliation">Link to this property</a>

<details>

<summary>

limits: optional object {cpu\_ms, subrequests }

Limits to apply for this Worker.

</summary>

cpu\_ms: optional number

The amount of CPU time this Worker can use in milliseconds.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20limits%20%3E%20(property)%20cpu_ms">Link to this property</a>

subrequests: optional number

The number of subrequests this Worker can make per request.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20limits%20%3E%20(property)%20subrequests">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20limits">Link to this property</a>

logpush: optional boolean

Whether Logpush is turned on for the Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20logpush">Link to this property</a>

<details>

<summary>

migrations: optional <a href="https://developers.cloudflare.com/api/resources/workers#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)">SingleStepMigration</a> { deleted\_classes, new\_classes, new\_sqlite\_classes, 4 more } or object {new\_tag, old\_tag, steps }

Migrations to apply for Durable Objects associated with this Worker.

</summary>

One of the following:

<details>

<summary>

SingleStepMigration object {deleted\_classes, new\_classes, new\_sqlite\_classes, 4 more }

A single set of migrations to apply.

</summary>

deleted\_classes: optional array of string

A list of classes to delete Durable Object namespaces from.

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20deleted_classes">Link to this property</a>

new\_classes: optional array of string

A list of classes to create Durable Object namespaces from.

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20new_classes">Link to this property</a>

new\_sqlite\_classes: optional array of string

A list of classes to create Durable Object namespaces with SQLite from.

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20new_sqlite_classes">Link to this property</a>

new\_tag: optional string

Tag to set as the latest migration tag.

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20new_tag">Link to this property</a>

old\_tag: optional string

Tag used to verify against the latest migration tag for this Worker. If they don’t match, the upload is rejected.

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20old_tag">Link to this property</a>

<details>

<summary>

renamed\_classes: optional array of object {from, to }

A list of classes with Durable Object namespaces that were renamed.

</summary>

from: optional string

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20renamed_classes%20%3E%20(items)%20%3E%20(property)%20from">Link to this property</a>

to: optional string

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20renamed_classes%20%3E%20(items)%20%3E%20(property)%20to">Link to this property</a>

</details>

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20renamed_classes">Link to this property</a>

<details>

<summary>

transferred\_classes: optional array of object {from, from\_script, to }

A list of transfers for Durable Object namespaces from a different Worker and class to a class defined in this Worker.

</summary>

from: optional string

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20transferred_classes%20%3E%20(items)%20%3E%20(property)%20from">Link to this property</a>

from\_script: optional string

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20transferred_classes%20%3E%20(items)%20%3E%20(property)%20from_script">Link to this property</a>

to: optional string

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20transferred_classes%20%3E%20(items)%20%3E%20(property)%20to">Link to this property</a>

</details>

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)%20%3E%20(property)%20transferred_classes">Link to this property</a>

</details>

<a href="#(resource)%20workers%20%3E%20(model)%20single_step_migration%20%3E%20(schema)">Link to this property</a>

<details>

<summary>

WorkersMultipleStepMigrations object {new\_tag, old\_tag, steps }

</summary>

new\_tag: optional string

Tag to set as the latest migration tag.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20migrations%20%3E%20(variant)%201%20%3E%20(property)%20new_tag">Link to this property</a>

old\_tag: optional string

Tag used to verify against the latest migration tag for this Worker. If they don’t match, the upload is rejected.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20migrations%20%3E%20(variant)%201%20%3E%20(property)%20old_tag">Link to this property</a>

<details>

<summary>

steps: optional array of <a href="https://developers.cloudflare.com/api/resources/workers#(resource)%20workers%20%3E%20(model)%20migration_step%20%3E%20(schema)">MigrationStep</a> { deleted\_classes, new\_classes, new\_sqlite\_classes, 2 more }

Migrations to apply in order.

</summary>

deleted\_classes: optional array of string

A list of classes to delete Durable Object namespaces from.

<a href="#(resource)%20workers%20%3E%20(model)%20migration_step%20%3E%20(schema)%20%3E%20(property)%20deleted_classes">Link to this property</a>

new\_classes: optional array of string

A list of classes to create Durable Object namespaces from.

<a href="#(resource)%20workers%20%3E%20(model)%20migration_step%20%3E%20(schema)%20%3E%20(property)%20new_classes">Link to this property</a>

new\_sqlite\_classes: optional array of string

A list of classes to create Durable Object namespaces with SQLite from.

<a href="#(resource)%20workers%20%3E%20(model)%20migration_step%20%3E%20(schema)%20%3E%20(property)%20new_sqlite_classes">Link to this property</a>

<details>

<summary>

renamed\_classes: optional array of object {from, to }

A list of classes with Durable Object namespaces that were renamed.

</summary>

from: optional string

<a href="#(resource)%20workers%20%3E%20(model)%20migration_step%20%3E%20(schema)%20%3E%20(property)%20renamed_classes%20%3E%20(items)%20%3E%20(property)%20from">Link to this property</a>

to: optional string

<a href="#(resource)%20workers%20%3E%20(model)%20migration_step%20%3E%20(schema)%20%3E%20(property)%20renamed_classes%20%3E%20(items)%20%3E%20(property)%20to">Link to this property</a>

</details>

<a href="#(resource)%20workers%20%3E%20(model)%20migration_step%20%3E%20(schema)%20%3E%20(property)%20renamed_classes">Link to this property</a>

<details>

<summary>

transferred\_classes: optional array of object {from, from\_script, to }

A list of transfers for Durable Object namespaces from a different Worker and class to a class defined in this Worker.

</summary>

from: optional string

<a href="#(resource)%20workers%20%3E%20(model)%20migration_step%20%3E%20(schema)%20%3E%20(property)%20transferred_classes%20%3E%20(items)%20%3E%20(property)%20from">Link to this property</a>

from\_script: optional string

<a href="#(resource)%20workers%20%3E%20(model)%20migration_step%20%3E%20(schema)%20%3E%20(property)%20transferred_classes%20%3E%20(items)%20%3E%20(property)%20from_script">Link to this property</a>

to: optional string

<a href="#(resource)%20workers%20%3E%20(model)%20migration_step%20%3E%20(schema)%20%3E%20(property)%20transferred_classes%20%3E%20(items)%20%3E%20(property)%20to">Link to this property</a>

</details>

<a href="#(resource)%20workers%20%3E%20(model)%20migration_step%20%3E%20(schema)%20%3E%20(property)%20transferred_classes">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20migrations%20%3E%20(variant)%201%20%3E%20(property)%20steps">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20migrations%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20migrations">Link to this property</a>

<details>

<summary>

observability: optional object {enabled, head\_sampling\_rate, issues, 3 more }

Observability settings for the Worker.

</summary>

enabled: boolean

Whether observability is enabled for the Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20enabled">Link to this property</a>

head\_sampling\_rate: optional number

The sampling rate for incoming requests. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20head_sampling_rate">Link to this property</a>

<details>

<summary>

issues: optional object {enabled }

Real-time Issues settings for the Worker.

</summary>

enabled: optional boolean

Whether real-time Issues are enabled for the Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20issues%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20issues">Link to this property</a>

<details>

<summary>

logs: optional object {enabled, invocation\_logs, destinations, 2 more }

Log settings for the Worker.

</summary>

enabled: boolean

Whether logs are enabled for the Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20enabled">Link to this property</a>

invocation\_logs: boolean

Whether <a href="https://developers.cloudflare.com/workers/observability/logs/workers-logs/#invocation-logs">invocation logs</a> are enabled for the Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20invocation_logs">Link to this property</a>

destinations: optional array of string

A list of destinations where logs will be exported to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20destinations">Link to this property</a>

head\_sampling\_rate: optional number

The sampling rate for logs. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20head_sampling_rate">Link to this property</a>

persist: optional boolean

Whether log persistence is enabled for the Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs%20%3E%20(property)%20persist">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20logs">Link to this property</a>

redact\_query\_string: optional boolean

Whether query strings are removed from request URLs in logs and traces.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20redact_query_string">Link to this property</a>

<details>

<summary>

traces: optional object {destinations, enabled, head\_sampling\_rate, 2 more }

Trace settings for the Worker.

</summary>

destinations: optional array of string

A list of destinations where traces will be exported to.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20destinations">Link to this property</a>

enabled: optional boolean

Whether traces are enabled for the Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20enabled">Link to this property</a>

head\_sampling\_rate: optional number

The sampling rate for traces. From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20head_sampling_rate">Link to this property</a>

persist: optional boolean

Whether trace persistence is enabled for the Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20persist">Link to this property</a>

<details>

<summary>

propagation\_policy: optional "authenticated"or "accept"

Controls how inbound trace context (traceparent/tracestate) headers on incoming requests are handled. “authenticated” honors inbound trace context only when accompanied by a valid trace auth token. “accept” unconditionally accepts inbound trace context. Requires the trace propagation feature to be enabled. Returns null when the trace propagation feature is not enabled for the account.

</summary>

One of the following:

"authenticated"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20propagation_policy%20%3E%20(member)%200">Link to this property</a>

"accept"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20propagation_policy%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces%20%3E%20(property)%20propagation_policy">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20observability%20%3E%20(property)%20traces">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20observability">Link to this property</a>

<details>

<summary>

placement: optional object {mode } or object {region } or object {hostname } or 5 more

Configuration for <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>. Specify mode=‘smart’ for Smart Placement, or one of region/hostname/host.

</summary>

One of the following:

<details>

<summary>

Mode object {mode }

</summary>

mode: "smart"

Enables <a href="https://developers.cloudflare.com/workers/configuration/smart-placement">Smart Placement</a>.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200%20%3E%20(property)%20mode">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

Region object {region }

</summary>

region: string

Cloud region for targeted placement in format ‘provider:region’.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201%20%3E%20(property)%20region">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

Hostname object {hostname }

</summary>

hostname: string

HTTP hostname for targeted placement.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202%20%3E%20(property)%20hostname">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

Host object {host }

</summary>

host: string

TCP host and port for targeted placement.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203%20%3E%20(property)%20host">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

object {mode, region }

</summary>

mode: "targeted"

Targeted placement mode.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20mode">Link to this property</a>

region: string

Cloud region for targeted placement in format ‘provider:region’.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204%20%3E%20(property)%20region">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

object {hostname, mode }

</summary>

hostname: string

HTTP hostname for targeted placement.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20hostname">Link to this property</a>

mode: "targeted"

Targeted placement mode.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205%20%3E%20(property)%20mode">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%205">Link to this property</a>

<details>

<summary>

object {host, mode }

</summary>

host: string

TCP host and port for targeted placement.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20host">Link to this property</a>

mode: "targeted"

Targeted placement mode.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206%20%3E%20(property)%20mode">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%206">Link to this property</a>

<details>

<summary>

object {mode, target }

</summary>

mode: "targeted"

Targeted placement mode.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20mode">Link to this property</a>

<details>

<summary>

target: array of object {region } or object {hostname } or object {host }

Array of placement targets (currently limited to single target).

</summary>

One of the following:

<details>

<summary>

Region object {region }

</summary>

region: string

Cloud region in format ‘provider:region’.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20region">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

Hostname object {hostname }

</summary>

hostname: string

HTTP hostname for targeted placement.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20hostname">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

Host object {host }

</summary>

host: string

TCP host:port for targeted placement.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20host">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207%20%3E%20(property)%20target">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement%20%3E%20(variant)%207">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20placement">Link to this property</a>

tags: optional array of string

Tags associated with the Worker.

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

<details>

<summary>

tail\_consumers: optional array of <a href="https://developers.cloudflare.com/api/resources/workers#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)">ConsumerScript</a> { service, environment, namespace }

List of Workers that will consume logs from the attached Worker.

</summary>

service: string

Name of Worker that is to be the consumer.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20service">Link to this property</a>

environment: optional string

Optional environment if the Worker utilizes one.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20environment">Link to this property</a>

namespace: optional string

Optional dispatch namespace the script belongs to.

<a href="#(resource)%20workers.scripts.tail%20%3E%20(model)%20consumer_script%20%3E%20(schema)%20%3E%20(property)%20namespace">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20tail_consumers">Link to this property</a>

<details>

<summary>

usage\_model: optional "standard"or "bundled"or "unbound"

Usage model for the Worker invocations.

</summary>

One of the following:

"standard"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20usage_model%20%3E%20(member)%200">Link to this property</a>

"bundled"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20usage_model%20%3E%20(member)%201">Link to this property</a>

"unbound"

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20usage_model%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)%20%3E%20(property)%20usage_model">Link to this property</a>

</details>

[Link to this property](<#(resource)%20workers.scripts.script_and_version_settings%20%3E%20(model)%20script_and_version_setting_edit_response%20%3E%20(schema)>)