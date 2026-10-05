---
title: Servers
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[Access](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access)

[AI Controls](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/ai_controls)

[Mcp](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/ai_controls/subresources/mcp)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Servers

##### [List MCP Servers](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/ai_controls/subresources/mcp/subresources/servers/methods/list)

GET/accounts/{account\_id}/access/ai-controls/mcp/servers

##### [Create a new MCP Server](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/ai_controls/subresources/mcp/subresources/servers/methods/create)

POST/accounts/{account\_id}/access/ai-controls/mcp/servers

##### [Read the details of an MCP Server](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/ai_controls/subresources/mcp/subresources/servers/methods/read)

GET/accounts/{account\_id}/access/ai-controls/mcp/servers/{id}

##### [Update an MCP Server](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/ai_controls/subresources/mcp/subresources/servers/methods/update)

PUT/accounts/{account\_id}/access/ai-controls/mcp/servers/{id}

##### [Delete an MCP Server](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/ai_controls/subresources/mcp/subresources/servers/methods/delete)

DELETE/accounts/{account\_id}/access/ai-controls/mcp/servers/{id}

##### [Sync MCP Server Capabilities](https://developers.cloudflare.com/api/resources/zero_trust/subresources/access/subresources/ai_controls/subresources/mcp/subresources/servers/methods/sync)

POST/accounts/{account\_id}/access/ai-controls/mcp/servers/{id}/sync

##### ModelsExpand Collapse

<details>

<summary>

ServerListResponse object {id, auth\_type, hostname, 19 more }

</summary>

id: string

Unique identifier for the MCP server.

maxLength32

minLength1

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

auth\_type: "oauth"or "bearer"or "unauthenticated"

Authentication method used to connect to the upstream MCP server.

</summary>

One of the following:

"oauth"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_type%20%3E%20(member)%200">Link to this property</a>

"bearer"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_type%20%3E%20(member)%201">Link to this property</a>

"unauthenticated"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_type%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_type">Link to this property</a>

hostname: string

URL of the upstream MCP endpoint.

formaturi

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20hostname">Link to this property</a>

name: string

Display name for the MCP server.

maxLength350

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

prompts: array of map\[unknown]

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20prompts">Link to this property</a>

tools: array of map\[unknown]

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20tools">Link to this property</a>

<details>

<summary>

auth\_config\_summary: optional object {auth\_mode, client\_secret\_version, config, 2 more }

Safe subset of auth\_credentials surfaced to the dashboard. Includes auth\_mode (dcr|manual), has\_client\_secret, client\_secret\_version, and the OAuth endpoints + client\_id for manual servers. Never includes the secret value.

</summary>

<details>

<summary>

auth\_mode: optional "dcr"or "manual"

</summary>

One of the following:

"dcr"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20auth_mode%20%3E%20(member)%200">Link to this property</a>

"manual"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20auth_mode%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20auth_mode">Link to this property</a>

client\_secret\_version: optional number

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20client_secret_version">Link to this property</a>

<details>

<summary>

config: optional object {authorization\_endpoint, issuer, resource, 2 more }

</summary>

authorization\_endpoint: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20authorization_endpoint">Link to this property</a>

issuer: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20issuer">Link to this property</a>

resource: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20resource">Link to this property</a>

revocation\_endpoint: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20revocation_endpoint">Link to this property</a>

token\_endpoint: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20token_endpoint">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config">Link to this property</a>

has\_client\_secret: optional boolean

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20has_client_secret">Link to this property</a>

<details>

<summary>

registration\_info: optional object {client\_id, redirect\_uris, scope, token\_endpoint\_auth\_method }

</summary>

client\_id: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info%20%3E%20(property)%20client_id">Link to this property</a>

redirect\_uris: optional array of string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info%20%3E%20(property)%20redirect_uris">Link to this property</a>

scope: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info%20%3E%20(property)%20scope">Link to this property</a>

token\_endpoint\_auth\_method: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info%20%3E%20(property)%20token_endpoint_auth_method">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary">Link to this property</a>

<details>

<summary>

