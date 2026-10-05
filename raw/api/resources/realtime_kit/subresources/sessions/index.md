---
title: Sessions
---

[Skip to content](#_top)

[API Reference](https://developers.cloudflare.com/api)

[Realtime Kit](https://developers.cloudflare.com/api/resources/realtime_kit)

Copy Markdown

Open in **Claude**Open in **ChatGPT**Open in **Cursor**

---

**Copy Markdown****View as Markdown**

# Sessions

##### [Fetch all sessions of an App](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_sessions)

GET/accounts/{account\_id}/realtime/kit/{app\_id}/sessions

##### [Fetch details of a session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_details)

GET/accounts/{account\_id}/realtime/kit/{app\_id}/sessions/{session\_id}

##### [Fetch participants list of a session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_participants)

GET/accounts/{account\_id}/realtime/kit/{app\_id}/sessions/{session\_id}/participants

##### [Fetch details of a participant](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_participant_details)

GET/accounts/{account\_id}/realtime/kit/{app\_id}/sessions/{session\_id}/participants/{participant\_id}

##### [Fetch all chat messages of a session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_chat)

GET/accounts/{account\_id}/realtime/kit/{app\_id}/sessions/{session\_id}/chat

##### [Fetch the complete transcript for a session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_transcripts)

GET/accounts/{account\_id}/realtime/kit/{app\_id}/sessions/{session\_id}/transcript

##### [Fetch summary of transcripts for a session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_session_summary)

GET/accounts/{account\_id}/realtime/kit/{app\_id}/sessions/{session\_id}/summary

##### [Generate summary of Transcripts for the session](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/generate_summary_of_transcripts)

POST/accounts/{account\_id}/realtime/kit/{app\_id}/sessions/{session\_id}/summary

##### [Fetch details of peer](https://developers.cloudflare.com/api/resources/realtime_kit/subresources/sessions/methods/get_participant_data_from_peer_id)

GET/accounts/{account\_id}/realtime/kit/{app\_id}/sessions/peer-report/{peer\_id}

##### ModelsExpand Collapse

<details>

<summary>

SessionGetSessionsResponse object {data, paging, success }

</summary>

<details>

<summary>

data: optional object {sessions }

</summary>

<details>

<summary>

sessions: optional array of object {id, associated\_id, created\_at, 11 more }

</summary>

id: string

ID of the session

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20sessions%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

associated\_id: string

ID of the meeting this session is associated with. In the case of V2 meetings, it is always a UUID. In V1 meetings, it is a room name of the form <code>abcdef-ghijkl</code>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20sessions%20%3E%20(items)%20%3E%20(property)%20associated_id">Link to this property</a>

created\_at: string

timestamp when session created

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20sessions%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

live\_participants: number

number of participants currently in the session

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20sessions%20%3E%20(items)%20%3E%20(property)%20live_participants">Link to this property</a>

max\_concurrent\_participants: number

number of maximum participants that were in the session

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20sessions%20%3E%20(items)%20%3E%20(property)%20max_concurrent_participants">Link to this property</a>

meeting\_display\_name: string

Title of the meeting this session belongs to

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20sessions%20%3E%20(items)%20%3E%20(property)%20meeting_display_name">Link to this property</a>

minutes\_consumed: number

number of minutes consumed since the session started

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20sessions%20%3E%20(items)%20%3E%20(property)%20minutes_consumed">Link to this property</a>

organization\_id: string

App id that hosted this session

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20sessions%20%3E%20(items)%20%3E%20(property)%20organization_id">Link to this property</a>

started\_at: string

timestamp when session started

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20sessions%20%3E%20(items)%20%3E%20(property)%20started_at">Link to this property</a>

<details>

<summary>

status: "LIVE"or "ENDED"

current status of session

</summary>

One of the following:

"LIVE"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20sessions%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"ENDED"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20sessions%20%3E%20(items)%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20sessions%20%3E%20(items)%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

type: "meeting"or "livestream"or "participant"

type of session

</summary>

One of the following:

"meeting"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20sessions%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"livestream"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20sessions%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"participant"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20sessions%20%3E%20(items)%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20sessions%20%3E%20(items)%20%3E%20(property)%20type">Link to this property</a>

updated\_at: string

timestamp when session was last updated

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20sessions%20%3E%20(items)%20%3E%20(property)%20updated_at">Link to this property</a>

breakout\_rooms: optional array of unknown

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20sessions%20%3E%20(items)%20%3E%20(property)%20breakout_rooms">Link to this property</a>

ended\_at: optional string

timestamp when session ended

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20sessions%20%3E%20(items)%20%3E%20(property)%20ended_at">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20sessions">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

<details>

<summary>

paging: optional object {end\_offset, start\_offset, total\_count }

</summary>

end\_offset: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20paging%20%3E%20(property)%20end_offset">Link to this property</a>

start\_offset: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20paging%20%3E%20(property)%20start_offset">Link to this property</a>

total\_count: optional number

minimum0

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20paging%20%3E%20(property)%20total_count">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20paging">Link to this property</a>

success: optional boolean

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_sessions_response%20%3E%20(schema)>)

<details>

<summary>

SessionGetSessionDetailsResponse object {data, success }

</summary>

<details>

<summary>

data: optional object {id, associated\_id, created\_at, 11 more }

</summary>

id: string

ID of the session

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20id">Link to this property</a>

associated\_id: string

ID of the meeting this session is associated with. In the case of V2 meetings, it is always a UUID. In V1 meetings, it is a room name of the form <code>abcdef-ghijkl</code>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20associated_id">Link to this property</a>

created\_at: string

timestamp when session created

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20created_at">Link to this property</a>

live\_participants: number

number of participants currently in the session

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20live_participants">Link to this property</a>

max\_concurrent\_participants: number

number of maximum participants that were in the session

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20max_concurrent_participants">Link to this property</a>

meeting\_display\_name: string

Title of the meeting this session belongs to

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20meeting_display_name">Link to this property</a>

minutes\_consumed: number

number of minutes consumed since the session started

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20minutes_consumed">Link to this property</a>

organization\_id: string

App id that hosted this session

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20organization_id">Link to this property</a>

started\_at: string

timestamp when session started

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20started_at">Link to this property</a>

<details>

<summary>

status: "LIVE"or "ENDED"

current status of session

</summary>

One of the following:

"LIVE"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20status%20%3E%20(member)%200">Link to this property</a>

"ENDED"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20status%20%3E%20(member)%201">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20status">Link to this property</a>

<details>

<summary>

type: "meeting"or "livestream"or "participant"

type of session

</summary>

One of the following:

"meeting"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20type%20%3E%20(member)%200">Link to this property</a>

"livestream"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20type%20%3E%20(member)%201">Link to this property</a>

"participant"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20type%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20type">Link to this property</a>

updated\_at: string

timestamp when session was last updated

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20updated_at">Link to this property</a>

breakout\_rooms: optional array of unknown

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20breakout_rooms">Link to this property</a>

ended\_at: optional string

timestamp when session ended

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20ended_at">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_details_response%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

success: optional boolean

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_details_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_details_response%20%3E%20(schema)>)

<details>

<summary>

SessionGetSessionParticipantsResponse object {data, success }

</summary>

<details>

<summary>

data: optional object {participants }

</summary>

<details>

<summary>

participants: optional array of object {id, created\_at, custom\_participant\_id, 8 more }

</summary>

id: optional string

Participant ID. This maps to the corresponding peerId.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

created\_at: optional string

timestamp when this participant was created.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

custom\_participant\_id: optional string

ID passed by client to create this participant.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20custom_participant_id">Link to this property</a>

display\_name: optional string

Display name of participant when joining the session.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20display_name">Link to this property</a>

duration: optional number

number of minutes for which the participant was in the session.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20duration">Link to this property</a>

joined\_at: optional string

timestamp at which participant joined the session.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20joined_at">Link to this property</a>

left\_at: optional string

timestamp at which participant left the session.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20left_at">Link to this property</a>

<details>

<summary>

peer\_events: optional array of object {id, created\_at, event\_name, 7 more }

Connection lifecycle events for the participant’s peer. Only included when <code>include_peer_events</code> is true.

</summary>

id: optional string

ID of the peer event.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

created\_at: optional string

Timestamp when this peer event was created.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

event\_name: optional "PEER\_CREATED"or "PEER\_JOINING"or "PEER\_LEAVING"

Name of the peer event.

</summary>

One of the following:

"PEER\_CREATED"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20event_name%20%3E%20(member)%200">Link to this property</a>

"PEER\_JOINING"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20event_name%20%3E%20(member)%201">Link to this property</a>

"PEER\_LEAVING"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20event_name%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20event_name">Link to this property</a>

minutes\_consumed: optional number

Minutes consumed attributed to this event.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20minutes_consumed">Link to this property</a>

participant\_id: optional string

ID of the participant this event belongs to.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20participant_id">Link to this property</a>

peer\_id: optional string

Peer ID this event belongs to.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20peer_id">Link to this property</a>

<details>

<summary>

preset\_view\_type: optional "GROUP\_CALL"or "WEBINAR"or "AUDIO\_ROOM"or 2 more

View type of the preset associated with the peer.

</summary>

One of the following:

"GROUP\_CALL"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20preset_view_type%20%3E%20(member)%200">Link to this property</a>

"WEBINAR"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20preset_view_type%20%3E%20(member)%201">Link to this property</a>

"AUDIO\_ROOM"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20preset_view_type%20%3E%20(member)%202">Link to this property</a>

"LIVESTREAM"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20preset_view_type%20%3E%20(member)%203">Link to this property</a>

"CHAT"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20preset_view_type%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20preset_view_type">Link to this property</a>

session\_id: optional string

ID of the session this event belongs to.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20session_id">Link to this property</a>

socket\_session\_id: optional string

ID of the socket session associated with this event.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20socket_session_id">Link to this property</a>

updated\_at: optional string

Timestamp when this peer event was last updated.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20peer_events">Link to this property</a>

preset\_name: optional string

Name of the preset associated with the participant.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20preset_name">Link to this property</a>

updated\_at: optional string

timestamp when this participant’s data was last updated.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20updated_at">Link to this property</a>

user\_id: optional string

User id for this participant.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants%20%3E%20(items)%20%3E%20(property)%20user_id">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participants">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

success: optional boolean

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participants_response%20%3E%20(schema)>)

