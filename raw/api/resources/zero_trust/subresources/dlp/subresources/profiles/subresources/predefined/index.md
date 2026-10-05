---
title: Predefined
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[DLP](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp)

[Profiles](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/profiles)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Predefined

##### [Get predefined profile config](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/profiles/subresources/predefined/methods/get)

GET/accounts/{account\_id}/dlp/profiles/predefined/{profile\_id}/config

##### [Update predefined profile config](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/profiles/subresources/predefined/methods/update)

PUT/accounts/{account\_id}/dlp/profiles/predefined/{profile\_id}/config

##### [Delete predefined profile](https://developers.cloudflare.com/api/resources/zero_trust/subresources/dlp/subresources/profiles/subresources/predefined/methods/delete)

DELETE/accounts/{account\_id}/dlp/profiles/predefined/{profile\_id}

##### ModelsExpand Collapse

<details>

<summary>

PredefinedProfile object {id, allowed\_match\_count, confidence\_threshold, 6 more }

</summary>

id: string

The id of the predefined profile (uuid).

formatuuid

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

allowed\_match\_count: number

formatint32

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20allowed_match_count">Link to this property</a>

confidence\_threshold: string

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20confidence_threshold">Link to this property</a>

enabled\_entries: array of string

Entries to enable for this predefined profile. Any entries not provided will be disabled.

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20enabled_entries">Link to this property</a>

<details>

<summary>

Deprecatedentries: array of object {id, created\_at, enabled, 6 more } or object {id, created\_at, enabled, 4 more } or object {id, confidence, enabled, 5 more } or 4 more

This field has been deprecated for <code>enabled_entries</code>.

</summary>

One of the following:

<details>

<summary>

