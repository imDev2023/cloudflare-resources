---
title: Zsk
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[DNS](https://developers.cloudflare.com/api/resources/dns)

[DNSSEC](https://developers.cloudflare.com/api/resources/dns/subresources/dnssec)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Zsk

##### [List DNSSEC ZSKs](https://developers.cloudflare.com/api/resources/dns/subresources/dnssec/subresources/zsk/methods/list)

GET/zones/{zone\_id}/dnssec/zsk

##### ModelsExpand Collapse

<details>

<summary>

ZskListResponse object {DNSKEY, Location, Name, 2 more }

</summary>

<details>

<summary>

DNSKEY: optional object {Algorithm, Flags, Hdr, 2 more }

</summary>

Algorithm: optional number

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20DNSKEY%20%3E%20(property)%20Algorithm">Link to this property</a>

Flags: optional number

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20DNSKEY%20%3E%20(property)%20Flags">Link to this property</a>

<details>

<summary>

Hdr: optional object {Class, Name, Rdlength, 2 more }

</summary>

Class: optional number

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20DNSKEY%20%3E%20(property)%20Hdr%20%3E%20(property)%20Class">Link to this property</a>

Name: optional string

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20DNSKEY%20%3E%20(property)%20Hdr%20%3E%20(property)%20Name">Link to this property</a>

Rdlength: optional number

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20DNSKEY%20%3E%20(property)%20Hdr%20%3E%20(property)%20Rdlength">Link to this property</a>

Rrtype: optional number

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20DNSKEY%20%3E%20(property)%20Hdr%20%3E%20(property)%20Rrtype">Link to this property</a>

Ttl: optional number

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20DNSKEY%20%3E%20(property)%20Hdr%20%3E%20(property)%20Ttl">Link to this property</a>

</details>

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20DNSKEY%20%3E%20(property)%20Hdr">Link to this property</a>

Protocol: optional number

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20DNSKEY%20%3E%20(property)%20Protocol">Link to this property</a>

PublicKey: optional string

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20DNSKEY%20%3E%20(property)%20PublicKey">Link to this property</a>

</details>

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20DNSKEY">Link to this property</a>

<details>

<summary>

Location: optional "database"or "vault"

Storage backend where the DNSSEC key material is stored.

</summary>

One of the following:

"database"

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20Location%20%3E%20(member)%200">Link to this property</a>

"vault"

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20Location%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20Location">Link to this property</a>

Name: optional string

Internal key name for the ZSK.

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20Name">Link to this property</a>

<details>

<summary>

SigningKey: optional object {kek, privkey, pubkey }

</summary>

kek: optional string

Key encryption key name used to encrypt the private key.

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20SigningKey%20%3E%20(property)%20kek">Link to this property</a>

privkey: optional string

Encrypted private key material for the signing key.

formatbyte

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20SigningKey%20%3E%20(property)%20privkey">Link to this property</a>

pubkey: optional string

Public key content associated with the signing key.

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20SigningKey%20%3E%20(property)%20pubkey">Link to this property</a>

</details>

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20SigningKey">Link to this property</a>

<details>

<summary>

Tag: optional "active"or "publish"or "external"or 3 more

Lifecycle state tag attached to the DNSSEC key.

</summary>

One of the following:

"active"

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20Tag%20%3E%20(member)%200">Link to this property</a>

"publish"

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20Tag%20%3E%20(member)%201">Link to this property</a>

"external"

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20Tag%20%3E%20(member)%202">Link to this property</a>

"retired"

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20Tag%20%3E%20(member)%203">Link to this property</a>

"revoked"

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20Tag%20%3E%20(member)%204">Link to this property</a>

"removed"

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20Tag%20%3E%20(member)%205">Link to this property</a>

</details>

<a href="#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)%20%3E%20(property)%20Tag">Link to this property</a>

</details>

[Link to this property](<#(resource)%20dns.dnssec.zsk%20%3E%20(model)%20zsk_list_response%20%3E%20(schema)>)