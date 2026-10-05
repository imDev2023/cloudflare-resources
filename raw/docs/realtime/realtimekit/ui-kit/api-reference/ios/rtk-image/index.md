---
description: API reference for RtkImage component (iOS Library)
title: RtkImage
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-image/og.png?v=3875c1525850ca04
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkImage

Last updated Apr 23, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/ios/rtk-image/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A struct that wraps a `UIImage` or a `URL` for image content. Used throughout the UI Kit for icons, avatars, and custom images.

## Initializer parameters

| Parameter | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `image` | `UIImage?` | ❌ | `nil` | A local UIImage to display |
| `url` | `URL?` | ❌ | `nil` | A remote URL to load the image from |

## Usage Examples

### With a local image

```swift
import RealtimeKitUI

let rtkImage = RtkImage(image: UIImage(systemName: "mic"))
```

### With a remote URL

```swift
import RealtimeKitUI

let rtkImage = RtkImage(url: URL(string: "https://example.com/avatar.png"))
```
