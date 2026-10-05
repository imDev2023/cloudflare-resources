---
description: API reference for rtk-debugger-screenshare component (Web Components (HTML) Library)
title: rtk-debugger-screenshare
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-debugger-screenshare/og.png?v=b00b38189f1ad5f4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-debugger-screenshare

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-debugger-screenshare/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

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
<rtk-debugger-screenshare></rtk-debugger-screenshare>
```

### With Properties

```html
<rtk-debugger-screenshare
 size="md">
</rtk-debugger-screenshare>
```

```html
<script>
  const el = document.querySelector("rtk-debugger-screenshare");

  el.meeting= meeting
</script>
```
