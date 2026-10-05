---
description: API reference for rtk-livestream-indicator component (Angular Library)
title: rtk-livestream-indicator
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-livestream-indicator/og.png?v=05b98351a8c55402
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-livestream-indicator

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-livestream-indicator/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-livestream-indicator></rtk-livestream-indicator>
```

### With Properties

```html
<!-- component.html -->
<rtk-livestream-indicator
 [meeting]="meeting"
 size="md">
</rtk-livestream-indicator>
```
