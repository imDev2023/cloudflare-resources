---
description: API reference for rtk-dialog-manager component (Angular Library)
title: rtk-dialog-manager
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-dialog-manager/og.png?v=63bc93188dc24fcd
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-dialog-manager

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-dialog-manager/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which handles all dialog elements in a component such as:

- rtk-settings
- rtk-leave-meeting
- rtk-permissions-message
- rtk-image-viewer
- rtk-breakout-rooms-manager This components depends on the values from `states` object.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-dialog-manager></rtk-dialog-manager>
```

### With Properties

```html
<!-- component.html -->
<rtk-dialog-manager
 [meeting]="meeting"
 size="md">
</rtk-dialog-manager>
```
