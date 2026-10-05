---
description: API reference for RtkWebinarControlBarView component (Android Library)
title: RtkWebinarControlBarView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/webinar-control-bar/og.png?v=d3aba26fb189e721
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkWebinarControlBarView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/webinar-control-bar/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A pre-built control bar for webinar meetings. Contains mic toggle, camera toggle, webinar stage toggle, more toggle, and leave button.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `activate` | `meeting: RealtimeKitClient` | Bind the control bar to the meeting state |
| `deactivate` | - | Unbind the control bar and remove event listeners |
| `refreshStageToggleButton` | - | Force a refresh of the stage toggle button state |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.controlbars.RtkWebinarControlBarView
    android:id="@+id/rtk_webinar_control_bar"
    android:layout_width="match_parent"
    android:layout_height="wrap_content" />
```

### With Methods

```kotlin
val controlBar = findViewById<RtkWebinarControlBarView>(R.id.rtk_webinar_control_bar)
controlBar.activate(meeting)
```
