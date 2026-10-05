---
title: DMARC Reports
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Email Auth](https://developers.cloudflare.com/api/resources/email_auth)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# DMARC Reports

##### [Get DMARC Report Status](https://developers.cloudflare.com/api/resources/email_auth/subresources/dmarc_reports/methods/get)

GET/zones/{zone\_id}/email/auth/dmarc-reports

##### [Configure DMARC Reports](https://developers.cloudflare.com/api/resources/email_auth/subresources/dmarc_reports/methods/edit)

PATCH/zones/{zone\_id}/email/auth/dmarc-reports

##### ModelsExpand Collapse

<details>

<summary>

DMARCReportGetResponse object {approved\_sources, created, created\_at, 9 more }

Response for GET/PATCH /dmarc-reports

</summary>

<details>

<summary>

approved\_sources: optional array of object {created, created\_at, domain, 6 more }

List of approved sending sources (omitted when empty)

</summary>

Deprecatedcreated: optional string

Use <code>created_at</code> instead.

Deprecated, use created\_at

formatdate-time

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20approved_sources%20%3E%20(items)%20%3E%20(property)%20created">Link to this property</a>

created\_at: optional string

Creation timestamp

formatdate-time

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20approved_sources%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

domain: optional string

The source domain

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20approved_sources%20%3E%20(items)%20%3E%20(property)%20domain">Link to this property</a>

ips: optional array of string

Resolved IP addresses from SPF

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20approved_sources%20%3E%20(items)%20%3E%20(property)%20ips">Link to this property</a>

Deprecatedmodified: optional string

Use <code>modified_at</code> instead.

Deprecated, use modified\_at

formatdate-time

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20approved_sources%20%3E%20(items)%20%3E%20(property)%20modified">Link to this property</a>

modified\_at: optional string

Last modification timestamp

formatdate-time

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20approved_sources%20%3E%20(items)%20%3E%20(property)%20modified_at">Link to this property</a>

name: optional string

Source name (typically same as domain)

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20approved_sources%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

slug: optional string

URL-friendly identifier

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20approved_sources%20%3E%20(items)%20%3E%20(property)%20slug">Link to this property</a>

tag: optional string

Source UUID

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20approved_sources%20%3E%20(items)%20%3E%20(property)%20tag">Link to this property</a>

</details>

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20approved_sources">Link to this property</a>

Deprecatedcreated: optional string

Use <code>created_at</code> instead.

Deprecated, use created\_at

formatdate-time

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

created\_at: optional string

Creation timestamp

formatdate-time

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

enabled: optional boolean

Whether DMARC reports are enabled

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

Deprecatedmodified: optional string

Use <code>modified_at</code> instead.

Deprecated, use modified\_at

formatdate-time

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20modified">Link to this property</a>

modified\_at: optional string

Last modification timestamp

formatdate-time

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

<details>

<summary>

records: optional object {bimi\_records, cname\_dkim\_records, cname\_dmarc\_records, 5 more }

Live DNS records for the zone, grouped by type

</summary>

<details>

<summary>

bimi\_records: optional array of object {id, content, name, 3 more }

BIMI TXT records

</summary>

id: optional string

DNS record ID

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20bimi_records%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

content: optional string

Record content

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20bimi_records%20%3E%20(items)%20%3E%20(property)%20content">Link to this property</a>

name: optional string

DNS record name

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20bimi_records%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

resolved: optional array of string

For a CNAME record, the TXT content(s) found by following the CNAME chain to its target. An empty array means the chain was resolved but nothing usable was found there; omitted/null means resolution was not attempted for this record (always the case for non-CNAME entries). A CNAME chain that terminates in more than one TXT value at the target yields multiple entries. Populated on entries in cname\_dmarc\_records, cname\_spf\_records, and cname\_dkim\_records.

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20bimi_records%20%3E%20(items)%20%3E%20(property)%20resolved">Link to this property</a>

ttl: optional number

Time to live in seconds

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20bimi_records%20%3E%20(items)%20%3E%20(property)%20ttl">Link to this property</a>

type: optional string

Record type

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20bimi_records%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20bimi_records">Link to this property</a>

<details>

<summary>

cname\_dkim\_records: optional array of object {id, content, name, 3 more }

CNAME records for DKIM selectors. Each selector is resolved independently; when a selector’s CNAME resolves to a DKIM TXT record, the API returns that record’s content in the <code>resolved</code> field of the corresponding entry.

</summary>

id: optional string

DNS record ID

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dkim_records%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

content: optional string

Record content

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dkim_records%20%3E%20(items)%20%3E%20(property)%20content">Link to this property</a>

name: optional string

DNS record name

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dkim_records%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

resolved: optional array of string

For a CNAME record, the TXT content(s) found by following the CNAME chain to its target. An empty array means the chain was resolved but nothing usable was found there; omitted/null means resolution was not attempted for this record (always the case for non-CNAME entries). A CNAME chain that terminates in more than one TXT value at the target yields multiple entries. Populated on entries in cname\_dmarc\_records, cname\_spf\_records, and cname\_dkim\_records.

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dkim_records%20%3E%20(items)%20%3E%20(property)%20resolved">Link to this property</a>

ttl: optional number

Time to live in seconds

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dkim_records%20%3E%20(items)%20%3E%20(property)%20ttl">Link to this property</a>

type: optional string

Record type

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dkim_records%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dkim_records">Link to this property</a>

<details>

<summary>

cname\_dmarc\_records: optional array of object {id, content, name, 3 more }

CNAME records at \_dmarc. When such a CNAME resolves to a DMARC TXT record, the API returns that record’s content in the <code>resolved</code> field of the corresponding entry.

</summary>

id: optional string

DNS record ID

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dmarc_records%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

content: optional string

Record content

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dmarc_records%20%3E%20(items)%20%3E%20(property)%20content">Link to this property</a>

name: optional string

DNS record name

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dmarc_records%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

resolved: optional array of string

For a CNAME record, the TXT content(s) found by following the CNAME chain to its target. An empty array means the chain was resolved but nothing usable was found there; omitted/null means resolution was not attempted for this record (always the case for non-CNAME entries). A CNAME chain that terminates in more than one TXT value at the target yields multiple entries. Populated on entries in cname\_dmarc\_records, cname\_spf\_records, and cname\_dkim\_records.

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dmarc_records%20%3E%20(items)%20%3E%20(property)%20resolved">Link to this property</a>

ttl: optional number

Time to live in seconds

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dmarc_records%20%3E%20(items)%20%3E%20(property)%20ttl">Link to this property</a>

type: optional string

Record type

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dmarc_records%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dmarc_records">Link to this property</a>

<details>

<summary>

cname\_spf\_records: optional array of object {id, content, name, 3 more }

CNAME records at the zone apex. When such a CNAME resolves to an SPF TXT record, the API returns that record’s content in the <code>resolved</code> field of the corresponding entry.

</summary>

id: optional string

DNS record ID

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_spf_records%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

content: optional string

Record content

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_spf_records%20%3E%20(items)%20%3E%20(property)%20content">Link to this property</a>

name: optional string

DNS record name

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_spf_records%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

resolved: optional array of string

For a CNAME record, the TXT content(s) found by following the CNAME chain to its target. An empty array means the chain was resolved but nothing usable was found there; omitted/null means resolution was not attempted for this record (always the case for non-CNAME entries). A CNAME chain that terminates in more than one TXT value at the target yields multiple entries. Populated on entries in cname\_dmarc\_records, cname\_spf\_records, and cname\_dkim\_records.

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_spf_records%20%3E%20(items)%20%3E%20(property)%20resolved">Link to this property</a>

ttl: optional number

Time to live in seconds

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_spf_records%20%3E%20(items)%20%3E%20(property)%20ttl">Link to this property</a>

type: optional string

Record type

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_spf_records%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_spf_records">Link to this property</a>

<details>

<summary>

dkim\_records: optional array of object {id, content, name, 3 more }

DKIM TXT records

</summary>

id: optional string

DNS record ID

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dkim_records%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

content: optional string

Record content

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dkim_records%20%3E%20(items)%20%3E%20(property)%20content">Link to this property</a>

name: optional string

DNS record name

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dkim_records%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

resolved: optional array of string

For a CNAME record, the TXT content(s) found by following the CNAME chain to its target. An empty array means the chain was resolved but nothing usable was found there; omitted/null means resolution was not attempted for this record (always the case for non-CNAME entries). A CNAME chain that terminates in more than one TXT value at the target yields multiple entries. Populated on entries in cname\_dmarc\_records, cname\_spf\_records, and cname\_dkim\_records.

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dkim_records%20%3E%20(items)%20%3E%20(property)%20resolved">Link to this property</a>

ttl: optional number

Time to live in seconds

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dkim_records%20%3E%20(items)%20%3E%20(property)%20ttl">Link to this property</a>

type: optional string

Record type

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dkim_records%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dkim_records">Link to this property</a>

<details>

<summary>

dmarc\_records: optional array of object {id, content, name, 3 more }

DMARC TXT records

</summary>

id: optional string

DNS record ID

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dmarc_records%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

content: optional string

Record content

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dmarc_records%20%3E%20(items)%20%3E%20(property)%20content">Link to this property</a>

name: optional string

DNS record name

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dmarc_records%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

resolved: optional array of string

For a CNAME record, the TXT content(s) found by following the CNAME chain to its target. An empty array means the chain was resolved but nothing usable was found there; omitted/null means resolution was not attempted for this record (always the case for non-CNAME entries). A CNAME chain that terminates in more than one TXT value at the target yields multiple entries. Populated on entries in cname\_dmarc\_records, cname\_spf\_records, and cname\_dkim\_records.

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dmarc_records%20%3E%20(items)%20%3E%20(property)%20resolved">Link to this property</a>

ttl: optional number

Time to live in seconds

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dmarc_records%20%3E%20(items)%20%3E%20(property)%20ttl">Link to this property</a>

type: optional string

Record type

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dmarc_records%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dmarc_records">Link to this property</a>

<details>

<summary>

Deprecatedresolved\_dmarc\_records: optional array of object {content, name }

Use the <code>resolved</code> field on the corresponding entry in cname\_dmarc\_records instead.

DMARC records that a recursive lookup of \_dmarc.{zone} returned. The API populates this only when the zone lacks a DMARC TXT record of its own, which usually means a CNAME delegates DMARC to another zone.

</summary>

content: optional string

The TXT record value. The API joins all character-strings into a single string.

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20resolved_dmarc_records%20%3E%20(items)%20%3E%20(property)%20content">Link to this property</a>

name: optional string

The name the API queried.

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20resolved_dmarc_records%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20resolved_dmarc_records">Link to this property</a>

<details>

<summary>

spf\_records: optional array of object {id, content, name, 3 more }

SPF TXT records

</summary>

id: optional string

DNS record ID

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20spf_records%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

content: optional string

Record content

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20spf_records%20%3E%20(items)%20%3E%20(property)%20content">Link to this property</a>

name: optional string

DNS record name

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20spf_records%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

resolved: optional array of string

For a CNAME record, the TXT content(s) found by following the CNAME chain to its target. An empty array means the chain was resolved but nothing usable was found there; omitted/null means resolution was not attempted for this record (always the case for non-CNAME entries). A CNAME chain that terminates in more than one TXT value at the target yields multiple entries. Populated on entries in cname\_dmarc\_records, cname\_spf\_records, and cname\_dkim\_records.

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20spf_records%20%3E%20(items)%20%3E%20(property)%20resolved">Link to this property</a>

ttl: optional number

Time to live in seconds

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20spf_records%20%3E%20(items)%20%3E%20(property)%20ttl">Link to this property</a>

type: optional string

Record type

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20spf_records%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20spf_records">Link to this property</a>

</details>

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20records">Link to this property</a>

rua\_prefix: optional string

Prefix for DMARC RUA addresses (32-char hex string)

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20rua_prefix">Link to this property</a>

skip\_wizard: optional boolean

Whether to skip the setup wizard

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20skip_wizard">Link to this property</a>

<details>

<summary>

status: optional "missing-dmarc-report"or "multiple-dmarc-reports"or "missing-dmarc-rua"or 2 more

DMARC configuration status. The API omits this field when DMARC is correctly configured. If the zone lacks a DMARC TXT record of its own, the API resolves \_dmarc.{zone} recursively and evaluates whatever that lookup returns. A CNAME at \_dmarc.{zone} that points to a valid DMARC record is therefore healthy; the cname-on-dmarc-record value means the CNAME resolves to no DMARC record at all.

</summary>

One of the following:

"missing-dmarc-report"

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"multiple-dmarc-reports"

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"missing-dmarc-rua"

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"cname-on-dmarc-record"

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"unauthorized-reporting-domain"

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

Deprecatedtag: optional string

Use <code>zone_id</code> instead.

Use <code>zone_id</code> instead

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20tag">Link to this property</a>

zone\_id: optional string

Zone identifier

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)%20%3E%20(property)%20zone_id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_get_response%20%3E%20(schema)>)

