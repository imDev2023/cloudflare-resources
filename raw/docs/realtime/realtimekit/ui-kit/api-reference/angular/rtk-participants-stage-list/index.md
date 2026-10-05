---
description: API reference for rtk-participants-stage-list component (Angular Library)
title: rtk-participants-stage-list
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participants-stage-list/og.png?v=f06e9067f21a3f5b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-participants-stage-list

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participants-stage-list/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which lists all participants, with ability to run privileged actions on each participant according to your permissions.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config |
| `hideHeader` | `boolean` | ✅ | - | Hide Stage Participants Count Header |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `search` | `string` | ✅ | - | Search |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States1` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `view` | `ParticipantsViewMode` | ✅ | - | View mode for participants list |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-participants-stage-list></rtk-participants-stage-list>
```

### With Properties

```html
<!-- component.html -->
<rtk-participants-stage-list
 [hideHeader]="true"
 [meeting]="meeting"
 search="example">
</rtk-participants-stage-list>
```
