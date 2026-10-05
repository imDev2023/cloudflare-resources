---
description: API reference for rtk-recording-indicator component (Angular Library)
title: rtk-recording-indicator
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-recording-indicator/og.png?v=435e332703b7b885
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-recording-indicator

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-recording-indicator/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which indicates the recording status of a meeting. It will not render anything if no recording is taking place.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-recording-indicator></rtk-recording-indicator>
```

### With Properties

```html
<!-- component.html -->
<rtk-recording-indicator
 [meeting]="meeting"
 size="md">
</rtk-recording-indicator>
```