<details>

<summary>

DMARCReportEditResponse object {approved\_sources, created, created\_at, 9 more }

Response for GET/PATCH /dmarc-reports

</summary>

<details>

<summary>

approved\_sources: optional array of object {created, created\_at, domain, 6 more }

List of approved sending sources (omitted when empty)

</summary>

Deprecatedcreated: optional string

Use <code>created_at</code> instead.

Deprecated, use created\_at

formatdate-time

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20approved_sources%20%3E%20(items)%20%3E%20(property)%20created">Link to this property</a>

created\_at: optional string

Creation timestamp

formatdate-time

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20approved_sources%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

domain: optional string

The source domain

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20approved_sources%20%3E%20(items)%20%3E%20(property)%20domain">Link to this property</a>

ips: optional array of string

Resolved IP addresses from SPF

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20approved_sources%20%3E%20(items)%20%3E%20(property)%20ips">Link to this property</a>

Deprecatedmodified: optional string

Use <code>modified_at</code> instead.

Deprecated, use modified\_at

formatdate-time

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20approved_sources%20%3E%20(items)%20%3E%20(property)%20modified">Link to this property</a>

modified\_at: optional string

Last modification timestamp

formatdate-time

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20approved_sources%20%3E%20(items)%20%3E%20(property)%20modified_at">Link to this property</a>

