---
description: API reference for rtk-emoji-picker-button component (Angular Library)
title: rtk-emoji-picker-button
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-emoji-picker-button/og.png?v=43a975a67ab98bb7
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-emoji-picker-button

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-emoji-picker-button/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `isActive` | `boolean` | ✅ | - | Active state indicator |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-emoji-picker-button></rtk-emoji-picker-button>
```

### With Properties

```html
<!-- component.html -->
<rtk-emoji-picker-button
 [isActive]="true">
</rtk-emoji-picker-button>
```
