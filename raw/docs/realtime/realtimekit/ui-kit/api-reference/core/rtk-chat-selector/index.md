---
description: API reference for rtk-chat-selector component (Web Components (HTML) Library)
title: rtk-chat-selector
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-selector/og.png?v=3a9aea99934bd958
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-chat-selector

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-selector/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `overrides` | `Overrides1` | ❌ | `defaultOverrides` | UI Overrides |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States1` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-chat-selector></rtk-chat-selector>
```

### With Properties

```html
<rtk-chat-selector
 size="md">
</rtk-chat-selector>
```

```html
<script>
  const el = document.querySelector("rtk-chat-selector");

  el.meeting= meeting
</script>
```
