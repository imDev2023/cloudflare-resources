---
title: DEX Tests
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Zero Trust](https://developers.cloudflare.com/api/resources/zero_trust)

[Devices](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# DEX Tests

##### [List Device DEX tests](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/dex_tests/methods/list)

GET/accounts/{account\_id}/dex/devices/dex\_tests

##### [Get Device DEX test](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/dex_tests/methods/get)

GET/accounts/{account\_id}/dex/devices/dex\_tests/{dex\_test\_id}

##### [Create Device DEX test](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/dex_tests/methods/create)

POST/accounts/{account\_id}/dex/devices/dex\_tests

##### [Update Device DEX test](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/dex_tests/methods/update)

PUT/accounts/{account\_id}/dex/devices/dex\_tests/{dex\_test\_id}

##### [Delete Device DEX test](https://developers.cloudflare.com/api/resources/zero_trust/subresources/devices/subresources/dex_tests/methods/delete)

DELETE/accounts/{account\_id}/dex/devices/dex\_tests/{dex\_test\_id}

##### ModelsExpand Collapse

<details>

<summary>

SchemaData object {host, kind, method }

The configuration object which contains the details for the WARP client to conduct the test.

</summary>

host: string

The desired endpoint to test.

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_data%20%3E%20(schema)%20%3E%20(property)%20host">Link to this property</a>

<details>

<summary>

kind: "http"or "traceroute"

The type of test.

</summary>

One of the following:

"http"

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_data%20%3E%20(schema)%20%3E%20(property)%20kind%20%3E%20(member)%200">Link to this property</a>

"traceroute"

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_data%20%3E%20(schema)%20%3E%20(property)%20kind%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_data%20%3E%20(schema)%20%3E%20(property)%20kind">Link to this property</a>

method: optional "GET"

The HTTP request method type.

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_data%20%3E%20(schema)%20%3E%20(property)%20method">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_data%20%3E%20(schema)>)

<details>

<summary>

SchemaHTTP object {data, enabled, interval, 7 more }

</summary>

data: <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_data%20%3E%20(schema)">SchemaData</a> { host, kind, method }

The configuration object which contains the details for the WARP client to conduct the test.

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

enabled: boolean

Determines whether or not the test is active.

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

interval: string

How often the test will run.

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20interval">Link to this property</a>

name: string

The name of the DEX test. Must be unique.

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

created: optional string

Date the test was created, in RFC 3339 format.

formatdate-time

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

description: optional string

Additional details about the test.

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

target\_policies: optional array of object {id, default, name }

DEX rules targeted by this test

</summary>

id: string

The id of the DEX rule.

maxLength36

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20target_policies%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

default: optional boolean

Whether the DEX rule is the account default.

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20target_policies%20%3E%20(items)%20%3E%20(property)%20default">Link to this property</a>

name: optional string

The name of the DEX rule.

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20target_policies%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20target_policies">Link to this property</a>

targeted: optional boolean

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20targeted">Link to this property</a>

test\_id: optional string

The unique identifier for the test.

maxLength32

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20test_id">Link to this property</a>

updated: optional string

Date the test was last updated, in RFC 3339 format.

formatdate-time

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20updated">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)>)

<details>

<summary>

DEXTestDeleteResponse object {dex\_tests }

</summary>

<details>

<summary>

dex\_tests: optional array of <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)">SchemaHTTP</a> { data, enabled, interval, 7 more }

</summary>

data: <a href="https://developers.cloudflare.com/api/resources/zero_trust#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_data%20%3E%20(schema)">SchemaData</a> { host, kind, method }

The configuration object which contains the details for the WARP client to conduct the test.

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

enabled: boolean

Determines whether or not the test is active.

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20enabled">Link to this property</a>

interval: string

How often the test will run.

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20interval">Link to this property</a>

name: string

The name of the DEX test. Must be unique.

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20name">Link to this property</a>

created: optional string

Date the test was created, in RFC 3339 format.

formatdate-time

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20created">Link to this property</a>

description: optional string

Additional details about the test.

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

<details>

<summary>

target\_policies: optional array of object {id, default, name }

DEX rules targeted by this test

</summary>

id: string

The id of the DEX rule.

maxLength36

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20target_policies%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

default: optional boolean

Whether the DEX rule is the account default.

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20target_policies%20%3E%20(items)%20%3E%20(property)%20default">Link to this property</a>

name: optional string

The name of the DEX rule.

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20target_policies%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20target_policies">Link to this property</a>

targeted: optional boolean

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20targeted">Link to this property</a>

test\_id: optional string

The unique identifier for the test.

maxLength32

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20test_id">Link to this property</a>

updated: optional string

Date the test was last updated, in RFC 3339 format.

formatdate-time

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20schema_http%20%3E%20(schema)%20%3E%20(property)%20updated">Link to this property</a>

</details>

<a href="#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20dex_test_delete_response%20%3E%20(schema)%20%3E%20(property)%20dex_tests">Link to this property</a>

</details>

[Link to this property](<#(resource)%20zero_trust.devices.dex_tests%20%3E%20(model)%20dex_test_delete_response%20%3E%20(schema)>)