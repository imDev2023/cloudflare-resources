---
description: API reference for rtk-icon component (Angular Library)
title: rtk-icon
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-icon/og.png?v=6ef74a29541c6f0a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-icon

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-icon/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

An icon component which accepts an svg string and renders it.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `icon` | `string` | ✅ | - | Icon |
| `size` | `Size1` | ✅ | - | Size |
| `variant` | `IconVariant` | ✅ | - | Icon variant |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-icon></rtk-icon>
```

### With Properties

```html
<!-- component.html -->
<rtk-icon
 icon="example"
 size="md"
 variant="primary">
</rtk-icon>
```
