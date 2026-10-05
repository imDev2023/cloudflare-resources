---
description: API reference for rtk-camera-selector component (Web Components (HTML) Library)
title: rtk-camera-selector
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-camera-selector/og.png?v=fc8b11ccceea1ffc
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-camera-selector

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-camera-selector/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which lets to manage your audio devices and audio preferences. Emits `rtkStateUpdate` event with data for muting notification sounds:

```ts
{
 prefs: {
   muteNotificationSounds: boolean
 }
}
```

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `'full' \| 'inline'` | ✅ | - | variant |

## Usage Examples

### Basic Usage

```html
<rtk-camera-selector></rtk-camera-selector>
```

### With Properties

```html
<rtk-camera-selector
 size="md">
</rtk-camera-selector>
```

```html
<script>
  const el = document.querySelector("rtk-camera-selector");

  el.meeting= meeting
</script>
```