authentication\_status: optional "not\_required"or "required"or "connected"or 2 more

Whether administrative authentication is required before capabilities can be synced. Manual OAuth is user-managed and has no administrative authentication flow.

</summary>

One of the following:

"not\_required"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%200">Link to this property</a>

"required"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%201">Link to this property</a>

"connected"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%202">Link to this property</a>

"stale"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%203">Link to this property</a>

"manual"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status">Link to this property</a>

created\_at: optional string

formatdate-time

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

created\_by: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20created_by">Link to this property</a>

description: optional string

Optional description of the MCP server.

maxLength512

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

error: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20error">Link to this property</a>

<details>

<summary>

error\_details: optional object {cause, is\_upstream, mcp\_code, 2 more }

</summary>

cause: optional string

Underlying error message

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20cause">Link to this property</a>

is\_upstream: optional boolean

True = MCP server returned an error. False = couldn’t reach the server

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20is_upstream">Link to this property</a>

mcp\_code: optional number

MCP protocol error code

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20mcp_code">Link to this property</a>

retryable: optional boolean

Whether the error is transient and worth retrying

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20retryable">Link to this property</a>

status\_code: optional number

HTTP status code from the server

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20status_code">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20error_details">Link to this property</a>

is\_shared\_oauth\_callback\_enabled: optional boolean

When true, the gateway worker uses the shared Cloudflare-owned OAuth callback endpoint as the redirect\_uri for upstream on-behalf OAuth, instead of the customer portal hostname. Defaults to false (off); opt in per server by setting true.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20is_shared_oauth_callback_enabled">Link to this property</a>

last\_successful\_sync: optional string

formatdate-time

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20last_successful_sync">Link to this property</a>

last\_synced: optional string

formatdate-time

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20last_synced">Link to this property</a>

modified\_at: optional string

formatdate-time

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

modified\_by: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20modified_by">Link to this property</a>

secure\_web\_gateway: optional boolean

Route outbound traffic to this MCP server through Zero Trust Secure Web Gateway.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20secure_web_gateway">Link to this property</a>

<details>

<summary>

status: optional "waiting"or "ready"or "stale"or "error"

Current sync state of the server

</summary>

One of the following:

"waiting"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"ready"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"stale"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"error"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

updated\_prompts: optional array of object {name, alias, description, enabled }

Server-wide prompt capability overrides.

</summary>

name: string

Name of the tool or prompt capability to override.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

alias: optional string

Custom name exposed for the capability.

maxLength40

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts%20%3E%20(items)%20%3E%20(property)%20alias">Link to this property</a>

description: optional string

Custom description exposed for the capability.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the capability is available through the MCP server.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts%20%3E%20(items)%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts">Link to this property</a>

<details>

<summary>

updated\_tools: optional array of object {name, alias, description, enabled }

Server-wide tool capability overrides.

</summary>

name: string

Name of the tool or prompt capability to override.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

alias: optional string

Custom name exposed for the capability.

maxLength40

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools%20%3E%20(items)%20%3E%20(property)%20alias">Link to this property</a>

description: optional string

Custom description exposed for the capability.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the capability is available through the MCP server.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools%20%3E%20(items)%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_list_response%20%3E%20(schema)>)

<details>

<summary>

ServerCreateResponse object {id, auth\_type, hostname, 19 more }

</summary>

id: string

Unique identifier for the MCP server.

maxLength32

minLength1

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

auth\_type: "oauth"or "bearer"or "unauthenticated"

Authentication method used to connect to the upstream MCP server.

</summary>

One of the following:

"oauth"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20auth_type%20%3E%20(member)%200">Link to this property</a>

"bearer"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20auth_type%20%3E%20(member)%201">Link to this property</a>

"unauthenticated"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20auth_type%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20auth_type">Link to this property</a>

hostname: string

URL of the upstream MCP endpoint.

formaturi

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20hostname">Link to this property</a>

name: string

Display name for the MCP server.

maxLength350

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

prompts: array of map\[unknown]

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20prompts">Link to this property</a>