name: optional string

Source name (typically same as domain)

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20approved_sources%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

slug: optional string

URL-friendly identifier

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20approved_sources%20%3E%20(items)%20%3E%20(property)%20slug">Link to this property</a>

tag: optional string

Source UUID

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20approved_sources%20%3E%20(items)%20%3E%20(property)%20tag">Link to this property</a>

</details>

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20approved_sources">Link to this property</a>

Deprecatedcreated: optional string

Use <code>created_at</code> instead.

Deprecated, use created\_at

formatdate-time

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

created\_at: optional string

Creation timestamp

formatdate-time

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20created_at">Link to this property</a>

enabled: optional boolean

Whether DMARC reports are enabled

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

Deprecatedmodified: optional string

Use <code>modified_at</code> instead.

Deprecated, use modified\_at

formatdate-time

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20modified">Link to this property</a>

modified\_at: optional string

Last modification timestamp

formatdate-time

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20modified_at">Link to this property</a>

<details>

<summary>

records: optional object {bimi\_records, cname\_dkim\_records, cname\_dmarc\_records, 5 more }

Live DNS records for the zone, grouped by type

</summary>

<details>

<summary>

bimi\_records: optional array of object {id, content, name, 3 more }

BIMI TXT records

</summary>

id: optional string

DNS record ID

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20bimi_records%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

