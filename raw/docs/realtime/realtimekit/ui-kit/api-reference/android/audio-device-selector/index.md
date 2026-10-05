---
description: API reference for RtkAudioDeviceSelector component (Android Library)
title: RtkAudioDeviceSelector
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/audio-device-selector/og.png?v=7bb2dc3a8e6cf16a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkAudioDeviceSelector

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/audio-device-selector/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

An audio device selector component which can be used to select audio devices.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `rtk_ds_label` | `string` | ❌ | `Audio` | Custom label text |

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `activate` | `meeting: RealtimeKitClient` | Bind the selector to the meeting state |
| `disableLabel` | - | Disable the label text above the dropdown |
| `applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.RtkAudioDeviceSelector
    android:id="@+id/audioSelector"
    app:rtk_ds_label="Audio"
    android:layout_width="0dp"
    android:layout_height="wrap_content" />
```

### With Methods

```kotlin
val audioSelector = findViewById<RtkAudioDeviceSelector>(R.id.audioSelector)
audioSelector.activate(meeting)
```
