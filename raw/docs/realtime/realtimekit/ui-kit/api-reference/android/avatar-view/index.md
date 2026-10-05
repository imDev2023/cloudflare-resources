---
description: API reference for RtkAvatarView component (Android Library)
title: RtkAvatarView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/avatar-view/og.png?v=f6014ad7b6545b68
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkAvatarView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/android/avatar-view/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Avatar component which renders a participant's profile picture or their initials.

## Methods

| Method | Parameters | Description |
| --- | --- | --- |
| `activate` | `participant: RtkMeetingParticipant` | Bind the avatar to a participant |
| `refresh` | - | Refresh the avatar based on the participant's name |
| `applyDesignTokens` | `designTokens: RtkDesignTokens` | Apply custom design tokens for theming |

## Usage Examples

### Basic Usage

```xml
<com.cloudflare.realtimekit.ui.view.avatarview.RtkAvatarView
    android:id="@+id/rtk_avatar"
    android:layout_width="48dp"
    android:layout_height="48dp" />
```

### With Methods

```kotlin
val avatar = findViewById<RtkAvatarView>(R.id.rtk_avatar)
avatar.activate(participant)
```