content: optional string

Record content

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20bimi_records%20%3E%20(items)%20%3E%20(property)%20content">Link to this property</a>

name: optional string

DNS record name

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20bimi_records%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

resolved: optional array of string

For a CNAME record, the TXT content(s) found by following the CNAME chain to its target. An empty array means the chain was resolved but nothing usable was found there; omitted/null means resolution was not attempted for this record (always the case for non-CNAME entries). A CNAME chain that terminates in more than one TXT value at the target yields multiple entries. Populated on entries in cname\_dmarc\_records, cname\_spf\_records, and cname\_dkim\_records.

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20bimi_records%20%3E%20(items)%20%3E%20(property)%20resolved">Link to this property</a>

ttl: optional number

Time to live in seconds

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20bimi_records%20%3E%20(items)%20%3E%20(property)%20ttl">Link to this property</a>

type: optional string

Record type

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20bimi_records%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20bimi_records">Link to this property</a>

<details>

<summary>

cname\_dkim\_records: optional array of object {id, content, name, 3 more }

CNAME records for DKIM selectors. Each selector is resolved independently; when a selector’s CNAME resolves to a DKIM TXT record, the API returns that record’s content in the <code>resolved</code> field of the corresponding entry.

</summary>

id: optional string

DNS record ID

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dkim_records%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

content: optional string

Record content

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dkim_records%20%3E%20(items)%20%3E%20(property)%20content">Link to this property</a>

name: optional string

DNS record name

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dkim_records%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

resolved: optional array of string

