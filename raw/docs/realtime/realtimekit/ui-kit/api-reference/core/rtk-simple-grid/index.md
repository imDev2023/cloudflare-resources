---
description: API reference for rtk-simple-grid component (Web Components (HTML) Library)
title: rtk-simple-grid
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-simple-grid/og.png?v=57f8eba9d298fbbc
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-simple-grid

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-simple-grid/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A grid component which renders only the participants in a simple grid.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `aspectRatio` | `string` | ✅ | - | Aspect Ratio of participant tile Format: `width:height` |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config |
| `gap` | `number` | ✅ | - | Gap between participant tiles |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `participants` | `Peer[]` | ✅ | - | Participants |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-simple-grid></rtk-simple-grid>
```

### With Properties

```html
<rtk-simple-grid
 aspectRatio="example">
</rtk-simple-grid>
```

```html
<script>
  const el = document.querySelector("rtk-simple-grid");

  el.gap= 42;
  el.meeting= meeting
</script>
```
