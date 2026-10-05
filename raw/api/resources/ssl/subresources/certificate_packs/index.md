---
title: Certificate Packs
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[SSL](https://developers.cloudflare.com/api/resources/ssl)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Certificate Packs

##### [List Certificate Packs](https://developers.cloudflare.com/api/resources/ssl/subresources/certificate_packs/methods/list)

GET/zones/{zone\_id}/ssl/certificate\_packs

##### [Get Certificate Pack](https://developers.cloudflare.com/api/resources/ssl/subresources/certificate_packs/methods/get)

GET/zones/{zone\_id}/ssl/certificate\_packs/{certificate\_pack\_id}

##### [Order Advanced Certificate Manager Certificate Pack](https://developers.cloudflare.com/api/resources/ssl/subresources/certificate_packs/methods/create)

POST/zones/{zone\_id}/ssl/certificate\_packs/order

##### [Restart Validation or Update Advanced Certificate Manager Certificate Pack](https://developers.cloudflare.com/api/resources/ssl/subresources/certificate_packs/methods/edit)

PATCH/zones/{zone\_id}/ssl/certificate\_packs/{certificate\_pack\_id}

##### [Delete Advanced Certificate Manager Certificate Pack](https://developers.cloudflare.com/api/resources/ssl/subresources/certificate_packs/methods/delete)

DELETE/zones/{zone\_id}/ssl/certificate\_packs/{certificate\_pack\_id}

##### ModelsExpand Collapse

Host = string

[Link to this property](<#(resource)%20ssl.certificate_packs%20%3E%20(model)%20host%20%3E%20(schema)>)

<details>

<summary>

RequestValidity = 7or 30or 90or 4 more

The number of days for which the certificate should be valid.

</summary>

One of the following:

7

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20request_validity%20%3E%20(schema)%20%3E%20(member)%200">Link to this property</a>

30

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20request_validity%20%3E%20(schema)%20%3E%20(member)%201">Link to this property</a>

90

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20request_validity%20%3E%20(schema)%20%3E%20(member)%202">Link to this property</a>

365

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20request_validity%20%3E%20(schema)%20%3E%20(member)%203">Link to this property</a>

730

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20request_validity%20%3E%20(schema)%20%3E%20(member)%204">Link to this property</a>

1095

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20request_validity%20%3E%20(schema)%20%3E%20(member)%205">Link to this property</a>

5475

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20request_validity%20%3E%20(schema)%20%3E%20(member)%206">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ssl.certificate_packs%20%3E%20(model)%20request_validity%20%3E%20(schema)>)

<details>

<summary>

Status = "initializing"or "pending\_validation"or "deleted"or 18 more

Status of certificate pack.

</summary>

One of the following:

"initializing"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)%20%3E%20(member)%200">Link to this property</a>

"pending\_validation"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)%20%3E%20(member)%201">Link to this property</a>

"deleted"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)%20%3E%20(member)%202">Link to this property</a>

"pending\_issuance"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)%20%3E%20(member)%203">Link to this property</a>

"pending\_deployment"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)%20%3E%20(member)%204">Link to this property</a>

"pending\_deletion"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)%20%3E%20(member)%205">Link to this property</a>

"pending\_expiration"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)%20%3E%20(member)%206">Link to this property</a>

"expired"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)%20%3E%20(member)%207">Link to this property</a>

"active"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)%20%3E%20(member)%208">Link to this property</a>

"initializing\_timed\_out"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)%20%3E%20(member)%209">Link to this property</a>

"validation\_timed\_out"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)%20%3E%20(member)%2010">Link to this property</a>

"issuance\_timed\_out"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)%20%3E%20(member)%2011">Link to this property</a>

"deployment\_timed\_out"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)%20%3E%20(member)%2012">Link to this property</a>

"deletion\_timed\_out"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)%20%3E%20(member)%2013">Link to this property</a>

"pending\_cleanup"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)%20%3E%20(member)%2014">Link to this property</a>

"staging\_deployment"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)%20%3E%20(member)%2015">Link to this property</a>

"staging\_active"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)%20%3E%20(member)%2016">Link to this property</a>

