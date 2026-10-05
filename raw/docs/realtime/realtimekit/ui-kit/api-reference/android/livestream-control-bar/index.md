---
description: API reference for RtkLivestreamControlBarView component (Android Library)
title: RtkLivestreamControlBarView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-control-bar/og.png?v=1a9daeab066d16ff
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkLivestreamControlBarView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-control-bar/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A pre-built control bar for livestream meetings. Contains mic toggle, camera toggle, livestream toggle, join stage button, more toggle, and leave button.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `activate` | `meeting: RealtimeKitClient` | Bind the control bar to the meeting state |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.controlbars.RtkLivestreamControlBarView
    android:id="@+id/rtk_livestream_control_bar"
    android:layout_width="match_parent"
    android:layout_height="wrap_content" />
```

### With Methods

```kotlin
val controlBar = findViewById<RtkLivestreamControlBarView>(R.id.rtk_livestream_control_bar)
controlBar.activate(meeting)
```
