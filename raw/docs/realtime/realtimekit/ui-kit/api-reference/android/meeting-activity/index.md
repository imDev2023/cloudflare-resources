---
description: API reference for RtkMeetingActivity component (Android Library)
title: RtkMeetingActivity
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-activity/og.png?v=1f726049b13f7d68
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkMeetingActivity

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-activity/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The main meeting activity that manages the full meeting lifecycle. Handles transitions between loading, setup, waiting room, group call, webinar, and error states. This is the activity launched by `RealtimeKitUI.startMeeting()`.

## Usage Examples

### Basic Usage

```kotlin
val meetingInfo = RtkMeetingInfo(authToken = authToken, baseUrl = baseUrl)
val realtimeKitUIInfo = RealtimeKitUIInfo(activity = this, rtkMeetingInfo = meetingInfo)
val realtimeKitUI = RealtimeKitUIBuilder.build(realtimeKitUIInfo)
realtimeKitUI.startMeeting()
```
