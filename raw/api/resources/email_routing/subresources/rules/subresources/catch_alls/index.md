---
title: Catch Alls
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Email Routing](https://developers.cloudflare.com/api/resources/email_routing)

[Rules](https://developers.cloudflare.com/api/resources/email_routing/subresources/rules)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Catch Alls

##### [Get catch-all rule](https://developers.cloudflare.com/api/resources/email_routing/subresources/rules/subresources/catch_alls/methods/get)

GET/zones/{zone\_id}/email/routing/rules/catch\_all

##### [Update catch-all rule](https://developers.cloudflare.com/api/resources/email_routing/subresources/rules/subresources/catch_alls/methods/update)

PUT/zones/{zone\_id}/email/routing/rules/catch\_all

##### ModelsExpand Collapse

<details>

<summary>

CatchAllAction object {type, value }

Action for the catch-all routing rule.

</summary>

<details>

<summary>

type: "drop"or "forward"or "worker"

Type of action for catch-all rule.

</summary>

One of the following:

"drop"

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_action%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"forward"

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_action%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"worker"

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_action%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_action%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

value: optional array of string

List of values for the action. Currently limited to a single value.

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_action%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_action%20%3E%20(schema)>)

<details>

<summary>

CatchAllMatcher object {type }

Matcher for catch-all routing rule.

</summary>

type: "all"

Type of matcher. Default is ‘all’.

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_matcher%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_matcher%20%3E%20(schema)>)

<details>

<summary>

CatchAllGetResponse object {id, actions, enabled, 4 more }

</summary>

id: optional string

Routing rule identifier.

maxLength32

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

actions: optional array of <a href="https://developers.cloudflare.com/api/resources/email_routing#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_action%20%3E%20(schema)">CatchAllAction</a> { type, value }

List actions for the catch-all routing rule.

</summary>

<details>

<summary>

type: "drop"or "forward"or "worker"

Type of action for catch-all rule.

</summary>

One of the following:

"drop"

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_action%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"forward"

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_action%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"worker"

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_action%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_action%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

value: optional array of string

List of values for the action. Currently limited to a single value.

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_action%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_get_response%20%3E%20(schema)%20%3E%20(property)%20actions">Link to this property</a>

<details>

<summary>

enabled: optional trueor false

Routing rule status.

</summary>

One of the following:

true

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_get_response%20%3E%20(schema)%20%3E%20(property)%20enabled%20%3E%20(member)%200">Link to this property</a>

false

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_get_response%20%3E%20(schema)%20%3E%20(property)%20enabled%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_get_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

matchers: optional array of <a href="https://developers.cloudflare.com/api/resources/email_routing#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_matcher%20%3E%20(schema)">CatchAllMatcher</a> { type }

List of matchers for the catch-all routing rule.

</summary>

type: "all"

Type of matcher. Default is ‘all’.

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_matcher%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_get_response%20%3E%20(schema)%20%3E%20(property)%20matchers">Link to this property</a>

name: optional string

Routing rule name.

maxLength256

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

source: optional "api"or "wrangler"

Who manages the rule. <code>api</code> covers dashboard, generic API, and Terraform; <code>wrangler</code> means the rule is managed by a Worker’s wrangler.jsonc. Defaults to <code>api</code> when omitted on write.

</summary>

One of the following:

"api"

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"wrangler"

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_get_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_get_response%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

Deprecatedtag: optional string

Routing rule tag. (Deprecated, replaced by routing rule identifier)

maxLength32

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_get_response%20%3E%20(schema)%20%3E%20(property)%20tag">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_get_response%20%3E%20(schema)>)

<details>

<summary>

CatchAllUpdateResponse object {id, actions, enabled, 4 more }

</summary>

id: optional string

Routing rule identifier.

maxLength32

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_update_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

actions: optional array of <a href="https://developers.cloudflare.com/api/resources/email_routing#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_action%20%3E%20(schema)">CatchAllAction</a> { type, value }

List actions for the catch-all routing rule.

</summary>

<details>

<summary>

type: "drop"or "forward"or "worker"

Type of action for catch-all rule.

</summary>

One of the following:

"drop"

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_action%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"forward"

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_action%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"worker"

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_action%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_action%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

value: optional array of string

List of values for the action. Currently limited to a single value.

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_action%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_update_response%20%3E%20(schema)%20%3E%20(property)%20actions">Link to this property</a>

<details>

<summary>

enabled: optional trueor false

Routing rule status.

</summary>

One of the following:

true

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_update_response%20%3E%20(schema)%20%3E%20(property)%20enabled%20%3E%20(member)%200">Link to this property</a>

false

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_update_response%20%3E%20(schema)%20%3E%20(property)%20enabled%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_update_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

<details>

<summary>

matchers: optional array of <a href="https://developers.cloudflare.com/api/resources/email_routing#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_matcher%20%3E%20(schema)">CatchAllMatcher</a> { type }

List of matchers for the catch-all routing rule.

</summary>

type: "all"

Type of matcher. Default is ‘all’.

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_matcher%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_update_response%20%3E%20(schema)%20%3E%20(property)%20matchers">Link to this property</a>

name: optional string

Routing rule name.

maxLength256

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_update_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

<details>

<summary>

source: optional "api"or "wrangler"

Who manages the rule. <code>api</code> covers dashboard, generic API, and Terraform; <code>wrangler</code> means the rule is managed by a Worker’s wrangler.jsonc. Defaults to <code>api</code> when omitted on write.

</summary>

One of the following:

"api"

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%200">Link to this property</a>

"wrangler"

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_update_response%20%3E%20(schema)%20%3E%20(property)%20source%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_update_response%20%3E%20(schema)%20%3E%20(property)%20source">Link to this property</a>

Deprecatedtag: optional string

Routing rule tag. (Deprecated, replaced by routing rule identifier)

maxLength32

<a href="#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_update_response%20%3E%20(schema)%20%3E%20(property)%20tag">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_routing.rules.catch_alls%20%3E%20(model)%20catch_all_update_response%20%3E%20(schema)>)