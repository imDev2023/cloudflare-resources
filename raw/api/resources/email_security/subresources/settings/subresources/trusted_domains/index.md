---
title: Trusted Domains
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Email Security](https://developers.cloudflare.com/api/resources/email_security)

[Settings](https://developers.cloudflare.com/api/resources/email_security/subresources/settings)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Trusted Domains

##### [List trusted email domains](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/trusted_domains/methods/list)

GET/accounts/{account\_id}/email-security/settings/trusted\_domains

##### [Get a trusted email domain](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/trusted_domains/methods/get)

GET/accounts/{account\_id}/email-security/settings/trusted\_domains/{trusted\_domain\_id}

##### [Create trusted email domain](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/trusted_domains/methods/create)

POST/accounts/{account\_id}/email-security/settings/trusted\_domains

##### [Update a trusted email domain](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/trusted_domains/methods/edit)

PATCH/accounts/{account\_id}/email-security/settings/trusted\_domains/{trusted\_domain\_id}

##### [Delete a trusted email domain](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/trusted_domains/methods/delete)

DELETE/accounts/{account\_id}/email-security/settings/trusted\_domains/{trusted\_domain\_id}

##### [Batch trusted domain operations](https://developers.cloudflare.com/api/resources/email_security/subresources/settings/subresources/trusted_domains/methods/batch)

POST/accounts/{account\_id}/email-security/settings/trusted\_domains/batch

##### ModelsExpand Collapse

<details>

<summary>

TrustedDomainListResponse object {id, comments, created\_at, 6 more }

A trusted email domain.

</summary>

id: optional string

Trusted domain identifier.

formatuuid

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

comments: optional string

maxLength1024

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_list_response%20%3E%20(schema)%20%3E%20(property)%20comments">Link to this property</a>

created\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_list_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

is\_recent: optional boolean

Select to prevent recently registered domains from triggering a Suspicious or Malicious disposition.

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_list_response%20%3E%20(schema)%20%3E%20(property)%20is_recent">Link to this property</a>

is\_regex: optional boolean

Whether <code>pattern</code> is a regular expression instead of a literal domain.

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_list_response%20%3E%20(schema)%20%3E%20(property)%20is_regex">Link to this property</a>

is\_similarity: optional boolean

Select for partner or other approved domains that have similar spelling to your connected domains. Prevents listed domains from triggering a Spoof disposition.

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_list_response%20%3E%20(schema)%20%3E%20(property)%20is_similarity">Link to this property</a>

Deprecatedlast\_modified: optional string

Use <code>modified_at</code> instead.

Deprecated, use <code>modified_at</code> instead. End of life: November 1, 2026.

formatdate-time

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_list_response%20%3E%20(schema)%20%3E%20(property)%20last_modified">Link to this property</a>

modified\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_list_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

pattern: optional string

The domain pattern to trust, e.g. <code>example.com</code>.

maxLength1024

minLength1

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_list_response%20%3E%20(schema)%20%3E%20(property)%20pattern">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_list_response%20%3E%20(schema)>)

<details>

<summary>

TrustedDomainGetResponse object {id, comments, created\_at, 6 more }

A trusted email domain.

</summary>

id: optional string

Trusted domain identifier.

formatuuid

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

comments: optional string

maxLength1024

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_get_response%20%3E%20(schema)%20%3E%20(property)%20comments">Link to this property</a>

created\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_get_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

is\_recent: optional boolean

Select to prevent recently registered domains from triggering a Suspicious or Malicious disposition.

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_get_response%20%3E%20(schema)%20%3E%20(property)%20is_recent">Link to this property</a>

is\_regex: optional boolean

Whether <code>pattern</code> is a regular expression instead of a literal domain.

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_get_response%20%3E%20(schema)%20%3E%20(property)%20is_regex">Link to this property</a>

is\_similarity: optional boolean

Select for partner or other approved domains that have similar spelling to your connected domains. Prevents listed domains from triggering a Spoof disposition.

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_get_response%20%3E%20(schema)%20%3E%20(property)%20is_similarity">Link to this property</a>

Deprecatedlast\_modified: optional string

Use <code>modified_at</code> instead.

Deprecated, use <code>modified_at</code> instead. End of life: November 1, 2026.

formatdate-time

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_get_response%20%3E%20(schema)%20%3E%20(property)%20last_modified">Link to this property</a>

modified\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_get_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

pattern: optional string

The domain pattern to trust, e.g. <code>example.com</code>.

maxLength1024

minLength1

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_get_response%20%3E%20(schema)%20%3E%20(property)%20pattern">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_get_response%20%3E%20(schema)>)

<details>

<summary>

TrustedDomainCreateResponse object {id, comments, created\_at, 6 more }

A trusted email domain.

</summary>

id: optional string

Trusted domain identifier.

formatuuid

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

comments: optional string

maxLength1024

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_create_response%20%3E%20(schema)%20%3E%20(property)%20comments">Link to this property</a>

created\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_create_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

is\_recent: optional boolean

Select to prevent recently registered domains from triggering a Suspicious or Malicious disposition.

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_create_response%20%3E%20(schema)%20%3E%20(property)%20is_recent">Link to this property</a>

is\_regex: optional boolean

Whether <code>pattern</code> is a regular expression instead of a literal domain.

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_create_response%20%3E%20(schema)%20%3E%20(property)%20is_regex">Link to this property</a>

is\_similarity: optional boolean

Select for partner or other approved domains that have similar spelling to your connected domains. Prevents listed domains from triggering a Spoof disposition.

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_create_response%20%3E%20(schema)%20%3E%20(property)%20is_similarity">Link to this property</a>

Deprecatedlast\_modified: optional string

Use <code>modified_at</code> instead.

Deprecated, use <code>modified_at</code> instead. End of life: November 1, 2026.

formatdate-time

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_create_response%20%3E%20(schema)%20%3E%20(property)%20last_modified">Link to this property</a>

modified\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_create_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

pattern: optional string

The domain pattern to trust, e.g. <code>example.com</code>.

maxLength1024

minLength1

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_create_response%20%3E%20(schema)%20%3E%20(property)%20pattern">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_create_response%20%3E%20(schema)>)

<details>

<summary>

TrustedDomainEditResponse object {id, comments, created\_at, 6 more }

A trusted email domain.

</summary>

id: optional string

Trusted domain identifier.

formatuuid

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

comments: optional string

maxLength1024

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20comments">Link to this property</a>

created\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

is\_recent: optional boolean

Select to prevent recently registered domains from triggering a Suspicious or Malicious disposition.

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20is_recent">Link to this property</a>

is\_regex: optional boolean

Whether <code>pattern</code> is a regular expression instead of a literal domain.

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20is_regex">Link to this property</a>

is\_similarity: optional boolean

Select for partner or other approved domains that have similar spelling to your connected domains. Prevents listed domains from triggering a Spoof disposition.

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20is_similarity">Link to this property</a>

Deprecatedlast\_modified: optional string

Use <code>modified_at</code> instead.

Deprecated, use <code>modified_at</code> instead. End of life: November 1, 2026.

formatdate-time

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20last_modified">Link to this property</a>

modified\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

pattern: optional string

The domain pattern to trust, e.g. <code>example.com</code>.

maxLength1024

minLength1

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_edit_response%20%3E%20(schema)%20%3E%20(property)%20pattern">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_edit_response%20%3E%20(schema)>)

<details>

<summary>

TrustedDomainDeleteResponse object {id }

</summary>

id: string

Trusted domain identifier.

formatuuid

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_delete_response%20%3E%20(schema)>)

<details>

<summary>

TrustedDomainBatchResponse object {deletes, patches, posts, puts }

</summary>

<details>

<summary>

deletes: optional array of object {id }

</summary>

id: string

Trusted domain identifier.

formatuuid

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20deletes%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

</details>

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20deletes">Link to this property</a>

<details>

<summary>

patches: optional array of object {id, comments, created\_at, 6 more }

</summary>

id: optional string

Trusted domain identifier.

formatuuid

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20patches%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

comments: optional string

maxLength1024

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20patches%20%3E%20(items)%20%3E%20(property)%20comments">Link to this property</a>

created\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20patches%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

is\_recent: optional boolean

Select to prevent recently registered domains from triggering a Suspicious or Malicious disposition.

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20patches%20%3E%20(items)%20%3E%20(property)%20is_recent">Link to this property</a>

is\_regex: optional boolean

Whether <code>pattern</code> is a regular expression instead of a literal domain.

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20patches%20%3E%20(items)%20%3E%20(property)%20is_regex">Link to this property</a>

is\_similarity: optional boolean

Select for partner or other approved domains that have similar spelling to your connected domains. Prevents listed domains from triggering a Spoof disposition.

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20patches%20%3E%20(items)%20%3E%20(property)%20is_similarity">Link to this property</a>

Deprecatedlast\_modified: optional string

Use <code>modified_at</code> instead.

Deprecated, use <code>modified_at</code> instead. End of life: November 1, 2026.

formatdate-time

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20patches%20%3E%20(items)%20%3E%20(property)%20last_modified">Link to this property</a>

modified\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20patches%20%3E%20(items)%20%3E%20(property)%20modified_at">Link to this property</a>

pattern: optional string

The domain pattern to trust, e.g. <code>example.com</code>.

maxLength1024

minLength1

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20patches%20%3E%20(items)%20%3E%20(property)%20pattern">Link to this property</a>

</details>

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20patches">Link to this property</a>

<details>

<summary>

posts: optional array of object {id, comments, created\_at, 6 more }

</summary>

id: optional string

Trusted domain identifier.

formatuuid

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20posts%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

comments: optional string

maxLength1024

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20posts%20%3E%20(items)%20%3E%20(property)%20comments">Link to this property</a>

created\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20posts%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

is\_recent: optional boolean

Select to prevent recently registered domains from triggering a Suspicious or Malicious disposition.

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20posts%20%3E%20(items)%20%3E%20(property)%20is_recent">Link to this property</a>

is\_regex: optional boolean

Whether <code>pattern</code> is a regular expression instead of a literal domain.

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20posts%20%3E%20(items)%20%3E%20(property)%20is_regex">Link to this property</a>

is\_similarity: optional boolean

Select for partner or other approved domains that have similar spelling to your connected domains. Prevents listed domains from triggering a Spoof disposition.

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20posts%20%3E%20(items)%20%3E%20(property)%20is_similarity">Link to this property</a>

Deprecatedlast\_modified: optional string

Use <code>modified_at</code> instead.

Deprecated, use <code>modified_at</code> instead. End of life: November 1, 2026.

formatdate-time

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20posts%20%3E%20(items)%20%3E%20(property)%20last_modified">Link to this property</a>

modified\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20posts%20%3E%20(items)%20%3E%20(property)%20modified_at">Link to this property</a>

pattern: optional string

The domain pattern to trust, e.g. <code>example.com</code>.

maxLength1024

minLength1

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20posts%20%3E%20(items)%20%3E%20(property)%20pattern">Link to this property</a>

</details>

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20posts">Link to this property</a>

<details>

<summary>

puts: optional array of object {id, comments, created\_at, 6 more }

</summary>

id: optional string

Trusted domain identifier.

formatuuid

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20puts%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

comments: optional string

maxLength1024

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20puts%20%3E%20(items)%20%3E%20(property)%20comments">Link to this property</a>

created\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20puts%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

is\_recent: optional boolean

Select to prevent recently registered domains from triggering a Suspicious or Malicious disposition.

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20puts%20%3E%20(items)%20%3E%20(property)%20is_recent">Link to this property</a>

is\_regex: optional boolean

Whether <code>pattern</code> is a regular expression instead of a literal domain.

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20puts%20%3E%20(items)%20%3E%20(property)%20is_regex">Link to this property</a>

is\_similarity: optional boolean

Select for partner or other approved domains that have similar spelling to your connected domains. Prevents listed domains from triggering a Spoof disposition.

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20puts%20%3E%20(items)%20%3E%20(property)%20is_similarity">Link to this property</a>

Deprecatedlast\_modified: optional string

Use <code>modified_at</code> instead.

Deprecated, use <code>modified_at</code> instead. End of life: November 1, 2026.

formatdate-time

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20puts%20%3E%20(items)%20%3E%20(property)%20last_modified">Link to this property</a>

modified\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20puts%20%3E%20(items)%20%3E%20(property)%20modified_at">Link to this property</a>

pattern: optional string

The domain pattern to trust, e.g. <code>example.com</code>.

maxLength1024

minLength1

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20puts%20%3E%20(items)%20%3E%20(property)%20pattern">Link to this property</a>

</details>

<a href="#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)%20%3E%20(property)%20puts">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.settings.trusted_domains%20%3E%20(model)%20trusted_domain_batch_response%20%3E%20(schema)>)