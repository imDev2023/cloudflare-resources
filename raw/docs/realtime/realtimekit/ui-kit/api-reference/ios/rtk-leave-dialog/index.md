---
description: API reference for RtkLeaveDialog component (iOS Library)
title: RtkLeaveDialog
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-leave-dialog/og.png?v=86af4a2cbc286bfc
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkLeaveDialog

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-leave-dialog/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A dialog that presents leave and end meeting options. Displays different options based on host permissions.

## Initializer parameters

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance |
| `onClick` | `((RtkLeaveDialogAlertButtonType) -> Void)?` | ❌ | `nil` | Closure called when the user selects a dialog option |

## Methods

| Method | Return Type | Description |
| --- | --- | --- |
| `show(on:)` | `Void` | Presents the leave dialog on the specified view controller |

## Usage Examples

### Basic Usage

```swift
import RealtimeKitUI

let leaveDialog = RtkLeaveDialog(meeting: rtkClient)
leaveDialog.show(on: self)
```

### With selection handler

```swift
import RealtimeKitUI

let leaveDialog = RtkLeaveDialog(
    meeting: rtkClient,
    onClick: { buttonType in
        switch buttonType {
        case .leaveMeeting:
            print("Leaving meeting")
        case .endMeeting:
            print("Ending meeting for all")
        default:
            break
        }
    }
)
leaveDialog.show(on: self)
```
