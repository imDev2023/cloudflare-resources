---
description: API reference for RtkWebinarStageToggleButton component (Android Library)
title: RtkWebinarStageToggleButton
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/webinar-stage-toggle/og.png?v=41922a73f9a5c645
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkWebinarStageToggleButton

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/webinar-stage-toggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Component that lets you add provision for the local user to join the webinar stage.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `activate` | `meeting: RealtimeKitClient` | Bind the button to the meeting state |
| `deactivate` | - | Unbind the button and remove event listeners |
| `refresh` | - | Force a refresh of the button state |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.controlbarbuttons.webinarstagetogglebutton.RtkWebinarStageToggleButton
    android:id="@+id/rtk_webinar_stage_toggle"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content" />
```

### With Methods

```kotlin
val stageToggleButton = findViewById<RtkWebinarStageToggleButton>(R.id.rtk_webinar_stage_toggle)
stageToggleButton.activate(meeting)
```
