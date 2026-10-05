---
description: API reference for rtk-audio-grid component (Web Components (HTML) Library)
title: rtk-audio-grid
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-audio-grid/og.png?v=7d29043753b524f4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-audio-grid

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-audio-grid/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig1` | ✅ | - | Config |
| `hideSelf` | `boolean` | ✅ | - | Whether to hide self in the grid |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon Pack |
| `meeting` | `Meeting` | ✅ | - | Meeting |
| `size` | `Size1` | ✅ | - | Size |
| `states` | `States1` | ✅ | - | States |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-audio-grid></rtk-audio-grid>
```

### With Properties

```html
<rtk-audio-grid>
</rtk-audio-grid>
```

```html
<script>
  const el = document.querySelector("rtk-audio-grid");

  el.config= defaultUiConfig
  el.hideSelf= true;
  el.meeting= meeting
</script>
```
