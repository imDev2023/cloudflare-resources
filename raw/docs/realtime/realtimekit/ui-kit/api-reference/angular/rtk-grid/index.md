---
description: API reference for rtk-grid component (Angular Library)
title: rtk-grid
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-grid/og.png?v=fc43d4abae41eea7
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-grid

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-grid/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

The main grid component which abstracts all the grid handling logic and renders it for you.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `aspectRatio` | `string` | ✅ | - | The aspect ratio of each participant |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `gap` | `number` | ✅ | - | Gap between participants |
| `gridSize` | `GridSize` | ✅ | - | Grid size |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `layout` | `GridLayout` | ✅ | - | Grid Layout |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `overrides` | `any` | ✅ | - | @deprecated |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-grid></rtk-grid>
```

### With Properties

```html
<!-- component.html -->
<rtk-grid
 aspectRatio="example"
 gap="42"
 gridSize="md">
</rtk-grid>
```
