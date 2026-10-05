---
title: Rules
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Rulesets](https://developers.cloudflare.com/api/resources/rulesets)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Rules

##### [Create an account or zone ruleset rule](https://developers.cloudflare.com/api/resources/rulesets/subresources/rules/methods/create)

POST/{accounts\_or\_zones}/{account\_or\_zone\_id}/rulesets/{ruleset\_id}/rules

##### [Update an account or zone ruleset rule](https://developers.cloudflare.com/api/resources/rulesets/subresources/rules/methods/edit)

PATCH/{accounts\_or\_zones}/{account\_or\_zone\_id}/rulesets/{ruleset\_id}/rules/{rule\_id}

##### [Delete an account or zone ruleset rule](https://developers.cloudflare.com/api/resources/rulesets/subresources/rules/methods/delete)

DELETE/{accounts\_or\_zones}/{account\_or\_zone\_id}/rulesets/{ruleset\_id}/rules/{rule\_id}

##### ModelsExpand Collapse

<details>

<summary>

BlockRule object {last\_updated, version, id, 10 more }

</summary>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

id: optional string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

action: optional "block"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

action\_parameters: optional object {response }

The parameters configuring the rule’s action.

</summary>

<details>

<summary>

response: optional object {content, content\_type, status\_code }

The response to show when the block is applied.

</summary>

content: string

The content to return.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20response%20%3E%20(property)%20content">Link to this property</a>

content\_type: string

The type of the content to return.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20response%20%3E%20(property)%20content_type">Link to this property</a>

status\_code: number

The status code to return.

maximum499

minimum400

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20response%20%3E%20(property)%20status_code">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20response">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the rule should be executed.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

expression: optional string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit">Link to this property</a>

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)%20%3E%20(property)%20ref">Link to this property</a>

</details>

[Link to this property](<#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)>)

<details>

<summary>

CompressResponseRule object {last\_updated, version, id, 10 more }

</summary>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

id: optional string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

action: optional "compress\_response"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

action\_parameters: optional object {algorithms }

The parameters configuring the rule’s action.

</summary>

<details>

<summary>

algorithms: array of object {name }

Custom order for compression algorithms.

</summary>

<details>

<summary>

name: optional "none"or "auto"or "default"or 3 more

Name of the compression algorithm to enable.

</summary>

One of the following:

"none"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20algorithms%20%3E%20(items)%20%3E%20(property)%20name%20%3E%20(member)%200">Link to this property</a>

"auto"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20algorithms%20%3E%20(items)%20%3E%20(property)%20name%20%3E%20(member)%201">Link to this property</a>

"default"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20algorithms%20%3E%20(items)%20%3E%20(property)%20name%20%3E%20(member)%202">Link to this property</a>

"gzip"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20algorithms%20%3E%20(items)%20%3E%20(property)%20name%20%3E%20(member)%203">Link to this property</a>

"brotli"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20algorithms%20%3E%20(items)%20%3E%20(property)%20name%20%3E%20(member)%204">Link to this property</a>

"zstd"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20algorithms%20%3E%20(items)%20%3E%20(property)%20name%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20algorithms%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20algorithms">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the rule should be executed.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

expression: optional string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit">Link to this property</a>

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)%20%3E%20(property)%20ref">Link to this property</a>

</details>

[Link to this property](<#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)>)

<details>

<summary>

DDoSDynamicRule object {last\_updated, version, id, 10 more }

</summary>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

id: optional string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

action: optional "ddos\_dynamic"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

action\_parameters: optional unknown

The parameters configuring the rule’s action.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the rule should be executed.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

expression: optional string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit">Link to this property</a>

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)%20%3E%20(property)%20ref">Link to this property</a>

</details>

[Link to this property](<#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)>)

<details>

<summary>

ExecuteRule object {last\_updated, version, id, 10 more }

</summary>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

id: optional string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

action: optional "execute"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

action\_parameters: optional object {id, matched\_data, overrides }

The parameters configuring the rule’s action.

</summary>

id: string

The ID of the ruleset to execute.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

matched\_data: optional object {public\_key }

The configuration to use for matched data logging.

</summary>

public\_key: string

The public key to encrypt matched data logs with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20matched_data%20%3E%20(property)%20public_key">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20matched_data">Link to this property</a>

<details>

<summary>

overrides: optional object {action, categories, enabled, 2 more }

A set of overrides to apply to the target ruleset.

</summary>

action: optional string

An action to override all rules with. This option has lower precedence than rule and category overrides.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

categories: optional array of object {category, action, enabled, sensitivity\_level }

A list of category-level overrides. This option has the second-highest precedence after rule-level overrides.

</summary>

category: string

The name of the category to override.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20category">Link to this property</a>

action: optional string

The action to override rules in the category with.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

enabled: optional boolean

Whether to enable execution of rules in the category.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

sensitivity\_level: optional "default"or "medium"or "low"or "eoff"

The sensitivity level to use for rules in the category. This option is only applicable for DDoS phases.

</summary>

One of the following:

"default"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20sensitivity_level%20%3E%20(member)%200">Link to this property</a>

"medium"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20sensitivity_level%20%3E%20(member)%201">Link to this property</a>

"low"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20sensitivity_level%20%3E%20(member)%202">Link to this property</a>

"eoff"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20sensitivity_level%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20categories%20%3E%20(items)%20%3E%20(property)%20sensitivity_level">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20categories">Link to this property</a>

enabled: optional boolean

Whether to enable execution of all rules. This option has lower precedence than rule and category overrides.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

rules: optional array of object {id, action, enabled, 2 more }

A list of rule-level overrides. This option has the highest precedence.

</summary>

id: string

The ID of the rule to override.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

action: optional string

The action to override the rule with.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

enabled: optional boolean

Whether to enable execution of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20enabled">Link to this property</a>

score\_threshold: optional number

The score threshold to use for the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20score_threshold">Link to this property</a>

<details>

<summary>

sensitivity\_level: optional "default"or "medium"or "low"or "eoff"

The sensitivity level to use for the rule. This option is only applicable for DDoS phases.

</summary>

One of the following:

"default"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20sensitivity_level%20%3E%20(member)%200">Link to this property</a>

"medium"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20sensitivity_level%20%3E%20(member)%201">Link to this property</a>

"low"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20sensitivity_level%20%3E%20(member)%202">Link to this property</a>

"eoff"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20sensitivity_level%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20sensitivity_level">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20rules">Link to this property</a>

<details>

<summary>

sensitivity\_level: optional "default"or "medium"or "low"or "eoff"

A sensitivity level to set for all rules. This option has lower precedence than rule and category overrides and is only applicable for DDoS phases.

</summary>

One of the following:

"default"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20sensitivity_level%20%3E%20(member)%200">Link to this property</a>

"medium"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20sensitivity_level%20%3E%20(member)%201">Link to this property</a>

"low"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20sensitivity_level%20%3E%20(member)%202">Link to this property</a>

"eoff"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20sensitivity_level%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides%20%3E%20(property)%20sensitivity_level">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20overrides">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the rule should be executed.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

expression: optional string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit">Link to this property</a>

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)%20%3E%20(property)%20ref">Link to this property</a>

</details>

[Link to this property](<#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)>)

<details>

<summary>

ForceConnectionCloseRule object {last\_updated, version, id, 10 more }

</summary>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

id: optional string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

action: optional "force\_connection\_close"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

action\_parameters: optional unknown

The parameters configuring the rule’s action.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the rule should be executed.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

expression: optional string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit">Link to this property</a>

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)%20%3E%20(property)%20ref">Link to this property</a>

</details>

[Link to this property](<#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)>)

<details>

<summary>

LogCustomFieldRule object {last\_updated, version, id, 10 more }

</summary>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

id: optional string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

action: optional "log\_custom\_field"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

action\_parameters: optional object {cookie\_fields, raw\_response\_fields, request\_fields, 2 more }

The parameters configuring the rule’s action.

</summary>

<details>

<summary>

cookie\_fields: optional array of object {name }

The cookie fields to log.

</summary>

name: string

The name of the cookie.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cookie_fields%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cookie_fields">Link to this property</a>

<details>

<summary>

raw\_response\_fields: optional array of object {name, preserve\_duplicates }

The raw response fields to log.

</summary>

name: string

The name of the response header.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20raw_response_fields%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

preserve\_duplicates: optional boolean

Whether to log duplicate values of the same header.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20raw_response_fields%20%3E%20(items)%20%3E%20(property)%20preserve_duplicates">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20raw_response_fields">Link to this property</a>

<details>

<summary>

request\_fields: optional array of object {name }

The raw request fields to log.

</summary>

name: string

The name of the header.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20request_fields%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20request_fields">Link to this property</a>

<details>

<summary>

response\_fields: optional array of object {name, preserve\_duplicates }

The transformed response fields to log.

</summary>

name: string

The name of the response header.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20response_fields%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

preserve\_duplicates: optional boolean

Whether to log duplicate values of the same header.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20response_fields%20%3E%20(items)%20%3E%20(property)%20preserve_duplicates">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20response_fields">Link to this property</a>

<details>

<summary>

transformed\_request\_fields: optional array of object {name }

The transformed request fields to log.

</summary>

name: string

The name of the header.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20transformed_request_fields%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20transformed_request_fields">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the rule should be executed.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

expression: optional string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit">Link to this property</a>

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)%20%3E%20(property)%20ref">Link to this property</a>