"deactivating"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)%20%3E%20(member)%2017">Link to this property</a>

"inactive"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)%20%3E%20(member)%2018">Link to this property</a>

"backup\_issued"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)%20%3E%20(member)%2019">Link to this property</a>

"holding\_deployment"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)%20%3E%20(member)%2020">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)>)

<details>

<summary>

ValidationMethod = "http"or "cname"or "txt"

Validation method in use for a certificate pack order.

</summary>

One of the following:

"http"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20validation_method%20%3E%20(schema)%20%3E%20(member)%200">Link to this property</a>

"cname"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20validation_method%20%3E%20(schema)%20%3E%20(member)%201">Link to this property</a>

"txt"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20validation_method%20%3E%20(schema)%20%3E%20(member)%202">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ssl.certificate_packs%20%3E%20(model)%20validation_method%20%3E%20(schema)>)

<details>

<summary>

CertificatePackListResponse object {id, certificates, hosts, 10 more }

A certificate pack with all its properties.

</summary>

id: string

The unique identifier for a certificate\_pack.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

certificates: array of object {id, hosts, status, 9 more }

Array of certificates in this pack.

</summary>

id: string

Certificate identifier.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

hosts: array of string

Hostnames covered by this certificate.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20hosts">Link to this property</a>

status: string

Certificate status.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

bundle\_method: optional string

Certificate bundle method.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20bundle_method">Link to this property</a>

expires\_on: optional string

When the certificate from the authority expires.

formatdate-time

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20expires_on">Link to this property</a>

<details>

<summary>

geo\_restrictions: optional object {label }

Specify the region where your private key can be held locally.

</summary>

<details>

<summary>

label: optional "us"or "eu"or "highest\_security"

</summary>

One of the following:

"us"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20geo_restrictions%20%3E%20(property)%20label%20%3E%20(member)%200">Link to this property</a>

"eu"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20geo_restrictions%20%3E%20(property)%20label%20%3E%20(member)%201">Link to this property</a>

"highest\_security"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20geo_restrictions%20%3E%20(property)%20label%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20geo_restrictions%20%3E%20(property)%20label">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20geo_restrictions">Link to this property</a>

issuer: optional string

The certificate authority that issued the certificate.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20issuer">Link to this property</a>

modified\_on: optional string

When the certificate was last modified.

formatdate-time

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20modified_on">Link to this property</a>

priority: optional number

The order/priority in which the certificate will be used.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20priority">Link to this property</a>

signature: optional string

The type of hash used for the certificate.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20signature">Link to this property</a>

uploaded\_on: optional string

When the certificate was uploaded to Cloudflare.

formatdate-time

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20uploaded_on">Link to this property</a>

zone\_id: optional string

Identifier.

maxLength32

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20zone_id">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20certificates">Link to this property</a>

hosts: array of <a href="https://developers.cloudflare.com/api/resources/ssl#(resource)%20ssl.certificate_packs%20%3E%20(model)%20host%20%3E%20(schema)">Host</a>

Comma separated list of valid host names for the certificate packs. Must contain the zone apex, may not contain more than 50 hosts, and may not be empty.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20hosts">Link to this property</a>

status: <a href="https://developers.cloudflare.com/api/resources/ssl#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)">Status</a>

Status of certificate pack.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

type: "mh\_custom"or "managed\_hostname"or "sni\_custom"or 5 more

Type of certificate pack.

</summary>

One of the following:

"mh\_custom"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"managed\_hostname"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"sni\_custom"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"universal"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"advanced"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

"total\_tls"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205">Link to this property</a>

"keyless"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%206">Link to this property</a>

"legacy\_custom"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

certificate\_authority: optional "google"or "lets\_encrypt"or "ssl\_com"

Certificate Authority selected for the order. For information on any certificate authority specific details or restrictions <a href="https://developers.cloudflare.com/ssl/reference/certificate-authorities">see this page for more details</a>.

</summary>

One of the following:

"google"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%200">Link to this property</a>

"lets\_encrypt"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%201">Link to this property</a>

"ssl\_com"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority">Link to this property</a>

cloudflare\_branding: optional boolean

