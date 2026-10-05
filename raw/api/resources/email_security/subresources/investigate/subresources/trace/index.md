---
title: Trace
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Email Security](https://developers.cloudflare.com/api/resources/email_security)

[Investigate](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Trace

##### [Get email trace](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/trace/methods/get)

GET/accounts/{account\_id}/email-security/investigate/{investigate\_id}/trace

##### ModelsExpand Collapse

<details>

<summary>

TraceGetResponse object {inbound, outbound }

</summary>

<details>

<summary>

inbound: object {lines, pending }

</summary>

<details>

<summary>

lines: optional array of object {lineno, logged\_at, message, ts }

</summary>

lineno: optional number

Line number in the trace log.

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20inbound%20%3E%20(property)%20lines%20%3E%20(items)%20%3E%20(property)%20lineno">Link to this property</a>

logged\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20inbound%20%3E%20(property)%20lines%20%3E%20(items)%20%3E%20(property)%20logged_at">Link to this property</a>

message: optional string

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20inbound%20%3E%20(property)%20lines%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

Deprecatedts: optional string

Use <code>logged_at</code> instead.

Deprecated, use <code>logged_at</code> instead. End of life: November 1, 2026.

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20inbound%20%3E%20(property)%20lines%20%3E%20(items)%20%3E%20(property)%20ts">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20inbound%20%3E%20(property)%20lines">Link to this property</a>

pending: optional boolean

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20inbound%20%3E%20(property)%20pending">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20inbound">Link to this property</a>

<details>

<summary>

outbound: object {lines, pending }

</summary>

<details>

<summary>

lines: optional array of object {lineno, logged\_at, message, ts }

</summary>

lineno: optional number

Line number in the trace log.

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20outbound%20%3E%20(property)%20lines%20%3E%20(items)%20%3E%20(property)%20lineno">Link to this property</a>

logged\_at: optional string

formatdate-time

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20outbound%20%3E%20(property)%20lines%20%3E%20(items)%20%3E%20(property)%20logged_at">Link to this property</a>

message: optional string

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20outbound%20%3E%20(property)%20lines%20%3E%20(items)%20%3E%20(property)%20message">Link to this property</a>

Deprecatedts: optional string

Use <code>logged_at</code> instead.

Deprecated, use <code>logged_at</code> instead. End of life: November 1, 2026.

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20outbound%20%3E%20(property)%20lines%20%3E%20(items)%20%3E%20(property)%20ts">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20outbound%20%3E%20(property)%20lines">Link to this property</a>

pending: optional boolean

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20outbound%20%3E%20(property)%20pending">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)%20%3E%20(property)%20outbound">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.investigate.trace%20%3E%20(model)%20trace_get_response%20%3E%20(schema)>)