</details>

[Link to this property](<#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)>)

<details>

<summary>

LogRule object {last\_updated, version, id, 10 more }

</summary>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

id: optional string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

action: optional "log"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

action\_parameters: optional unknown

The parameters configuring the rule’s action.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the rule should be executed.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

expression: optional string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit">Link to this property</a>

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)%20%3E%20(property)%20ref">Link to this property</a>

</details>

[Link to this property](<#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)>)

<details>

<summary>

Logging object {enabled }

An object configuring the rule’s logging behavior.

</summary>

enabled: boolean

Whether to generate a log when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

</details>

[Link to this property](<#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)>)

<details>

<summary>

ManagedChallengeRule object {last\_updated, version, id, 10 more }

</summary>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

id: optional string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

action: optional "managed\_challenge"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

action\_parameters: optional unknown

The parameters configuring the rule’s action.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the rule should be executed.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

expression: optional string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit">Link to this property</a>

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)%20%3E%20(property)%20ref">Link to this property</a>

</details>

[Link to this property](<#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)>)

<details>

<summary>

RedirectRule object {last\_updated, version, id, 10 more }

</summary>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

id: optional string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

action: optional "redirect"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

action\_parameters: optional object {from\_list, from\_value }

The parameters configuring the rule’s action.

</summary>

<details>

<summary>

from\_list: optional object {key, name }

A redirect based on a bulk list lookup.

</summary>

key: string

An expression that evaluates to the list lookup key.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20from_list%20%3E%20(property)%20key">Link to this property</a>

name: string

The name of the list to match against.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20from_list%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20from_list">Link to this property</a>

<details>

<summary>

from\_value: optional object {target\_url, preserve\_query\_string, status\_code }

A redirect based on the request properties.

</summary>

<details>

<summary>

target\_url: object {expression, value }

A URL to redirect the request to.

</summary>

expression: optional string

An expression that evaluates to a URL to redirect the request to.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20from_value%20%3E%20(property)%20target_url%20%3E%20(property)%20expression">Link to this property</a>

value: optional string

A URL to redirect the request to.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20from_value%20%3E%20(property)%20target_url%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20from_value%20%3E%20(property)%20target_url">Link to this property</a>

preserve\_query\_string: optional boolean

Whether to keep the query string of the original request.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20from_value%20%3E%20(property)%20preserve_query_string">Link to this property</a>

<details>

<summary>

status\_code: optional 301or 302or 303or 2 more

The status code to use for the redirect.

</summary>

One of the following:

301

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20from_value%20%3E%20(property)%20status_code%20%3E%20(member)%200">Link to this property</a>

302

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20from_value%20%3E%20(property)%20status_code%20%3E%20(member)%201">Link to this property</a>

303

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20from_value%20%3E%20(property)%20status_code%20%3E%20(member)%202">Link to this property</a>

307

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20from_value%20%3E%20(property)%20status_code%20%3E%20(member)%203">Link to this property</a>

308

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20from_value%20%3E%20(property)%20status_code%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20from_value%20%3E%20(property)%20status_code">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20from_value">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the rule should be executed.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

expression: optional string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit">Link to this property</a>

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)%20%3E%20(property)%20ref">Link to this property</a>

</details>

[Link to this property](<#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)>)

<details>

<summary>

RewriteRule object {last\_updated, version, id, 10 more }

</summary>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

id: optional string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

action: optional "rewrite"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

action\_parameters: optional object {headers, uri }

The parameters configuring the rule’s action.

</summary>

<details>

<summary>

headers: optional map\[object {operation, value } or object {expression, operation } or object {operation, value } or 2 more]

A map of headers to rewrite.

</summary>

One of the following:

<details>

<summary>

AddStaticHeader object {operation, value }

A header with a static value to add.

</summary>

operation: "add"

The operation to perform on the header.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

value: string

A static value for the header.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

AddDynamicHeader object {expression, operation }

A header with a dynamic value to add.

</summary>

expression: string

An expression that evaluates to a value for the header.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20expression">Link to this property</a>

operation: "add"

The operation to perform on the header.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

SetStaticHeader object {operation, value }

A header with a static value to set.

</summary>

operation: "set"

The operation to perform on the header.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20operation">Link to this property</a>

value: string

A static value for the header.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

SetDynamicHeader object {expression, operation }

A header with a dynamic value to set.

</summary>

expression: string

An expression that evaluates to a value for the header.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20expression">Link to this property</a>

operation: "set"

The operation to perform on the header.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20operation">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

RemoveHeader object {operation }

A header to remove.

</summary>

operation: "remove"

The operation to perform on the header.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20operation">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20headers">Link to this property</a>

<details>

<summary>

uri: optional object {path, origin } or object {query, origin }

A URI path rewrite.

</summary>

One of the following:

<details>

<summary>

URIPath object {path, origin }

A URI path rewrite.

</summary>

<details>

<summary>

path: object {expression, value }

A URI path rewrite.

</summary>

expression: optional string

An expression that evaluates to a value to rewrite the URI path to.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20uri%20%3E%20(variant)%200%20%3E%20(property)%20path%20%3E%20(property)%20expression">Link to this property</a>

value: optional string

A value to rewrite the URI path to.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20uri%20%3E%20(variant)%200%20%3E%20(property)%20path%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20uri%20%3E%20(variant)%200%20%3E%20(property)%20path">Link to this property</a>

origin: optional boolean

Whether to propagate the rewritten URI to origin.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20uri%20%3E%20(variant)%200%20%3E%20(property)%20origin">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20uri%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

URIQuery object {query, origin }

A URI query rewrite.

</summary>

<details>

<summary>

query: object {expression, value }

A URI query rewrite.

</summary>

expression: optional string

An expression that evaluates to a value to rewrite the URI query to.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20uri%20%3E%20(variant)%201%20%3E%20(property)%20query%20%3E%20(property)%20expression">Link to this property</a>

value: optional string

A value to rewrite the URI query to.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20uri%20%3E%20(variant)%201%20%3E%20(property)%20query%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20uri%20%3E%20(variant)%201%20%3E%20(property)%20query">Link to this property</a>

origin: optional boolean

Whether to propagate the rewritten URI to origin.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20uri%20%3E%20(variant)%201%20%3E%20(property)%20origin">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20uri%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20uri">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the rule should be executed.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

expression: optional string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit">Link to this property</a>

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)%20%3E%20(property)%20ref">Link to this property</a>

</details>

[Link to this property](<#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)>)

<details>

<summary>

RouteRule object {last\_updated, version, id, 10 more }

</summary>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

id: optional string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

action: optional "route"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

action\_parameters: optional object {host\_header, origin, sni }

The parameters configuring the rule’s action.

</summary>

host\_header: optional string

A value to rewrite the HTTP host header to.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20host_header">Link to this property</a>

<details>

<summary>

origin: optional object {host, port }

An origin to route to.

</summary>

host: optional string

A resolved host to route to.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20origin%20%3E%20(property)%20host">Link to this property</a>

port: optional number

A destination port to route to.

maximum65535

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20origin%20%3E%20(property)%20port">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20origin">Link to this property</a>

<details>

<summary>

sni: optional object {value }

A Server Name Indication (SNI) override.

</summary>

value: string

A value to override the SNI to.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20sni%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20sni">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the rule should be executed.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

expression: optional string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit">Link to this property</a>

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)%20%3E%20(property)%20ref">Link to this property</a>

</details>

[Link to this property](<#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)>)

<details>

<summary>

RulesetRule object {last\_updated, version, id, 10 more }

</summary>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

id: optional string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

action: optional string

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

action\_parameters: optional unknown

The parameters configuring the rule’s action.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the rule should be executed.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

expression: optional string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit">Link to this property</a>

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)%20%3E%20(property)%20ref">Link to this property</a>

</details>

[Link to this property](<#(resource)%20rulesets.rules%20%3E%20(model)%20ruleset_rule%20%3E%20(schema)>)

<details>

<summary>

ScoreRule object {last\_updated, version, id, 10 more }

</summary>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

id: optional string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

action: optional "score"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

action\_parameters: optional object {increment }

The parameters configuring the rule’s action.

</summary>

increment: number

A delta to change the score by, which can be either positive or negative.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20increment">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

expression: optional string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit">Link to this property</a>

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)%20%3E%20(property)%20ref">Link to this property</a>

</details>

[Link to this property](<#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)>)

<details>

<summary>

ServeErrorRule object {last\_updated, version, id, 10 more }

</summary>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

id: optional string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

action: optional "serve\_error"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

action\_parameters: optional object {content, content\_type, status\_code } or object {asset\_name, content\_type, status\_code }

The parameters configuring the rule’s action.

</summary>

One of the following:

<details>

<summary>

ActionParametersContent object {content, content\_type, status\_code }

</summary>

content: string

The response content.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20content">Link to this property</a>

<details>

<summary>

content\_type: optional "application/json"or "text/html"or "text/plain"or "text/xml"

The content type header to set with the error response.

</summary>

One of the following:

"application/json"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20content_type%20%3E%20(member)%200">Link to this property</a>

"text/html"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20content_type%20%3E%20(member)%201">Link to this property</a>

"text/plain"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20content_type%20%3E%20(member)%202">Link to this property</a>

"text/xml"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20content_type%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20content_type">Link to this property</a>

status\_code: optional number

The status code to use for the error.

maximum999

minimum400

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20status_code">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

ActionParametersAsset object {asset\_name, content\_type, status\_code }

</summary>

asset\_name: string

The name of a custom asset to serve as the error response.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20asset_name">Link to this property</a>

<details>

<summary>

content\_type: optional "application/json"or "text/html"or "text/plain"or "text/xml"

The content type header to set with the error response.

</summary>

One of the following:

"application/json"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20content_type%20%3E%20(member)%200">Link to this property</a>

"text/html"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20content_type%20%3E%20(member)%201">Link to this property</a>

"text/plain"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20content_type%20%3E%20(member)%202">Link to this property</a>

"text/xml"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20content_type%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20content_type">Link to this property</a>

status\_code: optional number

The status code to use for the error.

maximum999

minimum400

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20status_code">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

expression: optional string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit">Link to this property</a>

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)%20%3E%20(property)%20ref">Link to this property</a>

</details>

[Link to this property](<#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)>)

<details>

<summary>

SetCacheSettingsRule object {last\_updated, version, id, 10 more }

</summary>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

id: optional string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

action: optional "set\_cache\_settings"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

action\_parameters: optional object {additional\_cacheable\_ports, browser\_ttl, cache, 14 more }

The parameters configuring the rule’s action.

</summary>

additional\_cacheable\_ports: optional array of number

A list of additional ports that caching should be enabled on.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20additional_cacheable_ports">Link to this property</a>

<details>

<summary>

browser\_ttl: optional object {mode, default }

How long client browsers should cache the response. Cloudflare cache purge will not purge content cached on client browsers, so high browser TTLs may lead to stale content.

</summary>

<details>

<summary>

mode: "respect\_origin"or "bypass\_by\_default"or "override\_origin"or "bypass"

The browser TTL mode.

</summary>

One of the following:

"respect\_origin"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20browser_ttl%20%3E%20(property)%20mode%20%3E%20(member)%200">Link to this property</a>

"bypass\_by\_default"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20browser_ttl%20%3E%20(property)%20mode%20%3E%20(member)%201">Link to this property</a>

"override\_origin"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20browser_ttl%20%3E%20(property)%20mode%20%3E%20(member)%202">Link to this property</a>

"bypass"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20browser_ttl%20%3E%20(property)%20mode%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20browser_ttl%20%3E%20(property)%20mode">Link to this property</a>

default: optional number

The browser TTL (in seconds) if you choose the “override\_origin” mode.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20browser_ttl%20%3E%20(property)%20default">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20browser_ttl">Link to this property</a>

cache: optional boolean

Whether the request’s response from the origin is eligible for caching. Caching itself will still depend on the cache control header and your other caching configurations.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache">Link to this property</a>

<details>

<summary>

cache\_key: optional object {cache\_by\_device\_type, cache\_deception\_armor, custom\_key, ignore\_query\_strings\_order }

Which components of the request are included in or excluded from the cache key Cloudflare uses to store the response in cache.

</summary>

cache\_by\_device\_type: optional boolean

Whether to separate cached content based on the visitor’s device type.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20cache_by_device_type">Link to this property</a>

cache\_deception\_armor: optional boolean

Whether to protect from web cache deception attacks, while allowing static assets to be cached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20cache_deception_armor">Link to this property</a>

<details>

<summary>

custom\_key: optional object {cookie, header, host, 2 more }

Which components of the request are included or excluded from the cache key.

</summary>

<details>

<summary>

cookie: optional object {check\_presence, include }

Which cookies to include in the cache key.

</summary>

check\_presence: optional array of string

A list of cookies to check for the presence of. The presence of these cookies is included in the cache key.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20custom_key%20%3E%20(property)%20cookie%20%3E%20(property)%20check_presence">Link to this property</a>

include: optional array of string

A list of cookies to include in the cache key.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20custom_key%20%3E%20(property)%20cookie%20%3E%20(property)%20include">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20custom_key%20%3E%20(property)%20cookie">Link to this property</a>

<details>

<summary>

header: optional object {check\_presence, contains, exclude\_origin, include }

Which headers to include in the cache key.

</summary>

check\_presence: optional array of string

A list of headers to check for the presence of. The presence of these headers is included in the cache key.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20custom_key%20%3E%20(property)%20header%20%3E%20(property)%20check_presence">Link to this property</a>

contains: optional map\[array of string]

A mapping of header names to a list of values. If a header is present in the request and contains any of the values provided, its value is included in the cache key.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20custom_key%20%3E%20(property)%20header%20%3E%20(property)%20contains">Link to this property</a>

exclude\_origin: optional boolean

Whether to exclude the origin header in the cache key.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20custom_key%20%3E%20(property)%20header%20%3E%20(property)%20exclude_origin">Link to this property</a>

include: optional array of string

A list of headers to include in the cache key.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20custom_key%20%3E%20(property)%20header%20%3E%20(property)%20include">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20custom_key%20%3E%20(property)%20header">Link to this property</a>

<details>

<summary>

host: optional object {resolved }

How to use the host in the cache key.

</summary>

resolved: optional boolean

Whether to use the resolved host in the cache key.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20custom_key%20%3E%20(property)%20host%20%3E%20(property)%20resolved">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20custom_key%20%3E%20(property)%20host">Link to this property</a>

<details>

<summary>

query\_string: optional object {exclude, include }

Which query string parameters to include in or exclude from the cache key.

</summary>

<details>

<summary>

exclude: optional object {all, list }

Which query string parameters to exclude from the cache key.

</summary>

all: optional true

Whether to exclude all query string parameters from the cache key.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20custom_key%20%3E%20(property)%20query_string%20%3E%20(property)%20exclude%20%3E%20(property)%20all">Link to this property</a>

list: optional array of string

A list of query string parameters to exclude from the cache key.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20custom_key%20%3E%20(property)%20query_string%20%3E%20(property)%20exclude%20%3E%20(property)%20list">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20custom_key%20%3E%20(property)%20query_string%20%3E%20(property)%20exclude">Link to this property</a>

<details>

<summary>

include: optional object {all, list }

Which query string parameters to include in the cache key.

</summary>

all: optional true

Whether to include all query string parameters in the cache key.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20custom_key%20%3E%20(property)%20query_string%20%3E%20(property)%20include%20%3E%20(property)%20all">Link to this property</a>

list: optional array of string

A list of query string parameters to include in the cache key.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20custom_key%20%3E%20(property)%20query_string%20%3E%20(property)%20include%20%3E%20(property)%20list">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20custom_key%20%3E%20(property)%20query_string%20%3E%20(property)%20include">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20custom_key%20%3E%20(property)%20query_string">Link to this property</a>

<details>

<summary>

user: optional object {device\_type, geo, lang }

How to use characteristics of the request user agent in the cache key.

</summary>

device\_type: optional boolean

Whether to use the user agent’s device type in the cache key.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20custom_key%20%3E%20(property)%20user%20%3E%20(property)%20device_type">Link to this property</a>

geo: optional boolean

Whether to use the user agents’s country in the cache key.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20custom_key%20%3E%20(property)%20user%20%3E%20(property)%20geo">Link to this property</a>

lang: optional boolean

Whether to use the user agent’s language in the cache key.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20custom_key%20%3E%20(property)%20user%20%3E%20(property)%20lang">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20custom_key%20%3E%20(property)%20user">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20custom_key">Link to this property</a>

ignore\_query\_strings\_order: optional boolean

Whether to treat requests with the same query parameters the same, regardless of the order those query parameters are in.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key%20%3E%20(property)%20ignore_query_strings_order">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_key">Link to this property</a>

<details>

<summary>

cache\_reserve: optional object {eligible, minimum\_file\_size }

Settings to determine whether the request’s response from origin is eligible for Cache Reserve (requires a Cache Reserve add-on plan).

</summary>

eligible: boolean

Whether Cache Reserve is enabled. If this is true and a request meets eligibility criteria, Cloudflare will write the resource to Cache Reserve.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_reserve%20%3E%20(property)%20eligible">Link to this property</a>

minimum\_file\_size: optional number

The minimum file size eligible for storage in Cache Reserve.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_reserve%20%3E%20(property)%20minimum_file_size">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20cache_reserve">Link to this property</a>

<details>

<summary>

edge\_ttl: optional object {mode, default, status\_code\_ttl }

How long the Cloudflare edge network should cache the response.

</summary>

<details>

<summary>

mode: "respect\_origin"or "bypass\_by\_default"or "override\_origin"

The edge TTL mode.

</summary>

One of the following:

"respect\_origin"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20edge_ttl%20%3E%20(property)%20mode%20%3E%20(member)%200">Link to this property</a>

"bypass\_by\_default"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20edge_ttl%20%3E%20(property)%20mode%20%3E%20(member)%201">Link to this property</a>

"override\_origin"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20edge_ttl%20%3E%20(property)%20mode%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20edge_ttl%20%3E%20(property)%20mode">Link to this property</a>

default: optional number

The edge TTL (in seconds) if you choose the “override\_origin” mode.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20edge_ttl%20%3E%20(property)%20default">Link to this property</a>

<details>

<summary>

status\_code\_ttl: optional array of object {value, status\_code, status\_code\_range }

A list of TTLs to apply to specific status codes or status code ranges.

</summary>

value: number

The time to cache the response for (in seconds). A value of 0 is equivalent to setting the cache control header with the value “no-cache”. A value of -1 is equivalent to setting the cache control header with the value of “no-store”.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20edge_ttl%20%3E%20(property)%20status_code_ttl%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

status\_code: optional number

A single status code to apply the TTL to.

maximum999

minimum100

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20edge_ttl%20%3E%20(property)%20status_code_ttl%20%3E%20(items)%20%3E%20(property)%20status_code">Link to this property</a>

<details>

<summary>

status\_code\_range: optional object {from, to }

A range of status codes to apply the TTL to.

</summary>

from: optional number

The lower bound of the range.

maximum999

minimum100

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20edge_ttl%20%3E%20(property)%20status_code_ttl%20%3E%20(items)%20%3E%20(property)%20status_code_range%20%3E%20(property)%20from">Link to this property</a>

to: optional number

The upper bound of the range.

maximum999

minimum100

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20edge_ttl%20%3E%20(property)%20status_code_ttl%20%3E%20(items)%20%3E%20(property)%20status_code_range%20%3E%20(property)%20to">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20edge_ttl%20%3E%20(property)%20status_code_ttl%20%3E%20(items)%20%3E%20(property)%20status_code_range">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20edge_ttl%20%3E%20(property)%20status_code_ttl">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20edge_ttl">Link to this property</a>

origin\_cache\_control: optional boolean

Whether Cloudflare will aim to strictly adhere to RFC 7234.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20origin_cache_control">Link to this property</a>

origin\_error\_page\_passthru: optional boolean

Whether to generate Cloudflare error pages for issues from the origin server.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20origin_error_page_passthru">Link to this property</a>

<details>

<summary>

origin\_range\_requests: optional object {mode }

Controls whether Cloudflare fetches a large asset from the origin as a series of range requests instead of one whole-body request.

</summary>

<details>

<summary>

mode: "on"or "off"or "default"

Whether to use range requests. <code>default</code> is the behaviour the zone gets without this rule.

</summary>

One of the following:

"on"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20origin_range_requests%20%3E%20(property)%20mode%20%3E%20(member)%200">Link to this property</a>

"off"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20origin_range_requests%20%3E%20(property)%20mode%20%3E%20(member)%201">Link to this property</a>

"default"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20origin_range_requests%20%3E%20(property)%20mode%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20origin_range_requests%20%3E%20(property)%20mode">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20origin_range_requests">Link to this property</a>

read\_timeout: optional number

A timeout value between two successive read operations to use for your origin server. Historically, the timeout value between two read options from Cloudflare to an origin server is 100 seconds. If you are attempting to reduce HTTP 524 errors because of timeouts from an origin server, try increasing this timeout value.

maximum6000

minimum100

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20read_timeout">Link to this property</a>

respect\_strong\_etags: optional boolean

Whether Cloudflare should respect strong ETag (entity tag) headers. If false, Cloudflare converts strong ETag headers to weak ETag headers.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20respect_strong_etags">Link to this property</a>

<details>

<summary>

serve\_stale: optional object {disable\_stale\_while\_updating }

When to serve stale content from cache.

</summary>

disable\_stale\_while\_updating: optional boolean

Whether Cloudflare should disable serving stale content while getting the latest content from the origin.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20serve_stale%20%3E%20(property)%20disable_stale_while_updating">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20serve_stale">Link to this property</a>

<details>

<summary>

shared\_dictionary: optional object {match\_pattern }

Configuration for shared dictionary compression. When set, Cloudflare injects Use-As-Dictionary headers on matching cacheable responses.

</summary>

match\_pattern: string

URL pattern for the Use-As-Dictionary match field. This pattern specifies which URLs can use this response as a dictionary.

maxLength1024

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20shared_dictionary%20%3E%20(property)%20match_pattern">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20shared_dictionary">Link to this property</a>

strip\_etags: optional boolean

Whether to strip ETag headers from the origin response before caching.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20strip_etags">Link to this property</a>

strip\_last\_modified: optional boolean

Whether to strip Last-Modified headers from the origin response before caching.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20strip_last_modified">Link to this property</a>

strip\_set\_cookie: optional boolean

Whether to strip Set-Cookie headers from the origin response before caching.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20strip_set_cookie">Link to this property</a>

<details>

<summary>

vary: optional object {default, headers }

Controls how cached responses vary based on request headers. <code>default</code> is required by the API and applies to any Vary response header that does not have a per-header override.

</summary>

<details>

<summary>

default: optional object {action }

Controls how response Vary headers without a per-header override contribute to the cache key.

</summary>

<details>

<summary>

action: "bypass"or "passthrough"or "normalize"

How the header value is treated when building the cache key.

</summary>

One of the following:

"bypass"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20vary%20%3E%20(property)%20default%20%3E%20(property)%20action%20%3E%20(member)%200">Link to this property</a>

"passthrough"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20vary%20%3E%20(property)%20default%20%3E%20(property)%20action%20%3E%20(member)%201">Link to this property</a>

"normalize"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20vary%20%3E%20(property)%20default%20%3E%20(property)%20action%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20vary%20%3E%20(property)%20default%20%3E%20(property)%20action">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20vary%20%3E%20(property)%20default">Link to this property</a>

<details>

<summary>

headers: optional map\[object {action, languages, media\_types } ]

A mapping of lowercase request header names to their vary configuration.

</summary>

<details>

<summary>

action: "bypass"or "passthrough"or "normalize"

How the header value is treated when building the cache key.

</summary>

One of the following:

"bypass"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20vary%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(property)%20action%20%3E%20(member)%200">Link to this property</a>

"passthrough"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20vary%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(property)%20action%20%3E%20(member)%201">Link to this property</a>

"normalize"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20vary%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(property)%20action%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20vary%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(property)%20action">Link to this property</a>

languages: optional array of string

The set of languages to normalize against. Only valid for the <code>accept-language</code> header.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20vary%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(property)%20languages">Link to this property</a>

media\_types: optional array of string

The set of media types to normalize against. Only valid for the <code>accept</code> header.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20vary%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(property)%20media_types">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20vary%20%3E%20(property)%20headers">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20vary">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

expression: optional string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit">Link to this property</a>

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)%20%3E%20(property)%20ref">Link to this property</a>

</details>

[Link to this property](<#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)>)

<details>

<summary>

SetConfigRule object {last\_updated, version, id, 10 more }

</summary>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

id: optional string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

action: optional "set\_config"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

action\_parameters: optional object {automatic\_https\_rewrites, autominify, bic, 21 more }

The parameters configuring the rule’s action.

</summary>

automatic\_https\_rewrites: optional boolean

Whether to enable Automatic HTTPS Rewrites.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20automatic_https_rewrites">Link to this property</a>

<details>

<summary>

autominify: optional object {css, html, js }

Which file extensions to minify automatically.

</summary>

css: optional boolean

Whether to minify CSS files.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20autominify%20%3E%20(property)%20css">Link to this property</a>

html: optional boolean

Whether to minify HTML files.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20autominify%20%3E%20(property)%20html">Link to this property</a>

js: optional boolean

Whether to minify JavaScript files.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20autominify%20%3E%20(property)%20js">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20autominify">Link to this property</a>

bic: optional boolean

Whether to enable Browser Integrity Check (BIC).

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20bic">Link to this property</a>

content\_converter: optional boolean

Whether to enable content conversion (e.g., HTML to Markdown).

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20content_converter">Link to this property</a>

Deprecateddisable\_apps: optional true

Cloudflare Apps are deprected.

Whether to disable Cloudflare Apps.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20disable_apps">Link to this property</a>

disable\_pay\_per\_crawl: optional true

Whether to disable Pay Per Crawl.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20disable_pay_per_crawl">Link to this property</a>

disable\_rum: optional true

Whether to disable Real User Monitoring (RUM).

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20disable_rum">Link to this property</a>

disable\_zaraz: optional true

Whether to disable Zaraz.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20disable_zaraz">Link to this property</a>

email\_obfuscation: optional boolean

Whether to enable Email Obfuscation.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20email_obfuscation">Link to this property</a>

fonts: optional boolean

Whether to enable Cloudflare Fonts.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20fonts">Link to this property</a>

hotlink\_protection: optional boolean

Whether to enable Hotlink Protection.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20hotlink_protection">Link to this property</a>

Deprecatedmirage: optional boolean

Mirage is deprecated. More information at <a href="https://developers.cloudflare.com/speed/optimization/images/mirage/">https://developers.cloudflare.com/speed/optimization/images/mirage/</a>.

Whether to enable Mirage.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20mirage">Link to this property</a>

opportunistic\_encryption: optional boolean

Whether to enable Opportunistic Encryption.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20opportunistic_encryption">Link to this property</a>

<details>

<summary>

polish: optional "off"or "lossless"or "lossy"or "webp"

The Polish level to configure.

</summary>

One of the following:

"off"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20polish%20%3E%20(member)%200">Link to this property</a>

"lossless"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20polish%20%3E%20(member)%201">Link to this property</a>

"lossy"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20polish%20%3E%20(member)%202">Link to this property</a>

"webp"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20polish%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20polish">Link to this property</a>

redirects\_for\_ai\_training: optional boolean

Whether to redirect verified AI training crawlers to canonical URLs found in the HTML response.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20redirects_for_ai_training">Link to this property</a>

<details>

<summary>

request\_body\_buffering: optional "none"or "standard"or "full"

The request body buffering mode.

</summary>

One of the following:

"none"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20request_body_buffering%20%3E%20(member)%200">Link to this property</a>

"standard"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20request_body_buffering%20%3E%20(member)%201">Link to this property</a>

"full"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20request_body_buffering%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20request_body_buffering">Link to this property</a>

<details>

<summary>

response\_body\_buffering: optional "none"or "standard"

The response body buffering mode.

</summary>

One of the following:

"none"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20response_body_buffering%20%3E%20(member)%200">Link to this property</a>

"standard"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20response_body_buffering%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20response_body_buffering">Link to this property</a>

rocket\_loader: optional boolean

Whether to enable Rocket Loader.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20rocket_loader">Link to this property</a>

<details>

<summary>

security\_level: optional "off"or "essentially\_off"or "low"or 3 more

The Security Level to configure.

</summary>

One of the following:

"off"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20security_level%20%3E%20(member)%200">Link to this property</a>

"essentially\_off"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20security_level%20%3E%20(member)%201">Link to this property</a>

"low"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20security_level%20%3E%20(member)%202">Link to this property</a>

"medium"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20security_level%20%3E%20(member)%203">Link to this property</a>

"high"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20security_level%20%3E%20(member)%204">Link to this property</a>

"under\_attack"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20security_level%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20security_level">Link to this property</a>

server\_side\_excludes: optional boolean

Whether to enable Server-Side Excludes.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20server_side_excludes">Link to this property</a>

<details>

<summary>

ssl: optional "off"or "flexible"or "full"or 2 more

The SSL level to configure.

</summary>

One of the following:

"off"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20ssl%20%3E%20(member)%200">Link to this property</a>

"flexible"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20ssl%20%3E%20(member)%201">Link to this property</a>

"full"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20ssl%20%3E%20(member)%202">Link to this property</a>

"strict"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20ssl%20%3E%20(member)%203">Link to this property</a>

"origin\_pull"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20ssl%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20ssl">Link to this property</a>

Deprecatedsxg: optional boolean

Signed Exchanges (SXG) is deprecated.

Whether to enable Signed Exchanges (SXG).

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20sxg">Link to this property</a>

webmcp\_enabled: optional boolean

Whether to serve the WebMCP bridge script, which exposes the page’s tools to browser AI agents.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20webmcp_enabled">Link to this property</a>

webmcp\_packs: optional array of string

Bundled WebMCP tool packs to activate for matching requests. An empty array disables all packs. Omitting this parameter leaves the pack selection unchanged. Does not enable the WebMCP bridge itself. Non-empty selections require the WebMCP Configuration Rules entitlement.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20webmcp_packs">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

expression: optional string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit">Link to this property</a>

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)%20%3E%20(property)%20ref">Link to this property</a>

</details>

[Link to this property](<#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)>)

<details>

<summary>

SkipRule object {last\_updated, version, id, 10 more }

</summary>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

id: optional string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

action: optional "skip"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

action\_parameters: optional object {phase, phases, products, 3 more }

The parameters configuring the rule’s action.

</summary>

phase: optional "current"

A phase to skip the execution of. This option is only compatible with the products option.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20phase">Link to this property</a>

<details>

<summary>

phases: optional array of <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)">Phase</a>

A list of phases to skip the execution of. This option is incompatible with the rulesets option.

</summary>

One of the following:

"ddos\_l4"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%200">Link to this property</a>

"ddos\_l7"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%201">Link to this property</a>

"http\_config\_settings"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%202">Link to this property</a>

"http\_custom\_errors"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%203">Link to this property</a>

"http\_log\_custom\_fields"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%204">Link to this property</a>

"http\_ratelimit"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%205">Link to this property</a>

"http\_request\_cache\_settings"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%206">Link to this property</a>

"http\_request\_dynamic\_redirect"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%207">Link to this property</a>

"http\_request\_firewall\_custom"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%208">Link to this property</a>

"http\_request\_firewall\_managed"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%209">Link to this property</a>

"http\_request\_late\_transform"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%2010">Link to this property</a>

"http\_request\_origin"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%2011">Link to this property</a>

"http\_request\_redirect"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%2012">Link to this property</a>

"http\_request\_sanitize"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%2013">Link to this property</a>

"http\_request\_sbfm"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%2014">Link to this property</a>

"http\_request\_transform"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%2015">Link to this property</a>

"http\_response\_cache\_settings"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%2016">Link to this property</a>

"http\_response\_compression"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%2017">Link to this property</a>

"http\_response\_firewall\_managed"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%2018">Link to this property</a>

"http\_response\_headers\_transform"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%2019">Link to this property</a>

"magic\_transit"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%2020">Link to this property</a>

"magic\_transit\_ids\_managed"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%2021">Link to this property</a>

"magic\_transit\_managed"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%2022">Link to this property</a>

"magic\_transit\_ratelimit"

<a href="#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)%20%3E%20(member)%2023">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20phases">Link to this property</a>

<details>

<summary>

products: optional array of "bic"or "hot"or "rateLimit"or 4 more

A list of legacy security products to skip the execution of.

</summary>

One of the following:

"bic"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20products%20%3E%20(items)%20%3E%20(member)%200">Link to this property</a>

"hot"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20products%20%3E%20(items)%20%3E%20(member)%201">Link to this property</a>

"rateLimit"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20products%20%3E%20(items)%20%3E%20(member)%202">Link to this property</a>

"securityLevel"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20products%20%3E%20(items)%20%3E%20(member)%203">Link to this property</a>

"uaBlock"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20products%20%3E%20(items)%20%3E%20(member)%204">Link to this property</a>

"waf"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20products%20%3E%20(items)%20%3E%20(member)%205">Link to this property</a>

"zoneLockdown"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20products%20%3E%20(items)%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20products">Link to this property</a>

rules: optional map\[array of string]

A mapping of ruleset IDs to a list of rule IDs in that ruleset to skip the execution of. This option is incompatible with the ruleset option.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20rules">Link to this property</a>

ruleset: optional "current"

A ruleset to skip the execution of. This option is incompatible with the rulesets option.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20ruleset">Link to this property</a>

rulesets: optional array of string

A list of ruleset IDs to skip the execution of. This option is incompatible with the ruleset and phases options.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters%20%3E%20(property)%20rulesets">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

expression: optional string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20ratelimit">Link to this property</a>

ref: optional string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)%20%3E%20(property)%20ref">Link to this property</a>

