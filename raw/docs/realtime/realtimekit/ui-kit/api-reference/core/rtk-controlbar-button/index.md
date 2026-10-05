---
description: API reference for rtk-controlbar-button component (Web Components (HTML) Library)
title: rtk-controlbar-button
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-controlbar-button/og.png?v=5ee8492d34cf28ac
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-controlbar-button

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-controlbar-button/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A skeleton component used for composing custom controlbar buttons.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `brandIcon` | `boolean` | ✅ | - | Whether icon requires brand color |
| `disabled` | `boolean` | ✅ | - | Whether button is disabled |
| `icon` | `string` | ✅ | - | Icon |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `isLoading` | `boolean` | ✅ | - | Loading state Ignores current icon and shows a spinner if true |
| `label` | `string` | ✅ | - | Label of button |
| `showWarning` | `boolean` | ✅ | - | Whether to show warning icon |
| `size` | `Size` | ✅ | - | Size |
| `variant` | `ControlBarVariant1` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<rtk-controlbar-button></rtk-controlbar-button>
```

### With Properties

```html
<rtk-controlbar-button
 icon="example">
</rtk-controlbar-button>
```

```html
<script>
  const el = document.querySelector("rtk-controlbar-button");

  el.brandIcon= true;
  el.disabled= true;
</script>
```
