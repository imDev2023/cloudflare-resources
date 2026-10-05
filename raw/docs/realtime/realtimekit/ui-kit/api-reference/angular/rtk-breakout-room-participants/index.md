---
description: API reference for rtk-breakout-room-participants component (Angular Library)
title: rtk-breakout-room-participants
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-breakout-room-participants/og.png?v=5c7adcce59b5bee3
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-breakout-room-participants

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-breakout-room-participants/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which lists all participants, with ability to run privileged actions on each participant according to your permissions.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `participantIds` | `string[]` | ✅ | - | Participant ids |
| `selectedParticipantIds` | `string[]` | ✅ | - | selected participants |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-breakout-room-participants></rtk-breakout-room-participants>
```

### With Properties

```html
<!-- component.html -->
<rtk-breakout-room-participants
 [meeting]="meeting"
 participantIds="example"
 selectedParticipantIds="example">
</rtk-breakout-room-participants>
```
