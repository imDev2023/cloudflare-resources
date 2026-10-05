---
description: API reference for RtkParticipantCountView component (iOS Library)
title: RtkParticipantCountView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-participant-count-view/og.png?v=123adf502262d02f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkParticipantCountView

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-participant-count-view/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A label that displays the current participant count. Automatically updates when participants join or leave the meeting.

## Initializer parameters

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `meeting` | `RealtimeKitClient` | ✅ | - | The RealtimeKit client instance for the active meeting |
| `appearance` | `RtkTextAppearance` | ❌ | `AppTheme.shared.participantCountAppearance` | Text appearance configuration for font and color |

## Usage Examples

### Basic Usage

```swift
import RealtimeKitUI

let countView = RtkParticipantCountView(meeting: rtkClient)
view.addSubview(countView)
```

### With custom appearance

```swift
import RealtimeKitUI

let appearance = RtkTextAppearance(
    font: UIFont.systemFont(ofSize: 14, weight: .medium),
    textColor: .lightGray
)
let countView = RtkParticipantCountView(
    meeting: rtkClient,
    appearance: appearance
)
view.addSubview(countView)
```
