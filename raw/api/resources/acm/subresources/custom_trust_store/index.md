---
title: Custom Trust Store
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[ACM](https://developers.cloudflare.com/api/resources/acm)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Custom Trust Store

##### [List Custom Origin Trust Store Details](https://developers.cloudflare.com/api/resources/acm/subresources/custom_trust_store/methods/list)

GET/zones/{zone\_id}/acm/custom\_trust\_store

##### [Upload Custom Origin Trust Store](https://developers.cloudflare.com/api/resources/acm/subresources/custom_trust_store/methods/create)

POST/zones/{zone\_id}/acm/custom\_trust\_store

##### [Custom Origin Trust Store Details](https://developers.cloudflare.com/api/resources/acm/subresources/custom_trust_store/methods/get)

GET/zones/{zone\_id}/acm/custom\_trust\_store/{custom\_origin\_trust\_store\_id}

##### [Delete Custom Origin Trust Store](https://developers.cloudflare.com/api/resources/acm/subresources/custom_trust_store/methods/delete)

DELETE/zones/{zone\_id}/acm/custom\_trust\_store/{custom\_origin\_trust\_store\_id}

##### ModelsExpand Collapse

<details>

<summary>

CustomTrustStore object {id, certificate, expires\_on, 5 more }

</summary>

id: string

Certificate identifier tag.

maxLength36

<a href="#(resource)%20acm.custom_trust_store%20%3E%20(model)%20custom-trust-store%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

certificate: string

The root CA certificate in PEM format. Only root CA certificates are accepted; intermediate and leaf certificates are not supported.

<a href="#(resource)%20acm.custom_trust_store%20%3E%20(model)%20custom-trust-store%20%3E%20(schema)%20%3E%20(property)%20certificate">Link to this property</a>

expires\_on: string

When the certificate expires.

formatdate-time

<a href="#(resource)%20acm.custom_trust_store%20%3E%20(model)%20custom-trust-store%20%3E%20(schema)%20%3E%20(property)%20expires_on">Link to this property</a>

issuer: string

The certificate authority that issued the certificate.

<a href="#(resource)%20acm.custom_trust_store%20%3E%20(model)%20custom-trust-store%20%3E%20(schema)%20%3E%20(property)%20issuer">Link to this property</a>

signature: string

The type of hash used for the certificate.

<a href="#(resource)%20acm.custom_trust_store%20%3E%20(model)%20custom-trust-store%20%3E%20(schema)%20%3E%20(property)%20signature">Link to this property</a>

<details>

<summary>

status: "initializing"or "pending\_deployment"or "active"or 3 more

Status of the zone’s custom SSL.

</summary>

One of the following:

"initializing"

<a href="#(resource)%20acm.custom_trust_store%20%3E%20(model)%20custom-trust-store%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending\_deployment"

<a href="#(resource)%20acm.custom_trust_store%20%3E%20(model)%20custom-trust-store%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"active"

<a href="#(resource)%20acm.custom_trust_store%20%3E%20(model)%20custom-trust-store%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"pending\_deletion"

<a href="#(resource)%20acm.custom_trust_store%20%3E%20(model)%20custom-trust-store%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"deleted"

<a href="#(resource)%20acm.custom_trust_store%20%3E%20(model)%20custom-trust-store%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"expired"

<a href="#(resource)%20acm.custom_trust_store%20%3E%20(model)%20custom-trust-store%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20acm.custom_trust_store%20%3E%20(model)%20custom-trust-store%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

updated\_at: string

When the certificate was last modified.

formatdate-time

<a href="#(resource)%20acm.custom_trust_store%20%3E%20(model)%20custom-trust-store%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

uploaded\_on: string

When the certificate was uploaded to Cloudflare.

formatdate-time

<a href="#(resource)%20acm.custom_trust_store%20%3E%20(model)%20custom-trust-store%20%3E%20(schema)%20%3E%20(property)%20uploaded_on">Link to this property</a>

</details>

[Link to this property](<#(resource)%20acm.custom_trust_store%20%3E%20(model)%20custom-trust-store%20%3E%20(schema)>)

<details>

<summary>

CustomTrustStoreDeleteResponse object {id }

</summary>

id: optional string

Certificate identifier tag.

maxLength36

<a href="#(resource)%20acm.custom_trust_store%20%3E%20(model)%20custom_trust_store_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20acm.custom_trust_store%20%3E%20(model)%20custom_trust_store_delete_response%20%3E%20(schema)>)