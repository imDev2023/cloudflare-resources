---
title: Versions
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Rulesets](https://developers.cloudflare.com/api/resources/rulesets)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Versions

##### [List an account or zone ruleset's versions](https://developers.cloudflare.com/api/resources/rulesets/subresources/versions/methods/list)

GET/{accounts\_or\_zones}/{account\_or\_zone\_id}/rulesets/{ruleset\_id}/versions

##### [Get an account or zone ruleset version](https://developers.cloudflare.com/api/resources/rulesets/subresources/versions/methods/get)

GET/{accounts\_or\_zones}/{account\_or\_zone\_id}/rulesets/{ruleset\_id}/versions/{ruleset\_version}

##### [Delete an account or zone ruleset version](https://developers.cloudflare.com/api/resources/rulesets/subresources/versions/methods/delete)

DELETE/{accounts\_or\_zones}/{account\_or\_zone\_id}/rulesets/{ruleset\_id}/versions/{ruleset\_version}

##### ModelsExpand Collapse

<details>

<summary>

VersionListResponse object {id, kind, last\_updated, 4 more }

A ruleset object.

</summary>

id: string

The unique ID of the ruleset.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

kind: <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets%20%3E%20(model)%20kind%20%3E%20(schema)">Kind</a>

The kind of the ruleset.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20kind">Link to this property</a>

last\_updated: string

The timestamp of when the ruleset was last modified.

formatdate-time

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

name: string

The human-readable name of the ruleset.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

phase: <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)">Phase</a>

The phase of the ruleset.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20phase">Link to this property</a>

version: string

The version of the ruleset.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

description: optional string

An informative description of the ruleset.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

</details>

