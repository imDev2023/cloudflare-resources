---
description: API reference for rtk-header component (Angular Library)
title: rtk-header
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-header/og.png?v=a4eedf4424ecfe7d
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-header

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-header/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component that houses all the header components.

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
<rtk-header></rtk-header>
```

### With Properties

```html
<!-- component.html -->
<rtk-header
 [disableRender]="true"
 [meeting]="meeting"
 size="md">
</rtk-header>
```