Whether or not to add Cloudflare Branding for the order. This will add a subdomain of sni.cloudflaressl.com as the Common Name if set to true.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20cloudflare_branding">Link to this property</a>

<details>

<summary>

dcv\_delegation\_records: optional array of object {cname, cname\_target, emails, 5 more }

DCV Delegation records for domain validation.

</summary>

cname: optional string

The CNAME record hostname for DCV delegation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20cname">Link to this property</a>

cname\_target: optional string

The CNAME record target value for DCV delegation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20cname_target">Link to this property</a>

emails: optional array of string

The set of email addresses that the certificate authority (CA) will use to complete domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20emails">Link to this property</a>

http\_body: optional string

The content that the certificate authority (CA) will expect to find at the http\_url during the domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20http_body">Link to this property</a>

http\_url: optional string

The url that will be checked during domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20http_url">Link to this property</a>

status: optional string

Status of the validation record.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

txt\_name: optional string

The hostname that the certificate authority (CA) will check for a TXT record during domain validation .

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20txt_name">Link to this property</a>

txt\_value: optional string

The TXT record that the certificate authority (CA) will check during domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20txt_value">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records">Link to this property</a>

primary\_certificate: optional string

Identifier of the primary certificate in a pack.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20primary_certificate">Link to this property</a>

<details>

<summary>

validation\_errors: optional array of object {message }

Domain validation errors that have been received by the certificate authority (CA).

</summary>

message: optional string

A domain validation error.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_errors">Link to this property</a>

<details>

<summary>

validation\_method: optional "txt"or "http"or "email"

Validation Method selected for the order.

</summary>

One of the following:

"txt"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_method%20%3E%20(member)%200">Link to this property</a>

"http"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_method%20%3E%20(member)%201">Link to this property</a>

"email"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_method%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_method">Link to this property</a>

<details>

<summary>

validation\_records: optional array of object {cname, cname\_target, emails, 5 more }

Certificates’ validation records.

</summary>

cname: optional string

The CNAME record hostname for DCV delegation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20cname">Link to this property</a>

cname\_target: optional string

The CNAME record target value for DCV delegation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20cname_target">Link to this property</a>

emails: optional array of string

The set of email addresses that the certificate authority (CA) will use to complete domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20emails">Link to this property</a>

http\_body: optional string

The content that the certificate authority (CA) will expect to find at the http\_url during the domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20http_body">Link to this property</a>

http\_url: optional string

The url that will be checked during domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20http_url">Link to this property</a>

status: optional string

Status of the validation record.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

txt\_name: optional string

The hostname that the certificate authority (CA) will check for a TXT record during domain validation .

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20txt_name">Link to this property</a>

txt\_value: optional string

The TXT record that the certificate authority (CA) will check during domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20txt_value">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20validation_records">Link to this property</a>

<details>

<summary>

validity\_days: optional 14or 30or 90or 365

Validity Days selected for the order.

</summary>

One of the following:

14

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20validity_days%20%3E%20(member)%200">Link to this property</a>

30

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20validity_days%20%3E%20(member)%201">Link to this property</a>

90

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20validity_days%20%3E%20(member)%202">Link to this property</a>

365

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20validity_days%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)%20%3E%20(property)%20validity_days">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_list_response%20%3E%20(schema)>)

<details>

<summary>

CertificatePackGetResponse object {id, certificates, hosts, 10 more }

A certificate pack with all its properties.

</summary>

id: string

The unique identifier for a certificate\_pack.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

certificates: array of object {id, hosts, status, 9 more }

Array of certificates in this pack.

</summary>

id: string

Certificate identifier.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

hosts: array of string

Hostnames covered by this certificate.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20hosts">Link to this property</a>

status: string

Certificate status.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

bundle\_method: optional string

Certificate bundle method.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20bundle_method">Link to this property</a>

expires\_on: optional string

When the certificate from the authority expires.

formatdate-time

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20expires_on">Link to this property</a>

<details>

<summary>

geo\_restrictions: optional object {label }

Specify the region where your private key can be held locally.

</summary>

<details>

<summary>

label: optional "us"or "eu"or "highest\_security"

</summary>

One of the following:

