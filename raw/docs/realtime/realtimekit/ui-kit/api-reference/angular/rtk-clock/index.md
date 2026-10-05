---
description: API reference for rtk-clock component (Angular Library)
title: rtk-clock
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-clock/og.png?v=e377d8b29a9992aa
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-clock

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-clock/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Shows the time elapsed in a meeting.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-clock></rtk-clock>
```

### With Properties

```html
<!-- component.html -->
<rtk-clock
 [meeting]="meeting"
 size="md">
</rtk-clock>
```
