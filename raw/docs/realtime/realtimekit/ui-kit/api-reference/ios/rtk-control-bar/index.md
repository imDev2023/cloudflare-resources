---
description: API reference for RtkControlBar component (iOS Library)
title: RtkControlBar
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-control-bar/og.png?v=42c8c4e6952d0763
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkControlBar

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-control-bar/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Base control bar view with a More menu button and an End Call button. Serves as the foundation for `RtkMeetingControlBar` and `RtkWebinarControlBar`.

## Initializer parameters

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance |
| `delegate` | `RtkTabBarDelegate?` | ✅ | - | Delegate for handling tab bar interactions |
| `presentingViewController` | `UIViewController` | ✅ | - | View controller used for presenting modal screens |
| `appearance` | `RtkControlBarAppearance` | ❌ | `RtkControlBarAppearanceModel()` | Appearance configuration for the control bar |
| `settingViewControllerCompletion` | `(() -> Void)?` | ❌ | `nil` | Closure called when the settings view controller dismisses |
| `onLeaveMeetingCompletion` | `(() -> Void)?` | ❌ | `nil` | Closure called when the participant leaves the meeting |

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `moreButton` | `RtkMoreButtonControlBar` | - | - | The More menu button (read-only) |
| `endCallButton` | `RtkEndMeetingControlBarButton` | - | - | The End Call button |

## Usage Examples

### Basic Usage

```swift
import RealtimeKitUI

let controlBar = RtkControlBar(
    meeting: rtkClient,
    delegate: self,
    presentingViewController: self
)
view.addSubview(controlBar)
```

### With completion handlers

```swift
import RealtimeKitUI

let controlBar = RtkControlBar(
    meeting: rtkClient,
    delegate: self,
    presentingViewController: self,
    onLeaveMeetingCompletion: {
        self.dismiss(animated: true)
    }
)
view.addSubview(controlBar)
```
