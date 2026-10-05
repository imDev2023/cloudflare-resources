---
description: API reference for rtk-permissions-message component (Angular Library)
title: rtk-permissions-message
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-permissions-message/og.png?v=6f3e1eb5172062ce
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-permissions-message

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-permissions-message/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which shows permission related troubleshooting information.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-permissions-message></rtk-permissions-message>
```

### With Properties

```html
<!-- component.html -->
<rtk-permissions-message
 [meeting]="meeting">
</rtk-permissions-message>
```
