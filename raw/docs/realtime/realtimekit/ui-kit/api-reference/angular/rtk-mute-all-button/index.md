---
description: API reference for rtk-mute-all-button component (Angular Library)
title: rtk-mute-all-button
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-mute-all-button/og.png?v=ffbc31736cecbb51
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-mute-all-button

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-mute-all-button/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-mute-all-button></rtk-mute-all-button>
```

### With Properties

```html
<!-- component.html -->
<rtk-mute-all-button
 [meeting]="meeting"
 size="md"
 variant="button">
</rtk-mute-all-button>
```
