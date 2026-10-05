---
description: API reference for RtkMeetingOptionBottomSheet component (Android Library)
title: RtkMeetingOptionBottomSheet
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-option-bottomsheet/og.png?v=95c050517b4068f4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkMeetingOptionBottomSheet

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/meeting-option-bottomsheet/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A bottom sheet shown when tapping the more button. Contains options for participants, chat, polls, plugins, recording, screen share, mute all, and settings.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `show` | `fragmentManager: FragmentManager, tag: String?` | Display the meeting options bottom sheet |

## Usage Examples

### Basic Usage

```kotlin
val meetingOptions = RtkMeetingOptionBottomSheet()
meetingOptions.show(fragmentManager, "MEETING_OPTIONS_TAG")
```
