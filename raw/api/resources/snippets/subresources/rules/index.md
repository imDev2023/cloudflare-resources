---
title: Rules
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Snippets](https://developers.cloudflare.com/api/resources/snippets)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Rules

##### [List zone snippet rules](https://developers.cloudflare.com/api/resources/snippets/subresources/rules/methods/get)

GET/zones/{zone\_id}/snippets/snippet\_rules

##### [List zone snippet rules](https://developers.cloudflare.com/api/resources/snippets/subresources/rules/methods/list)

GET/zones/{zone\_id}/snippets/snippet\_rules

##### [Update zone snippet rules](https://developers.cloudflare.com/api/resources/snippets/subresources/rules/methods/update)

PUT/zones/{zone\_id}/snippets/snippet\_rules

##### [Delete zone snippet rules](https://developers.cloudflare.com/api/resources/snippets/subresources/rules/methods/delete)

DELETE/zones/{zone\_id}/snippets/snippet\_rules

##### ModelsExpand Collapse

<details>

<summary>

RuleGetResponse object {id, expression, last\_updated, 3 more }

Define a snippet rule.

</summary>

id: string

Specify the unique ID of the rule.

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

expression: string

Define the expression that determines which traffic matches the rule.

minLength1

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

Specify the timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

snippet\_name: string

Identify the snippet.

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20snippet_name">Link to this property</a>

description: optional string

Provide an informative description of the rule.

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Indicate whether to execute the rule.

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

</details>

[Link to this property](<#(resource)%20snippets.rules%20%3E%20(model)%20rule_get_response%20%3E%20(schema)>)

<details>

<summary>

RuleListResponse object {id, expression, last\_updated, 3 more }

Define a snippet rule.

</summary>

id: string

Specify the unique ID of the rule.

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

expression: string

Define the expression that determines which traffic matches the rule.

minLength1

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

Specify the timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

snippet\_name: string

Identify the snippet.

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20snippet_name">Link to this property</a>

description: optional string

Provide an informative description of the rule.

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Indicate whether to execute the rule.

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

</details>

[Link to this property](<#(resource)%20snippets.rules%20%3E%20(model)%20rule_list_response%20%3E%20(schema)>)

<details>

<summary>

RuleUpdateResponse object {id, expression, last\_updated, 3 more }

Define a snippet rule.

</summary>

id: string

Specify the unique ID of the rule.

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

expression: string

Define the expression that determines which traffic matches the rule.

minLength1

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

Specify the timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

snippet\_name: string

Identify the snippet.

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20snippet_name">Link to this property</a>

description: optional string

Provide an informative description of the rule.

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Indicate whether to execute the rule.

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

</details>

[Link to this property](<#(resource)%20snippets.rules%20%3E%20(model)%20rule_update_response%20%3E%20(schema)>)

<details>

<summary>

RuleDeleteResponse object {id, expression, last\_updated, 3 more }

Define a snippet rule.

</summary>

id: string

Specify the unique ID of the rule.

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

expression: string

Define the expression that determines which traffic matches the rule.

minLength1

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20expression">Link to this property</a>

last\_updated: string

Specify the timestamp of when the rule was last modified.

formatdate-time

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20last_updated">Link to this property</a>

snippet\_name: string

Identify the snippet.

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20snippet_name">Link to this property</a>

description: optional string

Provide an informative description of the rule.

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Indicate whether to execute the rule.

<a href="#(resource)%20snippets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

</details>

[Link to this property](<#(resource)%20snippets.rules%20%3E%20(model)%20rule_delete_response%20%3E%20(schema)>)