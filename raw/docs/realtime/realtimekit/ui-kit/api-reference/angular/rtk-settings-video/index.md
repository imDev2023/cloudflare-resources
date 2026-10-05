---
description: API reference for rtk-settings-video component (Angular Library)
title: rtk-settings-video
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-settings-video/og.png?v=d41cb82c18540b13
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-settings-video

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-settings-video/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which lets to manage your camera devices and your video preferences. Emits `rtkStateUpdate` event with data for toggling mirroring of self video:

```ts
{
 prefs: {
   mirrorVideo: boolean
 }
}
```

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
<rtk-settings-video></rtk-settings-video>
```

### With Properties

```html
<!-- component.html -->
<rtk-settings-video
 [meeting]="meeting"
 size="md">
</rtk-settings-video>
```