</details>

[Link to this property](<#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)>)

<details>

<summary>

RuleCreateResponse = object {id, kind, last\_updated, 5 more } or unknown

A result.

</summary>

One of the following:

<details>

<summary>

Ruleset object {id, kind, last\_updated, 5 more }

A ruleset object.

</summary>

id: string

The unique ID of the ruleset.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20id">Link to this property</a>

kind: <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets%20%3E%20(model)%20kind%20%3E%20(schema)">Kind</a>

The kind of the ruleset.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20kind">Link to this property</a>

last\_updated: string

The timestamp of when the ruleset was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20last_updated">Link to this property</a>

name: string

The human-readable name of the ruleset.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20name">Link to this property</a>

phase: <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)">Phase</a>

The phase of the ruleset.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20phase">Link to this property</a>

<details>

<summary>

rules: array of <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)">BlockRule</a> { last\_updated, version, id, 10 more } or object {id, action, enabled, 10 more } or <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)">CompressResponseRule</a> { last\_updated, version, id, 10 more } or 18 more

The list of rules in the ruleset.

</summary>

One of the following:

<details>

<summary>

BlockRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)">BlockRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

ChallengeRule object {id, action, enabled, 10 more }

</summary>

id: string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20id">Link to this property</a>

action: "challenge"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