"us"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20geo_restrictions%20%3E%20(property)%20label%20%3E%20(member)%200">Link to this property</a>

"eu"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20geo_restrictions%20%3E%20(property)%20label%20%3E%20(member)%201">Link to this property</a>

"highest\_security"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20geo_restrictions%20%3E%20(property)%20label%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20geo_restrictions%20%3E%20(property)%20label">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20geo_restrictions">Link to this property</a>

issuer: optional string

The certificate authority that issued the certificate.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20issuer">Link to this property</a>

modified\_on: optional string

When the certificate was last modified.

formatdate-time

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20modified_on">Link to this property</a>

priority: optional number

The order/priority in which the certificate will be used.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20priority">Link to this property</a>

signature: optional string

The type of hash used for the certificate.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20signature">Link to this property</a>

uploaded\_on: optional string

When the certificate was uploaded to Cloudflare.

formatdate-time

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20uploaded_on">Link to this property</a>

zone\_id: optional string

Identifier.

maxLength32

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20zone_id">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20certificates">Link to this property</a>

hosts: array of <a href="https://developers.cloudflare.com/api/resources/ssl#(resource)%20ssl.certificate_packs%20%3E%20(model)%20host%20%3E%20(schema)">Host</a>

Comma separated list of valid host names for the certificate packs. Must contain the zone apex, may not contain more than 50 hosts, and may not be empty.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20hosts">Link to this property</a>

status: <a href="https://developers.cloudflare.com/api/resources/ssl#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)">Status</a>

Status of certificate pack.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

type: "mh\_custom"or "managed\_hostname"or "sni\_custom"or 5 more

Type of certificate pack.

</summary>

One of the following:

"mh\_custom"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"managed\_hostname"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"sni\_custom"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"universal"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"advanced"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

"total\_tls"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205">Link to this property</a>

"keyless"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%206">Link to this property</a>

"legacy\_custom"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

certificate\_authority: optional "google"or "lets\_encrypt"or "ssl\_com"

Certificate Authority selected for the order. For information on any certificate authority specific details or restrictions <a href="https://developers.cloudflare.com/ssl/reference/certificate-authorities">see this page for more details</a>.

</summary>

One of the following:

"google"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%200">Link to this property</a>

"lets\_encrypt"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%201">Link to this property</a>

"ssl\_com"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority">Link to this property</a>

cloudflare\_branding: optional boolean

Whether or not to add Cloudflare Branding for the order. This will add a subdomain of sni.cloudflaressl.com as the Common Name if set to true.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20cloudflare_branding">Link to this property</a>

<details>

<summary>

dcv\_delegation\_records: optional array of object {cname, cname\_target, emails, 5 more }

DCV Delegation records for domain validation.

</summary>

cname: optional string

The CNAME record hostname for DCV delegation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20cname">Link to this property</a>

cname\_target: optional string

The CNAME record target value for DCV delegation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20cname_target">Link to this property</a>

emails: optional array of string

The set of email addresses that the certificate authority (CA) will use to complete domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20emails">Link to this property</a>

http\_body: optional string

The content that the certificate authority (CA) will expect to find at the http\_url during the domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20http_body">Link to this property</a>

http\_url: optional string

The url that will be checked during domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20http_url">Link to this property</a>

status: optional string

Status of the validation record.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

txt\_name: optional string

The hostname that the certificate authority (CA) will check for a TXT record during domain validation .

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20txt_name">Link to this property</a>

txt\_value: optional string

The TXT record that the certificate authority (CA) will check during domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20txt_value">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records">Link to this property</a>

primary\_certificate: optional string

Identifier of the primary certificate in a pack.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20primary_certificate">Link to this property</a>

<details>

<summary>

validation\_errors: optional array of object {message }

Domain validation errors that have been received by the certificate authority (CA).

</summary>

message: optional string

A domain validation error.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_errors">Link to this property</a>

<details>

<summary>

validation\_method: optional "txt"or "http"or "email"

Validation Method selected for the order.

</summary>

One of the following:

"txt"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_method%20%3E%20(member)%200">Link to this property</a>

"http"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_method%20%3E%20(member)%201">Link to this property</a>

"email"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_method%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_method">Link to this property</a>

