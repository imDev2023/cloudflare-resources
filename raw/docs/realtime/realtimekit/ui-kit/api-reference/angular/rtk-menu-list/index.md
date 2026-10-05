---
description: API reference for rtk-menu-list component (Angular Library)
title: rtk-menu-list
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-menu-list/og.png?v=ff7804769fd8a7d3
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-menu-list

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-menu-list/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A menu list component.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `menuVariant` | `'primary' \| 'secondary'` | ✅ | - | Variant |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-menu-list></rtk-menu-list>
```

### With Properties

```html
<!-- component.html -->
<rtk-menu-list
 [menuVariant]="'primary' | 'secondary'">
</rtk-menu-list>
```
