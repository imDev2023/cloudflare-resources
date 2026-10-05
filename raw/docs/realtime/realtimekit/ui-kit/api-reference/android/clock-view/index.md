---
description: API reference for RtkClockView component (Android Library)
title: RtkClockView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/clock-view/og.png?v=491335beaf6d882b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkClockView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/clock-view/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A clock component which shows the elapsed time of a meeting.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `activate` | `meeting: RealtimeKitClient` | Bind the clock to the meeting state |
| `applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.RtkClockView
    android:id="@+id/rtk_clock_view"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content" />
```

### With Methods

```kotlin
val clockView = findViewById<RtkClockView>(R.id.rtk_clock_view)
clockView.activate(meeting)
```