<details>

<summary>

SessionGetSessionParticipantDetailsResponse object {data, success }

</summary>

<details>

<summary>

data: optional object {participant }

</summary>

<details>

<summary>

participant: optional object {id, created\_at, custom\_participant\_id, 8 more }

</summary>

id: optional string

Participant ID. This maps to the corresponding peerId.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20id">Link to this property</a>

created\_at: optional string

timestamp when this participant was created.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20created_at">Link to this property</a>

custom\_participant\_id: optional string

ID passed by client to create this participant.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20custom_participant_id">Link to this property</a>

display\_name: optional string

Display name of participant when joining the session.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20display_name">Link to this property</a>

duration: optional number

number of minutes for which the participant was in the session.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20duration">Link to this property</a>

joined\_at: optional string

timestamp at which participant joined the session.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20joined_at">Link to this property</a>

left\_at: optional string

timestamp at which participant left the session.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20left_at">Link to this property</a>

<details>

<summary>

peer\_events: optional array of object {id, created\_at, event\_name, 7 more }

Connection lifecycle events for the participant’s peer. Only included when <code>include_peer_events</code> is true.

</summary>

id: optional string

ID of the peer event.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

created\_at: optional string

Timestamp when this peer event was created.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

event\_name: optional "PEER\_CREATED"or "PEER\_JOINING"or "PEER\_LEAVING"

Name of the peer event.

</summary>

One of the following:

"PEER\_CREATED"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20event_name%20%3E%20(member)%200">Link to this property</a>

"PEER\_JOINING"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20event_name%20%3E%20(member)%201">Link to this property</a>

"PEER\_LEAVING"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20event_name%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20event_name">Link to this property</a>

minutes\_consumed: optional number

Minutes consumed attributed to this event.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20minutes_consumed">Link to this property</a>

participant\_id: optional string

ID of the participant this event belongs to.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20participant_id">Link to this property</a>

peer\_id: optional string

Peer ID this event belongs to.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20peer_id">Link to this property</a>

<details>

<summary>

preset\_view\_type: optional "GROUP\_CALL"or "WEBINAR"or "AUDIO\_ROOM"or 2 more

View type of the preset associated with the peer.

</summary>

One of the following:

"GROUP\_CALL"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20preset_view_type%20%3E%20(member)%200">Link to this property</a>

"WEBINAR"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20preset_view_type%20%3E%20(member)%201">Link to this property</a>

"AUDIO\_ROOM"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20preset_view_type%20%3E%20(member)%202">Link to this property</a>

"LIVESTREAM"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20preset_view_type%20%3E%20(member)%203">Link to this property</a>

"CHAT"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20preset_view_type%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20preset_view_type">Link to this property</a>

session\_id: optional string

ID of the session this event belongs to.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20session_id">Link to this property</a>

socket\_session\_id: optional string

ID of the socket session associated with this event.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20socket_session_id">Link to this property</a>

updated\_at: optional string

Timestamp when this peer event was last updated.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events">Link to this property</a>

preset\_name: optional string

Name of the preset associated with the participant.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20preset_name">Link to this property</a>

updated\_at: optional string

timestamp when this participant’s data was last updated.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20updated_at">Link to this property</a>

user\_id: optional string

User id for this participant.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20user_id">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

success: optional boolean

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_participant_details_response%20%3E%20(schema)>)

<details>

<summary>

SessionGetSessionChatResponse object {data, success }

</summary>

<details>

<summary>

data: optional object {chat\_download\_url, chat\_download\_url\_expiry }

</summary>

chat\_download\_url: string

URL where the chat logs can be downloaded

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_chat_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20chat_download_url">Link to this property</a>

chat\_download\_url\_expiry: string

Time when the download URL will expire

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_chat_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20chat_download_url_expiry">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_chat_response%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

success: optional boolean

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_chat_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_chat_response%20%3E%20(schema)>)

<details>

<summary>

SessionGetSessionTranscriptsResponse object {data, success }

</summary>

<details>

<summary>

data: optional object {sessionId, transcript\_download\_url, transcript\_download\_url\_expiry }

</summary>

sessionId: string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_transcripts_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20sessionId">Link to this property</a>

transcript\_download\_url: string

URL where the transcript can be downloaded

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_transcripts_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20transcript_download_url">Link to this property</a>

transcript\_download\_url\_expiry: string

Time when the download URL will expire

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_transcripts_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20transcript_download_url_expiry">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_transcripts_response%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

success: optional boolean

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_transcripts_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_transcripts_response%20%3E%20(schema)>)

<details>

<summary>

SessionGetSessionSummaryResponse object {data, success }

</summary>

<details>

<summary>

data: optional object {sessionId, summaryDownloadUrl, summaryDownloadUrlExpiry }

</summary>

sessionId: string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_summary_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20sessionId">Link to this property</a>

summaryDownloadUrl: string

URL where the summary of transcripts can be downloaded

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_summary_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20summaryDownloadUrl">Link to this property</a>

summaryDownloadUrlExpiry: string

Time of Expiry before when you need to download the csv file.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_summary_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20summaryDownloadUrlExpiry">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_summary_response%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

success: optional boolean

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_summary_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_session_summary_response%20%3E%20(schema)>)

<details>

<summary>

SessionGenerateSummaryOfTranscriptsResponse object {data, success }

</summary>

<details>

<summary>

data: optional object {session\_id, status }

</summary>

session\_id: optional string

formatuuid

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_generate_summary_of_transcripts_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20session_id">Link to this property</a>

status: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_generate_summary_of_transcripts_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20status">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_generate_summary_of_transcripts_response%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

success: optional boolean

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_generate_summary_of_transcripts_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_generate_summary_of_transcripts_response%20%3E%20(schema)>)

<details>

<summary>

SessionGetParticipantDataFromPeerIDResponse object {data, success }

</summary>

<details>

<summary>

data: optional object {participant }

</summary>

<details>

<summary>

participant: optional object {id, created\_at, custom\_participant\_id, 10 more }

</summary>

id: optional string

ID of the participant.

formatuuid

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20id">Link to this property</a>

created\_at: optional string

timestamp when this participant was created.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20created_at">Link to this property</a>

custom\_participant\_id: optional string

ID passed by client to create this participant.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20custom_participant_id">Link to this property</a>

display\_name: optional string

Display name of participant when joining the session.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20display_name">Link to this property</a>

duration: optional number

number of minutes for which the participant was in the session.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20duration">Link to this property</a>

joined\_at: optional string

timestamp at which participant joined the session.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20joined_at">Link to this property</a>

left\_at: optional string

timestamp at which participant left the session.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20left_at">Link to this property</a>

<details>

<summary>

peer\_events: optional array of object {id, created\_at, event\_name, 7 more }

Connection lifecycle events for the participant’s peer.

</summary>

id: optional string

ID of the peer event.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20id">Link to this property</a>

created\_at: optional string

Timestamp when this peer event was created.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20created_at">Link to this property</a>

<details>

<summary>

event\_name: optional "PEER\_CREATED"or "PEER\_JOINING"or "PEER\_LEAVING"

Name of the peer event.

</summary>

One of the following:

"PEER\_CREATED"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20event_name%20%3E%20(member)%200">Link to this property</a>

"PEER\_JOINING"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20event_name%20%3E%20(member)%201">Link to this property</a>

"PEER\_LEAVING"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20event_name%20%3E%20(member)%202">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20event_name">Link to this property</a>

minutes\_consumed: optional number

Minutes consumed attributed to this event.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20minutes_consumed">Link to this property</a>

participant\_id: optional string

ID of the participant this event belongs to.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20participant_id">Link to this property</a>

peer\_id: optional string

Peer ID this event belongs to.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20peer_id">Link to this property</a>

<details>

<summary>

preset\_view\_type: optional "GROUP\_CALL"or "WEBINAR"or "AUDIO\_ROOM"or 2 more

View type of the preset associated with the peer.

</summary>

One of the following:

"GROUP\_CALL"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20preset_view_type%20%3E%20(member)%200">Link to this property</a>

"WEBINAR"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20preset_view_type%20%3E%20(member)%201">Link to this property</a>

"AUDIO\_ROOM"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20preset_view_type%20%3E%20(member)%202">Link to this property</a>

"LIVESTREAM"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20preset_view_type%20%3E%20(member)%203">Link to this property</a>

"CHAT"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20preset_view_type%20%3E%20(member)%204">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20preset_view_type">Link to this property</a>