tools: array of map\[unknown]

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20tools">Link to this property</a>

<details>

<summary>

auth\_config\_summary: optional object {auth\_mode, client\_secret\_version, config, 2 more }

Safe subset of auth\_credentials surfaced to the dashboard. Includes auth\_mode (dcr|manual), has\_client\_secret, client\_secret\_version, and the OAuth endpoints + client\_id for manual servers. Never includes the secret value.

</summary>

<details>

<summary>

auth\_mode: optional "dcr"or "manual"

</summary>

One of the following:

"dcr"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20auth_mode%20%3E%20(member)%200">Link to this property</a>

"manual"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20auth_mode%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20auth_mode">Link to this property</a>

client\_secret\_version: optional number

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20client_secret_version">Link to this property</a>

<details>

<summary>

config: optional object {authorization\_endpoint, issuer, resource, 2 more }

</summary>

authorization\_endpoint: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20authorization_endpoint">Link to this property</a>

issuer: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20issuer">Link to this property</a>

resource: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20resource">Link to this property</a>

revocation\_endpoint: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20revocation_endpoint">Link to this property</a>

token\_endpoint: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20token_endpoint">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config">Link to this property</a>

has\_client\_secret: optional boolean

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20has_client_secret">Link to this property</a>

<details>

<summary>

registration\_info: optional object {client\_id, redirect\_uris, scope, token\_endpoint\_auth\_method }

</summary>

client\_id: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info%20%3E%20(property)%20client_id">Link to this property</a>

redirect\_uris: optional array of string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info%20%3E%20(property)%20redirect_uris">Link to this property</a>

scope: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info%20%3E%20(property)%20scope">Link to this property</a>

token\_endpoint\_auth\_method: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info%20%3E%20(property)%20token_endpoint_auth_method">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary">Link to this property</a>

<details>

<summary>

authentication\_status: optional "not\_required"or "required"or "connected"or 2 more

Whether administrative authentication is required before capabilities can be synced. Manual OAuth is user-managed and has no administrative authentication flow.

</summary>

One of the following:

"not\_required"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%200">Link to this property</a>

"required"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%201">Link to this property</a>

"connected"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%202">Link to this property</a>

"stale"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%203">Link to this property</a>

"manual"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status">Link to this property</a>

created\_at: optional string

formatdate-time

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

created\_by: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20created_by">Link to this property</a>

description: optional string

Optional description of the MCP server.

maxLength512

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

error: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20error">Link to this property</a>

<details>

<summary>

error\_details: optional object {cause, is\_upstream, mcp\_code, 2 more }

</summary>

cause: optional string

Underlying error message

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20cause">Link to this property</a>

is\_upstream: optional boolean

True = MCP server returned an error. False = couldn’t reach the server

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20is_upstream">Link to this property</a>

mcp\_code: optional number

MCP protocol error code

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20mcp_code">Link to this property</a>

retryable: optional boolean

Whether the error is transient and worth retrying

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20retryable">Link to this property</a>

status\_code: optional number

HTTP status code from the server

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20status_code">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20error_details">Link to this property</a>

is\_shared\_oauth\_callback\_enabled: optional boolean

When true, the gateway worker uses the shared Cloudflare-owned OAuth callback endpoint as the redirect\_uri for upstream on-behalf OAuth, instead of the customer portal hostname. Defaults to false (off); opt in per server by setting true.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20is_shared_oauth_callback_enabled">Link to this property</a>

last\_successful\_sync: optional string

formatdate-time

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20last_successful_sync">Link to this property</a>

last\_synced: optional string

formatdate-time

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20last_synced">Link to this property</a>

modified\_at: optional string

formatdate-time

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

modified\_by: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20modified_by">Link to this property</a>

secure\_web\_gateway: optional boolean

Route outbound traffic to this MCP server through Zero Trust Secure Web Gateway.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20secure_web_gateway">Link to this property</a>

<details>

<summary>

status: optional "waiting"or "ready"or "stale"or "error"

Current sync state of the server

</summary>

One of the following:

"waiting"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"ready"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"stale"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"error"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

