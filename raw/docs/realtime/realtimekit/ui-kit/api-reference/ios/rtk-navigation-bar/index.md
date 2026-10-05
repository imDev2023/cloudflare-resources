---
description: API reference for RtkNavigationBar component (iOS Library)
title: RtkNavigationBar
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-navigation-bar/og.png?v=df3c6f4cd21580bb
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkNavigationBar

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-navigation-bar/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A navigation bar with a title label and a close or back button. Used for modal screens such as chat, polls, and participant lists.

## Initializer parameters

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `title` | `String` | ✅ | - | The title text displayed in the navigation bar |

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `titleLabel` | `RtkLabel` | - | - | The label displaying the navigation bar title (read-only) |
| `leftButton` | `RtkControlBarButton` | - | - | The close or back button on the left side (read-only) |

## Methods

| Method | Return Type | Description |
| --- | --- | --- |
| `setBackButtonClick(callBack:)` | `Void` | Sets the tap handler for the back or close button |

## Usage Examples

### Basic Usage

```swift
import RealtimeKitUI

let navBar = RtkNavigationBar(title: "Participants")
view.addSubview(navBar)
```

### With back button handler

```swift
import RealtimeKitUI

let navBar = RtkNavigationBar(title: "Chat")
navBar.setBackButtonClick {
    self.dismiss(animated: true)
}
view.addSubview(navBar)
```
