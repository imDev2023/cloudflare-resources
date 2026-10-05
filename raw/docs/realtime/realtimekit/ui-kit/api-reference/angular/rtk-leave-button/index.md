---
description: API reference for rtk-leave-button component (Angular Library)
title: rtk-leave-button
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-leave-button/og.png?v=21e60bc6e8997bfb
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-leave-button

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-leave-button/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles visilibility of the leave confirmation dialog.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-leave-button></rtk-leave-button>
```

### With Properties

```html
<!-- component.html -->
<rtk-leave-button
 size="md"
 variant="button">
</rtk-leave-button>
```
