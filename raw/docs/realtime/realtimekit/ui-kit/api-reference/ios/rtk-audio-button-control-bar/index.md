---
description: API reference for RtkAudioButtonControlBar component (iOS Library)
title: RtkAudioButtonControlBar
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-audio-button-control-bar/og.png?v=eec04b90bf5212d4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkAudioButtonControlBar

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-audio-button-control-bar/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A control bar button that toggles the local microphone on and off. Checks microphone permissions before toggling.

## Initializer parameters

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance |
| `onClick` | `((RtkAudioButtonControlBar) -> Void)?` | ❌ | `nil` | Closure called when the button is tapped |
| `appearance` | `RtkControlBarButtonAppearance` | ❌ | - | Appearance configuration for the button |

## Usage Examples

### Basic Usage

```swift
import RealtimeKitUI

let audioButton = RtkAudioButtonControlBar(meeting: rtkClient)
view.addSubview(audioButton)
```

### With tap handler

```swift
import RealtimeKitUI

let audioButton = RtkAudioButtonControlBar(
    meeting: rtkClient,
    onClick: { button in
        print("Audio toggled")
    }
)
view.addSubview(audioButton)
```
