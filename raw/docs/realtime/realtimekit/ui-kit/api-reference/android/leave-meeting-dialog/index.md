---
description: API reference for RtkLeaveMeetingView component (Android Library)
title: RtkLeaveMeetingView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/leave-meeting-dialog/og.png?v=4c83371aec40ffc7
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkLeaveMeetingView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/leave-meeting-dialog/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which allows you to leave a meeting or end meeting for all, if you have the permission.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `show` | - | Display the dialog |
| `dismiss` | - | Dismiss the dialog |

## Usage Examples

### Basic Usage

```kotlin
val endCallDialog = RtkLeaveMeetingView(context, meeting)
endCallDialog.show()
```
