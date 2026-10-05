---
description: API reference for RtkVideoDeviceSelector component (Android Library)
title: RtkVideoDeviceSelector
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/video-device-selector/og.png?v=c1925a8aea427d4a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkVideoDeviceSelector

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/video-device-selector/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A video device selector component which can be used to select video devices.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `rtk_ds_label` | `string` | ❌ | `Video` | Custom label text |

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `activate` | `meeting: RealtimeKitClient` | Bind the selector to the meeting state |
| `disableLabel` | - | Disable the label text above the dropdown |
| `applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.RtkVideoDeviceSelector
    android:id="@+id/videoSelector"
    app:rtk_ds_label="Camera"
    android:layout_width="0dp"
    android:layout_height="wrap_content" />
```

### With Methods

```kotlin
val videoSelector = findViewById<RtkVideoDeviceSelector>(R.id.videoSelector)
videoSelector.activate(meeting)
```