session\_id: optional string

ID of the session this event belongs to.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20session_id">Link to this property</a>

socket\_session\_id: optional string

ID of the socket session associated with this event.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20socket_session_id">Link to this property</a>

updated\_at: optional string

Timestamp when this peer event was last updated.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events%20%3E%20(items)%20%3E%20(property)%20updated_at">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_events">Link to this property</a>

<details>

<summary>

peer\_report: optional object {metadata, quality }

Peer call statistics report.

</summary>

<details>

<summary>

metadata: optional object {audio\_devices\_updates, browser\_metadata, candidate\_pairs, 12 more }

Connection and device metadata for the participant.

</summary>

<details>

<summary>

audio\_devices\_updates: optional array of object {added, removed, timestamp }

</summary>

<details>

<summary>

added: optional array of object {device\_id, kind, label }

Devices that became available.

</summary>

device\_id: optional string

ID of the device.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20audio_devices_updates%20%3E%20(items)%20%3E%20(property)%20added%20%3E%20(items)%20%3E%20(property)%20device_id">Link to this property</a>

kind: optional string

Kind of device, for example audioinput or videoinput.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20audio_devices_updates%20%3E%20(items)%20%3E%20(property)%20added%20%3E%20(items)%20%3E%20(property)%20kind">Link to this property</a>

label: optional string

Human-readable label of the device.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20audio_devices_updates%20%3E%20(items)%20%3E%20(property)%20added%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20audio_devices_updates%20%3E%20(items)%20%3E%20(property)%20added">Link to this property</a>

<details>

<summary>

removed: optional array of object {device\_id, kind, label }

Devices that became unavailable.

</summary>

device\_id: optional string

ID of the device.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20audio_devices_updates%20%3E%20(items)%20%3E%20(property)%20removed%20%3E%20(items)%20%3E%20(property)%20device_id">Link to this property</a>

kind: optional string

Kind of device, for example audioinput or videoinput.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20audio_devices_updates%20%3E%20(items)%20%3E%20(property)%20removed%20%3E%20(items)%20%3E%20(property)%20kind">Link to this property</a>

label: optional string

Human-readable label of the device.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20audio_devices_updates%20%3E%20(items)%20%3E%20(property)%20removed%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20audio_devices_updates%20%3E%20(items)%20%3E%20(property)%20removed">Link to this property</a>

timestamp: optional string

Timestamp of the device update.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20audio_devices_updates%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20audio_devices_updates">Link to this property</a>

<details>

<summary>

browser\_metadata: optional object {browser, browser\_version, engine, 2 more }

</summary>

browser: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20browser_metadata%20%3E%20(property)%20browser">Link to this property</a>

browser\_version: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20browser_metadata%20%3E%20(property)%20browser_version">Link to this property</a>

engine: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20browser_metadata%20%3E%20(property)%20engine">Link to this property</a>

user\_agent: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20browser_metadata%20%3E%20(property)%20user_agent">Link to this property</a>

webgl\_support: optional boolean

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20browser_metadata%20%3E%20(property)%20webgl_support">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20browser_metadata">Link to this property</a>

<details>

<summary>

candidate\_pairs: optional object {consuming\_transport, producing\_transport }

</summary>

<details>

<summary>

consuming\_transport: optional array of object {available\_incoming\_bitrate, available\_outgoing\_bitrate, bytes\_discarded\_on\_send, 25 more }

</summary>

available\_incoming\_bitrate: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20available_incoming_bitrate">Link to this property</a>

available\_outgoing\_bitrate: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20available_outgoing_bitrate">Link to this property</a>

bytes\_discarded\_on\_send: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20bytes_discarded_on_send">Link to this property</a>

bytes\_received: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20bytes_received">Link to this property</a>

bytes\_sent: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20bytes_sent">Link to this property</a>

current\_round\_trip\_time: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20current_round_trip_time">Link to this property</a>

last\_packet\_received\_timestamp: optional number

Epoch milliseconds when the last packet was received.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20last_packet_received_timestamp">Link to this property</a>

last\_packet\_sent\_timestamp: optional number

Epoch milliseconds when the last packet was sent.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20last_packet_sent_timestamp">Link to this property</a>

local\_candidate\_address: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20local_candidate_address">Link to this property</a>

local\_candidate\_id: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20local_candidate_id">Link to this property</a>

local\_candidate\_network\_type: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20local_candidate_network_type">Link to this property</a>

local\_candidate\_port: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20local_candidate_port">Link to this property</a>

local\_candidate\_protocol: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20local_candidate_protocol">Link to this property</a>

local\_candidate\_related\_address: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20local_candidate_related_address">Link to this property</a>

local\_candidate\_related\_port: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20local_candidate_related_port">Link to this property</a>

local\_candidate\_type: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20local_candidate_type">Link to this property</a>

local\_candidate\_url: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20local_candidate_url">Link to this property</a>

nominated: optional boolean

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20nominated">Link to this property</a>

packets\_discarded\_on\_send: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20packets_discarded_on_send">Link to this property</a>

packets\_received: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20packets_received">Link to this property</a>

packets\_sent: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20packets_sent">Link to this property</a>

remote\_candidate\_address: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20remote_candidate_address">Link to this property</a>

remote\_candidate\_id: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20remote_candidate_id">Link to this property</a>

remote\_candidate\_port: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20remote_candidate_port">Link to this property</a>

remote\_candidate\_protocol: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20remote_candidate_protocol">Link to this property</a>

remote\_candidate\_type: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20remote_candidate_type">Link to this property</a>

remote\_candidate\_url: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20remote_candidate_url">Link to this property</a>

total\_round\_trip\_time: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport%20%3E%20(items)%20%3E%20(property)%20total_round_trip_time">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20consuming_transport">Link to this property</a>

<details>

<summary>

producing\_transport: optional array of object {available\_incoming\_bitrate, available\_outgoing\_bitrate, bytes\_discarded\_on\_send, 25 more }

</summary>

available\_incoming\_bitrate: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20available_incoming_bitrate">Link to this property</a>

available\_outgoing\_bitrate: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20available_outgoing_bitrate">Link to this property</a>

bytes\_discarded\_on\_send: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20bytes_discarded_on_send">Link to this property</a>

bytes\_received: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20bytes_received">Link to this property</a>

bytes\_sent: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20bytes_sent">Link to this property</a>

current\_round\_trip\_time: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20current_round_trip_time">Link to this property</a>

last\_packet\_received\_timestamp: optional number

Epoch milliseconds when the last packet was received.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20last_packet_received_timestamp">Link to this property</a>

last\_packet\_sent\_timestamp: optional number

Epoch milliseconds when the last packet was sent.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20last_packet_sent_timestamp">Link to this property</a>

local\_candidate\_address: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20local_candidate_address">Link to this property</a>

local\_candidate\_id: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20local_candidate_id">Link to this property</a>

local\_candidate\_network\_type: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20local_candidate_network_type">Link to this property</a>

local\_candidate\_port: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20local_candidate_port">Link to this property</a>

local\_candidate\_protocol: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20local_candidate_protocol">Link to this property</a>

local\_candidate\_related\_address: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20local_candidate_related_address">Link to this property</a>

local\_candidate\_related\_port: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20local_candidate_related_port">Link to this property</a>

local\_candidate\_type: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20local_candidate_type">Link to this property</a>

local\_candidate\_url: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20local_candidate_url">Link to this property</a>

nominated: optional boolean

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20nominated">Link to this property</a>

packets\_discarded\_on\_send: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20packets_discarded_on_send">Link to this property</a>

packets\_received: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20packets_received">Link to this property</a>

packets\_sent: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20packets_sent">Link to this property</a>

remote\_candidate\_address: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20remote_candidate_address">Link to this property</a>

remote\_candidate\_id: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20remote_candidate_id">Link to this property</a>

remote\_candidate\_port: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20remote_candidate_port">Link to this property</a>

remote\_candidate\_protocol: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20remote_candidate_protocol">Link to this property</a>

remote\_candidate\_type: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20remote_candidate_type">Link to this property</a>

remote\_candidate\_url: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20remote_candidate_url">Link to this property</a>

total\_round\_trip\_time: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport%20%3E%20(items)%20%3E%20(property)%20total_round_trip_time">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs%20%3E%20(property)%20producing_transport">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20candidate_pairs">Link to this property</a>

<details>

<summary>

device\_info: optional object {cpus, is\_mobile, os, os\_version }

</summary>

cpus: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20device_info%20%3E%20(property)%20cpus">Link to this property</a>

is\_mobile: optional boolean

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20device_info%20%3E%20(property)%20is_mobile">Link to this property</a>

os: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20device_info%20%3E%20(property)%20os">Link to this property</a>

os\_version: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20device_info%20%3E%20(property)%20os_version">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20device_info">Link to this property</a>

<details>

<summary>

events: optional array of object {metadata, name, timestamp }

</summary>

<details>

<summary>

metadata: optional map\[stringor numberor boolean]

Event-specific metadata. Keys vary per event; values are primitive scalars (string, number, boolean, or null).

</summary>

One of the following:

string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20metadata%20%3E%20(items)%20%3E%20(variant)%200">Link to this property</a>

number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20metadata%20%3E%20(items)%20%3E%20(variant)%201">Link to this property</a>

boolean

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20metadata%20%3E%20(items)%20%3E%20(variant)%202">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20metadata">Link to this property</a>

