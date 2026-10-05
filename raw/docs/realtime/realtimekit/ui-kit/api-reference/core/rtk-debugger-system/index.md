---
description: API reference for rtk-debugger-system component (Web Components (HTML) Library)
title: rtk-debugger-system
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-debugger-system/og.png?v=a149afa59ba5e066
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-debugger-system

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-debugger-system/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `states` | `States1` | ✅ | - | States object |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-debugger-system></rtk-debugger-system>
```

### With Properties

```html
<rtk-debugger-system
 size="md">
</rtk-debugger-system>
```

```html
<script>
  const el = document.querySelector("rtk-debugger-system");

  el.meeting= meeting
</script>
```
