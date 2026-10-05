---
description: API reference for RtkSettingsFragment component (Android Library)
title: RtkSettingsFragment
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/settings-fragment/og.png?v=864b704117d23266
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkSettingsFragment

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/settings-fragment/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A settings dialog that contains audio and video device selectors and a self-preview tile. Used in landscape orientation.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `show` | `fragmentManager: FragmentManager, tag: String?` | Display the settings dialog |
| `setBottomSheetEnabled` | `onClick: () -> Unit` | Enable a button to switch to the bottom sheet view |

## Usage Examples

### Basic Usage

```kotlin
val settingsFragment = RtkSettingsFragment()
settingsFragment.show(fragmentManager, "SETTINGS_TAG")
```
