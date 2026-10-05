---
description: API reference for RtkNameTag component (iOS Library)
title: RtkNameTag
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-name-tag/og.png?v=2ea405d9650023aa
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkNameTag

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-name-tag/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Base name tag view with an icon, title, and optional subtitle. Serves as the foundation for `RtkMeetingNameTag`.

## Initializer parameters

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `image` | `RtkImage` | ✅ | - | The icon image displayed in the name tag |
| `appearance` | `RtkNameTagAppearance` | ❌ | - | Appearance configuration for the name tag |
| `title` | `String` | ✅ | - | The primary text displayed in the name tag |
| `subtitle` | `String` | ❌ | `""` | Optional secondary text displayed below the title |

## Usage Examples

### Basic Usage

```swift
import RealtimeKitUI

let nameTag = RtkNameTag(
    image: RtkImage(image: UIImage(systemName: "mic")),
    title: "John Doe"
)
view.addSubview(nameTag)
```

### With subtitle

```swift
import RealtimeKitUI

let nameTag = RtkNameTag(
    image: RtkImage(image: UIImage(systemName: "mic")),
    title: "John Doe",
    subtitle: "Host"
)
view.addSubview(nameTag)
```