name: optional string

Name of the event.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20name">Link to this property</a>

timestamp: optional string

Timestamp when the event occurred.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20events%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20events">Link to this property</a>

<details>

<summary>

ip\_information: optional object {asn, city, country, 4 more }

</summary>

<details>

<summary>

asn: optional object {asn, domain, name, 2 more }

</summary>

asn: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20ip_information%20%3E%20(property)%20asn%20%3E%20(property)%20asn">Link to this property</a>

domain: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20ip_information%20%3E%20(property)%20asn%20%3E%20(property)%20domain">Link to this property</a>

name: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20ip_information%20%3E%20(property)%20asn%20%3E%20(property)%20name">Link to this property</a>

route: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20ip_information%20%3E%20(property)%20asn%20%3E%20(property)%20route">Link to this property</a>

type: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20ip_information%20%3E%20(property)%20asn%20%3E%20(property)%20type">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20ip_information%20%3E%20(property)%20asn">Link to this property</a>

city: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20ip_information%20%3E%20(property)%20city">Link to this property</a>

country: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20ip_information%20%3E%20(property)%20country">Link to this property</a>

ipv4: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20ip_information%20%3E%20(property)%20ipv4">Link to this property</a>

org: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20ip_information%20%3E%20(property)%20org">Link to this property</a>

region: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20ip_information%20%3E%20(property)%20region">Link to this property</a>

timezone: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20ip_information%20%3E%20(property)%20timezone">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20ip_information">Link to this property</a>

<details>

<summary>

native\_metadata: optional object {audio\_encoder, video\_encoder }

</summary>

audio\_encoder: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20native_metadata%20%3E%20(property)%20audio_encoder">Link to this property</a>

video\_encoder: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20native_metadata%20%3E%20(property)%20video_encoder">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20native_metadata">Link to this property</a>

<details>

<summary>

pc\_metadata: optional array of object {effective\_network\_type, reflexive\_connectivity, relay\_connectivity, 3 more }

</summary>

effective\_network\_type: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20pc_metadata%20%3E%20(items)%20%3E%20(property)%20effective_network_type">Link to this property</a>

reflexive\_connectivity: optional boolean

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20pc_metadata%20%3E%20(items)%20%3E%20(property)%20reflexive_connectivity">Link to this property</a>

relay\_connectivity: optional boolean

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20pc_metadata%20%3E%20(items)%20%3E%20(property)%20relay_connectivity">Link to this property</a>

sdp: optional array of string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20pc_metadata%20%3E%20(items)%20%3E%20(property)%20sdp">Link to this property</a>

timestamp: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20pc_metadata%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

turn\_connectivity: optional boolean

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20pc_metadata%20%3E%20(items)%20%3E%20(property)%20turn_connectivity">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20pc_metadata">Link to this property</a>

room\_view\_type: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20room_view_type">Link to this property</a>

sdk\_name: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20sdk_name">Link to this property</a>

sdk\_type: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20sdk_type">Link to this property</a>

sdk\_version: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20sdk_version">Link to this property</a>

<details>

<summary>

selected\_device\_updates: optional array of object {device, timestamp }

</summary>

<details>

<summary>

device: optional object {device\_id, kind, label }

A media device (camera, microphone, or speaker).

</summary>

device\_id: optional string

ID of the device.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20selected_device_updates%20%3E%20(items)%20%3E%20(property)%20device%20%3E%20(property)%20device_id">Link to this property</a>

kind: optional string

Kind of device, for example audioinput or videoinput.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20selected_device_updates%20%3E%20(items)%20%3E%20(property)%20device%20%3E%20(property)%20kind">Link to this property</a>

label: optional string

Human-readable label of the device.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20selected_device_updates%20%3E%20(items)%20%3E%20(property)%20device%20%3E%20(property)%20label">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20selected_device_updates%20%3E%20(items)%20%3E%20(property)%20device">Link to this property</a>

timestamp: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20selected_device_updates%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20selected_device_updates">Link to this property</a>

<details>

<summary>

speaker\_devices\_updates: optional array of object {added, removed, timestamp }

</summary>

<details>

<summary>

added: optional array of object {device\_id, kind, label }

Devices that became available.

</summary>

device\_id: optional string

ID of the device.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20speaker_devices_updates%20%3E%20(items)%20%3E%20(property)%20added%20%3E%20(items)%20%3E%20(property)%20device_id">Link to this property</a>

kind: optional string

Kind of device, for example audioinput or videoinput.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20speaker_devices_updates%20%3E%20(items)%20%3E%20(property)%20added%20%3E%20(items)%20%3E%20(property)%20kind">Link to this property</a>

label: optional string

Human-readable label of the device.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20speaker_devices_updates%20%3E%20(items)%20%3E%20(property)%20added%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20speaker_devices_updates%20%3E%20(items)%20%3E%20(property)%20added">Link to this property</a>

<details>

<summary>

removed: optional array of object {device\_id, kind, label }

Devices that became unavailable.

</summary>

device\_id: optional string

ID of the device.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20speaker_devices_updates%20%3E%20(items)%20%3E%20(property)%20removed%20%3E%20(items)%20%3E%20(property)%20device_id">Link to this property</a>

kind: optional string

Kind of device, for example audioinput or videoinput.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20speaker_devices_updates%20%3E%20(items)%20%3E%20(property)%20removed%20%3E%20(items)%20%3E%20(property)%20kind">Link to this property</a>

label: optional string

Human-readable label of the device.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20speaker_devices_updates%20%3E%20(items)%20%3E%20(property)%20removed%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20speaker_devices_updates%20%3E%20(items)%20%3E%20(property)%20removed">Link to this property</a>

timestamp: optional string

Timestamp of the device update.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20speaker_devices_updates%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20speaker_devices_updates">Link to this property</a>

<details>

<summary>

video\_devices\_updates: optional array of object {added, removed, timestamp }

</summary>

<details>

<summary>

added: optional array of object {device\_id, kind, label }

Devices that became available.

</summary>

device\_id: optional string

ID of the device.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20video_devices_updates%20%3E%20(items)%20%3E%20(property)%20added%20%3E%20(items)%20%3E%20(property)%20device_id">Link to this property</a>

kind: optional string

Kind of device, for example audioinput or videoinput.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20video_devices_updates%20%3E%20(items)%20%3E%20(property)%20added%20%3E%20(items)%20%3E%20(property)%20kind">Link to this property</a>

label: optional string

Human-readable label of the device.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20video_devices_updates%20%3E%20(items)%20%3E%20(property)%20added%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20video_devices_updates%20%3E%20(items)%20%3E%20(property)%20added">Link to this property</a>

<details>

<summary>

removed: optional array of object {device\_id, kind, label }

Devices that became unavailable.

</summary>

device\_id: optional string

ID of the device.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20video_devices_updates%20%3E%20(items)%20%3E%20(property)%20removed%20%3E%20(items)%20%3E%20(property)%20device_id">Link to this property</a>

kind: optional string

Kind of device, for example audioinput or videoinput.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20video_devices_updates%20%3E%20(items)%20%3E%20(property)%20removed%20%3E%20(items)%20%3E%20(property)%20kind">Link to this property</a>

label: optional string

Human-readable label of the device.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20video_devices_updates%20%3E%20(items)%20%3E%20(property)%20removed%20%3E%20(items)%20%3E%20(property)%20label">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20video_devices_updates%20%3E%20(items)%20%3E%20(property)%20removed">Link to this property</a>

timestamp: optional string

Timestamp of the device update.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20video_devices_updates%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata%20%3E%20(property)%20video_devices_updates">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20metadata">Link to this property</a>

<details>

<summary>

quality: optional object {audio\_consumer, audio\_consumer\_cumulative, audio\_producer, 13 more }

Media quality statistics for the participant.

</summary>

<details>

<summary>

audio\_consumer: optional array of object {bytes\_received, concealment\_events, consumer\_id, 11 more }

</summary>

bytes\_received: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer%20%3E%20(items)%20%3E%20(property)%20bytes_received">Link to this property</a>

concealment\_events: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer%20%3E%20(items)%20%3E%20(property)%20concealment_events">Link to this property</a>

consumer\_id: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer%20%3E%20(items)%20%3E%20(property)%20consumer_id">Link to this property</a>

jitter: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer%20%3E%20(items)%20%3E%20(property)%20jitter">Link to this property</a>

jitter\_buffer\_delay: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer%20%3E%20(items)%20%3E%20(property)%20jitter_buffer_delay">Link to this property</a>

jitter\_buffer\_emitted\_count: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer%20%3E%20(items)%20%3E%20(property)%20jitter_buffer_emitted_count">Link to this property</a>

mid: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer%20%3E%20(items)%20%3E%20(property)%20mid">Link to this property</a>

mos\_quality: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer%20%3E%20(items)%20%3E%20(property)%20mos_quality">Link to this property</a>

packets\_lost: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer%20%3E%20(items)%20%3E%20(property)%20packets_lost">Link to this property</a>

packets\_received: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer%20%3E%20(items)%20%3E%20(property)%20packets_received">Link to this property</a>

peer\_id: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer%20%3E%20(items)%20%3E%20(property)%20peer_id">Link to this property</a>

producer\_id: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer%20%3E%20(items)%20%3E%20(property)%20producer_id">Link to this property</a>

ssrc: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer%20%3E%20(items)%20%3E%20(property)%20ssrc">Link to this property</a>

