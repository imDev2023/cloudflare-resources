---
description: API reference for rtk-participant-count component (Web Components (HTML) Library)
title: rtk-participant-count
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participant-count/og.png?v=74692724b6f494d1
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-participant-count

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participant-count/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which shows count of total joined participants in a meeting.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-participant-count></rtk-participant-count>
```

### With Properties

```html
<rtk-participant-count
 size="md">
</rtk-participant-count>
```

```html
<script>
  const el = document.querySelector("rtk-participant-count");

  el.meeting= meeting
</script>
```