updated\_prompts: optional array of object {name, alias, description, enabled }

Server-wide prompt capability overrides.

</summary>

name: string

Name of the tool or prompt capability to override.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

alias: optional string

Custom name exposed for the capability.

maxLength40

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts%20%3E%20(items)%20%3E%20(property)%20alias">Link to this property</a>

description: optional string

Custom description exposed for the capability.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the capability is available through the MCP server.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts%20%3E%20(items)%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts">Link to this property</a>

<details>

<summary>

updated\_tools: optional array of object {name, alias, description, enabled }

Server-wide tool capability overrides.

</summary>

name: string

Name of the tool or prompt capability to override.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

alias: optional string

Custom name exposed for the capability.

maxLength40

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools%20%3E%20(items)%20%3E%20(property)%20alias">Link to this property</a>

description: optional string

Custom description exposed for the capability.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the capability is available through the MCP server.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools%20%3E%20(items)%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_create_response%20%3E%20(schema)>)

<details>

<summary>

ServerReadResponse object {id, auth\_type, hostname, 19 more }

</summary>

id: string

Unique identifier for the MCP server.

maxLength32

minLength1

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

auth\_type: "oauth"or "bearer"or "unauthenticated"

Authentication method used to connect to the upstream MCP server.

</summary>

One of the following:

"oauth"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20auth_type%20%3E%20(member)%200">Link to this property</a>

"bearer"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20auth_type%20%3E%20(member)%201">Link to this property</a>

"unauthenticated"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20auth_type%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20auth_type">Link to this property</a>

hostname: string

URL of the upstream MCP endpoint.

formaturi

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20hostname">Link to this property</a>

name: string

Display name for the MCP server.

maxLength350

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

prompts: array of map\[unknown]

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20prompts">Link to this property</a>

tools: array of map\[unknown]

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20tools">Link to this property</a>

<details>

<summary>

auth\_config\_summary: optional object {auth\_mode, client\_secret\_version, config, 2 more }

Safe subset of auth\_credentials surfaced to the dashboard. Includes auth\_mode (dcr|manual), has\_client\_secret, client\_secret\_version, and the OAuth endpoints + client\_id for manual servers. Never includes the secret value.

</summary>

<details>

<summary>

auth\_mode: optional "dcr"or "manual"

</summary>

One of the following:

"dcr"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20auth_mode%20%3E%20(member)%200">Link to this property</a>

"manual"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20auth_mode%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20auth_mode">Link to this property</a>

client\_secret\_version: optional number

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20client_secret_version">Link to this property</a>

<details>

<summary>

config: optional object {authorization\_endpoint, issuer, resource, 2 more }

</summary>

authorization\_endpoint: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20authorization_endpoint">Link to this property</a>

issuer: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20issuer">Link to this property</a>

resource: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20resource">Link to this property</a>

revocation\_endpoint: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20revocation_endpoint">Link to this property</a>

token\_endpoint: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20token_endpoint">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config">Link to this property</a>

has\_client\_secret: optional boolean

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20has_client_secret">Link to this property</a>

<details>

<summary>

registration\_info: optional object {client\_id, redirect\_uris, scope, token\_endpoint\_auth\_method }

</summary>

client\_id: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info%20%3E%20(property)%20client_id">Link to this property</a>

redirect\_uris: optional array of string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info%20%3E%20(property)%20redirect_uris">Link to this property</a>

scope: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info%20%3E%20(property)%20scope">Link to this property</a>

token\_endpoint\_auth\_method: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info%20%3E%20(property)%20token_endpoint_auth_method">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary">Link to this property</a>

<details>

<summary>

authentication\_status: optional "not\_required"or "required"or "connected"or 2 more

Whether administrative authentication is required before capabilities can be synced. Manual OAuth is user-managed and has no administrative authentication flow.

</summary>

One of the following:

"not\_required"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%200">Link to this property</a>

"required"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%201">Link to this property</a>

"connected"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%202">Link to this property</a>

"stale"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%203">Link to this property</a>

