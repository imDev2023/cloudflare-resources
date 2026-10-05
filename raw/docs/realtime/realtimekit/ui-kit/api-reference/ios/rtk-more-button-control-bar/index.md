---
description: API reference for RtkMoreButtonControlBar component (iOS Library)
title: RtkMoreButtonControlBar
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-more-button-control-bar/og.png?v=a271abca6eba206f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkMoreButtonControlBar

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-more-button-control-bar/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A control bar button that opens a bottom sheet menu with meeting actions such as chat, polls, and participant list.

## Initializer parameters

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance |
| `presentingViewController` | `UIViewController` | ✅ | - | View controller used to present the bottom sheet |
| `settingViewControllerCompletion` | `(() -> Void)?` | ❌ | `nil` | Closure called when the settings view controller dismisses |

## Methods

| Method | Return Type | Description |
| --- | --- | --- |
| `hideBottomSheet()` | `Void` | Programmatically dismisses the bottom sheet menu |

## Usage Examples

### Basic Usage

```swift
import RealtimeKitUI

let moreButton = RtkMoreButtonControlBar(
    meeting: rtkClient,
    presentingViewController: self
)
view.addSubview(moreButton)
```

### With settings completion

```swift
import RealtimeKitUI

let moreButton = RtkMoreButtonControlBar(
    meeting: rtkClient,
    presentingViewController: self,
    settingViewControllerCompletion: {
        print("Settings dismissed")
    }
)
view.addSubview(moreButton)
```
