---
title: Devtools
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Browser Rendering](https://developers.cloudflare.com/api/resources/browser_rendering)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Devtools

#### DevtoolsSession

##### [List sessions.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/session/methods/list)

GET/accounts/{account\_id}/browser-rendering/devtools/session

##### [Get session details.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/session/methods/get)

GET/accounts/{account\_id}/browser-rendering/devtools/session/{session\_id}

##### ModelsExpand Collapse

<details>

<summary>

SessionListResponse = array of object {sessionId, closeReason, closeReasonText, 8 more }

</summary>

sessionId: string

Session ID.

formatuuid

<a href="#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20sessionId">Link to this property</a>

closeReason: optional number

Reason code for session closure.

<a href="#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20closeReason">Link to this property</a>

closeReasonText: optional string

Human-readable close reason.

<a href="#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20closeReasonText">Link to this property</a>

connectionEndTime: optional number

Connection end time.

<a href="#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20connectionEndTime">Link to this property</a>

connectionId: optional string

Connection ID.

<a href="#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20connectionId">Link to this property</a>

connectionStartTime: optional number

Connection start time.

<a href="#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20connectionStartTime">Link to this property</a>

devtoolsFrontendUrl: optional string

DevTools frontend URL.

<a href="#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20devtoolsFrontendUrl">Link to this property</a>

endTime: optional number

Session end time.

<a href="#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20endTime">Link to this property</a>

lastUpdated: optional number

Last updated timestamp.

<a href="#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20lastUpdated">Link to this property</a>

startTime: optional number

Session start time.

<a href="#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20startTime">Link to this property</a>

webSocketDebuggerUrl: optional string

WebSocket URL for debugging this target.

<a href="#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20webSocketDebuggerUrl">Link to this property</a>

</details>

[Link to this property](<#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_list_response%20%3E%20(schema)>)

<details>

<summary>

SessionGetResponse object {sessionId, closeReason, closeReasonText, 8 more }

</summary>

sessionId: string

Session ID.

formatuuid

<a href="#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_get_response%20%3E%20(schema)%20%3E%20(property)%20sessionId">Link to this property</a>

closeReason: optional number

Reason code for session closure.

<a href="#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_get_response%20%3E%20(schema)%20%3E%20(property)%20closeReason">Link to this property</a>

closeReasonText: optional string

Human-readable close reason.

<a href="#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_get_response%20%3E%20(schema)%20%3E%20(property)%20closeReasonText">Link to this property</a>

connectionEndTime: optional number

Connection end time.

<a href="#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_get_response%20%3E%20(schema)%20%3E%20(property)%20connectionEndTime">Link to this property</a>

connectionId: optional string

Connection ID.

<a href="#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_get_response%20%3E%20(schema)%20%3E%20(property)%20connectionId">Link to this property</a>

connectionStartTime: optional number

Connection start time.

<a href="#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_get_response%20%3E%20(schema)%20%3E%20(property)%20connectionStartTime">Link to this property</a>

devtoolsFrontendUrl: optional string

DevTools frontend URL.

<a href="#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_get_response%20%3E%20(schema)%20%3E%20(property)%20devtoolsFrontendUrl">Link to this property</a>

endTime: optional number

Session end time.

<a href="#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_get_response%20%3E%20(schema)%20%3E%20(property)%20endTime">Link to this property</a>

lastUpdated: optional number

Last updated timestamp.

<a href="#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_get_response%20%3E%20(schema)%20%3E%20(property)%20lastUpdated">Link to this property</a>

startTime: optional number

Session start time.

<a href="#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_get_response%20%3E%20(schema)%20%3E%20(property)%20startTime">Link to this property</a>

webSocketDebuggerUrl: optional string

WebSocket URL for debugging this target.

<a href="#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_get_response%20%3E%20(schema)%20%3E%20(property)%20webSocketDebuggerUrl">Link to this property</a>

</details>

[Link to this property](<#(resource)%20browser_rendering.devtools.session%20%3E%20(model)%20session_get_response%20%3E%20(schema)>)

#### DevtoolsBrowser

##### [Get a browser session ID.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/methods/create)

POST/accounts/{account\_id}/browser-rendering/devtools/browser

##### [Close browser session.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/methods/delete)

DELETE/accounts/{account\_id}/browser-rendering/devtools/browser/{session\_id}

##### [Get browser version metadata.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/methods/version)

GET/accounts/{account\_id}/browser-rendering/devtools/browser/{session\_id}/json/version

##### [Get Chrome DevTools Protocol schema.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/methods/protocol)

GET/accounts/{account\_id}/browser-rendering/devtools/browser/{session\_id}/json/protocol

##### ModelsExpand Collapse

<details>

<summary>

BrowserCreateResponse object {sessionId, webSocketDebuggerUrl }

</summary>

sessionId: string

Browser session ID.

<a href="#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_create_response%20%3E%20(schema)%20%3E%20(property)%20sessionId">Link to this property</a>

webSocketDebuggerUrl: optional string

WebSocket URL for the session.

<a href="#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_create_response%20%3E%20(schema)%20%3E%20(property)%20webSocketDebuggerUrl">Link to this property</a>

</details>

[Link to this property](<#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_create_response%20%3E%20(schema)>)

<details>

<summary>

BrowserDeleteResponse object {status }

</summary>

<details>

<summary>

status: "closing"or "closed"

</summary>

One of the following:

"closing"

<a href="#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_delete_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"closed"

<a href="#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_delete_response%20%3E%20(schema)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_delete_response%20%3E%20(schema)%20%3E%20(property)%20status">Link to this property</a>

</details>

[Link to this property](<#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_delete_response%20%3E%20(schema)>)

<details>

<summary>

BrowserVersionResponse object {Browser, "Protocol-Version", "User-Agent", 3 more }

</summary>

Browser: string

Browser name and version.

<a href="#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_version_response%20%3E%20(schema)%20%3E%20(property)%20Browser">Link to this property</a>

"Protocol-Version": string

Chrome DevTools Protocol version.

<a href="#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_version_response%20%3E%20(schema)%20%3E%20(property)%20Protocol-Version">Link to this property</a>

"User-Agent": string

User agent string.

<a href="#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_version_response%20%3E%20(schema)%20%3E%20(property)%20User-Agent">Link to this property</a>

"V8-Version": string

V8 JavaScript engine version.

<a href="#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_version_response%20%3E%20(schema)%20%3E%20(property)%20V8-Version">Link to this property</a>

"WebKit-Version": string

WebKit version.

<a href="#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_version_response%20%3E%20(schema)%20%3E%20(property)%20WebKit-Version">Link to this property</a>

webSocketDebuggerUrl: string

WebSocket URL for debugging the browser.

<a href="#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_version_response%20%3E%20(schema)%20%3E%20(property)%20webSocketDebuggerUrl">Link to this property</a>

</details>

[Link to this property](<#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_version_response%20%3E%20(schema)>)

<details>

<summary>

BrowserProtocolResponse object {domains, version }

</summary>

<details>

<summary>

domains: array of object {domain, commands, dependencies, 3 more }

List of protocol domains.

</summary>

domain: string

Domain name.

<a href="#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_protocol_response%20%3E%20(schema)%20%3E%20(property)%20domains%20%3E%20(items)%20%3E%20(property)%20domain">Link to this property</a>

commands: optional array of map\[unknown]

Available commands.

<a href="#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_protocol_response%20%3E%20(schema)%20%3E%20(property)%20domains%20%3E%20(items)%20%3E%20(property)%20commands">Link to this property</a>

dependencies: optional array of string

Domain dependencies.

<a href="#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_protocol_response%20%3E%20(schema)%20%3E%20(property)%20domains%20%3E%20(items)%20%3E%20(property)%20dependencies">Link to this property</a>

events: optional array of map\[unknown]

Available events.

<a href="#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_protocol_response%20%3E%20(schema)%20%3E%20(property)%20domains%20%3E%20(items)%20%3E%20(property)%20events">Link to this property</a>

experimental: optional boolean

Whether this domain is experimental.

<a href="#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_protocol_response%20%3E%20(schema)%20%3E%20(property)%20domains%20%3E%20(items)%20%3E%20(property)%20experimental">Link to this property</a>

types: optional array of map\[unknown]

Type definitions.

<a href="#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_protocol_response%20%3E%20(schema)%20%3E%20(property)%20domains%20%3E%20(items)%20%3E%20(property)%20types">Link to this property</a>

</details>

<a href="#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_protocol_response%20%3E%20(schema)%20%3E%20(property)%20domains">Link to this property</a>

<details>

<summary>

version: optional object {major, minor }

Protocol version.

</summary>

major: string

Major version.

<a href="#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_protocol_response%20%3E%20(schema)%20%3E%20(property)%20version%20%3E%20(property)%20major">Link to this property</a>

minor: string

Minor version.

<a href="#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_protocol_response%20%3E%20(schema)%20%3E%20(property)%20version%20%3E%20(property)%20minor">Link to this property</a>

</details>

<a href="#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_protocol_response%20%3E%20(schema)%20%3E%20(property)%20version">Link to this property</a>

</details>

[Link to this property](<#(resource)%20browser_rendering.devtools.browser%20%3E%20(model)%20browser_protocol_response%20%3E%20(schema)>)

#### DevtoolsBrowserLive View

##### [Mint live view URLs for a browser session](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/subresources/live_view/methods/create)

POST/accounts/{account\_id}/browser-rendering/devtools/browser/{session\_id}/live\_view

##### ModelsExpand Collapse

<details>

<summary>

LiveViewCreateResponse object {id, devtoolsFrontendUrl, options, webSocketDebuggerUrl }

</summary>

id: string

Target ID

<a href="#(resource)%20browser_rendering.devtools.browser.live_view%20%3E%20(model)%20live_view_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

devtoolsFrontendUrl: string

URL to open the live view in a browser

formaturi

<a href="#(resource)%20browser_rendering.devtools.browser.live_view%20%3E%20(model)%20live_view_create_response%20%3E%20(schema)%20%3E%20(property)%20devtoolsFrontendUrl">Link to this property</a>

<details>

<summary>

options: object {mode, guardrails }

</summary>

<details>

<summary>

mode: "devtools"or "tab"or "full"

UI mode for the live view

</summary>

One of the following:

"devtools"

<a href="#(resource)%20browser_rendering.devtools.browser.live_view%20%3E%20(model)%20live_view_create_response%20%3E%20(schema)%20%3E%20(property)%20options%20%3E%20(property)%20mode%20%3E%20(member)%200">Link to this property</a>

"tab"

<a href="#(resource)%20browser_rendering.devtools.browser.live_view%20%3E%20(model)%20live_view_create_response%20%3E%20(schema)%20%3E%20(property)%20options%20%3E%20(property)%20mode%20%3E%20(member)%201">Link to this property</a>

"full"

<a href="#(resource)%20browser_rendering.devtools.browser.live_view%20%3E%20(model)%20live_view_create_response%20%3E%20(schema)%20%3E%20(property)%20options%20%3E%20(property)%20mode%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20browser_rendering.devtools.browser.live_view%20%3E%20(model)%20live_view_create_response%20%3E%20(schema)%20%3E%20(property)%20options%20%3E%20(property)%20mode">Link to this property</a>

<details>

<summary>

guardrails: optional object {mode }

Connection guardrails applied to this link

</summary>

mode: "readonly"

<a href="#(resource)%20browser_rendering.devtools.browser.live_view%20%3E%20(model)%20live_view_create_response%20%3E%20(schema)%20%3E%20(property)%20options%20%3E%20(property)%20guardrails%20%3E%20(property)%20mode">Link to this property</a>

</details>

<a href="#(resource)%20browser_rendering.devtools.browser.live_view%20%3E%20(model)%20live_view_create_response%20%3E%20(schema)%20%3E%20(property)%20options%20%3E%20(property)%20guardrails">Link to this property</a>

</details>

<a href="#(resource)%20browser_rendering.devtools.browser.live_view%20%3E%20(model)%20live_view_create_response%20%3E%20(schema)%20%3E%20(property)%20options">Link to this property</a>

webSocketDebuggerUrl: string

WebSocket URL for CDP connection

formaturi

<a href="#(resource)%20browser_rendering.devtools.browser.live_view%20%3E%20(model)%20live_view_create_response%20%3E%20(schema)%20%3E%20(property)%20webSocketDebuggerUrl">Link to this property</a>

</details>

[Link to this property](<#(resource)%20browser_rendering.devtools.browser.live_view%20%3E%20(model)%20live_view_create_response%20%3E%20(schema)>)

#### DevtoolsBrowserPage

#### DevtoolsBrowserTargets

##### [Open a new browser tab.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/subresources/targets/methods/create)

PUT/accounts/{account\_id}/browser-rendering/devtools/browser/{session\_id}/json/new

##### [List targets.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/subresources/targets/methods/list)

GET/accounts/{account\_id}/browser-rendering/devtools/browser/{session\_id}/json/list

##### [Get a target by ID.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/subresources/targets/methods/get)

GET/accounts/{account\_id}/browser-rendering/devtools/browser/{session\_id}/json/list/{target\_id}

##### [Activate a browser target.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/subresources/targets/methods/activate)

GET/accounts/{account\_id}/browser-rendering/devtools/browser/{session\_id}/json/activate/{target\_id}

##### [Close a browser target.](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools/subresources/browser/subresources/targets/methods/close)

GET/accounts/{account\_id}/browser-rendering/devtools/browser/{session\_id}/json/close/{target\_id}

##### ModelsExpand Collapse

<details>

<summary>

TargetCreateResponse object {id, type, url, 4 more }

</summary>

id: string

Target ID.

<a href="#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_create_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

type: string

Target type (page, background\_page, worker, etc.).

<a href="#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_create_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

url: string

URL of the target.

<a href="#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_create_response%20%3E%20(schema)%20%3E%20(property)%20url">Link to this property</a>

description: optional string

Target description.

<a href="#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_create_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

devtoolsFrontendUrl: optional string

DevTools frontend URL.

<a href="#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_create_response%20%3E%20(schema)%20%3E%20(property)%20devtoolsFrontendUrl">Link to this property</a>

title: optional string

Title of the target.

<a href="#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_create_response%20%3E%20(schema)%20%3E%20(property)%20title">Link to this property</a>

webSocketDebuggerUrl: optional string

WebSocket URL for debugging this target.

<a href="#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_create_response%20%3E%20(schema)%20%3E%20(property)%20webSocketDebuggerUrl">Link to this property</a>

</details>

[Link to this property](<#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_create_response%20%3E%20(schema)>)

<details>

<summary>

TargetListResponse = array of object {id, type, url, 4 more }

</summary>

id: string

Target ID.

<a href="#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

type: string

Target type (page, background\_page, worker, etc.).

<a href="#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

url: string

URL of the target.

<a href="#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20url">Link to this property</a>

description: optional string

Target description.

<a href="#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20description">Link to this property</a>

devtoolsFrontendUrl: optional string

DevTools frontend URL.

<a href="#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20devtoolsFrontendUrl">Link to this property</a>

title: optional string

Title of the target.

<a href="#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20title">Link to this property</a>

webSocketDebuggerUrl: optional string

WebSocket URL for debugging this target.

<a href="#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_list_response%20%3E%20(schema)%20%3E%20(items)%20%3E%20(property)%20webSocketDebuggerUrl">Link to this property</a>

</details>

[Link to this property](<#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_list_response%20%3E%20(schema)>)

<details>

<summary>

TargetGetResponse object {id, type, url, 4 more }

</summary>

id: string

Target ID.

<a href="#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_get_response%20%3E%20(schema)%20%3E%20(property)%20id">Link to this property</a>

type: string

Target type (page, background\_page, worker, etc.).

<a href="#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_get_response%20%3E%20(schema)%20%3E%20(property)%20type">Link to this property</a>

url: string

URL of the target.

<a href="#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_get_response%20%3E%20(schema)%20%3E%20(property)%20url">Link to this property</a>

description: optional string

Target description.

<a href="#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_get_response%20%3E%20(schema)%20%3E%20(property)%20description">Link to this property</a>

devtoolsFrontendUrl: optional string

DevTools frontend URL.

<a href="#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_get_response%20%3E%20(schema)%20%3E%20(property)%20devtoolsFrontendUrl">Link to this property</a>

title: optional string

Title of the target.

<a href="#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_get_response%20%3E%20(schema)%20%3E%20(property)%20title">Link to this property</a>

webSocketDebuggerUrl: optional string

WebSocket URL for debugging this target.

<a href="#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_get_response%20%3E%20(schema)%20%3E%20(property)%20webSocketDebuggerUrl">Link to this property</a>

</details>

[Link to this property](<#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_get_response%20%3E%20(schema)>)

<details>

<summary>

TargetActivateResponse object {message }

</summary>

message: string

Target activated.

<a href="#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_activate_response%20%3E%20(schema)%20%3E%20(property)%20message">Link to this property</a>

</details>

[Link to this property](<#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_activate_response%20%3E%20(schema)>)

<details>

<summary>

TargetCloseResponse object {message }

</summary>

message: string

Target is closing.

<a href="#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_close_response%20%3E%20(schema)%20%3E%20(property)%20message">Link to this property</a>

</details>

[Link to this property](<#(resource)%20browser_rendering.devtools.browser.targets%20%3E%20(model)%20target_close_response%20%3E%20(schema)>)