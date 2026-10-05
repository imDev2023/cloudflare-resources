---
description: API reference for RtkLivestreamIndicator component (Android Library)
title: RtkLivestreamIndicator
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-indicator/og.png?v=1c8ce3f4ff7fc1f9
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkLivestreamIndicator

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/livestream-indicator/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A visual indicator that shows when a livestream is active.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `refresh` | `meeting: RealtimeKitClient` | Update the indicator based on the current livestream state |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.RtkLivestreamIndicator
    android:id="@+id/rtk_livestream_indicator"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content" />
```

### With Methods

```kotlin
val indicator = findViewById<RtkLivestreamIndicator>(R.id.rtk_livestream_indicator)
indicator.refresh(meeting)
```
