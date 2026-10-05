---
description: API reference for rtk-button component (Angular Library)
title: rtk-button
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-button/og.png?v=fc3c1f2687f82fa2
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-button

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-button/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button that follows RTK Design System.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `disabled` | `boolean` | ✅ | - | Where the button is disabled or not |
| `kind` | `ButtonKind` | ✅ | - | Button type |
| `reverse` | `boolean` | ✅ | - | Whether to reverse order of children |
| `size` | `Size` | ✅ | - | Size |
| `type` | `HTMLButtonElement['type']` | ✅ | - | Button type |
| `variant` | `ButtonVariant` | ✅ | - | Button variant |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-button></rtk-button>
```

### With Properties

```html
<!-- component.html -->
<rtk-button
 [disabled]="true"
 [kind]="buttonkind"
 [reverse]="true">
</rtk-button>
```
