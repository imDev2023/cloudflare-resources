---
description: API reference for rtk-breakout-rooms-toggle component (Angular Library)
title: rtk-breakout-rooms-toggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-breakout-rooms-toggle/og.png?v=746672cdbee45b32
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-breakout-rooms-toggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-breakout-rooms-toggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles visibility of breakout rooms. You need to pass the `meeting` object to it.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ✅ | - | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ✅ | - | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-breakout-rooms-toggle></rtk-breakout-rooms-toggle>
```

### With Properties

```html
<!-- component.html -->
<rtk-breakout-rooms-toggle
 [iconPack]="defaultIconPack"
 [meeting]="meeting"
 size="md">
</rtk-breakout-rooms-toggle>
```