timestamp: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer">Link to this property</a>

<details>

<summary>

audio\_consumer\_cumulative: optional object {jitter\_buffer\_delay, packet\_loss, quality\_mos }

Aggregated inbound (consumer) audio statistics for the session.

</summary>

<details>

<summary>

jitter\_buffer\_delay: optional object {"100ms\_or\_greater\_event\_fraction", "250ms\_or\_greater\_event\_fraction", "500ms\_or\_greater\_event\_fraction", avg }

Cumulative latency distribution (milliseconds-based thresholds).

</summary>

"100ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer_cumulative%20%3E%20(property)%20jitter_buffer_delay%20%3E%20(property)%20100ms_or_greater_event_fraction">Link to this property</a>

"250ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer_cumulative%20%3E%20(property)%20jitter_buffer_delay%20%3E%20(property)%20250ms_or_greater_event_fraction">Link to this property</a>

"500ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer_cumulative%20%3E%20(property)%20jitter_buffer_delay%20%3E%20(property)%20500ms_or_greater_event_fraction">Link to this property</a>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer_cumulative%20%3E%20(property)%20jitter_buffer_delay%20%3E%20(property)%20avg">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer_cumulative%20%3E%20(property)%20jitter_buffer_delay">Link to this property</a>

<details>

<summary>

packet\_loss: optional object {"10\_or\_greater\_event\_fraction", "25\_or\_greater\_event\_fraction", "5\_or\_greater\_event\_fraction", 2 more }

Cumulative packet loss distribution.

</summary>

"10\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2010_or_greater_event_fraction">Link to this property</a>

"25\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2025_or_greater_event_fraction">Link to this property</a>

"5\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%205_or_greater_event_fraction">Link to this property</a>

"50\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2050_or_greater_event_fraction">Link to this property</a>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%20avg">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer_cumulative%20%3E%20(property)%20packet_loss">Link to this property</a>

<details>

<summary>

quality\_mos: optional object {avg, p50, p75, p90 }

Distribution summary with average and percentiles.

</summary>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20avg">Link to this property</a>

p50: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p50">Link to this property</a>

p75: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p75">Link to this property</a>

p90: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p90">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer_cumulative%20%3E%20(property)%20quality_mos">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_consumer_cumulative">Link to this property</a>

<details>

<summary>

audio\_producer: optional array of object {bytes\_sent, jitter, mid, 7 more }

</summary>

bytes\_sent: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer%20%3E%20(items)%20%3E%20(property)%20bytes_sent">Link to this property</a>

jitter: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer%20%3E%20(items)%20%3E%20(property)%20jitter">Link to this property</a>

mid: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer%20%3E%20(items)%20%3E%20(property)%20mid">Link to this property</a>

mos\_quality: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer%20%3E%20(items)%20%3E%20(property)%20mos_quality">Link to this property</a>

packets\_lost: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer%20%3E%20(items)%20%3E%20(property)%20packets_lost">Link to this property</a>

packets\_sent: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer%20%3E%20(items)%20%3E%20(property)%20packets_sent">Link to this property</a>

producer\_id: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer%20%3E%20(items)%20%3E%20(property)%20producer_id">Link to this property</a>

rtt: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer%20%3E%20(items)%20%3E%20(property)%20rtt">Link to this property</a>

ssrc: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer%20%3E%20(items)%20%3E%20(property)%20ssrc">Link to this property</a>

timestamp: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer">Link to this property</a>

<details>

<summary>

audio\_producer\_cumulative: optional object {packet\_loss, quality\_mos, rtt }

Aggregated outbound (producer) audio statistics for the session.

</summary>

<details>

<summary>

packet\_loss: optional object {"10\_or\_greater\_event\_fraction", "25\_or\_greater\_event\_fraction", "5\_or\_greater\_event\_fraction", 2 more }

Cumulative packet loss distribution.

</summary>

"10\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2010_or_greater_event_fraction">Link to this property</a>

"25\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2025_or_greater_event_fraction">Link to this property</a>

"5\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%205_or_greater_event_fraction">Link to this property</a>

"50\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2050_or_greater_event_fraction">Link to this property</a>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%20avg">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer_cumulative%20%3E%20(property)%20packet_loss">Link to this property</a>

<details>

<summary>

quality\_mos: optional object {avg, p50, p75, p90 }

Distribution summary with average and percentiles.

</summary>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20avg">Link to this property</a>

p50: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p50">Link to this property</a>

p75: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p75">Link to this property</a>

p90: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p90">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer_cumulative%20%3E%20(property)%20quality_mos">Link to this property</a>

<details>

<summary>

rtt: optional object {"100ms\_or\_greater\_event\_fraction", "250ms\_or\_greater\_event\_fraction", "500ms\_or\_greater\_event\_fraction", avg }

Cumulative latency distribution (milliseconds-based thresholds).

</summary>

"100ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer_cumulative%20%3E%20(property)%20rtt%20%3E%20(property)%20100ms_or_greater_event_fraction">Link to this property</a>

"250ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer_cumulative%20%3E%20(property)%20rtt%20%3E%20(property)%20250ms_or_greater_event_fraction">Link to this property</a>

"500ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer_cumulative%20%3E%20(property)%20rtt%20%3E%20(property)%20500ms_or_greater_event_fraction">Link to this property</a>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer_cumulative%20%3E%20(property)%20rtt%20%3E%20(property)%20avg">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer_cumulative%20%3E%20(property)%20rtt">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20audio_producer_cumulative">Link to this property</a>

<details>

<summary>

screenshare\_audio\_consumer: optional array of object {bytes\_received, concealment\_events, consumer\_id, 11 more }

</summary>

bytes\_received: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer%20%3E%20(items)%20%3E%20(property)%20bytes_received">Link to this property</a>

concealment\_events: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer%20%3E%20(items)%20%3E%20(property)%20concealment_events">Link to this property</a>

consumer\_id: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer%20%3E%20(items)%20%3E%20(property)%20consumer_id">Link to this property</a>

jitter: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer%20%3E%20(items)%20%3E%20(property)%20jitter">Link to this property</a>

jitter\_buffer\_delay: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer%20%3E%20(items)%20%3E%20(property)%20jitter_buffer_delay">Link to this property</a>

jitter\_buffer\_emitted\_count: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer%20%3E%20(items)%20%3E%20(property)%20jitter_buffer_emitted_count">Link to this property</a>

mid: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer%20%3E%20(items)%20%3E%20(property)%20mid">Link to this property</a>

mos\_quality: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer%20%3E%20(items)%20%3E%20(property)%20mos_quality">Link to this property</a>

packets\_lost: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer%20%3E%20(items)%20%3E%20(property)%20packets_lost">Link to this property</a>

packets\_received: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer%20%3E%20(items)%20%3E%20(property)%20packets_received">Link to this property</a>

peer\_id: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer%20%3E%20(items)%20%3E%20(property)%20peer_id">Link to this property</a>

producer\_id: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer%20%3E%20(items)%20%3E%20(property)%20producer_id">Link to this property</a>

ssrc: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer%20%3E%20(items)%20%3E%20(property)%20ssrc">Link to this property</a>

timestamp: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer">Link to this property</a>

<details>

<summary>

screenshare\_audio\_consumer\_cumulative: optional object {jitter\_buffer\_delay, packet\_loss, quality\_mos }

Aggregated inbound (consumer) audio statistics for the session.

</summary>

<details>

<summary>

jitter\_buffer\_delay: optional object {"100ms\_or\_greater\_event\_fraction", "250ms\_or\_greater\_event\_fraction", "500ms\_or\_greater\_event\_fraction", avg }

Cumulative latency distribution (milliseconds-based thresholds).

</summary>

"100ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer_cumulative%20%3E%20(property)%20jitter_buffer_delay%20%3E%20(property)%20100ms_or_greater_event_fraction">Link to this property</a>

"250ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer_cumulative%20%3E%20(property)%20jitter_buffer_delay%20%3E%20(property)%20250ms_or_greater_event_fraction">Link to this property</a>

"500ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer_cumulative%20%3E%20(property)%20jitter_buffer_delay%20%3E%20(property)%20500ms_or_greater_event_fraction">Link to this property</a>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer_cumulative%20%3E%20(property)%20jitter_buffer_delay%20%3E%20(property)%20avg">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer_cumulative%20%3E%20(property)%20jitter_buffer_delay">Link to this property</a>

<details>

<summary>

packet\_loss: optional object {"10\_or\_greater\_event\_fraction", "25\_or\_greater\_event\_fraction", "5\_or\_greater\_event\_fraction", 2 more }

Cumulative packet loss distribution.

</summary>

"10\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2010_or_greater_event_fraction">Link to this property</a>

"25\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2025_or_greater_event_fraction">Link to this property</a>

"5\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%205_or_greater_event_fraction">Link to this property</a>

"50\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2050_or_greater_event_fraction">Link to this property</a>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%20avg">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer_cumulative%20%3E%20(property)%20packet_loss">Link to this property</a>

<details>

<summary>

quality\_mos: optional object {avg, p50, p75, p90 }

Distribution summary with average and percentiles.

</summary>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20avg">Link to this property</a>

p50: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p50">Link to this property</a>

p75: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p75">Link to this property</a>

p90: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p90">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer_cumulative%20%3E%20(property)%20quality_mos">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_consumer_cumulative">Link to this property</a>

<details>

<summary>

