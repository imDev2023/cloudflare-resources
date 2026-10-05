---
description: API reference for RtkMicToggleButton component (Android Library)
title: RtkMicToggleButton
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/mic-toggle/og.png?v=e07dbf5ea80e6c57
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkMicToggleButton

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/mic-toggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles the local user's microphone. It automatically listens to self audio events to update its state.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `activate` | `meeting: RealtimeKitClient` | Bind the button to the meeting state |
| `deactivate` | - | Unbind the button and remove event listeners |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.controlbarbuttons.RtkMicToggleButton
    android:id="@+id/btn_mic_toggle"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content" />
```

### With Methods

```kotlin
val micToggleButton = findViewById<RtkMicToggleButton>(R.id.btn_mic_toggle)
micToggleButton.activate(meeting)
```
