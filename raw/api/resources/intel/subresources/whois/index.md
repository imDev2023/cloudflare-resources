---
title: Whois
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Intel](https://developers.cloudflare.com/api/resources/intel)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Whois

##### [Get WHOIS Record](https://developers.cloudflare.com/api/resources/intel/subresources/whois/methods/get)

GET/accounts/{account\_id}/intel/whois

##### ModelsExpand Collapse

<details>

<summary>

Whois object {created\_date, domain, nameservers, 6 more }

</summary>

created\_date: optional string

formatdate

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois%20%3E%20(schema)%20%3E%20(property)%20created_date">Link to this property</a>

domain: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois%20%3E%20(schema)%20%3E%20(property)%20domain">Link to this property</a>

nameservers: optional array of string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois%20%3E%20(schema)%20%3E%20(property)%20nameservers">Link to this property</a>

registrant: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois%20%3E%20(schema)%20%3E%20(property)%20registrant">Link to this property</a>

registrant\_country: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois%20%3E%20(schema)%20%3E%20(property)%20registrant_country">Link to this property</a>

registrant\_email: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois%20%3E%20(schema)%20%3E%20(property)%20registrant_email">Link to this property</a>

registrant\_org: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois%20%3E%20(schema)%20%3E%20(property)%20registrant_org">Link to this property</a>

registrar: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois%20%3E%20(schema)%20%3E%20(property)%20registrar">Link to this property</a>

updated\_date: optional string

formatdate

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois%20%3E%20(schema)%20%3E%20(property)%20updated_date">Link to this property</a>

</details>

[Link to this property](<#(resource)%20intel.whois%20%3E%20(model)%20whois%20%3E%20(schema)>)

<details>

<summary>

WhoisGetResponse object {dnssec, domain, extension, 84 more }

</summary>

dnssec: boolean

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20dnssec">Link to this property</a>

domain: string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20domain">Link to this property</a>

extension: string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20extension">Link to this property</a>

found: boolean

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20found">Link to this property</a>

nameservers: array of string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20nameservers">Link to this property</a>

punycode: string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20punycode">Link to this property</a>

registrant: string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrant">Link to this property</a>

registrar: string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrar">Link to this property</a>

id: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

administrative\_city: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20administrative_city">Link to this property</a>

administrative\_country: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20administrative_country">Link to this property</a>

administrative\_email: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20administrative_email">Link to this property</a>

administrative\_fax: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20administrative_fax">Link to this property</a>

administrative\_fax\_ext: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20administrative_fax_ext">Link to this property</a>

administrative\_id: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20administrative_id">Link to this property</a>

administrative\_name: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20administrative_name">Link to this property</a>

administrative\_org: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20administrative_org">Link to this property</a>

administrative\_phone: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20administrative_phone">Link to this property</a>

administrative\_phone\_ext: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20administrative_phone_ext">Link to this property</a>

administrative\_postal\_code: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20administrative_postal_code">Link to this property</a>

administrative\_province: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20administrative_province">Link to this property</a>

administrative\_referral\_url: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20administrative_referral_url">Link to this property</a>

administrative\_street: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20administrative_street">Link to this property</a>

billing\_city: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20billing_city">Link to this property</a>

billing\_country: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20billing_country">Link to this property</a>

billing\_email: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20billing_email">Link to this property</a>

billing\_fax: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20billing_fax">Link to this property</a>

billing\_fax\_ext: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20billing_fax_ext">Link to this property</a>

billing\_id: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20billing_id">Link to this property</a>

billing\_name: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20billing_name">Link to this property</a>

billing\_org: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20billing_org">Link to this property</a>

billing\_phone: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20billing_phone">Link to this property</a>

billing\_phone\_ext: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20billing_phone_ext">Link to this property</a>

billing\_postal\_code: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20billing_postal_code">Link to this property</a>

billing\_province: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20billing_province">Link to this property</a>

billing\_referral\_url: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20billing_referral_url">Link to this property</a>

billing\_street: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20billing_street">Link to this property</a>

created\_date: optional string

formatdate-time

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20created_date">Link to this property</a>

created\_date\_raw: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20created_date_raw">Link to this property</a>

expiration\_date: optional string

formatdate-time

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20expiration_date">Link to this property</a>

expiration\_date\_raw: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20expiration_date_raw">Link to this property</a>

registrant\_city: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrant_city">Link to this property</a>

registrant\_country: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrant_country">Link to this property</a>

registrant\_email: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrant_email">Link to this property</a>

registrant\_fax: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrant_fax">Link to this property</a>

registrant\_fax\_ext: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrant_fax_ext">Link to this property</a>

registrant\_id: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrant_id">Link to this property</a>

registrant\_name: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrant_name">Link to this property</a>

registrant\_org: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrant_org">Link to this property</a>

registrant\_phone: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrant_phone">Link to this property</a>

registrant\_phone\_ext: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrant_phone_ext">Link to this property</a>

registrant\_postal\_code: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrant_postal_code">Link to this property</a>

registrant\_province: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrant_province">Link to this property</a>

registrant\_referral\_url: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrant_referral_url">Link to this property</a>

registrant\_street: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrant_street">Link to this property</a>

registrar\_city: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrar_city">Link to this property</a>

registrar\_country: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrar_country">Link to this property</a>

registrar\_email: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrar_email">Link to this property</a>

registrar\_fax: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrar_fax">Link to this property</a>

registrar\_fax\_ext: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrar_fax_ext">Link to this property</a>

registrar\_id: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrar_id">Link to this property</a>

registrar\_name: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrar_name">Link to this property</a>

registrar\_org: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrar_org">Link to this property</a>

registrar\_phone: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrar_phone">Link to this property</a>

registrar\_phone\_ext: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrar_phone_ext">Link to this property</a>

registrar\_postal\_code: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrar_postal_code">Link to this property</a>

registrar\_province: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrar_province">Link to this property</a>

registrar\_referral\_url: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrar_referral_url">Link to this property</a>

registrar\_street: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20registrar_street">Link to this property</a>

status: optional array of string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

technical\_city: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20technical_city">Link to this property</a>

technical\_country: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20technical_country">Link to this property</a>

technical\_email: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20technical_email">Link to this property</a>

technical\_fax: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20technical_fax">Link to this property</a>

technical\_fax\_ext: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20technical_fax_ext">Link to this property</a>

technical\_id: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20technical_id">Link to this property</a>

technical\_name: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20technical_name">Link to this property</a>

technical\_org: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20technical_org">Link to this property</a>

technical\_phone: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20technical_phone">Link to this property</a>

technical\_phone\_ext: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20technical_phone_ext">Link to this property</a>

technical\_postal\_code: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20technical_postal_code">Link to this property</a>

technical\_province: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20technical_province">Link to this property</a>

technical\_referral\_url: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20technical_referral_url">Link to this property</a>

technical\_street: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20technical_street">Link to this property</a>

updated\_date: optional string

formatdate-time

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20updated_date">Link to this property</a>

updated\_date\_raw: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20updated_date_raw">Link to this property</a>

whois\_server: optional string

<a href="#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)%20%3E%20(property)%20whois_server">Link to this property</a>

</details>

[Link to this property](<#(resource)%20intel.whois%20%3E%20(model)%20whois_get_response%20%3E%20(schema)>)