screenshare\_audio\_producer: optional array of object {bytes\_sent, jitter, mid, 7 more }

</summary>

bytes\_sent: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer%20%3E%20(items)%20%3E%20(property)%20bytes_sent">Link to this property</a>

jitter: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer%20%3E%20(items)%20%3E%20(property)%20jitter">Link to this property</a>

mid: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer%20%3E%20(items)%20%3E%20(property)%20mid">Link to this property</a>

mos\_quality: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer%20%3E%20(items)%20%3E%20(property)%20mos_quality">Link to this property</a>

packets\_lost: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer%20%3E%20(items)%20%3E%20(property)%20packets_lost">Link to this property</a>

packets\_sent: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer%20%3E%20(items)%20%3E%20(property)%20packets_sent">Link to this property</a>

producer\_id: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer%20%3E%20(items)%20%3E%20(property)%20producer_id">Link to this property</a>

rtt: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer%20%3E%20(items)%20%3E%20(property)%20rtt">Link to this property</a>

ssrc: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer%20%3E%20(items)%20%3E%20(property)%20ssrc">Link to this property</a>

timestamp: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer">Link to this property</a>

<details>

<summary>

screenshare\_audio\_producer\_cumulative: optional object {packet\_loss, quality\_mos, rtt }

Aggregated outbound (producer) audio statistics for the session.

</summary>

<details>

<summary>

packet\_loss: optional object {"10\_or\_greater\_event\_fraction", "25\_or\_greater\_event\_fraction", "5\_or\_greater\_event\_fraction", 2 more }

Cumulative packet loss distribution.

</summary>

"10\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2010_or_greater_event_fraction">Link to this property</a>

"25\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2025_or_greater_event_fraction">Link to this property</a>

"5\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%205_or_greater_event_fraction">Link to this property</a>

"50\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2050_or_greater_event_fraction">Link to this property</a>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%20avg">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer_cumulative%20%3E%20(property)%20packet_loss">Link to this property</a>

<details>

<summary>

quality\_mos: optional object {avg, p50, p75, p90 }

Distribution summary with average and percentiles.

</summary>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20avg">Link to this property</a>

p50: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p50">Link to this property</a>

p75: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p75">Link to this property</a>

p90: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p90">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer_cumulative%20%3E%20(property)%20quality_mos">Link to this property</a>

<details>

<summary>

rtt: optional object {"100ms\_or\_greater\_event\_fraction", "250ms\_or\_greater\_event\_fraction", "500ms\_or\_greater\_event\_fraction", avg }

Cumulative latency distribution (milliseconds-based thresholds).

</summary>

"100ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer_cumulative%20%3E%20(property)%20rtt%20%3E%20(property)%20100ms_or_greater_event_fraction">Link to this property</a>

"250ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer_cumulative%20%3E%20(property)%20rtt%20%3E%20(property)%20250ms_or_greater_event_fraction">Link to this property</a>

"500ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer_cumulative%20%3E%20(property)%20rtt%20%3E%20(property)%20500ms_or_greater_event_fraction">Link to this property</a>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer_cumulative%20%3E%20(property)%20rtt%20%3E%20(property)%20avg">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer_cumulative%20%3E%20(property)%20rtt">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_audio_producer_cumulative">Link to this property</a>

<details>

<summary>

screenshare\_video\_consumer: optional array of object {bytes\_received, consumer\_id, fir\_count, 17 more }

</summary>

bytes\_received: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer%20%3E%20(items)%20%3E%20(property)%20bytes_received">Link to this property</a>

consumer\_id: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer%20%3E%20(items)%20%3E%20(property)%20consumer_id">Link to this property</a>

fir\_count: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer%20%3E%20(items)%20%3E%20(property)%20fir_count">Link to this property</a>

frame\_height: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer%20%3E%20(items)%20%3E%20(property)%20frame_height">Link to this property</a>

frame\_width: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer%20%3E%20(items)%20%3E%20(property)%20frame_width">Link to this property</a>

frames\_decoded: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer%20%3E%20(items)%20%3E%20(property)%20frames_decoded">Link to this property</a>

frames\_dropped: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer%20%3E%20(items)%20%3E%20(property)%20frames_dropped">Link to this property</a>

frames\_per\_second: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer%20%3E%20(items)%20%3E%20(property)%20frames_per_second">Link to this property</a>

jitter: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer%20%3E%20(items)%20%3E%20(property)%20jitter">Link to this property</a>

jitter\_buffer\_delay: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer%20%3E%20(items)%20%3E%20(property)%20jitter_buffer_delay">Link to this property</a>

jitter\_buffer\_emitted\_count: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer%20%3E%20(items)%20%3E%20(property)%20jitter_buffer_emitted_count">Link to this property</a>

key\_frames\_decoded: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer%20%3E%20(items)%20%3E%20(property)%20key_frames_decoded">Link to this property</a>

mid: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer%20%3E%20(items)%20%3E%20(property)%20mid">Link to this property</a>

mos\_quality: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer%20%3E%20(items)%20%3E%20(property)%20mos_quality">Link to this property</a>

packets\_lost: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer%20%3E%20(items)%20%3E%20(property)%20packets_lost">Link to this property</a>

packets\_received: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer%20%3E%20(items)%20%3E%20(property)%20packets_received">Link to this property</a>

peer\_id: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer%20%3E%20(items)%20%3E%20(property)%20peer_id">Link to this property</a>

producer\_id: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer%20%3E%20(items)%20%3E%20(property)%20producer_id">Link to this property</a>

ssrc: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer%20%3E%20(items)%20%3E%20(property)%20ssrc">Link to this property</a>

timestamp: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer">Link to this property</a>

<details>

<summary>

screenshare\_video\_consumer\_cumulative: optional object {frame\_per\_second, frame\_width, issues, 4 more }

Aggregated inbound (consumer) video statistics for the session.

</summary>

<details>

<summary>

frame\_per\_second: optional object {avg, p50, p75, p90 }

Distribution summary with average and percentiles.

</summary>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20frame_per_second%20%3E%20(property)%20avg">Link to this property</a>

p50: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20frame_per_second%20%3E%20(property)%20p50">Link to this property</a>

p75: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20frame_per_second%20%3E%20(property)%20p75">Link to this property</a>

p90: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20frame_per_second%20%3E%20(property)%20p90">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20frame_per_second">Link to this property</a>

<details>

<summary>

frame\_width: optional object {avg, p50, p75, p90 }

Distribution summary with average and percentiles.

</summary>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20frame_width%20%3E%20(property)%20avg">Link to this property</a>

p50: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20frame_width%20%3E%20(property)%20p50">Link to this property</a>

p75: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20frame_width%20%3E%20(property)%20p75">Link to this property</a>

p90: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20frame_width%20%3E%20(property)%20p90">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20frame_width">Link to this property</a>

<details>

<summary>

issues: optional object {lag\_fraction, no\_video\_fraction, poor\_resolution\_fraction }

</summary>

lag\_fraction: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20issues%20%3E%20(property)%20lag_fraction">Link to this property</a>

no\_video\_fraction: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20issues%20%3E%20(property)%20no_video_fraction">Link to this property</a>

poor\_resolution\_fraction: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20issues%20%3E%20(property)%20poor_resolution_fraction">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20issues">Link to this property</a>

<details>

<summary>

jitter\_buffer\_delay: optional object {"100ms\_or\_greater\_event\_fraction", "250ms\_or\_greater\_event\_fraction", "500ms\_or\_greater\_event\_fraction", avg }

Cumulative latency distribution (milliseconds-based thresholds).

</summary>

"100ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20jitter_buffer_delay%20%3E%20(property)%20100ms_or_greater_event_fraction">Link to this property</a>

"250ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20jitter_buffer_delay%20%3E%20(property)%20250ms_or_greater_event_fraction">Link to this property</a>

"500ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20jitter_buffer_delay%20%3E%20(property)%20500ms_or_greater_event_fraction">Link to this property</a>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20jitter_buffer_delay%20%3E%20(property)%20avg">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20jitter_buffer_delay">Link to this property</a>

key\_frames\_decoded\_fraction: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20key_frames_decoded_fraction">Link to this property</a>

<details>

<summary>

packet\_loss: optional object {"10\_or\_greater\_event\_fraction", "25\_or\_greater\_event\_fraction", "5\_or\_greater\_event\_fraction", 2 more }

Cumulative packet loss distribution.

</summary>

"10\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2010_or_greater_event_fraction">Link to this property</a>

"25\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2025_or_greater_event_fraction">Link to this property</a>

"5\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%205_or_greater_event_fraction">Link to this property</a>

"50\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2050_or_greater_event_fraction">Link to this property</a>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%20avg">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20packet_loss">Link to this property</a>

<details>

<summary>

quality\_mos: optional object {avg, p50, p75, p90 }

Distribution summary with average and percentiles.

</summary>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20avg">Link to this property</a>

p50: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p50">Link to this property</a>

p75: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p75">Link to this property</a>

p90: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p90">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative%20%3E%20(property)%20quality_mos">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_consumer_cumulative">Link to this property</a>

<details>

<summary>

screenshare\_video\_producer: optional array of object {bytes\_sent, fir\_count, frame\_height, 17 more }

</summary>

bytes\_sent: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20bytes_sent">Link to this property</a>

fir\_count: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20fir_count">Link to this property</a>

frame\_height: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20frame_height">Link to this property</a>

