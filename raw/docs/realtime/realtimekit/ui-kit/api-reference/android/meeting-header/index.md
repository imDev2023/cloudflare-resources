---
description: API reference for RtkMeetingHeaderView component (Android Library)
title: RtkMeetingHeaderView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-header/og.png?v=1f308a959e351ccb
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkMeetingHeaderView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-header/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A pre-built meeting header that contains meeting title, clock, recording indicator, participant count, grid paginator, and switch camera button.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `activate` | `meeting: RealtimeKitClient` | Bind the header to the meeting state |
| `applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.headers.RtkMeetingHeaderView
    android:id="@+id/rtk_meeting_header"
    android:layout_width="match_parent"
    android:layout_height="wrap_content" />
```

### With Methods

```kotlin
val header = findViewById<RtkMeetingHeaderView>(R.id.rtk_meeting_header)
header.activate(meeting)
```
