---
description: API reference for RtkMeetingControlBarView component (Android Library)
title: RtkMeetingControlBarView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-control-bar/og.png?v=2ecf6790eed5da70
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkMeetingControlBarView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-control-bar/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A pre-built control bar for group call meetings. Contains mic toggle, camera toggle, more toggle, and leave button.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `activate` | `meeting: RealtimeKitClient` | Bind the control bar to the meeting state |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.controlbars.RtkMeetingControlBarView
    android:id="@+id/rtk_meeting_control_bar"
    android:layout_width="match_parent"
    android:layout_height="wrap_content" />
```

### With Methods

```kotlin
val controlBar = findViewById<RtkMeetingControlBarView>(R.id.rtk_meeting_control_bar)
controlBar.activate(meeting)
```