"manual"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status">Link to this property</a>

created\_at: optional string

formatdate-time

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

created\_by: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20created_by">Link to this property</a>

description: optional string

Optional description of the MCP server.

maxLength512

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

error: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20error">Link to this property</a>

<details>

<summary>

error\_details: optional object {cause, is\_upstream, mcp\_code, 2 more }

</summary>

cause: optional string

Underlying error message

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20cause">Link to this property</a>

is\_upstream: optional boolean

True = MCP server returned an error. False = couldn’t reach the server

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20is_upstream">Link to this property</a>

mcp\_code: optional number

MCP protocol error code

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20mcp_code">Link to this property</a>

retryable: optional boolean

Whether the error is transient and worth retrying

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20retryable">Link to this property</a>

status\_code: optional number

HTTP status code from the server

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20status_code">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20error_details">Link to this property</a>

is\_shared\_oauth\_callback\_enabled: optional boolean

When true, the gateway worker uses the shared Cloudflare-owned OAuth callback endpoint as the redirect\_uri for upstream on-behalf OAuth, instead of the customer portal hostname. Defaults to false (off); opt in per server by setting true.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20is_shared_oauth_callback_enabled">Link to this property</a>

last\_successful\_sync: optional string

formatdate-time

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20last_successful_sync">Link to this property</a>

last\_synced: optional string

formatdate-time

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20last_synced">Link to this property</a>

modified\_at: optional string

formatdate-time

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

modified\_by: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20modified_by">Link to this property</a>

secure\_web\_gateway: optional boolean

Route outbound traffic to this MCP server through Zero Trust Secure Web Gateway.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20secure_web_gateway">Link to this property</a>

<details>

<summary>

status: optional "waiting"or "ready"or "stale"or "error"

Current sync state of the server

</summary>

One of the following:

"waiting"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"ready"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"stale"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"error"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

updated\_prompts: optional array of object {name, alias, description, enabled }

Server-wide prompt capability overrides.

</summary>

name: string

Name of the tool or prompt capability to override.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

alias: optional string

Custom name exposed for the capability.

maxLength40

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts%20%3E%20(items)%20%3E%20(property)%20alias">Link to this property</a>

description: optional string

Custom description exposed for the capability.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the capability is available through the MCP server.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts%20%3E%20(items)%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts">Link to this property</a>

<details>

<summary>

updated\_tools: optional array of object {name, alias, description, enabled }

Server-wide tool capability overrides.

</summary>

name: string

Name of the tool or prompt capability to override.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

alias: optional string

Custom name exposed for the capability.

maxLength40

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools%20%3E%20(items)%20%3E%20(property)%20alias">Link to this property</a>

description: optional string

Custom description exposed for the capability.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the capability is available through the MCP server.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools%20%3E%20(items)%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_read_response%20%3E%20(schema)>)

<details>

<summary>

ServerUpdateResponse object {id, auth\_type, hostname, 19 more }

</summary>

id: string

Unique identifier for the MCP server.

maxLength32

minLength1

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

auth\_type: "oauth"or "bearer"or "unauthenticated"

Authentication method used to connect to the upstream MCP server.

</summary>

One of the following:

"oauth"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20auth_type%20%3E%20(member)%200">Link to this property</a>

"bearer"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20auth_type%20%3E%20(member)%201">Link to this property</a>

"unauthenticated"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20auth_type%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20auth_type">Link to this property</a>

hostname: string

URL of the upstream MCP endpoint.

formaturi

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20hostname">Link to this property</a>

name: string

Display name for the MCP server.

maxLength350

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

prompts: array of map\[unknown]

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20prompts">Link to this property</a>

tools: array of map\[unknown]

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20tools">Link to this property</a>

<details>

<summary>

auth\_config\_summary: optional object {auth\_mode, client\_secret\_version, config, 2 more }

Safe subset of auth\_credentials surfaced to the dashboard. Includes auth\_mode (dcr|manual), has\_client\_secret, client\_secret\_version, and the OAuth endpoints + client\_id for manual servers. Never includes the secret value.

</summary>

