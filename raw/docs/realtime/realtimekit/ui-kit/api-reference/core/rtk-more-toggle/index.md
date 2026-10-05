---
description: API reference for rtk-more-toggle component (Web Components (HTML) Library)
title: rtk-more-toggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-more-toggle/og.png?v=f4e53a7074dd9f07
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-more-toggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-more-toggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles visibility of a more menu. When clicked it emits a `rtkStateUpdate` event with the data:

```ts
{ activeMoreMenu: boolean; }
```

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-more-toggle></rtk-more-toggle>
```

### With Properties

```html
<rtk-more-toggle
 size="md">
</rtk-more-toggle>
```

```html
<script>
  const el = document.querySelector("rtk-more-toggle");

</script>
```
