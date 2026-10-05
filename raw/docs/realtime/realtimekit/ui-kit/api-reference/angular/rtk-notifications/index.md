---
description: API reference for rtk-notifications component (Angular Library)
title: rtk-notifications
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-notifications/og.png?v=d56f5082c7c85b24
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-notifications

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-notifications/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which handles notifications. You can configure which notifications you want to see and which ones you want to hear. There are also certain limits which you can set as well.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-notifications></rtk-notifications>
```

### With Properties

```html
<!-- component.html -->
<rtk-notifications
 [meeting]="meeting"
 size="md">
</rtk-notifications>
```
