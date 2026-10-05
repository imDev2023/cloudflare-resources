---
description: API reference for rtk-spotlight-indicator component (Angular Library)
title: rtk-spotlight-indicator
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-spotlight-indicator/og.png?v=ef472b9589036213
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-spotlight-indicator

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-spotlight-indicator/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-spotlight-indicator></rtk-spotlight-indicator>
```

### With Properties

```html
<!-- component.html -->
<rtk-spotlight-indicator
 [meeting]="meeting"
 size="md">
</rtk-spotlight-indicator>
```
