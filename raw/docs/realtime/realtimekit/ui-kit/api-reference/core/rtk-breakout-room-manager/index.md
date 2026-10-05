---
description: API reference for rtk-breakout-room-manager component (Web Components (HTML) Library)
title: rtk-breakout-room-manager
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-room-manager/og.png?v=db77268b8a814256
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-breakout-room-manager

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-breakout-room-manager/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `allowDelete` | `boolean` | ✅ | - | allow room delete |
| `assigningParticipants` | `boolean` | ✅ | - | Enable updating participants |
| `defaultExpanded` | `boolean` | ✅ | - | display expanded card by default |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `isDragMode` | `boolean` | ✅ | - | Drag mode |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `mode` | `'edit' \| 'create'` | ✅ | - | Mode in which selector is used |
| `room` | `DraftMeeting` | ✅ | - | Connected Room Config Object |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-breakout-room-manager></rtk-breakout-room-manager>
```

### With Properties

```html
<rtk-breakout-room-manager>
</rtk-breakout-room-manager>
```

```html
<script>
  const el = document.querySelector("rtk-breakout-room-manager");

  el.allowDelete= true;
  el.assigningParticipants= true;
  el.defaultExpanded= true;
</script>
```
