---
description: API reference for rtk-meeting-title component (Angular Library)
title: rtk-meeting-title
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-meeting-title/og.png?v=ce7faf3d2f97b763
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-meeting-title

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-meeting-title/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Displays the title of the meeting.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-meeting-title></rtk-meeting-title>
```

### With Properties

```html
<!-- component.html -->
<rtk-meeting-title
 [meeting]="meeting">
</rtk-meeting-title>
```