<details>

<summary>

validation\_records: optional array of object {cname, cname\_target, emails, 5 more }

Certificates’ validation records.

</summary>

cname: optional string

The CNAME record hostname for DCV delegation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20cname">Link to this property</a>

cname\_target: optional string

The CNAME record target value for DCV delegation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20cname_target">Link to this property</a>

emails: optional array of string

The set of email addresses that the certificate authority (CA) will use to complete domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20emails">Link to this property</a>

http\_body: optional string

The content that the certificate authority (CA) will expect to find at the http\_url during the domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20http_body">Link to this property</a>

http\_url: optional string

The url that will be checked during domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20http_url">Link to this property</a>

status: optional string

Status of the validation record.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

txt\_name: optional string

The hostname that the certificate authority (CA) will check for a TXT record during domain validation .

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20txt_name">Link to this property</a>

txt\_value: optional string

The TXT record that the certificate authority (CA) will check during domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20txt_value">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20validation_records">Link to this property</a>

<details>

<summary>

validity\_days: optional 14or 30or 90or 365

Validity Days selected for the order.

</summary>

One of the following:

14

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20validity_days%20%3E%20(member)%200">Link to this property</a>

30

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20validity_days%20%3E%20(member)%201">Link to this property</a>

90

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20validity_days%20%3E%20(member)%202">Link to this property</a>

365

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20validity_days%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)%20%3E%20(property)%20validity_days">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_get_response%20%3E%20(schema)>)

<details>

<summary>

CertificatePackCreateResponse object {id, certificates, hosts, 10 more }

A certificate pack with all its properties.

</summary>

id: string

The unique identifier for a certificate\_pack.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

certificates: array of object {id, hosts, status, 9 more }

Array of certificates in this pack.

</summary>

id: string

Certificate identifier.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

hosts: array of string

Hostnames covered by this certificate.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20hosts">Link to this property</a>

status: string

Certificate status.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

bundle\_method: optional string

Certificate bundle method.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20bundle_method">Link to this property</a>

expires\_on: optional string

When the certificate from the authority expires.

formatdate-time

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20expires_on">Link to this property</a>

<details>

<summary>

geo\_restrictions: optional object {label }

Specify the region where your private key can be held locally.

</summary>

<details>

<summary>

label: optional "us"or "eu"or "highest\_security"

</summary>

One of the following:

"us"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20geo_restrictions%20%3E%20(property)%20label%20%3E%20(member)%200">Link to this property</a>

"eu"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20geo_restrictions%20%3E%20(property)%20label%20%3E%20(member)%201">Link to this property</a>

"highest\_security"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20geo_restrictions%20%3E%20(property)%20label%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20geo_restrictions%20%3E%20(property)%20label">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20geo_restrictions">Link to this property</a>

issuer: optional string

The certificate authority that issued the certificate.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20issuer">Link to this property</a>

modified\_on: optional string

When the certificate was last modified.

formatdate-time

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20modified_on">Link to this property</a>

priority: optional number

The order/priority in which the certificate will be used.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20priority">Link to this property</a>

signature: optional string

The type of hash used for the certificate.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20signature">Link to this property</a>

uploaded\_on: optional string

When the certificate was uploaded to Cloudflare.

formatdate-time

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20uploaded_on">Link to this property</a>

zone\_id: optional string

Identifier.

maxLength32

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20zone_id">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20certificates">Link to this property</a>

hosts: array of <a href="https://developers.cloudflare.com/api/resources/ssl#(resource)%20ssl.certificate_packs%20%3E%20(model)%20host%20%3E%20(schema)">Host</a>

Comma separated list of valid host names for the certificate packs. Must contain the zone apex, may not contain more than 50 hosts, and may not be empty.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20hosts">Link to this property</a>

status: <a href="https://developers.cloudflare.com/api/resources/ssl#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)">Status</a>

Status of certificate pack.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

type: "mh\_custom"or "managed\_hostname"or "sni\_custom"or 5 more

Type of certificate pack.

</summary>

One of the following:

"mh\_custom"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"managed\_hostname"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"sni\_custom"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"universal"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"advanced"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

