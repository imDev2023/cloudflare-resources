---
description: API reference for rtk-grid-pagination component (Angular Library)
title: rtk-grid-pagination
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-grid-pagination/og.png?v=fa06c0bef78201f2
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-grid-pagination

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-grid-pagination/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which allows you to change current page and view mode of active participants list. This is reflected in the `rtk-grid` component.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size Prop |
| `states` | `States` | ✅ | - | States |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `GridPaginationVariants` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-grid-pagination></rtk-grid-pagination>
```

### With Properties

```html
<!-- component.html -->
<rtk-grid-pagination
 [meeting]="meeting"
 size="md"
 [variant]="gridpaginationvariants">
</rtk-grid-pagination>
```
