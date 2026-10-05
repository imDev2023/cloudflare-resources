---
description: API reference for rtk-mute-all-confirmation component (Angular Library)
title: rtk-mute-all-confirmation
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-mute-all-confirmation/og.png?v=b0a37e80ed13e1db
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-mute-all-confirmation

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-mute-all-confirmation/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

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
<rtk-mute-all-confirmation></rtk-mute-all-confirmation>
```

### With Properties

```html
<!-- component.html -->
<rtk-mute-all-confirmation
 [meeting]="meeting">
</rtk-mute-all-confirmation>
```
