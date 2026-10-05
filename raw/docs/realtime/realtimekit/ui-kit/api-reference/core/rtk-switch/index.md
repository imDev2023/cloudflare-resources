---
description: API reference for rtk-switch component (Web Components (HTML) Library)
title: rtk-switch
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-switch/og.png?v=97a7d3a863f6b6d4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-switch

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-switch/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A switch component which follows RTK Design System.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `checked` | `boolean` | ✅ | - | Whether the switch is enabled/checked |
| `disabled` | `boolean` | ✅ | - | Whether switch is readonly |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `readonly` | `boolean` | ✅ | - | Whether switch is readonly |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-switch></rtk-switch>
```

### With Properties

```html
<rtk-switch>
</rtk-switch>
```

```html
<script>
  const el = document.querySelector("rtk-switch");

  el.checked= true;
  el.disabled= true;
  el.readonly= true;
</script>
```
