---
description: API reference for rtk-idle-screen component (Web Components (HTML) Library)
title: rtk-idle-screen
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-idle-screen/og.png?v=9ae3eabfabc2faf5
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-idle-screen

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-idle-screen/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A screen that handles the idle state, i.e; when you are waiting for data about the meeting, specifically the `meeting` object.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-idle-screen></rtk-idle-screen>
```

### With Properties

```html
<rtk-idle-screen>
</rtk-idle-screen>
```

```html
<script>
  const el = document.querySelector("rtk-idle-screen");

  el.meeting= meeting
</script>
```