[Link to this property](<#(resource)%20rulesets.versions%20%3E%20(model)%20version_list_response%20%3E%20(schema)>)

<details>

<summary>

VersionGetResponse object {id, kind, last\_updated, 5 more }

A ruleset object.

</summary>

id: string

The unique ID of the ruleset.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

kind: <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets%20%3E%20(model)%20kind%20%3E%20(schema)">Kind</a>

The kind of the ruleset.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20kind">Link to this property</a>

last\_updated: string

The timestamp of when the ruleset was last modified.

formatdate-time

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

name: string

The human-readable name of the ruleset.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

phase: <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets%20%3E%20(model)%20phase%20%3E%20(schema)">Phase</a>

The phase of the ruleset.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20phase">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

ChallengeRule object {id, action, enabled, 10 more }

</summary>

id: string

The unique ID of the rule.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20id">Link to this property</a>

action: "challenge"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

Whether the rule should be executed.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20last_updated">Link to this property</a>

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ref">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20version">Link to this property</a>

action\_parameters: optional unknown

The parameters configuring the rule’s action.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20ratelimit">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

ResponseCompressionRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20compress_response_rule%20%3E%20(schema)">CompressResponseRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

DDoSDynamicRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20ddos_dynamic_rule%20%3E%20(schema)">DDoSDynamicRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

ExecuteRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20execute_rule%20%3E%20(schema)">ExecuteRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

ForceConnectionCloseRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20force_connection_close_rule%20%3E%20(schema)">ForceConnectionCloseRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%205">Link to this property</a>

<details>

<summary>

JavaScriptChallengeRule object {id, action, enabled, 10 more }

</summary>

id: string

The unique ID of the rule.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20id">Link to this property</a>

action: "js\_challenge"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

Whether the rule should be executed.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20last_updated">Link to this property</a>

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ref">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20version">Link to this property</a>

action\_parameters: optional unknown

The parameters configuring the rule’s action.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20ratelimit">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%206">Link to this property</a>

<details>

<summary>

LogRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20log_rule%20%3E%20(schema)">LogRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%207">Link to this property</a>

<details>

<summary>

LogCustomFieldRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20log_custom_field_rule%20%3E%20(schema)">LogCustomFieldRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%208">Link to this property</a>

<details>

<summary>

ManagedChallengeRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20managed_challenge_rule%20%3E%20(schema)">ManagedChallengeRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%209">Link to this property</a>

<details>

<summary>

RedirectRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20redirect_rule%20%3E%20(schema)">RedirectRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2010">Link to this property</a>

<details>

<summary>

RewriteRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20rewrite_rule%20%3E%20(schema)">RewriteRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2011">Link to this property</a>

<details>

<summary>

RouteRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20route_rule%20%3E%20(schema)">RouteRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2012">Link to this property</a>

<details>

<summary>

ScoreRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20score_rule%20%3E%20(schema)">ScoreRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2013">Link to this property</a>

<details>

<summary>

ServeErrorRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20serve_error_rule%20%3E%20(schema)">ServeErrorRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2014">Link to this property</a>

<details>

<summary>

SetCacheControlRule object {id, action, enabled, 10 more }

</summary>

id: string

The unique ID of the rule.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20id">Link to this property</a>

action: "set\_cache\_control"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20last_updated">Link to this property</a>

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ref">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20version">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%200">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20immutable">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

value: number

The duration value in seconds for the directive.

minimum0

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200%20%3E%20(property)%20value">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%200">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20max-age">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%200">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-revalidate">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%200">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20must-understand">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

qualifiers: optional array of string

Optional list of header names to qualify the directive (e.g., for “private” or “no-cache” directives).

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200%20%3E%20(property)%20qualifiers">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%200">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-cache">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%200">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-store">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%200">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20no-transform">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

qualifiers: optional array of string

Optional list of header names to qualify the directive (e.g., for “private” or “no-cache” directives).

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200%20%3E%20(property)%20qualifiers">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%200">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20private">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%200">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20proxy-revalidate">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%200">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20public">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

value: number

The duration value in seconds for the directive.

minimum0

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200%20%3E%20(property)%20value">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%200">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20s-maxage">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

value: number

The duration value in seconds for the directive.

minimum0

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200%20%3E%20(property)%20value">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%200">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-if-error">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

value: number

The duration value in seconds for the directive.

minimum0

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20value">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%200">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

cloudflare\_only: optional boolean

Whether the directive should only be applied to the Cloudflare CDN cache.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%201%20%3E%20(property)%20cloudflare_only">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters%20%3E%20(property)%20stale-while-revalidate">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015%20%3E%20(property)%20ratelimit">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2015">Link to this property</a>

<details>

<summary>

SetCacheSettingsRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20set_cache_settings_rule%20%3E%20(schema)">SetCacheSettingsRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2016">Link to this property</a>

<details>

<summary>

SetCacheTagsRule object {id, action, enabled, 10 more }

</summary>

id: string

The unique ID of the rule.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20id">Link to this property</a>

action: "set\_cache\_tags"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20last_updated">Link to this property</a>

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ref">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20version">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20operation">Link to this property</a>

values: array of string

A list of cache tag values.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200%20%3E%20(property)%20values">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

AddCacheTagsExpression object {expression, operation }

Add cache tags using an expression.

</summary>

expression: string

An expression that evaluates to an array of cache tag values.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20expression">Link to this property</a>

<details>

<summary>

operation: "add"or "remove"or "set"

The operation to perform on the cache tags.

</summary>

One of the following:

"add"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201%20%3E%20(property)%20operation">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%201">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202%20%3E%20(property)%20operation">Link to this property</a>

values: array of string

A list of cache tag values.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202%20%3E%20(property)%20values">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

RemoveCacheTagsExpression object {expression, operation }

Remove cache tags using an expression.

</summary>

expression: string

An expression that evaluates to an array of cache tag values.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203%20%3E%20(property)%20expression">Link to this property</a>

<details>

<summary>

operation: "add"or "remove"or "set"

The operation to perform on the cache tags.

</summary>

One of the following:

"add"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203%20%3E%20(property)%20operation">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%203">Link to this property</a>

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

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204%20%3E%20(property)%20operation">Link to this property</a>

values: array of string

A list of cache tag values.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204%20%3E%20(property)%20values">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

SetCacheTagsExpression object {expression, operation }

Set cache tags using an expression.

</summary>

expression: string

An expression that evaluates to an array of cache tag values.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205%20%3E%20(property)%20expression">Link to this property</a>

<details>

<summary>

operation: "add"or "remove"or "set"

The operation to perform on the cache tags.

</summary>

One of the following:

"add"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205%20%3E%20(property)%20operation%20%3E%20(member)%200">Link to this property</a>

"remove"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205%20%3E%20(property)%20operation%20%3E%20(member)%201">Link to this property</a>

"set"

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205%20%3E%20(property)%20operation%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205%20%3E%20(property)%20operation">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters%20%3E%20(variant)%205">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017%20%3E%20(property)%20ratelimit">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2017">Link to this property</a>

<details>

<summary>

SetConfigurationRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20set_config_rule%20%3E%20(schema)">SetConfigRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2018">Link to this property</a>

<details>

<summary>

SkipRule = <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20skip_rule%20%3E%20(schema)">SkipRule</a> { last\_updated, version, id, 10 more }

</summary>

id: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

action: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(entry)%201%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(entry)%201%20%3E%20(property)%20expression">Link to this property</a>

ref: string

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019%20%3E%20(entry)%201%20%3E%20(property)%20ref">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2019">Link to this property</a>

<details>

<summary>

TransformResponseHTMLRule object {id, action, enabled, 10 more }

</summary>

id: string

The unique ID of the rule.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20id">Link to this property</a>

action: "transform\_response\_html"

The action to perform when the rule matches.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20action">Link to this property</a>

enabled: boolean

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20enabled">Link to this property</a>

expression: string

The expression defining which traffic will match the rule.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

The timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20last_updated">Link to this property</a>

ref: string

The reference of the rule (the rule’s ID by default).

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ref">Link to this property</a>

version: string

The version of the rule.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20version">Link to this property</a>

<details>

<summary>

action\_parameters: optional object {link\_maze }

The parameters configuring the rule’s action.

</summary>

link\_maze: unknown

Enables the link maze transformation on the response.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20action_parameters%20%3E%20(property)%20link_maze">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20action_parameters">Link to this property</a>

categories: optional array of string

The categories of the rule.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20categories">Link to this property</a>

description: optional string

An informative description of the rule.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

exposed\_credential\_check: optional object {password\_expression, username\_expression }

Configuration for exposed credential checking.

</summary>

password\_expression: string

An expression that selects the password used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20password_expression">Link to this property</a>

username\_expression: string

An expression that selects the user ID used in the credentials check.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20exposed_credential_check%20%3E%20(property)%20username_expression">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20exposed_credential_check">Link to this property</a>

logging: optional <a href="https://developers.cloudflare.com/api/resources/rulesets#(resource)%20rulesets.rules%20%3E%20(model)%20logging%20%3E%20(schema)">Logging</a> { enabled }

An object configuring the rule’s logging behavior.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20logging">Link to this property</a>

<details>

<summary>

ratelimit: optional object {characteristics, period, counting\_expression, 5 more }

An object configuring the rule’s rate limit behavior.

</summary>

characteristics: array of string

Characteristics of the request on which the rate limit counter will be incremented.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20characteristics">Link to this property</a>

period: number

Period in seconds over which the counter is being incremented.

minimum0

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20period">Link to this property</a>

counting\_expression: optional string

An expression that defines when the rate limit counter should be incremented. It defaults to the same as the rule’s expression.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20counting_expression">Link to this property</a>

mitigation\_timeout: optional number

Period of time in seconds after which the action will be disabled following its first execution.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20mitigation_timeout">Link to this property</a>

requests\_per\_period: optional number

The threshold of requests per period after which the action will be executed for the first time.

minimum1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_per_period">Link to this property</a>

requests\_to\_origin: optional boolean

Whether counting is only performed when an origin is reached.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20requests_to_origin">Link to this property</a>

score\_per\_period: optional number

The score threshold per period for which the action will be executed the first time.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_per_period">Link to this property</a>

score\_response\_header\_name: optional string

A response header name provided by the origin, which contains the score to increment rate limit counter with.

minLength1

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit%20%3E%20(property)%20score_response_header_name">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020%20%3E%20(property)%20ratelimit">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(variant)%2020">Link to this property</a>

</details>

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20rules">Link to this property</a>

version: string

The version of the ruleset.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

description: optional string

An informative description of the ruleset.

<a href="#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

</details>

[Link to this property](<#(resource)%20rulesets.versions%20%3E%20(model)%20version_get_response%20%3E%20(schema)>)