For a CNAME record, the TXT content(s) found by following the CNAME chain to its target. An empty array means the chain was resolved but nothing usable was found there; omitted/null means resolution was not attempted for this record (always the case for non-CNAME entries). A CNAME chain that terminates in more than one TXT value at the target yields multiple entries. Populated on entries in cname\_dmarc\_records, cname\_spf\_records, and cname\_dkim\_records.

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dkim_records%20%3E%20(items)%20%3E%20(property)%20resolved">Link to this property</a>

ttl: optional number

Time to live in seconds

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dkim_records%20%3E%20(items)%20%3E%20(property)%20ttl">Link to this property</a>

type: optional string

Record type

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dkim_records%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dkim_records">Link to this property</a>

<details>

<summary>

cname\_dmarc\_records: optional array of object {id, content, name, 3 more }

CNAME records at \_dmarc. When such a CNAME resolves to a DMARC TXT record, the API returns that record’s content in the <code>resolved</code> field of the corresponding entry.

</summary>

id: optional string

DNS record ID

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dmarc_records%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

content: optional string

Record content

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dmarc_records%20%3E%20(items)%20%3E%20(property)%20content">Link to this property</a>

name: optional string

DNS record name

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dmarc_records%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

resolved: optional array of string

For a CNAME record, the TXT content(s) found by following the CNAME chain to its target. An empty array means the chain was resolved but nothing usable was found there; omitted/null means resolution was not attempted for this record (always the case for non-CNAME entries). A CNAME chain that terminates in more than one TXT value at the target yields multiple entries. Populated on entries in cname\_dmarc\_records, cname\_spf\_records, and cname\_dkim\_records.

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dmarc_records%20%3E%20(items)%20%3E%20(property)%20resolved">Link to this property</a>

ttl: optional number

Time to live in seconds

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dmarc_records%20%3E%20(items)%20%3E%20(property)%20ttl">Link to this property</a>

type: optional string

Record type

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dmarc_records%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_dmarc_records">Link to this property</a>

<details>

<summary>

cname\_spf\_records: optional array of object {id, content, name, 3 more }

CNAME records at the zone apex. When such a CNAME resolves to an SPF TXT record, the API returns that record’s content in the <code>resolved</code> field of the corresponding entry.

</summary>

id: optional string

DNS record ID

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_spf_records%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

content: optional string

Record content

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_spf_records%20%3E%20(items)%20%3E%20(property)%20content">Link to this property</a>

name: optional string

DNS record name

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_spf_records%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

resolved: optional array of string

For a CNAME record, the TXT content(s) found by following the CNAME chain to its target. An empty array means the chain was resolved but nothing usable was found there; omitted/null means resolution was not attempted for this record (always the case for non-CNAME entries). A CNAME chain that terminates in more than one TXT value at the target yields multiple entries. Populated on entries in cname\_dmarc\_records, cname\_spf\_records, and cname\_dkim\_records.

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_spf_records%20%3E%20(items)%20%3E%20(property)%20resolved">Link to this property</a>

ttl: optional number

Time to live in seconds

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_spf_records%20%3E%20(items)%20%3E%20(property)%20ttl">Link to this property</a>

type: optional string

Record type

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_spf_records%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20cname_spf_records">Link to this property</a>

<details>

<summary>

dkim\_records: optional array of object {id, content, name, 3 more }

DKIM TXT records

</summary>

id: optional string

DNS record ID

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dkim_records%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

content: optional string

Record content

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dkim_records%20%3E%20(items)%20%3E%20(property)%20content">Link to this property</a>

name: optional string

DNS record name

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dkim_records%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

resolved: optional array of string

For a CNAME record, the TXT content(s) found by following the CNAME chain to its target. An empty array means the chain was resolved but nothing usable was found there; omitted/null means resolution was not attempted for this record (always the case for non-CNAME entries). A CNAME chain that terminates in more than one TXT value at the target yields multiple entries. Populated on entries in cname\_dmarc\_records, cname\_spf\_records, and cname\_dkim\_records.

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dkim_records%20%3E%20(items)%20%3E%20(property)%20resolved">Link to this property</a>

ttl: optional number

Time to live in seconds

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dkim_records%20%3E%20(items)%20%3E%20(property)%20ttl">Link to this property</a>

type: optional string

Record type

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dkim_records%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dkim_records">Link to this property</a>

<details>

<summary>

