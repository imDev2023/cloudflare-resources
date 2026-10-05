---
description: API reference for RtkParticipantCountView component (Android Library)
title: RtkParticipantCountView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-count-view/og.png?v=123adf502262d02f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkParticipantCountView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participant-count-view/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A text view that displays the current number of participants in a meeting. It automatically updates when the participant count changes.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `activate` | `meeting: RealtimeKitClient` | Bind the view to the meeting state |
| `applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.RtkParticipantCountView
    android:id="@+id/rtk_participant_count"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content" />
```

### With Methods

```kotlin
val countView = findViewById<RtkParticipantCountView>(R.id.rtk_participant_count)
countView.activate(meeting)
```
