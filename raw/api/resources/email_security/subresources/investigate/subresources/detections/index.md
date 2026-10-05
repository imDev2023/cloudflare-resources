---
title: Detections
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Email Security](https://developers.cloudflare.com/api/resources/email_security)

[Investigate](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Detections

##### [Get message detection details](https://developers.cloudflare.com/api/resources/email_security/subresources/investigate/subresources/detections/methods/get)

GET/accounts/{account\_id}/email-security/investigate/{investigate\_id}/detections

##### ModelsExpand Collapse

<details>

<summary>

DetectionGetResponse object {action, attachments, findings, 6 more }

</summary>

action: string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20action">Link to this property</a>

<details>

<summary>

attachments: array of object {size, content\_type, detection, 6 more }

</summary>

size: number

Size of the attachment in bytes.

minimum0

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20size">Link to this property</a>

content\_type: optional string

MIME type of the attachment.

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20content_type">Link to this property</a>

<details>

<summary>

detection: optional "MALICIOUS"or "MALICIOUS-BEC"or "SUSPICIOUS"or 7 more

Detection result for this attachment.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%200">Link to this property</a>

"MALICIOUS-BEC"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%201">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%202">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%203">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%204">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%205">Link to this property</a>

"ENCRYPTED"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%206">Link to this property</a>

"EXTERNAL"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%207">Link to this property</a>

"UNKNOWN"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%208">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%209">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20detection">Link to this property</a>

encrypted: optional boolean

Whether the attachment is encrypted.

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20encrypted">Link to this property</a>

filename: optional string

Name of the attached file.

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20filename">Link to this property</a>

md5: optional string

MD5 hash of the attachment.

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20md5">Link to this property</a>

name: optional string

Attachment name (alternative to filename).

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

sha1: optional string

SHA1 hash of the attachment.

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20sha1">Link to this property</a>

sha256: optional string

SHA256 hash of the attachment.

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments%20%3E%20(items)%20%3E%20(property)%20sha256">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20attachments">Link to this property</a>

<details>

<summary>

findings: array of object {attachment, detail, detection, 6 more }

</summary>

attachment: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20attachment">Link to this property</a>

detail: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detail">Link to this property</a>

<details>

<summary>

detection: optional "MALICIOUS"or "MALICIOUS-BEC"or "SUSPICIOUS"or 7 more

Detection result associated with this finding.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%200">Link to this property</a>

"MALICIOUS-BEC"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%201">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%202">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%203">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%204">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%205">Link to this property</a>

"ENCRYPTED"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%206">Link to this property</a>

"EXTERNAL"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%207">Link to this property</a>

"UNKNOWN"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%208">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection%20%3E%20(member)%209">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20detection">Link to this property</a>

field: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20field">Link to this property</a>

name: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

portion: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20portion">Link to this property</a>

reason: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20reason">Link to this property</a>

score: optional number

formatdouble

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20score">Link to this property</a>

value: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20findings">Link to this property</a>

<details>

<summary>

headers: array of object {name, value }

</summary>

name: string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

value: string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20headers%20%3E%20(items)%20%3E%20(property)%20value">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20headers">Link to this property</a>

<details>

<summary>

links: array of object {href, text }

</summary>

href: string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20links%20%3E%20(items)%20%3E%20(property)%20href">Link to this property</a>

text: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20links%20%3E%20(items)%20%3E%20(property)%20text">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20links">Link to this property</a>

<details>

<summary>

sender\_info: object {as\_name, as\_number, geo, 2 more }

</summary>

as\_name: optional string

The name of the autonomous system.

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20sender_info%20%3E%20(property)%20as_name">Link to this property</a>

as\_number: optional number

The number of the autonomous system.

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20sender_info%20%3E%20(property)%20as_number">Link to this property</a>

geo: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20sender_info%20%3E%20(property)%20geo">Link to this property</a>

ip: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20sender_info%20%3E%20(property)%20ip">Link to this property</a>

pld: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20sender_info%20%3E%20(property)%20pld">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20sender_info">Link to this property</a>

<details>

<summary>

threat\_categories: array of object {id, description, name }

</summary>

id: optional number

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20threat_categories%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

description: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20threat_categories%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

name: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20threat_categories%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20threat_categories">Link to this property</a>

<details>

<summary>

validation: object {comment, dkim, dmarc, spf }

</summary>

comment: optional string

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20comment">Link to this property</a>

<details>

<summary>

dkim: optional "pass"or "neutral"or "fail"or 2 more

</summary>

One of the following:

"pass"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%200">Link to this property</a>

"neutral"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%201">Link to this property</a>

"fail"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%202">Link to this property</a>

"error"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%203">Link to this property</a>

"none"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dkim">Link to this property</a>

<details>

<summary>

dmarc: optional "pass"or "neutral"or "fail"or 2 more

</summary>

One of the following:

"pass"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%200">Link to this property</a>

"neutral"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%201">Link to this property</a>

"fail"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%202">Link to this property</a>

"error"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%203">Link to this property</a>

"none"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20dmarc">Link to this property</a>

<details>

<summary>

spf: optional "pass"or "neutral"or "fail"or 2 more

</summary>

One of the following:

"pass"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%200">Link to this property</a>

"neutral"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%201">Link to this property</a>

"fail"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%202">Link to this property</a>

"error"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%203">Link to this property</a>

"none"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation%20%3E%20(property)%20spf">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20validation">Link to this property</a>

<details>

<summary>

final\_disposition: optional "MALICIOUS"or "MALICIOUS-BEC"or "SUSPICIOUS"or 7 more

The verdict Email Security assigns to a message.

</summary>

One of the following:

"MALICIOUS"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%200">Link to this property</a>

"MALICIOUS-BEC"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%201">Link to this property</a>

"SUSPICIOUS"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%202">Link to this property</a>

"SPOOF"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%203">Link to this property</a>

"SPAM"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%204">Link to this property</a>

"BULK"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%205">Link to this property</a>

"ENCRYPTED"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%206">Link to this property</a>

"EXTERNAL"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%207">Link to this property</a>

"UNKNOWN"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%208">Link to this property</a>

"NONE"

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition%20%3E%20(member)%209">Link to this property</a>

</details>

<a href="#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)%20%3E%20(property)%20final_disposition">Link to this property</a>

</details>

[Link to this property](<#(resource)%20email_security.investigate.detections%20%3E%20(model)%20detection_get_response%20%3E%20(schema)>)