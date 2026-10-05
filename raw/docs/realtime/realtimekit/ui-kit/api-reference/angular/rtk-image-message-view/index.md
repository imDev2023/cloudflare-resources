---
description: API reference for rtk-image-message-view component (Angular Library)
title: rtk-image-message-view
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-image-message-view/og.png?v=9032032452e67999
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-image-message-view

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-image-message-view/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which renders an image message.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |
| `url` | `string` | ✅ | - | Url of the image |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-image-message-view></rtk-image-message-view>
```

### With Properties

```html
<!-- component.html -->
<rtk-image-message-view
 url="example">
</rtk-image-message-view>
```