"total\_tls"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205">Link to this property</a>

"keyless"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%206">Link to this property</a>

"legacy\_custom"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

certificate\_authority: optional "google"or "lets\_encrypt"or "ssl\_com"

Certificate Authority selected for the order. For information on any certificate authority specific details or restrictions <a href="https://developers.cloudflare.com/ssl/reference/certificate-authorities">see this page for more details</a>.

</summary>

One of the following:

"google"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%200">Link to this property</a>

"lets\_encrypt"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%201">Link to this property</a>

"ssl\_com"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority">Link to this property</a>

cloudflare\_branding: optional boolean

Whether or not to add Cloudflare Branding for the order. This will add a subdomain of sni.cloudflaressl.com as the Common Name if set to true.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20cloudflare_branding">Link to this property</a>

<details>

<summary>

dcv\_delegation\_records: optional array of object {cname, cname\_target, emails, 5 more }

DCV Delegation records for domain validation.

</summary>

cname: optional string

The CNAME record hostname for DCV delegation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20cname">Link to this property</a>

cname\_target: optional string

The CNAME record target value for DCV delegation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20cname_target">Link to this property</a>

emails: optional array of string

The set of email addresses that the certificate authority (CA) will use to complete domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20emails">Link to this property</a>

http\_body: optional string

The content that the certificate authority (CA) will expect to find at the http\_url during the domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20http_body">Link to this property</a>

http\_url: optional string

The url that will be checked during domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20http_url">Link to this property</a>

status: optional string

Status of the validation record.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

txt\_name: optional string

The hostname that the certificate authority (CA) will check for a TXT record during domain validation .

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20txt_name">Link to this property</a>

txt\_value: optional string

The TXT record that the certificate authority (CA) will check during domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20txt_value">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records">Link to this property</a>

primary\_certificate: optional string

Identifier of the primary certificate in a pack.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20primary_certificate">Link to this property</a>

<details>

<summary>

validation\_errors: optional array of object {message }

Domain validation errors that have been received by the certificate authority (CA).

</summary>

message: optional string

A domain validation error.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_errors">Link to this property</a>

<details>

<summary>

validation\_method: optional "txt"or "http"or "email"

Validation Method selected for the order.

</summary>

One of the following:

"txt"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_method%20%3E%20(member)%200">Link to this property</a>

"http"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_method%20%3E%20(member)%201">Link to this property</a>

"email"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_method%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_method">Link to this property</a>

<details>

<summary>

validation\_records: optional array of object {cname, cname\_target, emails, 5 more }

Certificates’ validation records.

</summary>

cname: optional string

The CNAME record hostname for DCV delegation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20cname">Link to this property</a>

cname\_target: optional string

The CNAME record target value for DCV delegation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20cname_target">Link to this property</a>

emails: optional array of string

The set of email addresses that the certificate authority (CA) will use to complete domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20emails">Link to this property</a>

http\_body: optional string

The content that the certificate authority (CA) will expect to find at the http\_url during the domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20http_body">Link to this property</a>

http\_url: optional string

The url that will be checked during domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20http_url">Link to this property</a>

status: optional string

Status of the validation record.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

txt\_name: optional string

The hostname that the certificate authority (CA) will check for a TXT record during domain validation .

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20txt_name">Link to this property</a>

txt\_value: optional string

The TXT record that the certificate authority (CA) will check during domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20txt_value">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20validation_records">Link to this property</a>

<details>

<summary>

validity\_days: optional 14or 30or 90or 365

Validity Days selected for the order.

</summary>

One of the following:

14

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20validity_days%20%3E%20(member)%200">Link to this property</a>

30

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20validity_days%20%3E%20(member)%201">Link to this property</a>

90

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20validity_days%20%3E%20(member)%202">Link to this property</a>

365

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20validity_days%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)%20%3E%20(property)%20validity_days">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_create_response%20%3E%20(schema)>)

<details>

<summary>

CertificatePackEditResponse object {id, certificates, hosts, 10 more }

A certificate pack with all its properties.

</summary>

id: string

The unique identifier for a certificate\_pack.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

<details>

<summary>

certificates: array of object {id, hosts, status, 9 more }

