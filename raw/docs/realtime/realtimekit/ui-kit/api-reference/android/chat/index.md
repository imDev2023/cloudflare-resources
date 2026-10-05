---
description: API reference for RtkChatBottomSheet component (Android Library)
title: RtkChatBottomSheet
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/chat/og.png?v=a4494d935b4d9cba
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkChatBottomSheet

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/chat/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Fully featured chat screen with image and file upload and auto-scroll.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `show` | `fragmentManager: FragmentManager, tag: String?` | Display the chat bottom sheet |

## Usage Examples

### Basic Usage

```kotlin
val rtkChatBottomSheet = RtkChatBottomSheet()
rtkChatBottomSheet.show(fragmentManager, "CHAT_TAG")
```
