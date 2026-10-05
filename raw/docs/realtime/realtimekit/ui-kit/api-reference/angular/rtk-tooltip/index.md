---
description: API reference for rtk-tooltip component (Angular Library)
title: rtk-tooltip
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-tooltip/og.png?v=b5c2e3366f718ab7
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-tooltip

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-tooltip/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Tooltip component which follows RTK Design System.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `delay` | `number` | ✅ | - | Delay before showing the tooltip |
| `disabled` | `boolean` | ✅ | - | Disabled |
| `kind` | `TooltipKind` | ✅ | - | Tooltip kind |
| `label` | `string` | ✅ | - | Tooltip label |
| `open` | `boolean` | ✅ | - | Open |
| `placement` | `Placement` | ✅ | - | Placement of menu |
| `size` | `Size` | ✅ | - | Size |
| `variant` | `TooltipVariant` | ✅ | - | Tooltip variant |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-tooltip></rtk-tooltip>
```

### With Properties

```html
<!-- component.html -->
<rtk-tooltip
 delay="42"
 [disabled]="true"
 [kind]="tooltipkind">
</rtk-tooltip>
```
