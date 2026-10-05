---
description: API reference for rtk-fullscreen-toggle component (Angular Library)
title: rtk-fullscreen-toggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-fullscreen-toggle/og.png?v=9304d9fe2cc6fc01
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-fullscreen-toggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-fullscreen-toggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles full screen mode for any existing `rtk-meeting` component in the DOM.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `targetElement` | `HTMLElement` | ✅ | - | Target Element to fullscreen |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-fullscreen-toggle></rtk-fullscreen-toggle>
```

### With Properties

```html
<!-- component.html -->
<rtk-fullscreen-toggle
 size="md"
 [targetElement]="htmlelement"
 variant="button">
</rtk-fullscreen-toggle>
```
