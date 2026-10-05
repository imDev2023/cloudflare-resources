---
description: API reference for rtk-ended-screen component (Web Components (HTML) Library)
title: rtk-ended-screen
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ended-screen/og.png?v=b5a3eae49b0cdfa6
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-ended-screen

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ended-screen/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A screen which shows a meeting has ended.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Global states |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | Global states |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-ended-screen></rtk-ended-screen>
```

### With Properties

```html
<rtk-ended-screen
 size="md">
</rtk-ended-screen>
```

```html
<script>
  const el = document.querySelector("rtk-ended-screen");

  el.meeting= meeting
</script>
```
