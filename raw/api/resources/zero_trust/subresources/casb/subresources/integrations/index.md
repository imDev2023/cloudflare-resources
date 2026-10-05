---
title: Integrations
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[Casb](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Integrations

##### [List integrations](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/integrations/methods/list)

GET/accounts/{account\_id}/one/integrations

##### [Get integration details](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/integrations/methods/get)

GET/accounts/{account\_id}/one/integrations/{id}

##### [Create integration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/integrations/methods/create)

POST/accounts/{account\_id}/one/integrations

##### [Update integration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/integrations/methods/update)

PATCH/accounts/{account\_id}/one/integrations/{id}

##### [Delete integration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/integrations/methods/delete)

DELETE/accounts/{account\_id}/one/integrations/{id}

##### [Pause integration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/integrations/methods/pause)

POST/accounts/{account\_id}/one/integrations/{id}/pause

##### [Resume integration](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/integrations/methods/resume)

POST/accounts/{account\_id}/one/integrations/{id}/resume

##### ModelsExpand Collapse

<details>

<summary>

IntegrationListResponse object {id, application, created, 4 more }

Serializer for v2 integration list responses.

</summary>

id: string

Integration ID.

formatuuid

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

application: map\[string]

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_list_response%20%3E%20(schema)%20%3E%20(property)%20application">Link to this property</a>

created: string

When the integration was created.

formatdate-time

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_list_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

is\_paused: boolean

Whether the user paused the integration.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_list_response%20%3E%20(schema)%20%3E%20(property)%20is_paused">Link to this property</a>

name: string

Name of the integration.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_list_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

status: string

Integration status.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_list_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

updated: string

When the integration was last updated.

formatdate-time

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_list_response%20%3E%20(schema)%20%3E%20(property)%20updated">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_list_response%20%3E%20(schema)>)

<details>

<summary>

IntegrationGetResponse object {id, application, auth\_method, 11 more }

The requested item.

</summary>

id: string

Integration ID.

formatuuid

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

application: map\[string]

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_get_response%20%3E%20(schema)%20%3E%20(property)%20application">Link to this property</a>

auth\_method: map\[string]

The integration’s authentication method.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_get_response%20%3E%20(schema)%20%3E%20(property)%20auth_method">Link to this property</a>

<details>

<summary>

authorization\_link: object {components, link }

Authorization link for the integration.

</summary>

components: map\[unknown]

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_get_response%20%3E%20(schema)%20%3E%20(property)%20authorization_link%20%3E%20(property)%20components">Link to this property</a>

link: string

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_get_response%20%3E%20(schema)%20%3E%20(property)%20authorization_link%20%3E%20(property)%20link">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_get_response%20%3E%20(schema)%20%3E%20(property)%20authorization_link">Link to this property</a>

created: string

When the integration was created.

formatdate-time

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_get_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

credentials\_expiry: string

Credentials expiry time.

formatdate-time

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_get_response%20%3E%20(schema)%20%3E%20(property)%20credentials_expiry">Link to this property</a>

dlp\_profiles: array of string

DLP Profiles enabled for the integration.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_get_response%20%3E%20(schema)%20%3E%20(property)%20dlp_profiles">Link to this property</a>

health\_details: array of map\[unknown]

Health details with remediation hints.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_get_response%20%3E%20(schema)%20%3E%20(property)%20health_details">Link to this property</a>

is\_paused: boolean

Whether the user paused the integration.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_get_response%20%3E%20(schema)%20%3E%20(property)%20is_paused">Link to this property</a>

last\_hydrated: string

Last time the integration was hydrated.

formatdate-time

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_get_response%20%3E%20(schema)%20%3E%20(property)%20last_hydrated">Link to this property</a>

name: string

Name of the integration.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

status: string

Integration status.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_get_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

updated: string

When the integration was last updated.

formatdate-time

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_get_response%20%3E%20(schema)%20%3E%20(property)%20updated">Link to this property</a>

use\_cases: array of map\[unknown]

Use cases enabled for the integration.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_get_response%20%3E%20(schema)>)

<details>

<summary>

IntegrationCreateResponse object {id, application, auth\_method, 11 more }

The requested item.

</summary>

id: string

Integration ID.

formatuuid

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

application: map\[string]

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_create_response%20%3E%20(schema)%20%3E%20(property)%20application">Link to this property</a>

auth\_method: map\[string]

The integration’s authentication method.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_create_response%20%3E%20(schema)%20%3E%20(property)%20auth_method">Link to this property</a>

<details>

<summary>

