---
description: API reference for RtkMoreToggleButton component (Android Library)
title: RtkMoreToggleButton
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/more-toggle-button/og.png?v=5d692a29ecd92e71
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkMoreToggleButton

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/more-toggle-button/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles visibility of a more menu.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `activate` | `meeting: RealtimeKitClient` | Bind the button to the meeting state |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.controlbarbuttons.RtkMoreToggleButton
    android:id="@+id/rtk_more_toggle"
    android:layout_width="50dp"
    android:layout_height="50dp" />
```

### With Methods

```kotlin
val moreToggleButton = findViewById<RtkMoreToggleButton>(R.id.rtk_more_toggle)
moreToggleButton.activate(meeting)
```
