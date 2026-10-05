---
description: API reference for RtkVideoButtonControlBar component (iOS Library)
title: RtkVideoButtonControlBar
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-video-button-control-bar/og.png?v=37ff5978b4710534
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkVideoButtonControlBar

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-video-button-control-bar/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A control bar button that toggles the local camera on and off. Checks camera permissions before toggling.

## Initializer parameters

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `rtkClient` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance |

## Usage Examples

### Basic Usage

```swift
import RealtimeKitUI

let videoButton = RtkVideoButtonControlBar(rtkClient: rtkClient)
view.addSubview(videoButton)
```
