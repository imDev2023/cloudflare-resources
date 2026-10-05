---
title: Origin CA Certificates
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Origin CA Certificates

##### [List Certificates](https://developers.cloudflare.com/api/resources/origin_ca_certificates/methods/list)

GET/certificates

##### [Get Certificate](https://developers.cloudflare.com/api/resources/origin_ca_certificates/methods/get)

GET/certificates/{certificate\_id}

##### [Create Certificate](https://developers.cloudflare.com/api/resources/origin_ca_certificates/methods/create)

POST/certificates

##### [Revoke Certificate](https://developers.cloudflare.com/api/resources/origin_ca_certificates/methods/delete)

DELETE/certificates/{certificate\_id}

##### ModelsExpand Collapse

<details>

<summary>

OriginCACertificate object {csr, hostnames, request\_type, 4 more }

</summary>

csr: string

The Certificate Signing Request (CSR). Must be newline-encoded.

<a href="#(resource)%20origin_ca_certificates%20%3E%20(model)%20origin_ca_certificate%20%3E%20(schema)%20%3E%20(property)%20csr">Link to this property</a>

hostnames: array of string

Array of hostnames or wildcard names bound to the certificate. Hostnames must be fully qualified domain names (FQDNs) belonging to zones on your account (e.g., <code>example.com</code> or <code>sub.example.com</code>). Wildcards are supported only as a <code>*.</code> prefix for a single level (e.g., <code>*.example.com</code>). Double wildcards (<code>*.*.example.com</code>) and interior wildcards (<code>foo.*.example.com</code>) are not allowed. The wildcard suffix must be a multi-label domain (<code>*.example.com</code> is valid, but <code>*.com</code> is not). Unicode/IDN hostnames are accepted and automatically converted to punycode.

<a href="#(resource)%20origin_ca_certificates%20%3E%20(model)%20origin_ca_certificate%20%3E%20(schema)%20%3E%20(property)%20hostnames">Link to this property</a>

request\_type: <a href="https://developers.cloudflare.com/api/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20certificate_request_type%20%3E%20(schema)">CertificateRequestType</a>

Signature type desired on certificate (“origin-rsa” (rsa), “origin-ecc” (ecdsa), or “keyless-certificate” (for Keyless SSL servers).

<a href="#(resource)%20origin_ca_certificates%20%3E%20(model)%20origin_ca_certificate%20%3E%20(schema)%20%3E%20(property)%20request_type">Link to this property</a>

requested\_validity: <a href="https://developers.cloudflare.com/api/resources/ssl#(resource)%20ssl.certificate_packs%20%3E%20(model)%20request_validity%20%3E%20(schema)">RequestValidity</a>

The number of days for which the certificate should be valid.

<a href="#(resource)%20origin_ca_certificates%20%3E%20(model)%20origin_ca_certificate%20%3E%20(schema)%20%3E%20(property)%20requested_validity">Link to this property</a>

id: optional string

The x509 serial number of the Origin CA certificate.

<a href="#(resource)%20origin_ca_certificates%20%3E%20(model)%20origin_ca_certificate%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

certificate: optional string

The Origin CA certificate. Will be newline-encoded.

<a href="#(resource)%20origin_ca_certificates%20%3E%20(model)%20origin_ca_certificate%20%3E%20(schema)%20%3E%20(property)%20certificate">Link to this property</a>

expires\_on: optional string

When the certificate will expire.

<a href="#(resource)%20origin_ca_certificates%20%3E%20(model)%20origin_ca_certificate%20%3E%20(schema)%20%3E%20(property)%20expires_on">Link to this property</a>

</details>

[Link to this property](<#(resource)%20origin_ca_certificates%20%3E%20(model)%20origin_ca_certificate%20%3E%20(schema)>)

<details>

<summary>

OriginCACertificateDeleteResponse object {id, revoked\_at }

</summary>

id: optional string

The x509 serial number of the Origin CA certificate.

<a href="#(resource)%20origin_ca_certificates%20%3E%20(model)%20origin_ca_certificate_delete_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

revoked\_at: optional string

When the certificate was revoked.

formatdate-time

<a href="#(resource)%20origin_ca_certificates%20%3E%20(model)%20origin_ca_certificate_delete_response%20%3E%20(schema)%20%3E%20(property)%20revoked_at">Link to this property</a>

</details>

[Link to this property](<#(resource)%20origin_ca_certificates%20%3E%20(model)%20origin_ca_certificate_delete_response%20%3E%20(schema)>)