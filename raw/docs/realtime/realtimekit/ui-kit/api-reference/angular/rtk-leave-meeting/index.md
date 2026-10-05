---
description: API reference for rtk-leave-meeting component (Angular Library)
title: rtk-leave-meeting
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-leave-meeting/og.png?v=2ef37d944be78cfe
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-leave-meeting

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-leave-meeting/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which allows you to leave a meeting or end meeting for all, if you have the permission.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-leave-meeting></rtk-leave-meeting>
```

### With Properties

```html
<!-- component.html -->
<rtk-leave-meeting
 [meeting]="meeting">
</rtk-leave-meeting>
```
