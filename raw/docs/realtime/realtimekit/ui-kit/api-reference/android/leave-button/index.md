---
description: API reference for RtkLeaveButton component (Android Library)
title: RtkLeaveButton
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/leave-button/og.png?v=9585f0f5c7a51f16
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkLeaveButton

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/leave-button/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles visibility of the leave confirmation dialog.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `activate` | `meeting: RealtimeKitClient` | Bind the button to the meeting state |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.controlbarbuttons.RtkLeaveButton
    android:id="@+id/rtk_leave_button"
    android:layout_width="48dp"
    android:layout_height="48dp" />
```

### With Methods

```kotlin
val leaveButton = findViewById<RtkLeaveButton>(R.id.rtk_leave_button)
leaveButton.activate(meeting)
```
