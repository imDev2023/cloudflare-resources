---
description: API reference for rtk-debugger-toggle component (Angular Library)
title: rtk-debugger-toggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-debugger-toggle/og.png?v=68e15a59ae734d3b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-debugger-toggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-debugger-toggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-debugger-toggle></rtk-debugger-toggle>
```

### With Properties

```html
<!-- component.html -->
<rtk-debugger-toggle
 [meeting]="meeting"
 size="md"
 variant="button">
</rtk-debugger-toggle>
```
