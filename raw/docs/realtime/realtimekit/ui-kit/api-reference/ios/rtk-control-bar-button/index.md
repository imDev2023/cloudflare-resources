---
description: API reference for RtkControlBarButton component (iOS Library)
title: RtkControlBarButton
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-control-bar-button/og.png?v=1fd291aff9381827
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkControlBarButton

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-control-bar-button/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Base button class for control bar items. Supports normal and selected states, notification badges, and theming through appearance configuration.

## Initializer parameters

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `image` | `RtkImage` | ✅ | - | The icon image for the button |
| `title` | `String` | ❌ | `""` | The title text displayed below the icon |
| `appearance` | `RtkControlBarButtonAppearance` | ❌ | - | Appearance configuration for colors and styling |

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `selectedStateTintColor` | `UIColor` | ❌ | - | Tint color applied when the button is in the selected state |
| `normalStateTintColor` | `UIColor` | ❌ | - | Tint color applied when the button is in the normal state |
| `notificationBadge` | `RtkNotificationBadgeView` | - | - | Badge view for displaying notification counts |

## Methods

| Method | Return Type | Description |
| --- | --- | --- |
| `setSelected(image:title:)` | `Void` | Sets the button to the selected state with a custom image and title |
| `setDefault(image:title:)` | `Void` | Sets the button to the default state with a custom image and title |

## Usage Examples

### Basic Usage

```swift
import RealtimeKitUI

let button = RtkControlBarButton(
    image: RtkImage(image: UIImage(systemName: "mic")),
    title: "Mute"
)
view.addSubview(button)
```

### With state changes

```swift
import RealtimeKitUI

let button = RtkControlBarButton(
    image: RtkImage(image: UIImage(systemName: "mic")),
    title: "Mute"
)

// Switch to selected state
button.setSelected(
    image: RtkImage(image: UIImage(systemName: "mic.slash")),
    title: "Unmute"
)

// Switch back to default state
button.setDefault(
    image: RtkImage(image: UIImage(systemName: "mic")),
    title: "Mute"
)
view.addSubview(button)
```
