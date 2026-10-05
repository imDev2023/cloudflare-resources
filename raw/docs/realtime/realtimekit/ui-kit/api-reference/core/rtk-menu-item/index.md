---
description: API reference for rtk-menu-item component (Web Components (HTML) Library)
title: rtk-menu-item
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-menu-item/og.png?v=45467a27c89a202c
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-menu-item

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-menu-item/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A menu item component.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `menuVariant` | `'primary' \| 'secondary'` | ✅ | - | Variant |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-menu-item></rtk-menu-item>
```

### With Properties

```html
<rtk-menu-item
 size="md">
</rtk-menu-item>
```

```html
<script>
  const el = document.querySelector("rtk-menu-item");

</script>
```
