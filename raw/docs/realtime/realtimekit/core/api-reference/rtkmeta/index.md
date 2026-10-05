---
title: RTKMeta
image: https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkmeta/og.png?v=12336b5b0cb38ada
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RTKMeta

Last updated Jul 22, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/core/api-reference/rtkmeta/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

This consists of the metadata of the meeting, such as the room name and the title.

- [RTKMeta](#module_RTKMeta)
  - [.selfActiveTab](#module_RTKMeta+selfActiveTab)
  - [.broadcastTabChanges](#module_RTKMeta+broadcastTabChanges)
  - [.viewType](#module_RTKMeta+viewType)
  - [.meetingStartedTimestamp](#module_RTKMeta+meetingStartedTimestamp)
  - [.meetingTitle](#module_RTKMeta+meetingTitle)
  - [.sessionId](#module_RTKMeta+sessionId)
  - [.meetingId](#module_RTKMeta+meetingId)
  - [.setBroadcastTabChanges(broadcastTabChanges)](#module_RTKMeta+setBroadcastTabChanges)
  - [.setSelfActiveTab(spotlightTab, tabChangeSource)](#module_RTKMeta+setSelfActiveTab)

### meeting.meta.selfActiveTab

Represents the current active tab

**Kind**: instance property of [`RTKMeta`](#module_RTKMeta)  

### meeting.meta.broadcastTabChanges

Represents whether current user is spotlighted

**Kind**: instance property of [`RTKMeta`](#module_RTKMeta)  

### meeting.meta.viewType

The `viewType` tells the type of the meeting possible values are: GROUP\_CALL| LIVESTREAM | CHAT | AUDIO\_ROOM

**Kind**: instance property of [`RTKMeta`](#module_RTKMeta)  

### meeting.meta.meetingStartedTimestamp

The timestamp of the time when the meeting started.

**Kind**: instance property of [`RTKMeta`](#module_RTKMeta)  

### meeting.meta.meetingTitle

The title of the meeting.

**Kind**: instance property of [`RTKMeta`](#module_RTKMeta)  

### meeting.meta.sessionId

(Experimental) The sessionId this meeting object is part of.

**Kind**: instance property of [`RTKMeta`](#module_RTKMeta)  

### meeting.meta.meetingId

The room name of the meeting.

**Kind**: instance property of [`RTKMeta`](#module_RTKMeta)  

### meeting.meta.setBroadcastTabChanges(broadcastTabChanges)

Sets current user as broadcasting tab changes

**Kind**: instance method of [`RTKMeta`](#module_RTKMeta)

| Param | Type |
| --- | --- |
| broadcastTabChanges | `boolean` |

### meeting.meta.setSelfActiveTab(spotlightTab, tabChangeSource)

Sets current active tab for user

**Kind**: instance method of [`RTKMeta`](#module_RTKMeta)

| Param | Type |
| --- | --- |
| spotlightTab | `ActiveTab` |
| tabChangeSource | `TabChangeSource` |
