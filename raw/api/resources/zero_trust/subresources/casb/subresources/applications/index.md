---
title: Applications
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[Casb](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Applications

##### [List applications](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/applications/methods/list)

GET/accounts/{account\_id}/one/applications

##### [Get application details](https://developers.cloudflare.com/api/resources/zero_trust/subresources/casb/subresources/applications/methods/get)

GET/accounts/{account\_id}/one/applications/{application\_id}

##### ModelsExpand Collapse

<details>

<summary>

ApplicationListResponse object {id, auth\_methods, category, 7 more }

Application item in list response.

</summary>

<details>

<summary>

id: "ANTHROPIC"or "AWS"or "BITBUCKET"or 12 more

Vendor identifier (e.g. microsoft\_internal, google\_workspace).

- <code>ANTHROPIC</code> - ANTHROPIC
- <code>AWS</code> - AWS
- <code>BITBUCKET</code> - BITBUCKET
- <code>BOX</code> - BOX
- <code>CONFLUENCE</code> - CONFLUENCE
- <code>DROPBOX</code> - DROPBOX
- <code>GITHUB</code> - GITHUB
- <code>GOOGLE_CLOUD_PLATFORM</code> - GOOGLE\_CLOUD\_PLATFORM
- <code>GOOGLE_WORKSPACE</code> - GOOGLE\_WORKSPACE
- <code>JIRA</code> - JIRA
- <code>MICROSOFT_INTERNAL</code> - MICROSOFT\_INTERNAL
- <code>OPENAI</code> - OPENAI
- <code>SALESFORCE</code> - SALESFORCE
- <code>SERVICENOW</code> - SERVICENOW
- <code>SLACK</code> - SLACK

</summary>

One of the following:

"ANTHROPIC"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%200">Link to this property</a>

"AWS"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%201">Link to this property</a>

"BITBUCKET"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%202">Link to this property</a>

"BOX"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%203">Link to this property</a>

"CONFLUENCE"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%204">Link to this property</a>

"DROPBOX"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%205">Link to this property</a>

"GITHUB"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%206">Link to this property</a>

"GOOGLE\_CLOUD\_PLATFORM"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%207">Link to this property</a>

"GOOGLE\_WORKSPACE"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%208">Link to this property</a>

"JIRA"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%209">Link to this property</a>

"MICROSOFT\_INTERNAL"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%2010">Link to this property</a>

"OPENAI"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%2011">Link to this property</a>

"SALESFORCE"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%2012">Link to this property</a>

"SERVICENOW"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%2013">Link to this property</a>

"SLACK"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%2014">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

auth\_methods: array of object {id, display\_name }

Available auth methods.

</summary>

id: string

Auth method identifier.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_methods%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

display\_name: string

Human-readable auth method name.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_methods%20%3E%20(items)%20%3E%20(property)%20display_name">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20auth_methods">Link to this property</a>

category: string

Vendor category (e.g. Productivity, AI).

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20category">Link to this property</a>

description: string

Brief description of the integration.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

display\_name: string

Human-readable vendor name.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20display_name">Link to this property</a>

dlp\_enabled: boolean

Whether DLP scanning is supported.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20dlp_enabled">Link to this property</a>

logo: string

Logo path.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20logo">Link to this property</a>

<details>

<summary>

permissions: array of object {display\_name, scope, severity }

All permissions with severity.

</summary>

display\_name: string

Human-readable permission name.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20permissions%20%3E%20(items)%20%3E%20(property)%20display_name">Link to this property</a>

scope: string

Vendor-native scope identifier.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20permissions%20%3E%20(items)%20%3E%20(property)%20scope">Link to this property</a>

<details>

<summary>

severity: "low"or "medium"or "high"or "critical"

Permission sensitivity level.

- <code>low</code> - low
- <code>medium</code> - medium
- <code>high</code> - high
- <code>critical</code> - critical

</summary>

One of the following:

"low"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20permissions%20%3E%20(items)%20%3E%20(property)%20severity%20%3E%20(member)%200">Link to this property</a>

"medium"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20permissions%20%3E%20(items)%20%3E%20(property)%20severity%20%3E%20(member)%201">Link to this property</a>

"high"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20permissions%20%3E%20(items)%20%3E%20(property)%20severity%20%3E%20(member)%202">Link to this property</a>

"critical"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20permissions%20%3E%20(items)%20%3E%20(property)%20severity%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20permissions%20%3E%20(items)%20%3E%20(property)%20severity">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20permissions">Link to this property</a>

supported\_environments: array of string

Environments this vendor supports (standard, fedramp).

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20supported_environments">Link to this property</a>

<details>

<summary>

use\_cases: array of object {id, display\_name }

Supported use cases.

</summary>

id: string

Use case identifier (e.g. casb, ces).

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

display\_name: string

Human-readable use case name.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20display_name">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)%20%3E%20(property)%20use_cases">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_list_response%20%3E%20(schema)>)

