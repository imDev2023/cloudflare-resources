---
description: API reference for RtkPluginsBottomSheet component (Android Library)
title: RtkPluginsBottomSheet
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/plugins/og.png?v=f314abd8ef438e18
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkPluginsBottomSheet

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/plugins/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which lists all available plugins from their preset, with the ability to enable or disable plugins.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `show` | `fragmentManager: FragmentManager, tag: String?` | Display the plugins bottom sheet |

## Usage Examples

### Basic Usage

```kotlin
val rtkPluginsBottomSheet = RtkPluginsBottomSheet()
rtkPluginsBottomSheet.show(fragmentManager, "PLUGINS_TAG")
```
