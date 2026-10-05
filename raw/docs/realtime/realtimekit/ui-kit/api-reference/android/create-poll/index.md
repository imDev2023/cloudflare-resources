---
description: API reference for RtkCreatePollBottomSheet component (Android Library)
title: RtkCreatePollBottomSheet
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/create-poll/og.png?v=5cf9c12c40447b0b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkCreatePollBottomSheet

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/create-poll/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component that lets you create a poll.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `show` | `fragmentManager: FragmentManager, tag: String?` | Display the create poll bottom sheet |

## Usage Examples

### Basic Usage

```kotlin
val rtkCreatePollBottomSheet = RtkCreatePollBottomSheet()
rtkCreatePollBottomSheet.show(fragmentManager, "CREATE_POLL_TAG")
```