CustomEntry object {id, created\_at, enabled, 6 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20created_at">Link to this property</a>

Deprecatedenabled: boolean

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20enabled">Link to this property</a>

name: string

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20name">Link to this property</a>

pattern: <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.dlp.profiles.custom%20%3E%20(model)%20pattern%20%3E%20(schema)">Pattern</a> { regex, validation }

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20pattern">Link to this property</a>

type: "custom"

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

updated\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20updated_at">Link to this property</a>

description: optional string

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20description">Link to this property</a>

Deprecatedprofile\_id: optional string

formatuuid

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%200%20%3E%20(property)%20profile_id">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

CustomPromptTopicEntry object {id, created\_at, enabled, 4 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20created_at">Link to this property</a>

Deprecatedenabled: boolean

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20enabled">Link to this property</a>

name: string

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20name">Link to this property</a>

type: "custom\_prompt\_topic"

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

updated\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20updated_at">Link to this property</a>

description: optional string

The optional description of the custom prompt topic entry.

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%201%20%3E%20(property)%20description">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

<details>

<summary>

PredefinedEntry object {id, confidence, enabled, 5 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

confidence: object {ai\_context\_available, available }

</summary>

ai\_context\_available: boolean

Indicates whether this entry has AI remote service validation.

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20confidence%20%3E%20(property)%20ai_context_available">Link to this property</a>

available: boolean

Indicates whether this entry has any form of validation that is not an AI remote service.

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20confidence%20%3E%20(property)%20available">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20confidence">Link to this property</a>

enabled: boolean

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20enabled">Link to this property</a>

name: string

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20name">Link to this property</a>

type: "predefined"

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20type">Link to this property</a>

deprecated: optional boolean

Whether this entry is deprecated for new use. This is computed from the static catalog and emitted only when true.

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20deprecated">Link to this property</a>

Deprecatedprofile\_id: optional string

formatuuid

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20profile_id">Link to this property</a>

<details>

<summary>

variant: optional object {topic\_type, type, description } or object {type, description }

A Predefined AI prompt classification topic entry.

</summary>

One of the following:

<details>

<summary>

object {topic\_type, type, description }

A Predefined AI prompt classification topic entry.

</summary>

<details>

<summary>

topic\_type: "Intent"or "Content"

</summary>

One of the following:

"Intent"

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20variant%20%3E%20(variant)%200%20%3E%20(property)%20topic_type%20%3E%20(member)%200">Link to this property</a>

"Content"

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20variant%20%3E%20(variant)%200%20%3E%20(property)%20topic_type%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20variant%20%3E%20(variant)%200%20%3E%20(property)%20topic_type">Link to this property</a>

type: "PromptTopic"

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20variant%20%3E%20(variant)%200%20%3E%20(property)%20type">Link to this property</a>

description: optional string

A customer-facing explanation of what this predefined AI prompt topic represents.

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20variant%20%3E%20(variant)%200%20%3E%20(property)%20description">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20variant%20%3E%20(variant)%200">Link to this property</a>

<details>

<summary>

object {type, description }

A general predefined entry.

</summary>

type: "General"

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20variant%20%3E%20(variant)%201%20%3E%20(property)%20type">Link to this property</a>

description: optional string

A customer-facing explanation of what this predefined entry represents.

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20variant%20%3E%20(variant)%201%20%3E%20(property)%20description">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20variant%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%202%20%3E%20(property)%20variant">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

<details>

<summary>

IntegrationEntry object {id, created\_at, enabled, 4 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20created_at">Link to this property</a>

enabled: boolean

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20enabled">Link to this property</a>

name: string

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20name">Link to this property</a>

type: "integration"

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20type">Link to this property</a>

updated\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20updated_at">Link to this property</a>

profile\_id: optional string

formatuuid

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%203%20%3E%20(property)%20profile_id">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%203">Link to this property</a>

<details>

<summary>

ExactDataEntry object {id, case\_sensitive, created\_at, 6 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20id">Link to this property</a>

case\_sensitive: boolean

Only applies to custom word lists. Determines if the words should be matched in a case-sensitive manner Cannot be set to false if secret is true

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20case_sensitive">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20created_at">Link to this property</a>

enabled: boolean

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20enabled">Link to this property</a>

name: string

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20name">Link to this property</a>

secret: boolean

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20secret">Link to this property</a>

type: "exact\_data"

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20type">Link to this property</a>

updated\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20updated_at">Link to this property</a>

description: optional string

The optional description of the exact data entry.

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%204%20%3E%20(property)%20description">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%204">Link to this property</a>

<details>

<summary>

DocumentFingerprintEntry object {id, created\_at, enabled, 4 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20created_at">Link to this property</a>

enabled: boolean

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20enabled">Link to this property</a>

name: string

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20name">Link to this property</a>

type: "document\_fingerprint"

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20type">Link to this property</a>

updated\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20updated_at">Link to this property</a>

description: optional string

The optional description of the document fingerprint entry.

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%205%20%3E%20(property)%20description">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%205">Link to this property</a>

<details>

<summary>

WordListEntry object {id, created\_at, enabled, 5 more }

</summary>

id: string

formatuuid

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20id">Link to this property</a>

created\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20created_at">Link to this property</a>

enabled: boolean

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20enabled">Link to this property</a>

name: string

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20name">Link to this property</a>

type: "word\_list"

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20type">Link to this property</a>

updated\_at: string

formatdate-time

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20updated_at">Link to this property</a>

word\_list: array of string

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20word_list">Link to this property</a>

profile\_id: optional string

formatuuid

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%206%20%3E%20(property)%20profile_id">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries%20%3E%20(items)%20%3E%20(variant)%206">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20entries">Link to this property</a>

name: string

The name of the predefined profile.

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

ai\_context\_enabled: optional boolean

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20ai_context_enabled">Link to this property</a>

ocr\_enabled: optional boolean

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20ocr_enabled">Link to this property</a>

open\_access: optional boolean

Whether this profile can be accessed by anyone.

<a href="#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)%20%3E%20(property)%20open_access">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_profile%20%3E%20(schema)>)

PredefinedDeleteResponse = unknown

[Link to this property](<#(resource)%20zero_trust.dlp.profiles.predefined%20%3E%20(model)%20predefined_delete_response%20%3E%20(schema)>)