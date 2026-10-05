---
description: API reference for rtk-ai component (Web Components (HTML) Library)
title: rtk-ai
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ai/og.png?v=18ed15be9f5339a7
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-ai

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ai/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `view` | `AIView` | ✅ | - | View type |

## Usage Examples

### Basic Usage

```html
<rtk-ai></rtk-ai>
```

### With Properties

```html
<rtk-ai
 size="md">
</rtk-ai>
```

```html
<script>
  const el = document.querySelector("rtk-ai");

  el.meeting= meeting
</script>
```
