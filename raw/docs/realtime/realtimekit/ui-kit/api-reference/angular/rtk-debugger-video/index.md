---
description: API reference for rtk-debugger-video component (Angular Library)
title: rtk-debugger-video
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-debugger-video/og.png?v=59f83d7182e9d9a3
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-debugger-video

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-debugger-video/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `states` | `States1` | ✅ | - | States object |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-debugger-video></rtk-debugger-video>
```

### With Properties

```html
<!-- component.html -->
<rtk-debugger-video
 [meeting]="meeting"
 size="md">
</rtk-debugger-video>
```
