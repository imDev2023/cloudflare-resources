---
description: API reference for RtkSwitchCameraButtonControlBar component (iOS Library)
title: RtkSwitchCameraButtonControlBar
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-switch-camera-button-control-bar/og.png?v=026891c5411ccc10
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkSwitchCameraButtonControlBar

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-switch-camera-button-control-bar/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A control bar button that switches between the front and rear cameras.

## Initializer parameters

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance |

## Usage Examples

### Basic Usage

```swift
import RealtimeKitUI

let switchCameraButton = RtkSwitchCameraButtonControlBar(meeting: rtkClient)
view.addSubview(switchCameraButton)
```
