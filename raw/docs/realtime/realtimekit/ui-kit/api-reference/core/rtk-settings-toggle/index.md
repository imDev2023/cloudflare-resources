---
description: API reference for rtk-settings-toggle component (Web Components (HTML) Library)
title: rtk-settings-toggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-settings-toggle/og.png?v=e213233321d468a1
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-settings-toggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-settings-toggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles visibility of settings module. When clicked it emits a `rtkStateUpdate` event with the data:

```ts
{ activeSettings: boolean; }
```

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<rtk-settings-toggle></rtk-settings-toggle>
```

### With Properties

```html
<rtk-settings-toggle
 size="md"
 variant"button">
</rtk-settings-toggle>
```

```html
<script>
  const el = document.querySelector("rtk-settings-toggle");

</script>
```
