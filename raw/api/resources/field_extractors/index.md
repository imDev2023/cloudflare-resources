---
title: Field Extractors
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Field Extractors

##### [Get Field Extractor](https://developers.cloudflare.com/api/resources/field_extractors/methods/get)

GET/accounts/{account\_id}/field\_extractors/{extractor}

##### [Update Field Extractor](https://developers.cloudflare.com/api/resources/field_extractors/methods/update)

PUT/accounts/{account\_id}/field\_extractors/{extractor}

##### [Delete Field Extractor](https://developers.cloudflare.com/api/resources/field_extractors/methods/delete)

DELETE/accounts/{account\_id}/field\_extractors/{extractor}

##### ModelsExpand Collapse

<details>

<summary>

FieldExtractorGetResponse object {extractor, rules }

</summary>

extractor: string

Extractor type.

<a href="#(resource)%20field_extractors%20%3E%20(model)%20field_extractor_get_response%20%3E%20(schema)%20%3E%20(property)%20extractor">Link to this property</a>

<details>

<summary>

rules: array of object {fields, ref, description }

</summary>

<details>

<summary>

fields: array of object {expression, name }

</summary>

expression: string

Wirefilter value expression.

<a href="#(resource)%20field_extractors%20%3E%20(model)%20field_extractor_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20fields%20%3E%20(items)%20%3E%20(property)%20expression">Link to this property</a>

name: string

Field name.

<a href="#(resource)%20field_extractors%20%3E%20(model)%20field_extractor_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20fields%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20field_extractors%20%3E%20(model)%20field_extractor_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20fields">Link to this property</a>

ref: string

Stable rule identifier.

<a href="#(resource)%20field_extractors%20%3E%20(model)%20field_extractor_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20ref">Link to this property</a>

description: optional string

Human-readable rule description.

<a href="#(resource)%20field_extractors%20%3E%20(model)%20field_extractor_get_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

</details>

<a href="#(resource)%20field_extractors%20%3E%20(model)%20field_extractor_get_response%20%3E%20(schema)%20%3E%20(property)%20rules">Link to this property</a>

</details>

[Link to this property](<#(resource)%20field_extractors%20%3E%20(model)%20field_extractor_get_response%20%3E%20(schema)>)

<details>

<summary>

FieldExtractorUpdateResponse object {extractor, rules }

</summary>

extractor: string

Extractor type.

<a href="#(resource)%20field_extractors%20%3E%20(model)%20field_extractor_update_response%20%3E%20(schema)%20%3E%20(property)%20extractor">Link to this property</a>

<details>

<summary>

rules: array of object {fields, ref, description }

</summary>

<details>

<summary>

fields: array of object {expression, name }

</summary>

expression: string

Wirefilter value expression.

<a href="#(resource)%20field_extractors%20%3E%20(model)%20field_extractor_update_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20fields%20%3E%20(items)%20%3E%20(property)%20expression">Link to this property</a>

name: string

Field name.

<a href="#(resource)%20field_extractors%20%3E%20(model)%20field_extractor_update_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20fields%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20field_extractors%20%3E%20(model)%20field_extractor_update_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20fields">Link to this property</a>

ref: string

Stable rule identifier.

<a href="#(resource)%20field_extractors%20%3E%20(model)%20field_extractor_update_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20ref">Link to this property</a>

description: optional string

Human-readable rule description.

<a href="#(resource)%20field_extractors%20%3E%20(model)%20field_extractor_update_response%20%3E%20(schema)%20%3E%20(property)%20rules%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

</details>

<a href="#(resource)%20field_extractors%20%3E%20(model)%20field_extractor_update_response%20%3E%20(schema)%20%3E%20(property)%20rules">Link to this property</a>

</details>

[Link to this property](<#(resource)%20field_extractors%20%3E%20(model)%20field_extractor_update_response%20%3E%20(schema)>)

FieldExtractorDeleteResponse = unknown

Result is null.

[Link to this property](<#(resource)%20field_extractors%20%3E%20(model)%20field_extractor_delete_response%20%3E%20(schema)>)