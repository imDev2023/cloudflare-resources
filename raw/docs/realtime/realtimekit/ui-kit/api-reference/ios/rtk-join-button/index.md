---
description: API reference for RtkJoinButton component (iOS Library)
title: RtkJoinButton
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-join-button/og.png?v=c7219c002ee1f854
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkJoinButton

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-join-button/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A pre-configured button that joins the meeting. Validates the participant name before joining.

## Initializer parameters

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance |
| `onClick` | `((RtkJoinButton, Bool) -> Void)?` | ❌ | `nil` | Closure called when the button is tapped. The `Bool` parameter indicates whether the join was successful. |
| `appearance` | `RtkButtonAppearance` | ❌ | - | Appearance configuration for the button |

## Usage Examples

### Basic Usage

```swift
import RealtimeKitUI

let joinButton = RtkJoinButton(meeting: rtkClient)
view.addSubview(joinButton)
```

### With tap handler

```swift
import RealtimeKitUI

let joinButton = RtkJoinButton(
    meeting: rtkClient,
    onClick: { button, success in
        if success {
            print("Joined meeting")
        } else {
            print("Join failed")
        }
    }
)
view.addSubview(joinButton)
```
