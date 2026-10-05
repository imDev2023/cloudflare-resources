---
description: API reference for rtk-counter component (Web Components (HTML) Library)
title: rtk-counter
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-counter/og.png?v=a59f74f7780a7ea7
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-counter

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-counter/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A number picker with increment and decrement buttons.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `minValue` | `number` | ✅ | - | Minimum value |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `value` | `number` | ✅ | - | Initial value |

## Usage Examples

### Basic Usage

```html
<rtk-counter></rtk-counter>
```

### With Properties

```html
<rtk-counter
 size="md">
</rtk-counter>
```

```html
<script>
  const el = document.querySelector("rtk-counter");

  el.minValue= 42;
  el.value= 42;
</script>
```