<details>

<summary>

auth\_mode: optional "dcr"or "manual"

</summary>

One of the following:

"dcr"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20auth_mode%20%3E%20(member)%200">Link to this property</a>

"manual"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20auth_mode%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20auth_mode">Link to this property</a>

client\_secret\_version: optional number

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20client_secret_version">Link to this property</a>

<details>

<summary>

config: optional object {authorization\_endpoint, issuer, resource, 2 more }

</summary>

authorization\_endpoint: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20authorization_endpoint">Link to this property</a>

issuer: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20issuer">Link to this property</a>

resource: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20resource">Link to this property</a>

revocation\_endpoint: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20revocation_endpoint">Link to this property</a>

token\_endpoint: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20token_endpoint">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config">Link to this property</a>

has\_client\_secret: optional boolean

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20has_client_secret">Link to this property</a>

<details>

<summary>

registration\_info: optional object {client\_id, redirect\_uris, scope, token\_endpoint\_auth\_method }

</summary>

client\_id: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info%20%3E%20(property)%20client_id">Link to this property</a>

redirect\_uris: optional array of string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info%20%3E%20(property)%20redirect_uris">Link to this property</a>

scope: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info%20%3E%20(property)%20scope">Link to this property</a>

token\_endpoint\_auth\_method: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info%20%3E%20(property)%20token_endpoint_auth_method">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary">Link to this property</a>

<details>

<summary>

authentication\_status: optional "not\_required"or "required"or "connected"or 2 more

Whether administrative authentication is required before capabilities can be synced. Manual OAuth is user-managed and has no administrative authentication flow.

</summary>

One of the following:

"not\_required"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%200">Link to this property</a>

"required"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%201">Link to this property</a>

"connected"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%202">Link to this property</a>

"stale"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%203">Link to this property</a>

"manual"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status">Link to this property</a>

created\_at: optional string

formatdate-time

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

created\_by: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20created_by">Link to this property</a>

description: optional string

Optional description of the MCP server.

maxLength512

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

error: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20error">Link to this property</a>

<details>

<summary>

error\_details: optional object {cause, is\_upstream, mcp\_code, 2 more }

</summary>

cause: optional string

Underlying error message

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20cause">Link to this property</a>

is\_upstream: optional boolean

True = MCP server returned an error. False = couldn’t reach the server

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20is_upstream">Link to this property</a>

mcp\_code: optional number

MCP protocol error code

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20mcp_code">Link to this property</a>

retryable: optional boolean

Whether the error is transient and worth retrying

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20retryable">Link to this property</a>

status\_code: optional number

HTTP status code from the server

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20status_code">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20error_details">Link to this property</a>

is\_shared\_oauth\_callback\_enabled: optional boolean

When true, the gateway worker uses the shared Cloudflare-owned OAuth callback endpoint as the redirect\_uri for upstream on-behalf OAuth, instead of the customer portal hostname. Defaults to false (off); opt in per server by setting true.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20is_shared_oauth_callback_enabled">Link to this property</a>

last\_successful\_sync: optional string

formatdate-time

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20last_successful_sync">Link to this property</a>

last\_synced: optional string

formatdate-time

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20last_synced">Link to this property</a>

modified\_at: optional string

formatdate-time

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

modified\_by: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20modified_by">Link to this property</a>

secure\_web\_gateway: optional boolean

Route outbound traffic to this MCP server through Zero Trust Secure Web Gateway.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20secure_web_gateway">Link to this property</a>

<details>

<summary>

status: optional "waiting"or "ready"or "stale"or "error"

Current sync state of the server

</summary>

One of the following:

"waiting"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"ready"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"stale"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"error"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

updated\_prompts: optional array of object {name, alias, description, enabled }

Server-wide prompt capability overrides.

</summary>

name: string

Name of the tool or prompt capability to override.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

alias: optional string

Custom name exposed for the capability.

maxLength40

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts%20%3E%20(items)%20%3E%20(property)%20alias">Link to this property</a>

description: optional string

