---
description: API reference for rtk-viewer-count component (Angular Library)
title: rtk-viewer-count
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-viewer-count/og.png?v=9999c11e8b194076
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-viewer-count

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-viewer-count/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which shows count of total joined participants in a meeting.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ViewerCountVariant` | ✅ | - | Viewer count variant |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-viewer-count></rtk-viewer-count>
```

### With Properties

```html
<!-- component.html -->
<rtk-viewer-count
 [meeting]="meeting"
 variant="primary">
</rtk-viewer-count>
```