Array of certificates in this pack.

</summary>

id: string

Certificate identifier.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

hosts: array of string

Hostnames covered by this certificate.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20hosts">Link to this property</a>

status: string

Certificate status.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

bundle\_method: optional string

Certificate bundle method.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20bundle_method">Link to this property</a>

expires\_on: optional string

When the certificate from the authority expires.

formatdate-time

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20expires_on">Link to this property</a>

<details>

<summary>

geo\_restrictions: optional object {label }

Specify the region where your private key can be held locally.

</summary>

<details>

<summary>

label: optional "us"or "eu"or "highest\_security"

</summary>

One of the following:

"us"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20geo_restrictions%20%3E%20(property)%20label%20%3E%20(member)%200">Link to this property</a>

"eu"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20geo_restrictions%20%3E%20(property)%20label%20%3E%20(member)%201">Link to this property</a>

"highest\_security"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20geo_restrictions%20%3E%20(property)%20label%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20geo_restrictions%20%3E%20(property)%20label">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20geo_restrictions">Link to this property</a>

issuer: optional string

The certificate authority that issued the certificate.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20issuer">Link to this property</a>

modified\_on: optional string

When the certificate was last modified.

formatdate-time

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20modified_on">Link to this property</a>

priority: optional number

The order/priority in which the certificate will be used.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20priority">Link to this property</a>

signature: optional string

The type of hash used for the certificate.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20signature">Link to this property</a>

uploaded\_on: optional string

When the certificate was uploaded to Cloudflare.

formatdate-time

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20uploaded_on">Link to this property</a>

zone\_id: optional string

Identifier.

maxLength32

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificates%20%3E%20(items)%20%3E%20(property)%20zone_id">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificates">Link to this property</a>

hosts: array of <a href="https://developers.cloudflare.com/api/resources/ssl#(resource)%20ssl.certificate_packs%20%3E%20(model)%20host%20%3E%20(schema)">Host</a>

Comma separated list of valid host names for the certificate packs. Must contain the zone apex, may not contain more than 50 hosts, and may not be empty.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20hosts">Link to this property</a>

status: <a href="https://developers.cloudflare.com/api/resources/ssl#(resource)%20ssl.certificate_packs%20%3E%20(model)%20status%20%3E%20(schema)">Status</a>

Status of certificate pack.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

type: "mh\_custom"or "managed\_hostname"or "sni\_custom"or 5 more

Type of certificate pack.

</summary>

One of the following:

"mh\_custom"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"managed\_hostname"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"sni\_custom"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"universal"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"advanced"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

"total\_tls"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205">Link to this property</a>

"keyless"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%206">Link to this property</a>

"legacy\_custom"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%207">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

<details>

<summary>

certificate\_authority: optional "google"or "lets\_encrypt"or "ssl\_com"

Certificate Authority selected for the order. For information on any certificate authority specific details or restrictions <a href="https://developers.cloudflare.com/ssl/reference/certificate-authorities">see this page for more details</a>.

</summary>

One of the following:

"google"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%200">Link to this property</a>

"lets\_encrypt"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%201">Link to this property</a>

"ssl\_com"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20certificate_authority">Link to this property</a>

cloudflare\_branding: optional boolean

Whether or not to add Cloudflare Branding for the order. This will add a subdomain of sni.cloudflaressl.com as the Common Name if set to true.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20cloudflare_branding">Link to this property</a>

<details>

<summary>

dcv\_delegation\_records: optional array of object {cname, cname\_target, emails, 5 more }

DCV Delegation records for domain validation.

</summary>

cname: optional string

The CNAME record hostname for DCV delegation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20cname">Link to this property</a>

cname\_target: optional string

The CNAME record target value for DCV delegation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20cname_target">Link to this property</a>

emails: optional array of string

The set of email addresses that the certificate authority (CA) will use to complete domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20emails">Link to this property</a>

http\_body: optional string

The content that the certificate authority (CA) will expect to find at the http\_url during the domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20http_body">Link to this property</a>

http\_url: optional string

The url that will be checked during domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20http_url">Link to this property</a>

status: optional string

Status of the validation record.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

txt\_name: optional string

