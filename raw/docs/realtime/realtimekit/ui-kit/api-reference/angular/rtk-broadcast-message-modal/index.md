---
description: API reference for rtk-broadcast-message-modal component (Angular Library)
title: rtk-broadcast-message-modal
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-broadcast-message-modal/og.png?v=75786741272b2c87
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-broadcast-message-modal

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-broadcast-message-modal/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `states` | `States1` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-broadcast-message-modal></rtk-broadcast-message-modal>
```

### With Properties

```html
<!-- component.html -->
<rtk-broadcast-message-modal
 [meeting]="meeting">
</rtk-broadcast-message-modal>
```
