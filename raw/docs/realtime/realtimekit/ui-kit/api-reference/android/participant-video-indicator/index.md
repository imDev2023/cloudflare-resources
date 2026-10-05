---
description: API reference for RtkParticipantVideoIndicator component (Android Library)
title: RtkParticipantVideoIndicator
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-video-indicator/og.png?v=659923be0d943a1c
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkParticipantVideoIndicator

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-video-indicator/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A video indicator that shows a participant's camera status.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `activate` | `participant: RtkMeetingParticipant` | Bind the indicator to a participant |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.RtkParticipantVideoIndicator
    android:id="@+id/video_indicator"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content" />
```

### With Methods

```kotlin
val videoIndicator = findViewById<RtkParticipantVideoIndicator>(R.id.video_indicator)
videoIndicator.activate(participant)
```