<details>

<summary>

ApplicationGetResponse object {id, auth\_methods, category, 6 more }

The requested item.

</summary>

<details>

<summary>

id: "ANTHROPIC"or "AWS"or "BITBUCKET"or 12 more

Vendor identifier.

- <code>ANTHROPIC</code> - ANTHROPIC
- <code>AWS</code> - AWS
- <code>BITBUCKET</code> - BITBUCKET
- <code>BOX</code> - BOX
- <code>CONFLUENCE</code> - CONFLUENCE
- <code>DROPBOX</code> - DROPBOX
- <code>GITHUB</code> - GITHUB
- <code>GOOGLE_CLOUD_PLATFORM</code> - GOOGLE\_CLOUD\_PLATFORM
- <code>GOOGLE_WORKSPACE</code> - GOOGLE\_WORKSPACE
- <code>JIRA</code> - JIRA
- <code>MICROSOFT_INTERNAL</code> - MICROSOFT\_INTERNAL
- <code>OPENAI</code> - OPENAI
- <code>SALESFORCE</code> - SALESFORCE
- <code>SERVICENOW</code> - SERVICENOW
- <code>SLACK</code> - SLACK

</summary>

One of the following:

"ANTHROPIC"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%200">Link to this property</a>

"AWS"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%201">Link to this property</a>

"BITBUCKET"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%202">Link to this property</a>

"BOX"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%203">Link to this property</a>

"CONFLUENCE"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%204">Link to this property</a>

"DROPBOX"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%205">Link to this property</a>

"GITHUB"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%206">Link to this property</a>

"GOOGLE\_CLOUD\_PLATFORM"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%207">Link to this property</a>

"GOOGLE\_WORKSPACE"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%208">Link to this property</a>

"JIRA"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%209">Link to this property</a>

"MICROSOFT\_INTERNAL"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%2010">Link to this property</a>

"OPENAI"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%2011">Link to this property</a>

"SALESFORCE"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%2012">Link to this property</a>

"SERVICENOW"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%2013">Link to this property</a>

"SLACK"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20id%20%3E%20(member)%2014">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

auth\_methods: array of object {id, display\_name, is\_default, supported\_environments }

Available authentication methods.

</summary>

id: string

Auth method identifier.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20auth_methods%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

display\_name: string

Human-readable auth method name.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20auth_methods%20%3E%20(items)%20%3E%20(property)%20display_name">Link to this property</a>

is\_default: boolean

Whether this is the default auth method.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20auth_methods%20%3E%20(items)%20%3E%20(property)%20is_default">Link to this property</a>

supported\_environments: array of string

Environments this auth method supports.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20auth_methods%20%3E%20(items)%20%3E%20(property)%20supported_environments">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20auth_methods">Link to this property</a>

category: string

Vendor category.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20category">Link to this property</a>

description: string

Brief description.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

display\_name: string

Human-readable vendor name.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20display_name">Link to this property</a>

dlp\_enabled: boolean

Whether DLP scanning is supported.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20dlp_enabled">Link to this property</a>

