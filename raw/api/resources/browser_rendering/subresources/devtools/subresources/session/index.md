---
title: Session
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Browser Rendering](https://developers.cloudflare.com/api/resources/browser_rendering)

[Devtools](https://developers.cloudflare.com/api/resources/browser_rendering/subresources/devtools)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Session

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