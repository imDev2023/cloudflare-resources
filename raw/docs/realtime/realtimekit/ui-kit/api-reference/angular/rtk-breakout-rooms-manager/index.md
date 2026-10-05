---
description: API reference for rtk-breakout-rooms-manager component (Angular Library)
title: rtk-breakout-rooms-manager
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-breakout-rooms-manager/og.png?v=90b2d65bfe96d763
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-breakout-rooms-manager

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-breakout-rooms-manager/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-breakout-rooms-manager></rtk-breakout-rooms-manager>
```

### With Properties

```html
<!-- component.html -->
<rtk-breakout-rooms-manager
 [meeting]="meeting">
</rtk-breakout-rooms-manager>
```
