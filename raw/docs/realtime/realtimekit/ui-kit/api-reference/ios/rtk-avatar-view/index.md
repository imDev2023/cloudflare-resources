---
description: API reference for RtkAvatarView component (iOS Library)
title: RtkAvatarView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-avatar-view/og.png?v=f6014ad7b6545b68
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkAvatarView

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-avatar-view/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A circular avatar view that displays a participant's profile image or name initials as a fallback.

## Initializer parameters

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `participant` | `RtkMeetingParticipant` | ✅ | - | The participant whose avatar to display |

## Methods

| Method | Return Type | Description |
| --- | --- | --- |
| `set(participant:)` | `Void` | Updates the avatar to display a different participant |
| `refresh()` | `Void` | Refreshes the avatar image or initials |
| `setInitialName(font:)` | `Void` | Sets the font used for rendering name initials |

## Usage Examples

### Basic Usage

```swift
import RealtimeKitUI

let avatarView = RtkAvatarView(participant: participant)
view.addSubview(avatarView)
```

### Update participant

```swift
import RealtimeKitUI

let avatarView = RtkAvatarView(participant: participant)
view.addSubview(avatarView)

// Update to a different participant
avatarView.set(participant: newParticipant)
avatarView.refresh()
```
