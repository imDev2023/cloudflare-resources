---
description: API reference for RtkStageActionButtonControlBar component (iOS Library)
title: RtkStageActionButtonControlBar
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-stage-action-button-control-bar/og.png?v=fd96eb672668a079
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkStageActionButtonControlBar

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-stage-action-button-control-bar/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A control bar button for webinar stage actions. Supports requesting to join, joining, leaving, and canceling stage requests based on the current stage status.

## Initializer parameters

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `rtkClient` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance |
| `buttonState` | `WebinarStageStatus` | ✅ | - | The current stage status that determines the button action |
| `presentingViewController` | `UIViewController` | ✅ | - | View controller used for presenting confirmation dialogs |

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `dataSource` | `RtkStageActionButtonControlBarDataSource?` | ❌ | `nil` | Data source for customizing stage action button behavior |

## Usage Examples

### Basic Usage

```swift
import RealtimeKitUI

let stageButton = RtkStageActionButtonControlBar(
    rtkClient: rtkClient,
    buttonState: .requestToJoinStage,
    presentingViewController: self
)
view.addSubview(stageButton)
```