dmarc\_records: optional array of object {id, content, name, 3 more }

DMARC TXT records

</summary>

id: optional string

DNS record ID

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dmarc_records%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

content: optional string

Record content

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dmarc_records%20%3E%20(items)%20%3E%20(property)%20content">Link to this property</a>

name: optional string

DNS record name

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dmarc_records%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

resolved: optional array of string

For a CNAME record, the TXT content(s) found by following the CNAME chain to its target. An empty array means the chain was resolved but nothing usable was found there; omitted/null means resolution was not attempted for this record (always the case for non-CNAME entries). A CNAME chain that terminates in more than one TXT value at the target yields multiple entries. Populated on entries in cname\_dmarc\_records, cname\_spf\_records, and cname\_dkim\_records.

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dmarc_records%20%3E%20(items)%20%3E%20(property)%20resolved">Link to this property</a>

ttl: optional number

Time to live in seconds

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dmarc_records%20%3E%20(items)%20%3E%20(property)%20ttl">Link to this property</a>

type: optional string

Record type

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dmarc_records%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20dmarc_records">Link to this property</a>

<details>

<summary>

Deprecatedresolved\_dmarc\_records: optional array of object {content, name }

Use the <code>resolved</code> field on the corresponding entry in cname\_dmarc\_records instead.

DMARC records that a recursive lookup of \_dmarc.{zone} returned. The API populates this only when the zone lacks a DMARC TXT record of its own, which usually means a CNAME delegates DMARC to another zone.

</summary>

content: optional string

The TXT record value. The API joins all character-strings into a single string.

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20resolved_dmarc_records%20%3E%20(items)%20%3E%20(property)%20content">Link to this property</a>

name: optional string

The name the API queried.

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20resolved_dmarc_records%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20resolved_dmarc_records">Link to this property</a>

<details>

<summary>

spf\_records: optional array of object {id, content, name, 3 more }

SPF TXT records

</summary>

id: optional string

DNS record ID

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20spf_records%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

content: optional string

Record content

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20spf_records%20%3E%20(items)%20%3E%20(property)%20content">Link to this property</a>

name: optional string

DNS record name

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20spf_records%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

resolved: optional array of string

For a CNAME record, the TXT content(s) found by following the CNAME chain to its target. An empty array means the chain was resolved but nothing usable was found there; omitted/null means resolution was not attempted for this record (always the case for non-CNAME entries). A CNAME chain that terminates in more than one TXT value at the target yields multiple entries. Populated on entries in cname\_dmarc\_records, cname\_spf\_records, and cname\_dkim\_records.

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20spf_records%20%3E%20(items)%20%3E%20(property)%20resolved">Link to this property</a>

ttl: optional number

Time to live in seconds

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20spf_records%20%3E%20(items)%20%3E%20(property)%20ttl">Link to this property</a>

type: optional string

Record type

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20spf_records%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records%20%3E%20(property)%20spf_records">Link to this property</a>

</details>

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20records">Link to this property</a>

rua\_prefix: optional string

Prefix for DMARC RUA addresses (32-char hex string)

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20rua_prefix">Link to this property</a>

skip\_wizard: optional boolean

Whether to skip the setup wizard

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20skip_wizard">Link to this property</a>

<details>

<summary>

status: optional "missing-dmarc-report"or "multiple-dmarc-reports"or "missing-dmarc-rua"or 2 more

DMARC configuration status. The API omits this field when DMARC is correctly configured. If the zone lacks a DMARC TXT record of its own, the API resolves \_dmarc.{zone} recursively and evaluates whatever that lookup returns. A CNAME at \_dmarc.{zone} that points to a valid DMARC record is therefore healthy; the cname-on-dmarc-record value means the CNAME resolves to no DMARC record at all.

</summary>

One of the following:

"missing-dmarc-report"

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"multiple-dmarc-reports"

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

"missing-dmarc-rua"

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%202">Link to this property</a>

"cname-on-dmarc-record"

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%203">Link to this property</a>

"unauthorized-reporting-domain"

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

Deprecatedtag: optional string

Use <code>zone_id</code> instead.

Use <code>zone_id</code> instead

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20tag">Link to this property</a>

zone\_id: optional string

Zone identifier

<a href="#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)%20%3E%20(property)%20zone_id">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_auth.dmarc_reports%20%3E%20(model)%20dmarc_report_edit_response%20%3E%20(schema)>)