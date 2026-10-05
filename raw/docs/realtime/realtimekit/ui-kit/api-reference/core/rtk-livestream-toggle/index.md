---
description: API reference for rtk-livestream-toggle component (Web Components (HTML) Library)
title: rtk-livestream-toggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-livestream-toggle/og.png?v=ce3a16e45e2040ad
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-livestream-toggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-livestream-toggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<rtk-livestream-toggle></rtk-livestream-toggle>
```

### With Properties

```html
<rtk-livestream-toggle
 size="md"
 variant"button">
</rtk-livestream-toggle>
```

```html
<script>
  const el = document.querySelector("rtk-livestream-toggle");

  el.meeting= meeting
</script>
```
