---
description: API reference for rtk-camera-toggle component (Angular Library)
title: rtk-camera-toggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-camera-toggle/og.png?v=05950388d500ad81
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-camera-toggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-camera-toggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles your camera.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-camera-toggle></rtk-camera-toggle>
```

### With Properties

```html
<!-- component.html -->
<rtk-camera-toggle
 [meeting]="meeting"
 size="md"
 variant="button">
</rtk-camera-toggle>
```