The hostname that the certificate authority (CA) will check for a TXT record during domain validation .

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20txt_name">Link to this property</a>

txt\_value: optional string

The TXT record that the certificate authority (CA) will check during domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records%20%3E%20(items)%20%3E%20(property)%20txt_value">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20dcv_delegation_records">Link to this property</a>

primary\_certificate: optional string

Identifier of the primary certificate in a pack.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20primary_certificate">Link to this property</a>

<details>

<summary>

validation\_errors: optional array of object {message }

Domain validation errors that have been received by the certificate authority (CA).

</summary>

message: optional string

A domain validation error.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_errors%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_errors">Link to this property</a>

<details>

<summary>

validation\_method: optional "txt"or "http"or "email"

Validation Method selected for the order.

</summary>

One of the following:

"txt"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_method%20%3E%20(member)%200">Link to this property</a>

"http"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_method%20%3E%20(member)%201">Link to this property</a>

"email"

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_method%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_method">Link to this property</a>

<details>

<summary>

validation\_records: optional array of object {cname, cname\_target, emails, 5 more }

Certificates’ validation records.

</summary>

cname: optional string

The CNAME record hostname for DCV delegation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20cname">Link to this property</a>

cname\_target: optional string

The CNAME record target value for DCV delegation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20cname_target">Link to this property</a>

emails: optional array of string

The set of email addresses that the certificate authority (CA) will use to complete domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20emails">Link to this property</a>

http\_body: optional string

The content that the certificate authority (CA) will expect to find at the http\_url during the domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20http_body">Link to this property</a>

http\_url: optional string

The url that will be checked during domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20http_url">Link to this property</a>

status: optional string

Status of the validation record.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

txt\_name: optional string

The hostname that the certificate authority (CA) will check for a TXT record during domain validation .

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20txt_name">Link to this property</a>

txt\_value: optional string

The TXT record that the certificate authority (CA) will check during domain validation.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_records%20%3E%20(items)%20%3E%20(property)%20txt_value">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20validation_records">Link to this property</a>

<details>

<summary>

validity\_days: optional 14or 30or 90or 365

Validity Days selected for the order.

</summary>

One of the following:

14

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20validity_days%20%3E%20(member)%200">Link to this property</a>

30

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20validity_days%20%3E%20(member)%201">Link to this property</a>

90

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20validity_days%20%3E%20(member)%202">Link to this property</a>

365

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20validity_days%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)%20%3E%20(property)%20validity_days">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_edit_response%20%3E%20(schema)>)

<details>

<summary>

CertificatePackDeleteResponse object {id }

</summary>

id: optional string

The unique identifier for a certificate\_pack.

<a href="#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ssl.certificate_packs%20%3E%20(model)%20certificate_pack_delete_response%20%3E%20(schema)>)

#### Certificate PacksQuota

##### [Get Certificate Pack Quotas](https://developers.cloudflare.com/api/resources/ssl/subresources/certificate_packs/subresources/quota/methods/get)

GET/zones/{zone\_id}/ssl/certificate\_packs/quota

##### ModelsExpand Collapse

<details>

<summary>

QuotaGetResponse object {advanced }

</summary>

<details>

<summary>

advanced: optional object {allocated, used }

</summary>

allocated: optional number

Quantity Allocated.

<a href="#(resource)%20ssl.certificate_packs.quota%20%3E%20(model)%20quota_get_response%20%3E%20(schema)%20%3E%20(property)%20advanced%20%3E%20(property)%20allocated">Link to this property</a>

used: optional number

Quantity Used.

<a href="#(resource)%20ssl.certificate_packs.quota%20%3E%20(model)%20quota_get_response%20%3E%20(schema)%20%3E%20(property)%20advanced%20%3E%20(property)%20used">Link to this property</a>

</details>

<a href="#(resource)%20ssl.certificate_packs.quota%20%3E%20(model)%20quota_get_response%20%3E%20(schema)%20%3E%20(property)%20advanced">Link to this property</a>

</details>

[Link to this property](<#(resource)%20ssl.certificate_packs.quota%20%3E%20(model)%20quota_get_response%20%3E%20(schema)>)