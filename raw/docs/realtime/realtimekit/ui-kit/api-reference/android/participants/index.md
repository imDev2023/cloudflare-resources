---
description: API reference for RtkParticipantsFragment component (Android Library)
title: RtkParticipantsFragment
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participants/og.png?v=e66bd12d702f6597
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkParticipantsFragment

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/participants/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which lists all participants, with the ability to run privileged actions on each participant according to your permissions.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `show` | `fragmentManager: FragmentManager, tag: String?` | Display the participant list bottom sheet |

## Usage Examples

### Basic Usage

```kotlin
val rtkParticipantsFragment = RtkParticipantsFragment()
rtkParticipantsFragment.show(fragmentManager, "PARTICIPANTS_TAG")
```
