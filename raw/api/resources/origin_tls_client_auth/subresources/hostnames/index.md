---
title: Hostnames
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Origin TLS Client Auth](https://developers.cloudflare.com/api/resources/origin_tls_client_auth)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Hostnames

##### [Get the Hostname Status for Client Authentication](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostnames/methods/get)

GET/zones/{zone\_id}/origin\_tls\_client\_auth/hostnames/{hostname}

##### [Enable or Disable a Hostname for Client Authentication](https://developers.cloudflare.com/api/resources/origin_tls_client_auth/subresources/hostnames/methods/update)

PUT/zones/{zone\_id}/origin\_tls\_client\_auth/hostnames

##### ModelsExpand Collapse

<details>

<summary>

AuthenticatedOriginPull object {cert\_id, cert\_status, cert\_updated\_at, 11 more }

</summary>

cert\_id: optional string

Certificate identifier tag.

maxLength36

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20cert_id">Link to this property</a>

<details>

<summary>

cert\_status: optional "initializing"or "pending\_deployment"or "pending\_deletion"or 4 more

Status of the certificate or the association.

</summary>

One of the following:

"initializing"

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20cert_status%20%3E%20(member)%200">Link to this property</a>

"pending\_deployment"

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20cert_status%20%3E%20(member)%201">Link to this property</a>

"pending\_deletion"

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20cert_status%20%3E%20(member)%202">Link to this property</a>

"active"

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20cert_status%20%3E%20(member)%203">Link to this property</a>

"deleted"

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20cert_status%20%3E%20(member)%204">Link to this property</a>

"deployment\_timed\_out"

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20cert_status%20%3E%20(member)%205">Link to this property</a>

"deletion\_timed\_out"

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20cert_status%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20cert_status">Link to this property</a>

cert\_updated\_at: optional string

The time when the certificate was updated.

formatdate-time

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20cert_updated_at">Link to this property</a>

cert\_uploaded\_on: optional string

The time when the certificate was uploaded.

formatdate-time

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20cert_uploaded_on">Link to this property</a>

certificate: optional string

The hostname certificate.

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20certificate">Link to this property</a>

created\_at: optional string

The time when the certificate was created.

formatdate-time

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

enabled: optional boolean

Indicates whether hostname-level authenticated origin pulls is enabled. A null value voids the association.

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

expires\_on: optional string

The date when the certificate expires.

formatdate-time

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20expires_on">Link to this property</a>

hostname: optional string

The hostname on the origin for which the client certificate uploaded will be used.

maxLength255

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20hostname">Link to this property</a>

issuer: optional string

The certificate authority that issued the certificate.

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20issuer">Link to this property</a>

serial\_number: optional string

The serial number on the uploaded certificate.

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20serial_number">Link to this property</a>

signature: optional string

The type of hash used for the certificate.

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20signature">Link to this property</a>

<details>

<summary>

status: optional "initializing"or "pending\_deployment"or "pending\_deletion"or 4 more

Status of the certificate or the association.

</summary>

One of the following:

"initializing"

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"pending\_deployment"

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"pending\_deletion"

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"active"

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"deleted"

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

"deployment\_timed\_out"

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%205">Link to this property</a>

"deletion\_timed\_out"

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%206">Link to this property</a>

</details>

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

updated\_at: optional string

The time when the certificate was updated.

formatdate-time

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)>)

<details>

<summary>

HostnameUpdateResponse = <a href="https://developers.cloudflare.com/api/resources/origin_tls_client_auth#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20authenticated_origin_pull%20%3E%20(schema)">AuthenticatedOriginPull</a> { cert\_id, cert\_status, cert\_updated\_at, 11 more }

</summary>

id: optional string

Certificate identifier tag.

maxLength36

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20hostname_update_response%20%3E%20(schema)%20%3E%20(entry)%201%20%3E%20(property)%20id">Link to this property</a>

cert\_id: optional string

Certificate identifier tag.

maxLength36

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20hostname_update_response%20%3E%20(schema)%20%3E%20(entry)%201%20%3E%20(property)%20cert_id">Link to this property</a>

certificate: optional string

The hostname certificate.

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20hostname_update_response%20%3E%20(schema)%20%3E%20(entry)%201%20%3E%20(property)%20certificate">Link to this property</a>

enabled: optional boolean

Indicates whether hostname-level authenticated origin pulls is enabled. A null value voids the association.

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20hostname_update_response%20%3E%20(schema)%20%3E%20(entry)%201%20%3E%20(property)%20enabled">Link to this property</a>

hostname: optional string

The hostname on the origin for which the client certificate uploaded will be used.

maxLength255

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20hostname_update_response%20%3E%20(schema)%20%3E%20(entry)%201%20%3E%20(property)%20hostname">Link to this property</a>

private\_key: optional string

The hostname certificate’s private key.

<a href="#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20hostname_update_response%20%3E%20(schema)%20%3E%20(entry)%201%20%3E%20(property)%20private_key">Link to this property</a>

</details>

[Link to this property](<#(resource)%20origin_tls_client_auth.hostnames%20%3E%20(model)%20hostname_update_response%20%3E%20(schema)>)