---
description: API reference for RtkButton component (iOS Library)
title: RtkButton
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-button/og.png?v=1f01e255896b340a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkButton

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-button/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A versatile button that follows the RTK Design System. Supports multiple styles, states, and sizes.

## Initializer parameters

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `style` | `Style` | ❌ | `.solid` | The button style (solid, line, icon-left, and others) |
| `rtkButtonState` | `States` | ❌ | `.active` | The initial state of the button |
| `size` | `Size` | ❌ | `.large` | The size of the button |
| `appearance` | `RtkButtonAppearance` | ❌ | - | Appearance configuration for colors and fonts |

## Usage Examples

### Basic Usage

```swift
import RealtimeKitUI

let button = RtkButton()
button.setTitle("Join", for: .normal)
view.addSubview(button)
```

### With custom style

```swift
import RealtimeKitUI

let button = RtkButton(
    style: .line,
    rtkButtonState: .active,
    size: .large
)
button.setTitle("Cancel", for: .normal)
view.addSubview(button)
```
