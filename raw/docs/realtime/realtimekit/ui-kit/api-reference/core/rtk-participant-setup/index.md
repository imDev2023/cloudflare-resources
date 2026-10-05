---
description: API reference for rtk-participant-setup component (Web Components (HTML) Library)
title: rtk-participant-setup
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participant-setup/og.png?v=a7accf3ccde04137
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-participant-setup

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participant-setup/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `isPreview` | `boolean` | ✅ | - | Whether tile is used for preview |
| `nameTagPosition` | `\| 'bottom-left' \| 'bottom-right' \| 'bottom-center' \| 'top-left' \| 'top-right' \| 'top-center'` | ✅ | - | Position of name tag |
| `participant` | `Peer` | ✅ | - | Participant object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `'solid' \| 'gradient'` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<rtk-participant-setup></rtk-participant-setup>
```

### With Properties

```html
<rtk-participant-setup>
</rtk-participant-setup>
```

```html
<script>
  const el = document.querySelector("rtk-participant-setup");

  el.isPreview= true;
  el.participant= participant
</script>
```