frame\_width: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20frame_width">Link to this property</a>

frames\_encoded: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20frames_encoded">Link to this property</a>

frames\_per\_second: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20frames_per_second">Link to this property</a>

jitter: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20jitter">Link to this property</a>

key\_frames\_encoded: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20key_frames_encoded">Link to this property</a>

mid: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20mid">Link to this property</a>

mos\_quality: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20mos_quality">Link to this property</a>

packets\_lost: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20packets_lost">Link to this property</a>

packets\_sent: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20packets_sent">Link to this property</a>

pli\_count: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20pli_count">Link to this property</a>

producer\_id: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20producer_id">Link to this property</a>

<details>

<summary>

quality\_limitation\_durations: optional object {bandwidth, cpu, none, other }

</summary>

bandwidth: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20quality_limitation_durations%20%3E%20(property)%20bandwidth">Link to this property</a>

cpu: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20quality_limitation_durations%20%3E%20(property)%20cpu">Link to this property</a>

none: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20quality_limitation_durations%20%3E%20(property)%20none">Link to this property</a>

other: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20quality_limitation_durations%20%3E%20(property)%20other">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20quality_limitation_durations">Link to this property</a>

<details>

<summary>

quality\_limitation\_reason: optional "cpu"or "bandwidth"or "none"or "other"

</summary>

One of the following:

"cpu"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20quality_limitation_reason%20%3E%20(member)%200">Link to this property</a>

"bandwidth"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20quality_limitation_reason%20%3E%20(member)%201">Link to this property</a>

"none"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20quality_limitation_reason%20%3E%20(member)%202">Link to this property</a>

"other"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20quality_limitation_reason%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20quality_limitation_reason">Link to this property</a>

quality\_limitation\_resolution\_changes: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20quality_limitation_resolution_changes">Link to this property</a>

rtt: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20rtt">Link to this property</a>

ssrc: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20ssrc">Link to this property</a>

timestamp: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer">Link to this property</a>

<details>

<summary>

screenshare\_video\_producer\_cumulative: optional object {frame\_per\_second, frame\_width, high\_negative\_feedback\_fraction, 5 more }

Aggregated outbound (producer) video statistics for the session.

</summary>

<details>

<summary>

frame\_per\_second: optional object {avg, p50, p75, p90 }

Distribution summary with average and percentiles.

</summary>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20frame_per_second%20%3E%20(property)%20avg">Link to this property</a>

p50: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20frame_per_second%20%3E%20(property)%20p50">Link to this property</a>

p75: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20frame_per_second%20%3E%20(property)%20p75">Link to this property</a>

p90: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20frame_per_second%20%3E%20(property)%20p90">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20frame_per_second">Link to this property</a>

<details>

<summary>

frame\_width: optional object {avg, p50, p75, p90 }

Distribution summary with average and percentiles.

</summary>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20frame_width%20%3E%20(property)%20avg">Link to this property</a>

p50: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20frame_width%20%3E%20(property)%20p50">Link to this property</a>

p75: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20frame_width%20%3E%20(property)%20p75">Link to this property</a>

p90: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20frame_width%20%3E%20(property)%20p90">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20frame_width">Link to this property</a>

high\_negative\_feedback\_fraction: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20high_negative_feedback_fraction">Link to this property</a>

<details>

<summary>

issues: optional object {bandwidth\_quality\_limitation\_fraction, cpu\_quality\_limitation\_fraction, no\_video\_fraction, 2 more }

</summary>

bandwidth\_quality\_limitation\_fraction: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20issues%20%3E%20(property)%20bandwidth_quality_limitation_fraction">Link to this property</a>

cpu\_quality\_limitation\_fraction: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20issues%20%3E%20(property)%20cpu_quality_limitation_fraction">Link to this property</a>

no\_video\_fraction: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20issues%20%3E%20(property)%20no_video_fraction">Link to this property</a>

poor\_resolution\_fraction: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20issues%20%3E%20(property)%20poor_resolution_fraction">Link to this property</a>

quality\_limitation\_fraction: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20issues%20%3E%20(property)%20quality_limitation_fraction">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20issues">Link to this property</a>

key\_frames\_encoded\_fraction: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20key_frames_encoded_fraction">Link to this property</a>

<details>

<summary>

packet\_loss: optional object {"10\_or\_greater\_event\_fraction", "25\_or\_greater\_event\_fraction", "5\_or\_greater\_event\_fraction", 2 more }

Cumulative packet loss distribution.

</summary>

"10\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2010_or_greater_event_fraction">Link to this property</a>

"25\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2025_or_greater_event_fraction">Link to this property</a>

"5\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%205_or_greater_event_fraction">Link to this property</a>

"50\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2050_or_greater_event_fraction">Link to this property</a>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%20avg">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20packet_loss">Link to this property</a>

<details>

<summary>

quality\_mos: optional object {avg, p50, p75, p90 }

Distribution summary with average and percentiles.

</summary>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20avg">Link to this property</a>

p50: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p50">Link to this property</a>

p75: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p75">Link to this property</a>

p90: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p90">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20quality_mos">Link to this property</a>

<details>

<summary>

rtt: optional object {"100ms\_or\_greater\_event\_fraction", "250ms\_or\_greater\_event\_fraction", "500ms\_or\_greater\_event\_fraction", avg }

Cumulative latency distribution (milliseconds-based thresholds).

</summary>

"100ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20rtt%20%3E%20(property)%20100ms_or_greater_event_fraction">Link to this property</a>

"250ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20rtt%20%3E%20(property)%20250ms_or_greater_event_fraction">Link to this property</a>

"500ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20rtt%20%3E%20(property)%20500ms_or_greater_event_fraction">Link to this property</a>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20rtt%20%3E%20(property)%20avg">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative%20%3E%20(property)%20rtt">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20screenshare_video_producer_cumulative">Link to this property</a>

<details>

<summary>

video\_consumer: optional array of object {bytes\_received, consumer\_id, fir\_count, 17 more }

</summary>

bytes\_received: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer%20%3E%20(items)%20%3E%20(property)%20bytes_received">Link to this property</a>

consumer\_id: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer%20%3E%20(items)%20%3E%20(property)%20consumer_id">Link to this property</a>

fir\_count: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer%20%3E%20(items)%20%3E%20(property)%20fir_count">Link to this property</a>

frame\_height: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer%20%3E%20(items)%20%3E%20(property)%20frame_height">Link to this property</a>

frame\_width: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer%20%3E%20(items)%20%3E%20(property)%20frame_width">Link to this property</a>

frames\_decoded: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer%20%3E%20(items)%20%3E%20(property)%20frames_decoded">Link to this property</a>

frames\_dropped: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer%20%3E%20(items)%20%3E%20(property)%20frames_dropped">Link to this property</a>

frames\_per\_second: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer%20%3E%20(items)%20%3E%20(property)%20frames_per_second">Link to this property</a>

jitter: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer%20%3E%20(items)%20%3E%20(property)%20jitter">Link to this property</a>

jitter\_buffer\_delay: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer%20%3E%20(items)%20%3E%20(property)%20jitter_buffer_delay">Link to this property</a>

jitter\_buffer\_emitted\_count: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer%20%3E%20(items)%20%3E%20(property)%20jitter_buffer_emitted_count">Link to this property</a>

key\_frames\_decoded: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer%20%3E%20(items)%20%3E%20(property)%20key_frames_decoded">Link to this property</a>

mid: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer%20%3E%20(items)%20%3E%20(property)%20mid">Link to this property</a>

mos\_quality: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer%20%3E%20(items)%20%3E%20(property)%20mos_quality">Link to this property</a>

packets\_lost: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer%20%3E%20(items)%20%3E%20(property)%20packets_lost">Link to this property</a>

packets\_received: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer%20%3E%20(items)%20%3E%20(property)%20packets_received">Link to this property</a>

peer\_id: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer%20%3E%20(items)%20%3E%20(property)%20peer_id">Link to this property</a>

producer\_id: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer%20%3E%20(items)%20%3E%20(property)%20producer_id">Link to this property</a>

ssrc: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer%20%3E%20(items)%20%3E%20(property)%20ssrc">Link to this property</a>

timestamp: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer">Link to this property</a>

<details>

<summary>

video\_consumer\_cumulative: optional object {frame\_per\_second, frame\_width, issues, 4 more }

Aggregated inbound (consumer) video statistics for the session.

</summary>

<details>

<summary>

frame\_per\_second: optional object {avg, p50, p75, p90 }

Distribution summary with average and percentiles.

</summary>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20frame_per_second%20%3E%20(property)%20avg">Link to this property</a>

p50: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20frame_per_second%20%3E%20(property)%20p50">Link to this property</a>

p75: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20frame_per_second%20%3E%20(property)%20p75">Link to this property</a>

p90: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20frame_per_second%20%3E%20(property)%20p90">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20frame_per_second">Link to this property</a>

<details>

<summary>

frame\_width: optional object {avg, p50, p75, p90 }

Distribution summary with average and percentiles.

</summary>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20frame_width%20%3E%20(property)%20avg">Link to this property</a>

p50: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20frame_width%20%3E%20(property)%20p50">Link to this property</a>

p75: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20frame_width%20%3E%20(property)%20p75">Link to this property</a>

p90: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20frame_width%20%3E%20(property)%20p90">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20frame_width">Link to this property</a>

<details>

<summary>

