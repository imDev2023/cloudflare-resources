---
description: API reference for RtkMeetingTitleView component (Android Library)
title: RtkMeetingTitleView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-title-view/og.png?v=f18379cb78e9a42d
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkMeetingTitleView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-title-view/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A text view that displays the meeting title. It automatically updates when the meeting title changes.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `activate` | `meeting: RealtimeKitClient` | Bind the view to the meeting state |
| `applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.RtkMeetingTitleView
    android:id="@+id/rtk_meeting_title"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content" />
```

### With Methods

```kotlin
val titleView = findViewById<RtkMeetingTitleView>(R.id.rtk_meeting_title)
titleView.activate(meeting)
```
