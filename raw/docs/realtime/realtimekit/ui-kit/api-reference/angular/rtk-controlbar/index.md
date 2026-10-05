---
description: API reference for rtk-controlbar component (Angular Library)
title: rtk-controlbar
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-controlbar/og.png?v=101198d9c7da13cd
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-controlbar

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-controlbar/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Controlbar component provides you with various designs as variants.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config |
| `disableRender` | `boolean` | ✅ | - | Whether to render the default UI |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon Pack |
| `meeting` | `Meeting` | ✅ | - | Meeting |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `'solid' \| 'boxed'` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-controlbar></rtk-controlbar>
```

### With Properties

```html
<!-- component.html -->
<rtk-controlbar
 [disableRender]="true"
 [meeting]="meeting"
 size="md">
</rtk-controlbar>
```