issues: optional object {lag\_fraction, no\_video\_fraction, poor\_resolution\_fraction }

</summary>

lag\_fraction: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20issues%20%3E%20(property)%20lag_fraction">Link to this property</a>

no\_video\_fraction: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20issues%20%3E%20(property)%20no_video_fraction">Link to this property</a>

poor\_resolution\_fraction: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20issues%20%3E%20(property)%20poor_resolution_fraction">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20issues">Link to this property</a>

<details>

<summary>

jitter\_buffer\_delay: optional object {"100ms\_or\_greater\_event\_fraction", "250ms\_or\_greater\_event\_fraction", "500ms\_or\_greater\_event\_fraction", avg }

Cumulative latency distribution (milliseconds-based thresholds).

</summary>

"100ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20jitter_buffer_delay%20%3E%20(property)%20100ms_or_greater_event_fraction">Link to this property</a>

"250ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20jitter_buffer_delay%20%3E%20(property)%20250ms_or_greater_event_fraction">Link to this property</a>

"500ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20jitter_buffer_delay%20%3E%20(property)%20500ms_or_greater_event_fraction">Link to this property</a>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20jitter_buffer_delay%20%3E%20(property)%20avg">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20jitter_buffer_delay">Link to this property</a>

key\_frames\_decoded\_fraction: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20key_frames_decoded_fraction">Link to this property</a>

<details>

<summary>

packet\_loss: optional object {"10\_or\_greater\_event\_fraction", "25\_or\_greater\_event\_fraction", "5\_or\_greater\_event\_fraction", 2 more }

Cumulative packet loss distribution.

</summary>

"10\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2010_or_greater_event_fraction">Link to this property</a>

"25\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2025_or_greater_event_fraction">Link to this property</a>

"5\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%205_or_greater_event_fraction">Link to this property</a>

"50\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2050_or_greater_event_fraction">Link to this property</a>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%20avg">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20packet_loss">Link to this property</a>

<details>

<summary>

quality\_mos: optional object {avg, p50, p75, p90 }

Distribution summary with average and percentiles.

</summary>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20avg">Link to this property</a>

p50: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p50">Link to this property</a>

p75: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p75">Link to this property</a>

p90: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p90">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative%20%3E%20(property)%20quality_mos">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_consumer_cumulative">Link to this property</a>

<details>

<summary>

video\_producer: optional array of object {bytes\_sent, fir\_count, frame\_height, 17 more }

</summary>

bytes\_sent: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20bytes_sent">Link to this property</a>

fir\_count: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20fir_count">Link to this property</a>

frame\_height: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20frame_height">Link to this property</a>

frame\_width: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20frame_width">Link to this property</a>

frames\_encoded: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20frames_encoded">Link to this property</a>

frames\_per\_second: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20frames_per_second">Link to this property</a>

jitter: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20jitter">Link to this property</a>

key\_frames\_encoded: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20key_frames_encoded">Link to this property</a>

mid: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20mid">Link to this property</a>

mos\_quality: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20mos_quality">Link to this property</a>

packets\_lost: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20packets_lost">Link to this property</a>

packets\_sent: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20packets_sent">Link to this property</a>

pli\_count: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20pli_count">Link to this property</a>

producer\_id: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20producer_id">Link to this property</a>

<details>

<summary>

quality\_limitation\_durations: optional object {bandwidth, cpu, none, other }

</summary>

bandwidth: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20quality_limitation_durations%20%3E%20(property)%20bandwidth">Link to this property</a>

cpu: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20quality_limitation_durations%20%3E%20(property)%20cpu">Link to this property</a>

none: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20quality_limitation_durations%20%3E%20(property)%20none">Link to this property</a>

other: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20quality_limitation_durations%20%3E%20(property)%20other">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20quality_limitation_durations">Link to this property</a>

<details>

<summary>

quality\_limitation\_reason: optional "cpu"or "bandwidth"or "none"or "other"

</summary>

One of the following:

"cpu"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20quality_limitation_reason%20%3E%20(member)%200">Link to this property</a>

"bandwidth"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20quality_limitation_reason%20%3E%20(member)%201">Link to this property</a>

"none"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20quality_limitation_reason%20%3E%20(member)%202">Link to this property</a>

"other"

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20quality_limitation_reason%20%3E%20(member)%203">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20quality_limitation_reason">Link to this property</a>

quality\_limitation\_resolution\_changes: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20quality_limitation_resolution_changes">Link to this property</a>

rtt: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20rtt">Link to this property</a>

ssrc: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20ssrc">Link to this property</a>

timestamp: optional string

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer%20%3E%20(items)%20%3E%20(property)%20timestamp">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer">Link to this property</a>

<details>

<summary>

video\_producer\_cumulative: optional object {frame\_per\_second, frame\_width, high\_negative\_feedback\_fraction, 5 more }

Aggregated outbound (producer) video statistics for the session.

</summary>

<details>

<summary>

frame\_per\_second: optional object {avg, p50, p75, p90 }

Distribution summary with average and percentiles.

</summary>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20frame_per_second%20%3E%20(property)%20avg">Link to this property</a>

p50: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20frame_per_second%20%3E%20(property)%20p50">Link to this property</a>

p75: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20frame_per_second%20%3E%20(property)%20p75">Link to this property</a>

p90: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20frame_per_second%20%3E%20(property)%20p90">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20frame_per_second">Link to this property</a>

<details>

<summary>

frame\_width: optional object {avg, p50, p75, p90 }

Distribution summary with average and percentiles.

</summary>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20frame_width%20%3E%20(property)%20avg">Link to this property</a>

p50: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20frame_width%20%3E%20(property)%20p50">Link to this property</a>

p75: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20frame_width%20%3E%20(property)%20p75">Link to this property</a>

p90: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20frame_width%20%3E%20(property)%20p90">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20frame_width">Link to this property</a>

high\_negative\_feedback\_fraction: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20high_negative_feedback_fraction">Link to this property</a>

<details>

<summary>

issues: optional object {bandwidth\_quality\_limitation\_fraction, cpu\_quality\_limitation\_fraction, no\_video\_fraction, 2 more }

</summary>

bandwidth\_quality\_limitation\_fraction: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20issues%20%3E%20(property)%20bandwidth_quality_limitation_fraction">Link to this property</a>

cpu\_quality\_limitation\_fraction: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20issues%20%3E%20(property)%20cpu_quality_limitation_fraction">Link to this property</a>

no\_video\_fraction: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20issues%20%3E%20(property)%20no_video_fraction">Link to this property</a>

poor\_resolution\_fraction: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20issues%20%3E%20(property)%20poor_resolution_fraction">Link to this property</a>

quality\_limitation\_fraction: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20issues%20%3E%20(property)%20quality_limitation_fraction">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20issues">Link to this property</a>

key\_frames\_encoded\_fraction: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20key_frames_encoded_fraction">Link to this property</a>

<details>

<summary>

packet\_loss: optional object {"10\_or\_greater\_event\_fraction", "25\_or\_greater\_event\_fraction", "5\_or\_greater\_event\_fraction", 2 more }

Cumulative packet loss distribution.

</summary>

"10\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2010_or_greater_event_fraction">Link to this property</a>

"25\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2025_or_greater_event_fraction">Link to this property</a>

"5\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%205_or_greater_event_fraction">Link to this property</a>

"50\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%2050_or_greater_event_fraction">Link to this property</a>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20packet_loss%20%3E%20(property)%20avg">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20packet_loss">Link to this property</a>

<details>

<summary>

quality\_mos: optional object {avg, p50, p75, p90 }

Distribution summary with average and percentiles.

</summary>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20avg">Link to this property</a>

p50: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p50">Link to this property</a>

p75: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p75">Link to this property</a>

p90: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20quality_mos%20%3E%20(property)%20p90">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20quality_mos">Link to this property</a>

<details>

<summary>

rtt: optional object {"100ms\_or\_greater\_event\_fraction", "250ms\_or\_greater\_event\_fraction", "500ms\_or\_greater\_event\_fraction", avg }

Cumulative latency distribution (milliseconds-based thresholds).

</summary>

"100ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20rtt%20%3E%20(property)%20100ms_or_greater_event_fraction">Link to this property</a>

"250ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20rtt%20%3E%20(property)%20250ms_or_greater_event_fraction">Link to this property</a>

"500ms\_or\_greater\_event\_fraction": optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20rtt%20%3E%20(property)%20500ms_or_greater_event_fraction">Link to this property</a>

avg: optional number

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20rtt%20%3E%20(property)%20avg">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative%20%3E%20(property)%20rtt">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality%20%3E%20(property)%20video_producer_cumulative">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report%20%3E%20(property)%20quality">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20peer_report">Link to this property</a>

role: optional string

Name of the preset associated with the participant.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20role">Link to this property</a>

session\_id: optional string

formatuuid

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20session_id">Link to this property</a>

updated\_at: optional string

timestamp when this participant’s data was last updated.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20updated_at">Link to this property</a>

user\_id: optional string

User id for this participant.

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant%20%3E%20(property)%20user_id">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data%20%3E%20(property)%20participant">Link to this property</a>

</details>

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20data">Link to this property</a>

success: optional boolean

<a href="#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)%20%3E%20(property)%20success">Link to this property</a>

</details>

[Link to this property](<#(resource)%20realtime_kit.sessions%20%3E%20(model)%20session_get_participant_data_from_peer_id_response%20%3E%20(schema)>)