---
title: Tags
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Cloudforce One](https://developers.cloudflare.com/api/resources/cloudforce_one)

[Threat Signals](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals)

[Articles](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Tags

##### [Add tag to Threat Signals article](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/subresources/tags/methods/create)

POST/accounts/{account\_id}/cloudforce-one/v2/threat-signals/articles/{article\_id}/tags

##### [Remove tag from Threat Signals article](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/subresources/tags/methods/delete)

DELETE/accounts/{account\_id}/cloudforce-one/v2/threat-signals/articles/{article\_id}/tags/{tag\_id}

##### [Generate Threat Signals article AI tags](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_signals/subresources/articles/subresources/tags/methods/generate)

POST/accounts/{account\_id}/cloudforce-one/v2/threat-signals/articles/{article\_id}/tag

##### ModelsExpand Collapse

<details>

<summary>

TagCreateResponse object {applied\_by, categoryId, uuid, value }

</summary>

<details>

<summary>

applied\_by: "ai"or "analyst"or "system"

</summary>

One of the following:

"ai"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20applied_by%20%3E%20(member)%200">Link to this property</a>

"analyst"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20applied_by%20%3E%20(member)%201">Link to this property</a>

"system"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20applied_by%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20applied_by">Link to this property</a>

categoryId: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20categoryId">Link to this property</a>

uuid: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_create_response%20%3E%20(schema)>)

<details>

<summary>

TagDeleteResponse object {applied\_by, categoryId, uuid, value }

</summary>

<details>

<summary>

applied\_by: "ai"or "analyst"or "system"

</summary>

One of the following:

"ai"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(property)%20applied_by%20%3E%20(member)%200">Link to this property</a>

"analyst"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(property)%20applied_by%20%3E%20(member)%201">Link to this property</a>

"system"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(property)%20applied_by%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(property)%20applied_by">Link to this property</a>

categoryId: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(property)%20categoryId">Link to this property</a>

uuid: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_delete_response%20%3E%20(schema)>)

<details>

<summary>

TagGenerateResponse object {tag\_skill\_version, tags }

</summary>

tag\_skill\_version: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tag_skill_version">Link to this property</a>

<details>

<summary>

tags: array of object {applied\_by, categoryId, uuid, value }

Final hydrated assignment set; may be empty when no applicable tags are selected.

</summary>

<details>

<summary>

applied\_by: "ai"or "analyst"or "system"

</summary>

One of the following:

"ai"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%200">Link to this property</a>

"analyst"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%201">Link to this property</a>

"system"

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20applied_by">Link to this property</a>

categoryId: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20categoryId">Link to this property</a>

uuid: string

formatuuid

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20uuid">Link to this property</a>

value: string

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)%20%3E%20(property)%20tags">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_signals.articles.tags%20%3E%20(model)%20tag_generate_response%20%3E%20(schema)>)