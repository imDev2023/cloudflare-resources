---
description: API reference for RtkCameraToggleButton component (Android Library)
title: RtkCameraToggleButton
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/camera-toggle/og.png?v=17e70eb3009fa692
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkCameraToggleButton

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/camera-toggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles the local user's camera. It automatically listens to self video events to update its state.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `activate` | `meeting: RealtimeKitClient` | Bind the button to the meeting state |
| `deactivate` | - | Unbind the button and remove event listeners |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.controlbarbuttons.RtkCameraToggleButton
    android:id="@+id/btn_camera_toggle"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content" />
```

### With Methods

```kotlin
val cameraToggleButton = findViewById<RtkCameraToggleButton>(R.id.btn_camera_toggle)
cameraToggleButton.activate(meeting)
```
