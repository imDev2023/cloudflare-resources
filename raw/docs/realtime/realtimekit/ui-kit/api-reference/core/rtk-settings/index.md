---
description: API reference for rtk-settings component (Web Components (HTML) Library)
title: rtk-settings
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-settings/og.png?v=39d168a59c78433f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-settings

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-settings/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A settings component to see and change your audio/video devices as well as see your connection quality.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-settings></rtk-settings>
```

### With Properties

```html
<rtk-settings
 size="md">
</rtk-settings>
```

```html
<script>
  const el = document.querySelector("rtk-settings");

  el.meeting= meeting
</script>
```
