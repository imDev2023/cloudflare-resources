---
title: Evaluate
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Flagship](https://developers.cloudflare.com/api/resources/flagship)

[Apps](https://developers.cloudflare.com/api/resources/flagship/subresources/apps)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Evaluate

##### [Evaluate flag from query context](https://developers.cloudflare.com/api/resources/flagship/subresources/apps/subresources/evaluate/methods/get)

GET/accounts/{account\_id}/flagship/apps/{app\_id}/evaluate

##### ModelsExpand Collapse

<details>

<summary>

EvaluateGetResponse object {flagKey, reason, variant, value }

</summary>

flagKey: string

Key of the evaluated flag.

<a href="#(resource)%20flagship.apps.evaluate%20%3E%20(model)%20evaluate_get_response%20%3E%20(schema)%20%3E%20(property)%20flagKey">Link to this property</a>

<details>

<summary>

reason: "STATIC"or "TARGETING\_MATCH"or "DEFAULT"or 2 more

Reason the evaluator selected this variation.

</summary>

One of the following:

"STATIC"

<a href="#(resource)%20flagship.apps.evaluate%20%3E%20(model)%20evaluate_get_response%20%3E%20(schema)%20%3E%20(property)%20reason%20%3E%20(member)%200">Link to this property</a>

"TARGETING\_MATCH"

<a href="#(resource)%20flagship.apps.evaluate%20%3E%20(model)%20evaluate_get_response%20%3E%20(schema)%20%3E%20(property)%20reason%20%3E%20(member)%201">Link to this property</a>

"DEFAULT"

<a href="#(resource)%20flagship.apps.evaluate%20%3E%20(model)%20evaluate_get_response%20%3E%20(schema)%20%3E%20(property)%20reason%20%3E%20(member)%202">Link to this property</a>

"DISABLED"

<a href="#(resource)%20flagship.apps.evaluate%20%3E%20(model)%20evaluate_get_response%20%3E%20(schema)%20%3E%20(property)%20reason%20%3E%20(member)%203">Link to this property</a>

"SPLIT"

<a href="#(resource)%20flagship.apps.evaluate%20%3E%20(model)%20evaluate_get_response%20%3E%20(schema)%20%3E%20(property)%20reason%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20flagship.apps.evaluate%20%3E%20(model)%20evaluate_get_response%20%3E%20(schema)%20%3E%20(property)%20reason">Link to this property</a>

variant: string

Name of the variation that supplied the resolved value.

<a href="#(resource)%20flagship.apps.evaluate%20%3E%20(model)%20evaluate_get_response%20%3E%20(schema)%20%3E%20(property)%20variant">Link to this property</a>

<details>

<summary>

value: optional stringor numberor booleanor 2 more

</summary>

One of the following:

string

<a href="#(resource)%20flagship.apps.evaluate%20%3E%20(model)%20evaluate_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%200">Link to this property</a>

number

<a href="#(resource)%20flagship.apps.evaluate%20%3E%20(model)%20evaluate_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%201">Link to this property</a>

boolean

<a href="#(resource)%20flagship.apps.evaluate%20%3E%20(model)%20evaluate_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%202">Link to this property</a>

map\[unknown]

<a href="#(resource)%20flagship.apps.evaluate%20%3E%20(model)%20evaluate_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%203">Link to this property</a>

array of unknown

<a href="#(resource)%20flagship.apps.evaluate%20%3E%20(model)%20evaluate_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(variant)%204">Link to this property</a>

</details>

<a href="#(resource)%20flagship.apps.evaluate%20%3E%20(model)%20evaluate_get_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

[Link to this property](<#(resource)%20flagship.apps.evaluate%20%3E%20(model)%20evaluate_get_response%20%3E%20(schema)>)