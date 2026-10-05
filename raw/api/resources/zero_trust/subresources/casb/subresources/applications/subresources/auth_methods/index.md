---
title: Auth Methods
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[Casb](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb)

[Applications](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/applications)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Auth Methods

##### [Get auth methods](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/applications/subresources/auth_methods/methods/list)

GET/accounts/{account\_id}/one/applications/{application\_id}/auth-methods

##### ModelsExpand Collapse

<details>

<summary>

AuthMethodListResponse object {id, display\_name, human\_interaction\_required, 4 more }

Detailed auth method info including credentials schema and instructions.

</summary>

id: string

Auth method identifier.

<a href="#(resource)%20zero_trust.casb.applications.auth_methods%20%3E%20(model)%20auth_method_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

display\_name: string

Human-readable auth method name.

<a href="#(resource)%20zero_trust.casb.applications.auth_methods%20%3E%20(model)%20auth_method_list_response%20%3E%20(schema)%20%3E%20(property)%20display_name">Link to this property</a>

human\_interaction\_required: boolean

Whether setup requires human interaction or integration can be created purely using API (e.g., For OAuth can not be created without user interaction).

<a href="#(resource)%20zero_trust.casb.applications.auth_methods%20%3E%20(model)%20auth_method_list_response%20%3E%20(schema)%20%3E%20(property)%20human_interaction_required">Link to this property</a>

<details>

<summary>

instructions: object {markdown }

Step-by-step instructions for obtaining credentials.

</summary>

markdown: string

Detailed instructions in markdown format.

<a href="#(resource)%20zero_trust.casb.applications.auth_methods%20%3E%20(model)%20auth_method_list_response%20%3E%20(schema)%20%3E%20(property)%20instructions%20%3E%20(property)%20markdown">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.applications.auth_methods%20%3E%20(model)%20auth_method_list_response%20%3E%20(schema)%20%3E%20(property)%20instructions">Link to this property</a>

payload\_example: map\[unknown]

Example credentials payload with placeholder values.

<a href="#(resource)%20zero_trust.casb.applications.auth_methods%20%3E%20(model)%20auth_method_list_response%20%3E%20(schema)%20%3E%20(property)%20payload_example">Link to this property</a>

payload\_schema: map\[unknown]

JSON Schema for the credentials object in POST /v2/integrations request.

<a href="#(resource)%20zero_trust.casb.applications.auth_methods%20%3E%20(model)%20auth_method_list_response%20%3E%20(schema)%20%3E%20(property)%20payload_schema">Link to this property</a>

redirect\_url: string

OAuth redirect URL for vendors requiring human interaction.

<a href="#(resource)%20zero_trust.casb.applications.auth_methods%20%3E%20(model)%20auth_method_list_response%20%3E%20(schema)%20%3E%20(property)%20redirect_url">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.casb.applications.auth_methods%20%3E%20(model)%20auth_method_list_response%20%3E%20(schema)>)