authorization\_link: object {components, link }

Authorization link for the integration.

</summary>

components: map\[unknown]

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_create_response%20%3E%20(schema)%20%3E%20(property)%20authorization_link%20%3E%20(property)%20components">Link to this property</a>

link: string

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_create_response%20%3E%20(schema)%20%3E%20(property)%20authorization_link%20%3E%20(property)%20link">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_create_response%20%3E%20(schema)%20%3E%20(property)%20authorization_link">Link to this property</a>

created: string

When the integration was created.

formatdate-time

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_create_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

credentials\_expiry: string

Credentials expiry time.

formatdate-time

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_create_response%20%3E%20(schema)%20%3E%20(property)%20credentials_expiry">Link to this property</a>

dlp\_profiles: array of string

DLP Profiles enabled for the integration.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_create_response%20%3E%20(schema)%20%3E%20(property)%20dlp_profiles">Link to this property</a>

health\_details: array of map\[unknown]

Health details with remediation hints.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_create_response%20%3E%20(schema)%20%3E%20(property)%20health_details">Link to this property</a>

is\_paused: boolean

Whether the user paused the integration.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_create_response%20%3E%20(schema)%20%3E%20(property)%20is_paused">Link to this property</a>

last\_hydrated: string

Last time the integration was hydrated.

formatdate-time

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_create_response%20%3E%20(schema)%20%3E%20(property)%20last_hydrated">Link to this property</a>

name: string

Name of the integration.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

status: string

Integration status.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_create_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

updated: string

When the integration was last updated.

formatdate-time

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_create_response%20%3E%20(schema)%20%3E%20(property)%20updated">Link to this property</a>

use\_cases: array of map\[unknown]

Use cases enabled for the integration.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_create_response%20%3E%20(schema)%20%3E%20(property)%20use_cases">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_create_response%20%3E%20(schema)>)

<details>

<summary>

IntegrationUpdateResponse object {id, application, auth\_method, 11 more }

The requested item.

</summary>

id: string

Integration ID.

formatuuid

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_update_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

application: map\[string]

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_update_response%20%3E%20(schema)%20%3E%20(property)%20application">Link to this property</a>

auth\_method: map\[string]

The integration’s authentication method.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_update_response%20%3E%20(schema)%20%3E%20(property)%20auth_method">Link to this property</a>

<details>

<summary>

authorization\_link: object {components, link }

Authorization link for the integration.

</summary>

components: map\[unknown]

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_update_response%20%3E%20(schema)%20%3E%20(property)%20authorization_link%20%3E%20(property)%20components">Link to this property</a>

link: string

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_update_response%20%3E%20(schema)%20%3E%20(property)%20authorization_link%20%3E%20(property)%20link">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_update_response%20%3E%20(schema)%20%3E%20(property)%20authorization_link">Link to this property</a>

created: string

When the integration was created.

formatdate-time

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_update_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

credentials\_expiry: string

Credentials expiry time.

formatdate-time

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_update_response%20%3E%20(schema)%20%3E%20(property)%20credentials_expiry">Link to this property</a>

dlp\_profiles: array of string

DLP Profiles enabled for the integration.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_update_response%20%3E%20(schema)%20%3E%20(property)%20dlp_profiles">Link to this property</a>

health\_details: array of map\[unknown]

Health details with remediation hints.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_update_response%20%3E%20(schema)%20%3E%20(property)%20health_details">Link to this property</a>

is\_paused: boolean

Whether the user paused the integration.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_update_response%20%3E%20(schema)%20%3E%20(property)%20is_paused">Link to this property</a>

last\_hydrated: string

Last time the integration was hydrated.

formatdate-time

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_update_response%20%3E%20(schema)%20%3E%20(property)%20last_hydrated">Link to this property</a>

name: string

Name of the integration.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_update_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

status: string

Integration status.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_update_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

updated: string

When the integration was last updated.

formatdate-time

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_update_response%20%3E%20(schema)%20%3E%20(property)%20updated">Link to this property</a>

use\_cases: array of map\[unknown]

Use cases enabled for the integration.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_update_response%20%3E%20(schema)%20%3E%20(property)%20use_cases">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_update_response%20%3E%20(schema)>)

<details>

<summary>

IntegrationPauseResponse object {id, application, auth\_method, 11 more }

The requested item.

</summary>

id: string

Integration ID.

formatuuid

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_pause_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

application: map\[string]

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_pause_response%20%3E%20(schema)%20%3E%20(property)%20application">Link to this property</a>

