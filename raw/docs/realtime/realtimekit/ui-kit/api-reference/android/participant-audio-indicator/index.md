---
description: API reference for RtkParticipantAudioIndicator component (Android Library)
title: RtkParticipantAudioIndicator
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-audio-indicator/og.png?v=dd9b0dff0c3df5d3
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkParticipantAudioIndicator

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-audio-indicator/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

An audio visualizer component which visualizes a participant's audio.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `activate` | `participant: RtkMeetingParticipant` | Bind the indicator to a participant |
| `refresh` | - | Force a refresh of the audio indicator state |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.RtkParticipantAudioIndicator
    android:id="@+id/audio_indicator"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content" />
```

### With Methods

```kotlin
val audioIndicator = findViewById<RtkParticipantAudioIndicator>(R.id.audio_indicator)
audioIndicator.activate(participant)
```
