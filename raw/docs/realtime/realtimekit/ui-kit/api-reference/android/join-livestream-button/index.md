---
description: API reference for RtkJoinLivestreamButton component (Android Library)
title: RtkJoinLivestreamButton
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/join-livestream-button/og.png?v=52da3ce805dcf45c
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkJoinLivestreamButton

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/join-livestream-button/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button for joining or leaving the livestream stage.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `activate` | `meeting: RealtimeKitClient` | Bind the button to the meeting state |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.RtkJoinLivestreamButton
    android:id="@+id/rtk_join_livestream"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content" />
```

### With Methods

```kotlin
val joinLivestreamButton = findViewById<RtkJoinLivestreamButton>(R.id.rtk_join_livestream)
joinLivestreamButton.activate(meeting)
```
