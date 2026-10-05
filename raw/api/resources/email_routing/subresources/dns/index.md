---
title: DNS
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Email Routing](https://developers.cloudflare.com/api/resources/email_routing)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# DNS

##### [Email Routing - DNS settings](https://developers.cloudflare.com/api/resources/email_routing/subresources/dns/methods/get)

GET/zones/{zone\_id}/email/routing/dns

##### [Enable Email Routing](https://developers.cloudflare.com/api/resources/email_routing/subresources/dns/methods/create)

POST/zones/{zone\_id}/email/routing/dns

##### [Unlock Email Routing DNS records](https://developers.cloudflare.com/api/resources/email_routing/subresources/dns/methods/edit)

PATCH/zones/{zone\_id}/email/routing/dns

##### [Disable Email Routing](https://developers.cloudflare.com/api/resources/email_routing/subresources/dns/methods/delete)

DELETE/zones/{zone\_id}/email/routing/dns

##### ModelsExpand Collapse

<details>

<summary>

DNSRecord object {content, name, priority, 2 more }

List of records needed to enable an Email Routing zone.

</summary>

content: optional string

DNS record content.

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20content">Link to this property</a>

name: optional string

DNS record name (or @ for the zone apex).

maxLength255

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

priority: optional number

Required for MX, SRV and URI records. Unused by other record types. Records with lower priorities are preferred.

maximum65535

minimum0

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20priority">Link to this property</a>

<details>

<summary>

ttl: optional numberor 1

Time to live, in seconds, of the DNS record. Must be between 60 and 86400, or 1 for ‘automatic’.

</summary>

One of the following:

number

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20ttl%20%3E%20(variant)%200">Link to this property</a>

1

Time to live, in seconds, of the DNS record. Must be between 60 and 86400, or 1 for ‘automatic’.

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20ttl%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20ttl">Link to this property</a>

<details>

<summary>

type: optional "A"or "AAAA"or "CNAME"or 15 more

DNS record type.

</summary>

One of the following:

"A"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"AAAA"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"CNAME"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"HTTPS"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"TXT"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

"SRV"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205">Link to this property</a>

"LOC"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%206">Link to this property</a>

"MX"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%207">Link to this property</a>

"NS"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%208">Link to this property</a>

"CERT"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%209">Link to this property</a>

"DNSKEY"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2010">Link to this property</a>

"DS"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2011">Link to this property</a>

"NAPTR"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2012">Link to this property</a>

"SMIMEA"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2013">Link to this property</a>

"SSHFP"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2014">Link to this property</a>

"SVCB"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2015">Link to this property</a>

"TLSA"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2016">Link to this property</a>

"URI"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2017">Link to this property</a>

</details>

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)>)

<details>

<summary>

DNSGetResponse = array of <a href="https://developers.cloudflare.com/api/resources/email_routing#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)">DNSRecord</a> { content, name, priority, 2 more }

</summary>

content: optional string

DNS record content.

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20content">Link to this property</a>

name: optional string

DNS record name (or @ for the zone apex).

maxLength255

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

priority: optional number

Required for MX, SRV and URI records. Unused by other record types. Records with lower priorities are preferred.

maximum65535

minimum0

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20priority">Link to this property</a>

<details>

<summary>

ttl: optional numberor 1

Time to live, in seconds, of the DNS record. Must be between 60 and 86400, or 1 for ‘automatic’.

</summary>

One of the following:

number

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20ttl%20%3E%20(variant)%200">Link to this property</a>

1

Time to live, in seconds, of the DNS record. Must be between 60 and 86400, or 1 for ‘automatic’.

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20ttl%20%3E%20(variant)%201">Link to this property</a>

</details>

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20ttl">Link to this property</a>

<details>

<summary>

type: optional "A"or "AAAA"or "CNAME"or 15 more

DNS record type.

</summary>

One of the following:

"A"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"AAAA"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"CNAME"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

"HTTPS"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%203">Link to this property</a>

"TXT"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%204">Link to this property</a>

"SRV"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%205">Link to this property</a>

"LOC"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%206">Link to this property</a>

"MX"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%207">Link to this property</a>

"NS"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%208">Link to this property</a>

"CERT"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%209">Link to this property</a>

"DNSKEY"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2010">Link to this property</a>

"DS"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2011">Link to this property</a>

"NAPTR"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2012">Link to this property</a>

"SMIMEA"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2013">Link to this property</a>

"SSHFP"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2014">Link to this property</a>

"SVCB"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2015">Link to this property</a>

"TLSA"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2016">Link to this property</a>

"URI"

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type%20%3E%20(member)%2017">Link to this property</a>

</details>

<a href="#(resource)%20email_routing.dns%20%3E%20(model)%20dns_record%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_routing.dns%20%3E%20(model)%20dns_get_response%20%3E%20(schema)>)