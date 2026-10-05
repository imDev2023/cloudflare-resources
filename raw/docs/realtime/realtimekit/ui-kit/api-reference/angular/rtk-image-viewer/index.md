---
description: API reference for rtk-image-viewer component (Angular Library)
title: rtk-image-viewer
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-image-viewer/og.png?v=2d963f6e4b1ff96e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-image-viewer

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-image-viewer/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which shows an image sent via chat.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `image` | `ImageMessage` | ✅ | - | Image message |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-image-viewer></rtk-image-viewer>
```

### With Properties

```html
<!-- component.html -->
<rtk-image-viewer
 [image]="imagemessage"
 size="md">
</rtk-image-viewer>
```
