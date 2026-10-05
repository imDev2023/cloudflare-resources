---
description: API reference for rtk-screen-share-toggle component (Angular Library)
title: rtk-screen-share-toggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-screen-share-toggle/og.png?v=c6672ae9c8273f56
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-screen-share-toggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-screen-share-toggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles your screenshare.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-screen-share-toggle></rtk-screen-share-toggle>
```

### With Properties

```html
<!-- component.html -->
<rtk-screen-share-toggle
 [meeting]="meeting"
 size="md"
 variant="button">
</rtk-screen-share-toggle>
```