Custom description exposed for the capability.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the capability is available through the MCP server.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts%20%3E%20(items)%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts">Link to this property</a>

<details>

<summary>

updated\_tools: optional array of object {name, alias, description, enabled }

Server-wide tool capability overrides.

</summary>

name: string

Name of the tool or prompt capability to override.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

alias: optional string

Custom name exposed for the capability.

maxLength40

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools%20%3E%20(items)%20%3E%20(property)%20alias">Link to this property</a>

description: optional string

Custom description exposed for the capability.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the capability is available through the MCP server.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools%20%3E%20(items)%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_update_response%20%3E%20(schema)>)

<details>

<summary>

ServerDeleteResponse object {id, auth\_type, hostname, 19 more }

</summary>

id: string

Unique identifier for the MCP server.

maxLength32

minLength1

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

auth\_type: "oauth"or "bearer"or "unauthenticated"

Authentication method used to connect to the upstream MCP server.

</summary>

One of the following:

"oauth"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20auth_type%20%3E%20(member)%200">Link to this property</a>

"bearer"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20auth_type%20%3E%20(member)%201">Link to this property</a>

"unauthenticated"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20auth_type%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20auth_type">Link to this property</a>

hostname: string

URL of the upstream MCP endpoint.

formaturi

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20hostname">Link to this property</a>

name: string

Display name for the MCP server.

maxLength350

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

prompts: array of map\[unknown]

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20prompts">Link to this property</a>

tools: array of map\[unknown]

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20tools">Link to this property</a>

<details>

<summary>

auth\_config\_summary: optional object {auth\_mode, client\_secret\_version, config, 2 more }

Safe subset of auth\_credentials surfaced to the dashboard. Includes auth\_mode (dcr|manual), has\_client\_secret, client\_secret\_version, and the OAuth endpoints + client\_id for manual servers. Never includes the secret value.

</summary>

<details>

<summary>

auth\_mode: optional "dcr"or "manual"

</summary>

One of the following:

"dcr"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20auth_mode%20%3E%20(member)%200">Link to this property</a>

"manual"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20auth_mode%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20auth_mode">Link to this property</a>

client\_secret\_version: optional number

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20client_secret_version">Link to this property</a>

<details>

<summary>

config: optional object {authorization\_endpoint, issuer, resource, 2 more }

</summary>

authorization\_endpoint: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20authorization_endpoint">Link to this property</a>

issuer: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20issuer">Link to this property</a>

resource: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20resource">Link to this property</a>

revocation\_endpoint: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20revocation_endpoint">Link to this property</a>

token\_endpoint: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config%20%3E%20(property)%20token_endpoint">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20config">Link to this property</a>

has\_client\_secret: optional boolean

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20has_client_secret">Link to this property</a>

<details>

<summary>

registration\_info: optional object {client\_id, redirect\_uris, scope, token\_endpoint\_auth\_method }

</summary>

client\_id: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info%20%3E%20(property)%20client_id">Link to this property</a>

redirect\_uris: optional array of string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info%20%3E%20(property)%20redirect_uris">Link to this property</a>

scope: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info%20%3E%20(property)%20scope">Link to this property</a>

token\_endpoint\_auth\_method: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info%20%3E%20(property)%20token_endpoint_auth_method">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary%20%3E%20(property)%20registration_info">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20auth_config_summary">Link to this property</a>

<details>

<summary>

authentication\_status: optional "not\_required"or "required"or "connected"or 2 more

Whether administrative authentication is required before capabilities can be synced. Manual OAuth is user-managed and has no administrative authentication flow.

</summary>

One of the following:

"not\_required"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%200">Link to this property</a>

"required"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%201">Link to this property</a>

"connected"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%202">Link to this property</a>

"stale"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%203">Link to this property</a>

"manual"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20authentication_status">Link to this property</a>

created\_at: optional string

formatdate-time

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

created\_by: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20created_by">Link to this property</a>

description: optional string

Optional description of the MCP server.

maxLength512

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

error: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20error">Link to this property</a>

<details>

<summary>

error\_details: optional object {cause, is\_upstream, mcp\_code, 2 more }