Whether the rule should be executed.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20last_updated">Link to this property</a>

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ref">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20version">Link to this property</a>

action\_parameters: optional unknown

The parameters configuring the rule’s action.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

ResponseCompressionRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)">CompressResponseRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

DDoSDynamicRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)">DDoSDynamicRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

ExecuteRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)">ExecuteRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

ForceConnectionCloseRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)">ForceConnectionCloseRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205">Link to this property</a>

<details>

<summary>

JavaScriptChallengeRule object {id, action, enabled, 10 more }

</summary>

id: string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20id">Link to this property</a>

action: "js\_challenge"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

Whether the rule should be executed.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20last_updated">Link to this property</a>

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ref">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20version">Link to this property</a>

action\_parameters: optional unknown

The parameters configuring the rule’s action.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206">Link to this property</a>

<details>

<summary>

LogRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)">LogRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207">Link to this property</a>

<details>

<summary>

LogCustomFieldRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)">LogCustomFieldRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208">Link to this property</a>

<details>

<summary>

ManagedChallengeRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)">ManagedChallengeRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209">Link to this property</a>

<details>

<summary>

RedirectRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)">RedirectRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010">Link to this property</a>

<details>

<summary>

RewriteRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)">RewriteRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011">Link to this property</a>

<details>

<summary>

RouteRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)">RouteRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012">Link to this property</a>

<details>

<summary>

ScoreRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)">ScoreRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013">Link to this property</a>

<details>

<summary>

ServeErrorRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)">ServeErrorRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014">Link to this property</a>

<details>

<summary>

SetCacheControlRule object {id, action, enabled, 10 more }

</summary>

id: string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20id">Link to this property</a>

action: "set\_cache\_control"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20last_updated">Link to this property</a>

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ref">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20version">Link to this property</a>

<details>

<summary>

action\_parameters: optional object {immutable, "max-age", "must-revalidate", 10 more }

The parameters configuring the rule’s action.

</summary>

<details>

<summary>

immutable: optional object {operation, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only }

Set the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable">Link to this property</a>

<details>

<summary>

"max-age": optional object {operation, value, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration that accepts a duration value in seconds.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, value, cloudflare\_only }

Set the directive with a duration value in seconds.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

value: number

The duration value in seconds for the directive.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200%20%3E%20(property)%20value">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age">Link to this property</a>

<details>

<summary>

"must-revalidate": optional object {operation, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only }

Set the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate">Link to this property</a>

<details>

<summary>

"must-understand": optional object {operation, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only }

Set the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand">Link to this property</a>

<details>

<summary>

"no-cache": optional object {operation, cloudflare\_only, qualifiers } or object {operation, cloudflare\_only }

