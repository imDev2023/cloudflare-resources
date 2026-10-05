---
description: API reference for rtk-menu component (Angular Library)
title: rtk-menu
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-menu/og.png?v=8b4fc8ee04474c78
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-menu

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-menu/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A menu component.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `offset` | `number` | ✅ | - | Offset in px |
| `placement` | `Placement` | ✅ | - | Placement of menu |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-menu></rtk-menu>
```

### With Properties

```html
<!-- component.html -->
<rtk-menu
 offset="42"
 [placement]="placement"
 size="md">
</rtk-menu>
```