</summary>

cause: optional string

Underlying error message

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20cause">Link to this property</a>

is\_upstream: optional boolean

True = MCP server returned an error. False = couldn’t reach the server

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20is_upstream">Link to this property</a>

mcp\_code: optional number

MCP protocol error code

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20mcp_code">Link to this property</a>

retryable: optional boolean

Whether the error is transient and worth retrying

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20retryable">Link to this property</a>

status\_code: optional number

HTTP status code from the server

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20status_code">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20error_details">Link to this property</a>

is\_shared\_oauth\_callback\_enabled: optional boolean

When true, the gateway worker uses the shared Cloudflare-owned OAuth callback endpoint as the redirect\_uri for upstream on-behalf OAuth, instead of the customer portal hostname. Defaults to false (off); opt in per server by setting true.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20is_shared_oauth_callback_enabled">Link to this property</a>

last\_successful\_sync: optional string

formatdate-time

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20last_successful_sync">Link to this property</a>

last\_synced: optional string

formatdate-time

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20last_synced">Link to this property</a>

modified\_at: optional string

formatdate-time

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

modified\_by: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20modified_by">Link to this property</a>

secure\_web\_gateway: optional boolean

Route outbound traffic to this MCP server through Zero Trust Secure Web Gateway.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20secure_web_gateway">Link to this property</a>

<details>

<summary>

status: optional "waiting"or "ready"or "stale"or "error"

Current sync state of the server

</summary>

One of the following:

"waiting"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"ready"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"stale"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"error"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

updated\_prompts: optional array of object {name, alias, description, enabled }

Server-wide prompt capability overrides.

</summary>

name: string

Name of the tool or prompt capability to override.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

alias: optional string

Custom name exposed for the capability.

maxLength40

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts%20%3E%20(items)%20%3E%20(property)%20alias">Link to this property</a>

description: optional string

Custom description exposed for the capability.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the capability is available through the MCP server.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts%20%3E%20(items)%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20updated_prompts">Link to this property</a>

<details>

<summary>

updated\_tools: optional array of object {name, alias, description, enabled }

Server-wide tool capability overrides.

</summary>

name: string

Name of the tool or prompt capability to override.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

alias: optional string

Custom name exposed for the capability.

maxLength40

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools%20%3E%20(items)%20%3E%20(property)%20alias">Link to this property</a>

description: optional string

Custom description exposed for the capability.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

enabled: optional boolean

Whether the capability is available through the MCP server.

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools%20%3E%20(items)%20%3E%20(property)%20enabled">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)%20%3E%20(property)%20updated_tools">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_delete_response%20%3E%20(schema)>)

<details>

<summary>

ServerSyncResponse object {error, error\_details, status }

</summary>

error: optional string

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_sync_response%20%3E%20(schema)%20%3E%20(property)%20error">Link to this property</a>

<details>

<summary>

error\_details: optional object {cause, is\_upstream, mcp\_code, 2 more }

</summary>

cause: optional string

Underlying error message

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_sync_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20cause">Link to this property</a>

is\_upstream: optional boolean

True = MCP server returned an error. False = couldn’t reach the server

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_sync_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20is_upstream">Link to this property</a>

mcp\_code: optional number

MCP protocol error code

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_sync_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20mcp_code">Link to this property</a>

retryable: optional boolean

Whether the error is transient and worth retrying

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_sync_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20retryable">Link to this property</a>

status\_code: optional number

HTTP status code from the server

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_sync_response%20%3E%20(schema)%20%3E%20(property)%20error_details%20%3E%20(property)%20status_code">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_sync_response%20%3E%20(schema)%20%3E%20(property)%20error_details">Link to this property</a>

<details>

<summary>

status: optional "waiting"or "ready"or "stale"or "error"

</summary>

One of the following:

"waiting"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_sync_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"ready"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_sync_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"stale"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_sync_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"error"

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_sync_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_sync_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.access.ai_controls.mcp.servers%20%3E%20(model)%20server_sync_response%20%3E%20(schema)>)