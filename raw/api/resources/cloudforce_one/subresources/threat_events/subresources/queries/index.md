---
title: Queries
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Cloudforce One](https://developers.cloudflare.com/api/resources/cloudforce_one)

[Threat Events](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Queries

##### [List all saved event queries](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/queries/methods/list)

GET/accounts/{account\_id}/cloudforce-one/events/queries

##### [Create a saved event query](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/queries/methods/create)

POST/accounts/{account\_id}/cloudforce-one/events/queries/create

##### [Read a saved event query](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/queries/methods/get)

GET/accounts/{account\_id}/cloudforce-one/events/queries/{query\_id}

##### [Update a saved event query](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/queries/methods/edit)

PATCH/accounts/{account\_id}/cloudforce-one/events/queries/{query\_id}

##### [Delete a saved event query](https://developers.cloudflare.com/api/resources/cloudforce_one/subresources/threat_events/subresources/queries/methods/delete)

DELETE/accounts/{account\_id}/cloudforce-one/events/queries/{query\_id}

##### ModelsExpand Collapse

<details>

<summary>

QueryListResponse = array of object {id, account\_id, alert\_enabled, 10 more }

</summary>

id: number

Unique identifier for the saved query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

account\_id: number

Account ID

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20account_id">Link to this property</a>

alert\_enabled: boolean

Whether alerts are enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20alert_enabled">Link to this property</a>

alert\_rollup\_enabled: boolean

Whether alert rollup is enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20alert_rollup_enabled">Link to this property</a>

created\_at: string

Creation timestamp

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

name: string

Name of the saved query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

query\_json: string

JSON string containing the query parameters

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20query_json">Link to this property</a>

rule\_enabled: boolean

Whether rule is enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20rule_enabled">Link to this property</a>

updated\_at: string

Last update timestamp

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20updated_at">Link to this property</a>

user\_email: string

Email of the user who created the query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20user_email">Link to this property</a>

custom\_threat\_feed\_id: optional number

Intel Indicator Feed ID (numeric)

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20custom_threat_feed_id">Link to this property</a>

rule\_list\_id: optional string

WAF rules list ID for blocking

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20rule_list_id">Link to this property</a>

rule\_scope: optional string

Scope for the rule

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20rule_scope">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_list_response%20%3E%20(schema)>)

<details>

<summary>

QueryCreateResponse object {id, account\_id, alert\_enabled, 10 more }

</summary>

id: number

Unique identifier for the saved query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

account\_id: number

Account ID

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20account_id">Link to this property</a>

alert\_enabled: boolean

Whether alerts are enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20alert_enabled">Link to this property</a>

alert\_rollup\_enabled: boolean

Whether alert rollup is enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20alert_rollup_enabled">Link to this property</a>

created\_at: string

Creation timestamp

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

name: string

Name of the saved query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

query\_json: string

JSON string containing the query parameters

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20query_json">Link to this property</a>

rule\_enabled: boolean

Whether rule is enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20rule_enabled">Link to this property</a>

updated\_at: string

Last update timestamp

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

user\_email: string

Email of the user who created the query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20user_email">Link to this property</a>

custom\_threat\_feed\_id: optional number

Intel Indicator Feed ID (numeric)

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20custom_threat_feed_id">Link to this property</a>

rule\_list\_id: optional string

WAF rules list ID for blocking

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20rule_list_id">Link to this property</a>

rule\_scope: optional string

Scope for the rule

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)%20%3E%20(property)%20rule_scope">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_create_response%20%3E%20(schema)>)

<details>

<summary>

QueryGetResponse object {id, account\_id, alert\_enabled, 10 more }

</summary>

id: number

Unique identifier for the saved query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

account\_id: number

Account ID

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20account_id">Link to this property</a>

alert\_enabled: boolean

Whether alerts are enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20alert_enabled">Link to this property</a>

alert\_rollup\_enabled: boolean

Whether alert rollup is enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20alert_rollup_enabled">Link to this property</a>

created\_at: string

Creation timestamp

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

name: string

Name of the saved query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

query\_json: string

JSON string containing the query parameters

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20query_json">Link to this property</a>

rule\_enabled: boolean

Whether rule is enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20rule_enabled">Link to this property</a>

updated\_at: string

Last update timestamp

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

user\_email: string

Email of the user who created the query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20user_email">Link to this property</a>

custom\_threat\_feed\_id: optional number

Intel Indicator Feed ID (numeric)

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20custom_threat_feed_id">Link to this property</a>

rule\_list\_id: optional string

WAF rules list ID for blocking

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20rule_list_id">Link to this property</a>

rule\_scope: optional string

Scope for the rule

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)%20%3E%20(property)%20rule_scope">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_get_response%20%3E%20(schema)>)

<details>

<summary>

QueryEditResponse object {id, account\_id, alert\_enabled, 10 more }

</summary>

id: number

Unique identifier for the saved query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

account\_id: number

Account ID

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20account_id">Link to this property</a>

alert\_enabled: boolean

Whether alerts are enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20alert_enabled">Link to this property</a>

alert\_rollup\_enabled: boolean

Whether alert rollup is enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20alert_rollup_enabled">Link to this property</a>

created\_at: string

Creation timestamp

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

name: string

Name of the saved query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

query\_json: string

JSON string containing the query parameters

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20query_json">Link to this property</a>

rule\_enabled: boolean

Whether rule is enabled

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20rule_enabled">Link to this property</a>

updated\_at: string

Last update timestamp

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

user\_email: string

Email of the user who created the query

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20user_email">Link to this property</a>

custom\_threat\_feed\_id: optional number

Intel Indicator Feed ID (numeric)

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20custom_threat_feed_id">Link to this property</a>

rule\_list\_id: optional string

WAF rules list ID for blocking

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20rule_list_id">Link to this property</a>

rule\_scope: optional string

Scope for the rule

<a href="#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)%20%3E%20(property)%20rule_scope">Link to this property</a>

</details>

[Link to this property](<#(resource)%20cloudforce_one.threat_events.queries%20%3E%20(model)%20query_edit_response%20%3E%20(schema)>)