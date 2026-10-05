---
description: API reference for rtk-audio-tile component (Angular Library)
title: rtk-audio-tile
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-audio-tile/og.png?v=c84ac18186162faf
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-audio-tile

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-audio-tile/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ✅ | - | Config |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting |
| `participant` | `Peer` | ✅ | - | Participant object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States1` | ✅ | - | States |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-audio-tile></rtk-audio-tile>
```

### With Properties

```html
<!-- component.html -->
<rtk-audio-tile
 [config]="defaultUiConfig"
 [meeting]="meeting"
 [participant]="participant">
</rtk-audio-tile>
```
