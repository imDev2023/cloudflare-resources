---
description: API reference for rtk-participants component (Angular Library)
title: rtk-participants
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participants/og.png?v=af9c4fc3c7b2caa7
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-participants

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participants/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which lists all participants, with ability to run privileged actions on each participant according to your permissions.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config |
| `defaultParticipantsTabId` | `ParticipantsTabId` | ✅ | - | Default section |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-participants></rtk-participants>
```

### With Properties

```html
<!-- component.html -->
<rtk-participants
 [defaultParticipantsTabId]="participantstabid"
 [meeting]="meeting"
 size="md">
</rtk-participants>
```
