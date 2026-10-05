---
title: Origin Post Quantum Encryption
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Origin Post Quantum Encryption

##### [Get Origin Post-Quantum Encryption setting](https://developers.cloudflare.com/api/resources/origin_post_quantum_encryption/methods/get)

Deprecated

GET/zones/{zone\_id}/cache/origin\_post\_quantum\_encryption

##### [Change Origin Post-Quantum Encryption setting](https://developers.cloudflare.com/api/resources/origin_post_quantum_encryption/methods/update)

Deprecated

PUT/zones/{zone\_id}/cache/origin\_post\_quantum\_encryption

##### ModelsExpand Collapse

<details>

<summary>

OriginPostQuantumEncryptionGetResponse object {id, editable, value, modified\_on }

</summary>

id: "origin\_pqe"

The identifier of the caching setting.

<a href="#(resource)%20origin_post_quantum_encryption%20%3E%20(model)%20origin_post_quantum_encryption_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

editable: boolean

Whether the setting is editable.

<a href="#(resource)%20origin_post_quantum_encryption%20%3E%20(model)%20origin_post_quantum_encryption_get_response%20%3E%20(schema)%20%3E%20(property)%20editable">Link to this property</a>

<details>

<summary>

value: "preferred"or "supported"or "off"

Value of the Origin Post Quantum Encryption Setting.

</summary>

One of the following:

"preferred"

<a href="#(resource)%20origin_post_quantum_encryption%20%3E%20(model)%20origin_post_quantum_encryption_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%200">Link to this property</a>

"supported"

<a href="#(resource)%20origin_post_quantum_encryption%20%3E%20(model)%20origin_post_quantum_encryption_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%201">Link to this property</a>

"off"

<a href="#(resource)%20origin_post_quantum_encryption%20%3E%20(model)%20origin_post_quantum_encryption_get_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20origin_post_quantum_encryption%20%3E%20(model)%20origin_post_quantum_encryption_get_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

modified\_on: optional string

Last time this setting was modified.

formatdate-time

<a href="#(resource)%20origin_post_quantum_encryption%20%3E%20(model)%20origin_post_quantum_encryption_get_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

</details>

[Link to this property](<#(resource)%20origin_post_quantum_encryption%20%3E%20(model)%20origin_post_quantum_encryption_get_response%20%3E%20(schema)>)

<details>

<summary>

OriginPostQuantumEncryptionUpdateResponse object {id, editable, value, modified\_on }

</summary>

id: "origin\_pqe"

The identifier of the caching setting.

<a href="#(resource)%20origin_post_quantum_encryption%20%3E%20(model)%20origin_post_quantum_encryption_update_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

editable: boolean

Whether the setting is editable.

<a href="#(resource)%20origin_post_quantum_encryption%20%3E%20(model)%20origin_post_quantum_encryption_update_response%20%3E%20(schema)%20%3E%20(property)%20editable">Link to this property</a>

<details>

<summary>

value: "preferred"or "supported"or "off"

Value of the Origin Post Quantum Encryption Setting.

</summary>

One of the following:

"preferred"

<a href="#(resource)%20origin_post_quantum_encryption%20%3E%20(model)%20origin_post_quantum_encryption_update_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%200">Link to this property</a>

"supported"

<a href="#(resource)%20origin_post_quantum_encryption%20%3E%20(model)%20origin_post_quantum_encryption_update_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%201">Link to this property</a>

"off"

<a href="#(resource)%20origin_post_quantum_encryption%20%3E%20(model)%20origin_post_quantum_encryption_update_response%20%3E%20(schema)%20%3E%20(property)%20value%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20origin_post_quantum_encryption%20%3E%20(model)%20origin_post_quantum_encryption_update_response%20%3E%20(schema)%20%3E%20(property)%20value">Link to this property</a>

modified\_on: optional string

Last time this setting was modified.

formatdate-time

<a href="#(resource)%20origin_post_quantum_encryption%20%3E%20(model)%20origin_post_quantum_encryption_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_on">Link to this property</a>

</details>

[Link to this property](<#(resource)%20origin_post_quantum_encryption%20%3E%20(model)%20origin_post_quantum_encryption_update_response%20%3E%20(schema)>)