---
description: API reference for rtk-mic-toggle component (Web Components (HTML) Library)
title: rtk-mic-toggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-mic-toggle/og.png?v=9a55578a6f7da7c6
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-mic-toggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-mic-toggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles your microphone.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<rtk-mic-toggle></rtk-mic-toggle>
```

### With Properties

```html
<rtk-mic-toggle
 size="md"
 variant"button">
</rtk-mic-toggle>
```

```html
<script>
  const el = document.querySelector("rtk-mic-toggle");

  el.meeting= meeting
</script>
```
