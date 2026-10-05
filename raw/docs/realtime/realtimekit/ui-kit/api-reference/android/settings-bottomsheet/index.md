---
description: API reference for RtkSettingsBottomsheet component (Android Library)
title: RtkSettingsBottomsheet
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/settings-bottomsheet/og.png?v=7cb98910c65a50a0
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkSettingsBottomsheet

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/settings-bottomsheet/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A settings bottom sheet that contains audio and video device selectors and a self-preview tile. Used in portrait orientation.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `show` | `fragmentManager: FragmentManager, tag: String?` | Display the settings bottom sheet |

## Usage Examples

### Basic Usage

```kotlin
val settingsBottomSheet = RtkSettingsBottomsheet()
settingsBottomSheet.show(fragmentManager, "SETTINGS_TAG")
```
