---
description: API reference for rtk-livestream-player component (Angular Library)
title: rtk-livestream-player
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-livestream-player/og.png?v=a5128dc647339d3a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-livestream-player

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-livestream-player/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-livestream-player></rtk-livestream-player>
```

### With Properties

```html
<!-- component.html -->
<rtk-livestream-player
 [meeting]="meeting"
 size="md">
</rtk-livestream-player>
```
