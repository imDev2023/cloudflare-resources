---
description: API reference for RtkPollsBottomSheet component (Android Library)
title: RtkPollsBottomSheet
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/polls/og.png?v=dace6f69be80a656
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkPollsBottomSheet

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/polls/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which lists all available polls a user can access.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `show` | `fragmentManager: FragmentManager, tag: String?` | Display the polls bottom sheet |

## Usage Examples

### Basic Usage

```kotlin
val rtkPollsBottomSheet = RtkPollsBottomSheet()
rtkPollsBottomSheet.show(fragmentManager, "POLLS_TAG")
```