A cache-control directive configuration that accepts optional qualifiers (header names).

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only, qualifiers }

Set the directive with optional qualifiers.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

qualifiers: optional array of string

Optional list of header names to qualify the directive (e.g., for “private” or “no-cache” directives).

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200%20%3E%20(property)%20qualifiers">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache">Link to this property</a>

<details>

<summary>

"no-store": optional object {operation, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only }

Set the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store">Link to this property</a>

<details>

<summary>

"no-transform": optional object {operation, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only }

Set the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform">Link to this property</a>

<details>

<summary>

private: optional object {operation, cloudflare\_only, qualifiers } or object {operation, cloudflare\_only }

A cache-control directive configuration that accepts optional qualifiers (header names).

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only, qualifiers }

Set the directive with optional qualifiers.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

qualifiers: optional array of string

Optional list of header names to qualify the directive (e.g., for “private” or “no-cache” directives).

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200%20%3E%20(property)%20qualifiers">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private">Link to this property</a>

<details>

<summary>

"proxy-revalidate": optional object {operation, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only }

Set the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate">Link to this property</a>

<details>

<summary>

public: optional object {operation, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only }

Set the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public">Link to this property</a>

<details>

<summary>

"s-maxage": optional object {operation, value, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration that accepts a duration value in seconds.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, value, cloudflare\_only }

Set the directive with a duration value in seconds.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

value: number

The duration value in seconds for the directive.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200%20%3E%20(property)%20value">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage">Link to this property</a>

<details>

<summary>

"stale-if-error": optional object {operation, value, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration that accepts a duration value in seconds.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, value, cloudflare\_only }

Set the directive with a duration value in seconds.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

value: number

The duration value in seconds for the directive.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200%20%3E%20(property)%20value">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error">Link to this property</a>

<details>

<summary>

"stale-while-revalidate": optional object {operation, value, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration that accepts a duration value in seconds.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, value, cloudflare\_only }

Set the directive with a duration value in seconds.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

value: number

The duration value in seconds for the directive.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20value">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015">Link to this property</a>

<details>

<summary>

SetCacheSettingsRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)">SetCacheSettingsRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016">Link to this property</a>

<details>

<summary>

SetCacheTagsRule object {id, action, enabled, 10 more }

</summary>

id: string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20id">Link to this property</a>

action: "set\_cache\_tags"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20last_updated">Link to this property</a>

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ref">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20version">Link to this property</a>

<details>

<summary>

action\_parameters: optional object {operation, values } or object {expression, operation } or object {operation, values } or 3 more

The parameters configuring the rule’s action.

</summary>

One of the following:

<details>

<summary>

AddCacheTagsValues object {operation, values }

Add cache tags using a list of values.

</summary>

<details>

<summary>

operation: "add"or "remove"or "set"

The operation to perform on the cache tags.

</summary>

One of the following:

"add"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

values: array of string

A list of cache tag values.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20values">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

AddCacheTagsExpression object {expression, operation }

Add cache tags using an expression.

</summary>

expression: string

An expression that evaluates to an array of cache tag values.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20expression">Link to this property</a>

<details>

<summary>

operation: "add"or "remove"or "set"

The operation to perform on the cache tags.

</summary>

One of the following:

"add"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

RemoveCacheTagsValues object {operation, values }

Remove cache tags using a list of values.

</summary>

<details>

<summary>

operation: "add"or "remove"or "set"

The operation to perform on the cache tags.

</summary>

One of the following:

"add"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202%20%3E%20(property)%20operation">Link to this property</a>

values: array of string

A list of cache tag values.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202%20%3E%20(property)%20values">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

RemoveCacheTagsExpression object {expression, operation }

Remove cache tags using an expression.

</summary>

expression: string

An expression that evaluates to an array of cache tag values.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203%20%3E%20(property)%20expression">Link to this property</a>

<details>

<summary>

operation: "add"or "remove"or "set"

The operation to perform on the cache tags.

</summary>

One of the following:

"add"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203%20%3E%20(property)%20operation">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

SetCacheTagsValues object {operation, values }

Set cache tags using a list of values.

</summary>

<details>

<summary>

operation: "add"or "remove"or "set"

The operation to perform on the cache tags.

</summary>

One of the following:

"add"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204%20%3E%20(property)%20operation">Link to this property</a>

values: array of string

A list of cache tag values.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204%20%3E%20(property)%20values">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

SetCacheTagsExpression object {expression, operation }

Set cache tags using an expression.

</summary>

expression: string

An expression that evaluates to an array of cache tag values.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205%20%3E%20(property)%20expression">Link to this property</a>

<details>

<summary>

operation: "add"or "remove"or "set"

The operation to perform on the cache tags.

</summary>

One of the following:

"add"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205%20%3E%20(property)%20operation">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017">Link to this property</a>

<details>

<summary>

SetConfigurationRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)">SetConfigRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018">Link to this property</a>

<details>

<summary>

SkipRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)">SkipRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019">Link to this property</a>

<details>

<summary>

TransformResponseHTMLRule object {id, action, enabled, 10 more }

</summary>

id: string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20id">Link to this property</a>

action: "transform\_response\_html"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20last_updated">Link to this property</a>

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ref">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20version">Link to this property</a>

<details>

<summary>

action\_parameters: optional object {link\_maze }

The parameters configuring the rule’s action.

</summary>

link\_maze: unknown

Enables the link maze transformation on the response.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20action_parameters%20%3E%20(property)%20link_maze">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules">Link to this property</a>

version: string

The version of the ruleset.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20version">Link to this property</a>

description: optional string

An informative description of the ruleset.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20description">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

unknown

Returned when dry\_run is true.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20rulesets.rules%20%3E%20(model)%20rule_create_response%20%3E%20(schema)>)

<details>

<summary>

RuleEditResponse = object {id, kind, last\_updated, 5 more } or unknown

A result.

</summary>

One of the following:

<details>

<summary>

Ruleset object {id, kind, last\_updated, 5 more }

A ruleset object.

</summary>

id: string

The unique ID of the ruleset.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20id">Link to this property</a>

kind: <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets%20%3E%20(model)%20kind%20%3E%20(schema)">Kind</a>

The kind of the ruleset.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20kind">Link to this property</a>

last\_updated: string

The timestamp of when the ruleset was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20last_updated">Link to this property</a>

name: string

The human-readable name of the ruleset.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20name">Link to this property</a>

phase: <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)">Phase</a>

The phase of the ruleset.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20phase">Link to this property</a>

<details>

<summary>

rules: array of <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)">BlockRule</a> { last\_updated, version, id, 10 more } or object {id, action, enabled, 10 more } or <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)">CompressResponseRule</a> { last\_updated, version, id, 10 more } or 18 more

The list of rules in the ruleset.

</summary>

One of the following:

<details>

<summary>

BlockRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)">BlockRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

ChallengeRule object {id, action, enabled, 10 more }

</summary>

id: string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20id">Link to this property</a>

action: "challenge"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

Whether the rule should be executed.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20last_updated">Link to this property</a>

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ref">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20version">Link to this property</a>

action\_parameters: optional unknown

The parameters configuring the rule’s action.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

ResponseCompressionRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)">CompressResponseRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

DDoSDynamicRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)">DDoSDynamicRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

ExecuteRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)">ExecuteRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

ForceConnectionCloseRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)">ForceConnectionCloseRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205">Link to this property</a>

<details>

<summary>

JavaScriptChallengeRule object {id, action, enabled, 10 more }

</summary>

id: string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20id">Link to this property</a>

action: "js\_challenge"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

Whether the rule should be executed.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20last_updated">Link to this property</a>

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ref">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20version">Link to this property</a>

action\_parameters: optional unknown

The parameters configuring the rule’s action.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206">Link to this property</a>

<details>

<summary>

LogRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)">LogRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207">Link to this property</a>

<details>

<summary>

LogCustomFieldRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)">LogCustomFieldRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208">Link to this property</a>

<details>

<summary>

ManagedChallengeRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)">ManagedChallengeRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209">Link to this property</a>

<details>

<summary>

RedirectRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)">RedirectRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010">Link to this property</a>

<details>

<summary>

RewriteRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)">RewriteRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011">Link to this property</a>

<details>

<summary>

RouteRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)">RouteRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012">Link to this property</a>

<details>

<summary>

ScoreRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)">ScoreRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013">Link to this property</a>

<details>

<summary>

ServeErrorRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)">ServeErrorRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014">Link to this property</a>

<details>

<summary>

SetCacheControlRule object {id, action, enabled, 10 more }

</summary>

id: string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20id">Link to this property</a>

action: "set\_cache\_control"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20last_updated">Link to this property</a>

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ref">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20version">Link to this property</a>

<details>

<summary>

action\_parameters: optional object {immutable, "max-age", "must-revalidate", 10 more }

The parameters configuring the rule’s action.

</summary>

<details>

<summary>

immutable: optional object {operation, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only }

Set the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable">Link to this property</a>

<details>

<summary>

"max-age": optional object {operation, value, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration that accepts a duration value in seconds.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, value, cloudflare\_only }

Set the directive with a duration value in seconds.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

value: number

The duration value in seconds for the directive.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200%20%3E%20(property)%20value">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age">Link to this property</a>

<details>

<summary>

"must-revalidate": optional object {operation, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only }

Set the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate">Link to this property</a>

<details>

<summary>

"must-understand": optional object {operation, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only }

Set the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand">Link to this property</a>

<details>

<summary>

"no-cache": optional object {operation, cloudflare\_only, qualifiers } or object {operation, cloudflare\_only }

A cache-control directive configuration that accepts optional qualifiers (header names).

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only, qualifiers }

Set the directive with optional qualifiers.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

qualifiers: optional array of string

Optional list of header names to qualify the directive (e.g., for “private” or “no-cache” directives).

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200%20%3E%20(property)%20qualifiers">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache">Link to this property</a>

<details>

<summary>

"no-store": optional object {operation, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only }

Set the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store">Link to this property</a>

<details>

<summary>

"no-transform": optional object {operation, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only }

Set the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform">Link to this property</a>

<details>

<summary>

private: optional object {operation, cloudflare\_only, qualifiers } or object {operation, cloudflare\_only }

A cache-control directive configuration that accepts optional qualifiers (header names).

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only, qualifiers }

Set the directive with optional qualifiers.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

qualifiers: optional array of string

Optional list of header names to qualify the directive (e.g., for “private” or “no-cache” directives).

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200%20%3E%20(property)%20qualifiers">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private">Link to this property</a>

<details>

<summary>

"proxy-revalidate": optional object {operation, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only }

Set the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate">Link to this property</a>

<details>

<summary>

public: optional object {operation, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only }

Set the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public">Link to this property</a>

<details>

<summary>

"s-maxage": optional object {operation, value, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration that accepts a duration value in seconds.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, value, cloudflare\_only }

Set the directive with a duration value in seconds.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

value: number

The duration value in seconds for the directive.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200%20%3E%20(property)%20value">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage">Link to this property</a>

<details>

<summary>

"stale-if-error": optional object {operation, value, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration that accepts a duration value in seconds.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, value, cloudflare\_only }

Set the directive with a duration value in seconds.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

value: number

The duration value in seconds for the directive.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200%20%3E%20(property)%20value">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error">Link to this property</a>

<details>

<summary>

"stale-while-revalidate": optional object {operation, value, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration that accepts a duration value in seconds.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, value, cloudflare\_only }

Set the directive with a duration value in seconds.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

value: number

The duration value in seconds for the directive.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20value">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015">Link to this property</a>

<details>

<summary>

SetCacheSettingsRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)">SetCacheSettingsRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016">Link to this property</a>

<details>

<summary>

SetCacheTagsRule object {id, action, enabled, 10 more }

</summary>

id: string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20id">Link to this property</a>

action: "set\_cache\_tags"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20last_updated">Link to this property</a>

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ref">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20version">Link to this property</a>

<details>

<summary>

action\_parameters: optional object {operation, values } or object {expression, operation } or object {operation, values } or 3 more

The parameters configuring the rule’s action.

</summary>

One of the following:

<details>

<summary>

AddCacheTagsValues object {operation, values }

Add cache tags using a list of values.

</summary>

<details>

<summary>

operation: "add"or "remove"or "set"

The operation to perform on the cache tags.

</summary>

One of the following:

"add"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

values: array of string

A list of cache tag values.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20values">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

AddCacheTagsExpression object {expression, operation }

Add cache tags using an expression.

</summary>

expression: string

An expression that evaluates to an array of cache tag values.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20expression">Link to this property</a>

<details>

<summary>

operation: "add"or "remove"or "set"

The operation to perform on the cache tags.

</summary>

One of the following:

"add"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

RemoveCacheTagsValues object {operation, values }

Remove cache tags using a list of values.

</summary>

<details>

<summary>

operation: "add"or "remove"or "set"

The operation to perform on the cache tags.

</summary>

One of the following:

"add"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202%20%3E%20(property)%20operation">Link to this property</a>

values: array of string

A list of cache tag values.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202%20%3E%20(property)%20values">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

RemoveCacheTagsExpression object {expression, operation }

Remove cache tags using an expression.

</summary>

expression: string

An expression that evaluates to an array of cache tag values.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203%20%3E%20(property)%20expression">Link to this property</a>

<details>

<summary>

operation: "add"or "remove"or "set"

The operation to perform on the cache tags.

</summary>

One of the following:

"add"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203%20%3E%20(property)%20operation">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

SetCacheTagsValues object {operation, values }

Set cache tags using a list of values.

</summary>

<details>

<summary>

operation: "add"or "remove"or "set"

The operation to perform on the cache tags.

</summary>

One of the following:

"add"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204%20%3E%20(property)%20operation">Link to this property</a>

values: array of string

A list of cache tag values.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204%20%3E%20(property)%20values">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

SetCacheTagsExpression object {expression, operation }

Set cache tags using an expression.

</summary>

expression: string

An expression that evaluates to an array of cache tag values.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205%20%3E%20(property)%20expression">Link to this property</a>

<details>

<summary>

operation: "add"or "remove"or "set"

The operation to perform on the cache tags.

</summary>

One of the following:

"add"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205%20%3E%20(property)%20operation">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017">Link to this property</a>

<details>

<summary>

SetConfigurationRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)">SetConfigRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018">Link to this property</a>

<details>

<summary>

SkipRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)">SkipRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019">Link to this property</a>

<details>

<summary>

TransformResponseHTMLRule object {id, action, enabled, 10 more }

</summary>

id: string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20id">Link to this property</a>

action: "transform\_response\_html"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20last_updated">Link to this property</a>

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ref">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20version">Link to this property</a>

<details>

<summary>

action\_parameters: optional object {link\_maze }

The parameters configuring the rule’s action.

</summary>

link\_maze: unknown

Enables the link maze transformation on the response.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20action_parameters%20%3E%20(property)%20link_maze">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules">Link to this property</a>

version: string

The version of the ruleset.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20version">Link to this property</a>

description: optional string

An informative description of the ruleset.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20description">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

unknown

Returned when dry\_run is true.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20rulesets.rules%20%3E%20(model)%20rule_edit_response%20%3E%20(schema)>)

<details>

<summary>

RuleDeleteResponse = object {id, kind, last\_updated, 5 more } or unknown

A result.

</summary>

One of the following:

<details>

<summary>

Ruleset object {id, kind, last\_updated, 5 more }

A ruleset object.

</summary>

id: string

The unique ID of the ruleset.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20id">Link to this property</a>

kind: <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets%20%3E%20(model)%20kind%20%3E%20(schema)">Kind</a>

The kind of the ruleset.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20kind">Link to this property</a>

last\_updated: string

The timestamp of when the ruleset was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20last_updated">Link to this property</a>

name: string

The human-readable name of the ruleset.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20name">Link to this property</a>

phase: <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)">Phase</a>

The phase of the ruleset.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20phase">Link to this property</a>

<details>

<summary>

rules: array of <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)">BlockRule</a> { last\_updated, version, id, 10 more } or object {id, action, enabled, 10 more } or <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)">CompressResponseRule</a> { last\_updated, version, id, 10 more } or 18 more

