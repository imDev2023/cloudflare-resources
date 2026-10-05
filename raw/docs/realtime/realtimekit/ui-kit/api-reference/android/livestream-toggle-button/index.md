---
description: API reference for RtkLivestreamToggleButton component (Android Library)
title: RtkLivestreamToggleButton
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-toggle-button/og.png?v=46b7b2a0441b8aef
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkLivestreamToggleButton

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-toggle-button/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A toggle button for starting or stopping a livestream.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `activate` | `meeting: RealtimeKitClient` | Bind the button to the meeting state |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.RtkLivestreamToggleButton
    android:id="@+id/rtk_livestream_toggle"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content" />
```

### With Methods

```kotlin
val livestreamToggle = findViewById<RtkLivestreamToggleButton>(R.id.rtk_livestream_toggle)
livestreamToggle.activate(meeting)
```
