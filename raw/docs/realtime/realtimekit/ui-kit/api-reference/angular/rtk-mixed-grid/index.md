---
description: API reference for rtk-mixed-grid component (Angular Library)
title: rtk-mixed-grid
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-mixed-grid/og.png?v=f7dc944ae826ca98
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-mixed-grid

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-mixed-grid/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A grid component which handles screenshares, plugins and participants.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `aspectRatio` | `string` | ✅ | - | Aspect Ratio of participant tile Format: `width:height` |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config |
| `gap` | `number` | ✅ | - | Gap between participant tiles |
| `gridSize` | `GridSize1` | ✅ | - | Grid size |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack |
| `layout` | `GridLayout1` | ✅ | - | Grid Layout |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `participants` | `Peer[]` | ✅ | - | Participants |
| `pinnedParticipants` | `Peer[]` | ✅ | - | Pinned Participants |
| `plugins` | `RTKPlugin[]` | ✅ | - | Active Plugins |
| `screenShareParticipants` | `Peer[]` | ✅ | - | Screenshare Participants |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-mixed-grid></rtk-mixed-grid>
```

### With Properties

```html
<!-- component.html -->
<rtk-mixed-grid
 aspectRatio="example"
 gap="42"
 gridSize="md">
</rtk-mixed-grid>
```