instructions: string

Setup instructions for the user.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20instructions">Link to this property</a>

logo: string

Logo path.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20logo">Link to this property</a>

<details>

<summary>

use\_cases: array of object {id, base\_scopes, description, 2 more }

Use cases with full scope details.

</summary>

id: string

Use case identifier.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

base\_scopes: array of object {display\_name, scope, severity }

Scopes always required for this use case.

</summary>

display\_name: string

Human-readable permission name.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20base_scopes%20%3E%20(items)%20%3E%20(property)%20display_name">Link to this property</a>

scope: string

Vendor-native scope identifier.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20base_scopes%20%3E%20(items)%20%3E%20(property)%20scope">Link to this property</a>

<details>

<summary>

severity: "low"or "medium"or "high"or "critical"

Permission sensitivity level.

- <code>low</code> - low
- <code>medium</code> - medium
- <code>high</code> - high
- <code>critical</code> - critical

</summary>

One of the following:

"low"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20base_scopes%20%3E%20(items)%20%3E%20(property)%20severity%20%3E%20(member)%200">Link to this property</a>

"medium"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20base_scopes%20%3E%20(items)%20%3E%20(property)%20severity%20%3E%20(member)%201">Link to this property</a>

"high"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20base_scopes%20%3E%20(items)%20%3E%20(property)%20severity%20%3E%20(member)%202">Link to this property</a>

"critical"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20base_scopes%20%3E%20(items)%20%3E%20(property)%20severity%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20base_scopes%20%3E%20(items)%20%3E%20(property)%20severity">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20base_scopes">Link to this property</a>

description: string

Use case description.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

display\_name: string

Human-readable use case name.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20display_name">Link to this property</a>

<details>

<summary>

features: array of object {id, description, display\_name, scopes }

Optional features with extra scopes.

</summary>

id: string

Feature identifier.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20features%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

description: string

Feature description.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20features%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

display\_name: string

Human-readable feature name.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20features%20%3E%20(items)%20%3E%20(property)%20display_name">Link to this property</a>

<details>

<summary>

scopes: array of object {display\_name, scope, severity }

Additional scopes when feature is enabled.

</summary>

display\_name: string

Human-readable permission name.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20features%20%3E%20(items)%20%3E%20(property)%20scopes%20%3E%20(items)%20%3E%20(property)%20display_name">Link to this property</a>

scope: string

Vendor-native scope identifier.

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20features%20%3E%20(items)%20%3E%20(property)%20scopes%20%3E%20(items)%20%3E%20(property)%20scope">Link to this property</a>

<details>

<summary>

severity: "low"or "medium"or "high"or "critical"

Permission sensitivity level.

- <code>low</code> - low
- <code>medium</code> - medium
- <code>high</code> - high
- <code>critical</code> - critical

</summary>

One of the following:

"low"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20features%20%3E%20(items)%20%3E%20(property)%20scopes%20%3E%20(items)%20%3E%20(property)%20severity%20%3E%20(member)%200">Link to this property</a>

"medium"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20features%20%3E%20(items)%20%3E%20(property)%20scopes%20%3E%20(items)%20%3E%20(property)%20severity%20%3E%20(member)%201">Link to this property</a>

"high"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20features%20%3E%20(items)%20%3E%20(property)%20scopes%20%3E%20(items)%20%3E%20(property)%20severity%20%3E%20(member)%202">Link to this property</a>

"critical"

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20features%20%3E%20(items)%20%3E%20(property)%20scopes%20%3E%20(items)%20%3E%20(property)%20severity%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20features%20%3E%20(items)%20%3E%20(property)%20scopes%20%3E%20(items)%20%3E%20(property)%20severity">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20features%20%3E%20(items)%20%3E%20(property)%20scopes">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases%20%3E%20(items)%20%3E%20(property)%20features">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)%20%3E%20(property)%20use_cases">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.casb.applications%20%3E%20(model)%20application_get_response%20%3E%20(schema)>)

#### ApplicationsAuth Methods

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