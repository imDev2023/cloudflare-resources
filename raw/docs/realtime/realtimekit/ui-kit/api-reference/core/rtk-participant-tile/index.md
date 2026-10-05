---
description: API reference for rtk-participant-tile component (Web Components (HTML) Library)
title: rtk-participant-tile
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participant-tile/og.png?v=4bf284a1fa20deaf
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-participant-tile

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participant-tile/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which plays a participants video and allows for placement of components like `rtk-name-tag`, `rtk-audio-visualizer` or any other component.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `isPreview` | `boolean` | ✅ | - | Whether tile is used for preview |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `nameTagPosition` | `\| 'bottom-left' \| 'bottom-right' \| 'bottom-center' \| 'top-left' \| 'top-right' \| 'top-center'` | ✅ | - | Position of name tag |
| `participant` | `Peer` | ✅ | - | Participant object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `'solid' \| 'gradient'` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<rtk-participant-tile></rtk-participant-tile>
```

### With Properties

```html
<rtk-participant-tile>
</rtk-participant-tile>
```

```html
<script>
  const el = document.querySelector("rtk-participant-tile");

  el.isPreview= true;
  el.meeting= meeting
</script>
```
