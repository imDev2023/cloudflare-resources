---
description: API reference for RtkLivestreamHeaderView component (Android Library)
title: RtkLivestreamHeaderView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-header-view/og.png?v=147ebeacecdff39e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkLivestreamHeaderView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-header-view/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A pre-built header for livestream meetings. Contains the livestream indicator, viewer count, clock, and meeting title.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `activate` | `meeting: RealtimeKitClient` | Bind the header to the meeting state |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.RtkLivestreamHeaderView
    android:id="@+id/rtk_livestream_header"
    android:layout_width="match_parent"
    android:layout_height="wrap_content" />
```

### With Methods

```kotlin
val header = findViewById<RtkLivestreamHeaderView>(R.id.rtk_livestream_header)
header.activate(meeting)
```