auth\_method: map\[string]

The integration’s authentication method.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_pause_response%20%3E%20(schema)%20%3E%20(property)%20auth_method">Link to this property</a>

<details>

<summary>

authorization\_link: object {components, link }

Authorization link for the integration.

</summary>

components: map\[unknown]

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_pause_response%20%3E%20(schema)%20%3E%20(property)%20authorization_link%20%3E%20(property)%20components">Link to this property</a>

link: string

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_pause_response%20%3E%20(schema)%20%3E%20(property)%20authorization_link%20%3E%20(property)%20link">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_pause_response%20%3E%20(schema)%20%3E%20(property)%20authorization_link">Link to this property</a>

created: string

When the integration was created.

formatdate-time

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_pause_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

credentials\_expiry: string

Credentials expiry time.

formatdate-time

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_pause_response%20%3E%20(schema)%20%3E%20(property)%20credentials_expiry">Link to this property</a>

dlp\_profiles: array of string

DLP Profiles enabled for the integration.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_pause_response%20%3E%20(schema)%20%3E%20(property)%20dlp_profiles">Link to this property</a>

health\_details: array of map\[unknown]

Health details with remediation hints.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_pause_response%20%3E%20(schema)%20%3E%20(property)%20health_details">Link to this property</a>

is\_paused: boolean

Whether the user paused the integration.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_pause_response%20%3E%20(schema)%20%3E%20(property)%20is_paused">Link to this property</a>

last\_hydrated: string

Last time the integration was hydrated.

formatdate-time

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_pause_response%20%3E%20(schema)%20%3E%20(property)%20last_hydrated">Link to this property</a>

name: string

Name of the integration.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_pause_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

status: string

Integration status.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_pause_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

updated: string

When the integration was last updated.

formatdate-time

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_pause_response%20%3E%20(schema)%20%3E%20(property)%20updated">Link to this property</a>

use\_cases: array of map\[unknown]

Use cases enabled for the integration.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_pause_response%20%3E%20(schema)%20%3E%20(property)%20use_cases">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_pause_response%20%3E%20(schema)>)

<details>

<summary>

IntegrationResumeResponse object {id, application, auth\_method, 11 more }

The requested item.

</summary>

id: string

Integration ID.

formatuuid

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_resume_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

application: map\[string]

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_resume_response%20%3E%20(schema)%20%3E%20(property)%20application">Link to this property</a>

auth\_method: map\[string]

The integration’s authentication method.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_resume_response%20%3E%20(schema)%20%3E%20(property)%20auth_method">Link to this property</a>

<details>

<summary>

authorization\_link: object {components, link }

Authorization link for the integration.

</summary>

components: map\[unknown]

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_resume_response%20%3E%20(schema)%20%3E%20(property)%20authorization_link%20%3E%20(property)%20components">Link to this property</a>

link: string

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_resume_response%20%3E%20(schema)%20%3E%20(property)%20authorization_link%20%3E%20(property)%20link">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_resume_response%20%3E%20(schema)%20%3E%20(property)%20authorization_link">Link to this property</a>

created: string

When the integration was created.

formatdate-time

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_resume_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

credentials\_expiry: string

Credentials expiry time.

formatdate-time

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_resume_response%20%3E%20(schema)%20%3E%20(property)%20credentials_expiry">Link to this property</a>

dlp\_profiles: array of string

DLP Profiles enabled for the integration.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_resume_response%20%3E%20(schema)%20%3E%20(property)%20dlp_profiles">Link to this property</a>

health\_details: array of map\[unknown]

Health details with remediation hints.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_resume_response%20%3E%20(schema)%20%3E%20(property)%20health_details">Link to this property</a>

is\_paused: boolean

Whether the user paused the integration.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_resume_response%20%3E%20(schema)%20%3E%20(property)%20is_paused">Link to this property</a>

last\_hydrated: string

Last time the integration was hydrated.

formatdate-time

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_resume_response%20%3E%20(schema)%20%3E%20(property)%20last_hydrated">Link to this property</a>

name: string

Name of the integration.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_resume_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

status: string

Integration status.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_resume_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

updated: string

When the integration was last updated.

formatdate-time

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_resume_response%20%3E%20(schema)%20%3E%20(property)%20updated">Link to this property</a>

use\_cases: array of map\[unknown]

Use cases enabled for the integration.

<a href="#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_resume_response%20%3E%20(schema)%20%3E%20(property)%20use_cases">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.casb.integrations%20%3E%20(model)%20integration_resume_response%20%3E%20(schema)>)