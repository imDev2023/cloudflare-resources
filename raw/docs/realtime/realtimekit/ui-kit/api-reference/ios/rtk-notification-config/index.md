---
description: API reference for RtkNotificationConfig component (iOS Library)
title: RtkNotificationConfig
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-notification-config/og.png?v=2baa2067923668d4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkNotificationConfig

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-notification-config/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Configuration class for controlling notification behavior in meetings. Manages sound and toast notifications for participant join/leave events, chat messages, and polls.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `participantJoined` | `RtkNotification` | ❌ | `RtkNotification()` | Notification settings for participant join events |
| `participantLeft` | `RtkNotification` | ❌ | `RtkNotification()` | Notification settings for participant leave events |
| `newChatArrived` | `RtkNotification` | ❌ | `RtkNotification()` | Notification settings for new chat messages |
| `newPollArrived` | `RtkNotification` | ❌ | `RtkNotification()` | Notification settings for new poll events |

## RtkNotification properties

Each `RtkNotification` instance contains the following properties:

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `playSound` | `Bool` | ❌ | `true` | Whether to play a notification sound |
| `showToast` | `Bool` | ❌ | `true` | Whether to show a toast notification |

## Usage Examples

### Basic Usage

```swift
import RealtimeKitUI

let rtkUI = RealtimeKitUI(meetingInfo: meetingInfo)
// Access the default notification config
let notificationConfig = rtkUI.notification
```

### Customize notifications

```swift
import RealtimeKitUI

let rtkUI = RealtimeKitUI(meetingInfo: meetingInfo)

// Disable sound for participant join events
rtkUI.notification.participantJoined.playSound = false

// Disable toast for chat messages
rtkUI.notification.newChatArrived.showToast = false
```