The list of rules in the ruleset.

</summary>

One of the following:

<details>

<summary>

BlockRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20block_rule%20%3E%20(schema)">BlockRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

ChallengeRule object {id, action, enabled, 10 more }

</summary>

id: string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20id">Link to this property</a>

action: "challenge"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

Whether the rule should be executed.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20last_updated">Link to this property</a>

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ref">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20version">Link to this property</a>

action\_parameters: optional unknown

The parameters configuring the rule’s action.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

ResponseCompressionRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)">CompressResponseRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

DDoSDynamicRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)">DDoSDynamicRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

ExecuteRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)">ExecuteRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

ForceConnectionCloseRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)">ForceConnectionCloseRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205">Link to this property</a>

<details>

<summary>

JavaScriptChallengeRule object {id, action, enabled, 10 more }

</summary>

id: string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20id">Link to this property</a>

action: "js\_challenge"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

Whether the rule should be executed.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20last_updated">Link to this property</a>

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ref">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20version">Link to this property</a>

action\_parameters: optional unknown

The parameters configuring the rule’s action.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206">Link to this property</a>

<details>

<summary>

LogRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)">LogRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207">Link to this property</a>

<details>

<summary>

LogCustomFieldRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)">LogCustomFieldRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208">Link to this property</a>

<details>

<summary>

ManagedChallengeRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)">ManagedChallengeRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209">Link to this property</a>

<details>

<summary>

RedirectRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)">RedirectRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010">Link to this property</a>

<details>

<summary>

RewriteRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)">RewriteRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011">Link to this property</a>

<details>

<summary>

RouteRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)">RouteRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012">Link to this property</a>

<details>

<summary>

ScoreRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)">ScoreRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013">Link to this property</a>

<details>

<summary>

ServeErrorRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)">ServeErrorRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014">Link to this property</a>

<details>

<summary>

SetCacheControlRule object {id, action, enabled, 10 more }

</summary>

id: string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20id">Link to this property</a>

action: "set\_cache\_control"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20last_updated">Link to this property</a>

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ref">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20version">Link to this property</a>

<details>

<summary>

action\_parameters: optional object {immutable, "max-age", "must-revalidate", 10 more }

The parameters configuring the rule’s action.

</summary>

<details>

<summary>

immutable: optional object {operation, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only }

Set the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable">Link to this property</a>

<details>

<summary>

"max-age": optional object {operation, value, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration that accepts a duration value in seconds.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, value, cloudflare\_only }

Set the directive with a duration value in seconds.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

value: number

The duration value in seconds for the directive.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200%20%3E%20(property)%20value">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age">Link to this property</a>

<details>

<summary>

"must-revalidate": optional object {operation, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only }

Set the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate">Link to this property</a>

<details>

<summary>

"must-understand": optional object {operation, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only }

Set the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand">Link to this property</a>

<details>

<summary>

"no-cache": optional object {operation, cloudflare\_only, qualifiers } or object {operation, cloudflare\_only }

A cache-control directive configuration that accepts optional qualifiers (header names).

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only, qualifiers }

Set the directive with optional qualifiers.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

qualifiers: optional array of string

Optional list of header names to qualify the directive (e.g., for “private” or “no-cache” directives).

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200%20%3E%20(property)%20qualifiers">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache">Link to this property</a>

<details>

<summary>

"no-store": optional object {operation, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only }

Set the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store">Link to this property</a>

<details>

<summary>

"no-transform": optional object {operation, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only }

Set the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform">Link to this property</a>

<details>

<summary>

private: optional object {operation, cloudflare\_only, qualifiers } or object {operation, cloudflare\_only }

A cache-control directive configuration that accepts optional qualifiers (header names).

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only, qualifiers }

Set the directive with optional qualifiers.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

qualifiers: optional array of string

Optional list of header names to qualify the directive (e.g., for “private” or “no-cache” directives).

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200%20%3E%20(property)%20qualifiers">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private">Link to this property</a>

<details>

<summary>

"proxy-revalidate": optional object {operation, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only }

Set the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate">Link to this property</a>

<details>

<summary>

public: optional object {operation, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, cloudflare\_only }

Set the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public">Link to this property</a>

<details>

<summary>

"s-maxage": optional object {operation, value, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration that accepts a duration value in seconds.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, value, cloudflare\_only }

Set the directive with a duration value in seconds.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

value: number

The duration value in seconds for the directive.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200%20%3E%20(property)%20value">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage">Link to this property</a>

<details>

<summary>

"stale-if-error": optional object {operation, value, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration that accepts a duration value in seconds.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, value, cloudflare\_only }

Set the directive with a duration value in seconds.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

value: number

The duration value in seconds for the directive.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200%20%3E%20(property)%20value">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error">Link to this property</a>

<details>

<summary>

"stale-while-revalidate": optional object {operation, value, cloudflare\_only } or object {operation, cloudflare\_only }

A cache-control directive configuration that accepts a duration value in seconds.

</summary>

One of the following:

<details>

<summary>

SetDirective object {operation, value, cloudflare\_only }

Set the directive with a duration value in seconds.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

value: number

The duration value in seconds for the directive.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20value">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

RemoveDirective object {operation, cloudflare\_only }

Remove the directive.

</summary>

<details>

<summary>

operation: "set"or "remove"

The operation to perform on the cache-control directive.

</summary>

One of the following:

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015">Link to this property</a>

<details>

<summary>

SetCacheSettingsRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)">SetCacheSettingsRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016">Link to this property</a>

<details>

<summary>

SetCacheTagsRule object {id, action, enabled, 10 more }

</summary>

id: string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20id">Link to this property</a>

action: "set\_cache\_tags"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20last_updated">Link to this property</a>

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ref">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20version">Link to this property</a>

<details>

<summary>

action\_parameters: optional object {operation, values } or object {expression, operation } or object {operation, values } or 3 more

The parameters configuring the rule’s action.

</summary>

One of the following:

<details>

<summary>

AddCacheTagsValues object {operation, values }

Add cache tags using a list of values.

</summary>

<details>

<summary>

operation: "add"or "remove"or "set"

The operation to perform on the cache tags.

</summary>

One of the following:

"add"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

values: array of string

A list of cache tag values.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20values">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

AddCacheTagsExpression object {expression, operation }

Add cache tags using an expression.

</summary>

expression: string

An expression that evaluates to an array of cache tag values.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20expression">Link to this property</a>

<details>

<summary>

operation: "add"or "remove"or "set"

The operation to perform on the cache tags.

</summary>

One of the following:

"add"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

RemoveCacheTagsValues object {operation, values }

Remove cache tags using a list of values.

</summary>

<details>

<summary>

operation: "add"or "remove"or "set"

The operation to perform on the cache tags.

</summary>

One of the following:

"add"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202%20%3E%20(property)%20operation">Link to this property</a>

values: array of string

A list of cache tag values.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202%20%3E%20(property)%20values">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

RemoveCacheTagsExpression object {expression, operation }

Remove cache tags using an expression.

</summary>

expression: string

An expression that evaluates to an array of cache tag values.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203%20%3E%20(property)%20expression">Link to this property</a>

<details>

<summary>

operation: "add"or "remove"or "set"

The operation to perform on the cache tags.

</summary>

One of the following:

"add"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203%20%3E%20(property)%20operation">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

SetCacheTagsValues object {operation, values }

Set cache tags using a list of values.

</summary>

<details>

<summary>

operation: "add"or "remove"or "set"

The operation to perform on the cache tags.

</summary>

One of the following:

"add"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204%20%3E%20(property)%20operation">Link to this property</a>

values: array of string

A list of cache tag values.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204%20%3E%20(property)%20values">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

SetCacheTagsExpression object {expression, operation }

Set cache tags using an expression.

</summary>

expression: string

An expression that evaluates to an array of cache tag values.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205%20%3E%20(property)%20expression">Link to this property</a>

<details>

<summary>

operation: "add"or "remove"or "set"

The operation to perform on the cache tags.

</summary>

One of the following:

"add"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205%20%3E%20(property)%20operation">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017">Link to this property</a>

<details>

<summary>

SetConfigurationRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)">SetConfigRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018">Link to this property</a>

<details>

<summary>

SkipRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)">SkipRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019">Link to this property</a>

<details>

<summary>

TransformResponseHTMLRule object {id, action, enabled, 10 more }

</summary>

id: string

The unique ID of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20id">Link to this property</a>

action: "transform\_response\_html"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20last_updated">Link to this property</a>

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ref">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20version">Link to this property</a>

<details>

<summary>

action\_parameters: optional object {link\_maze }

The parameters configuring the rule’s action.

</summary>

link\_maze: unknown

Enables the link maze transformation on the response.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20action_parameters%20%3E%20(property)%20link_maze">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20rules">Link to this property</a>

version: string

The version of the ruleset.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20version">Link to this property</a>

description: optional string

An informative description of the ruleset.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200%20%3E%20(property)%20description">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%200">Link to this property</a>

unknown

Returned when dry\_run is true.

<a href="#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(variant)%201">Link to this property</a>

</details>

[Link to this property](<#(resource)%20rulesets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)>)