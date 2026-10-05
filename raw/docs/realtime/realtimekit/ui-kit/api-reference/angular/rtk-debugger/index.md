---
description: API reference for rtk-debugger component (Angular Library)
title: rtk-debugger
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-debugger/og.png?v=eaf6655e4ca7f24b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-debugger

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-debugger/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A troubleshooting component to identify and fix any issues in the meeting.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-debugger></rtk-debugger>
```

### With Properties

```html
<!-- component.html -->
<rtk-debugger
 [meeting]="meeting"
 size="md">
</rtk-debugger>
```
