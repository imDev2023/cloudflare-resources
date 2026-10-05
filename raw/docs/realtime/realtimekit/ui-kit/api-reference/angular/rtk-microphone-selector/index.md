---
description: API reference for rtk-microphone-selector component (Angular Library)
title: rtk-microphone-selector
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-microphone-selector/og.png?v=b765b91ac39b6434
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-microphone-selector

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-microphone-selector/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

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
<!-- component.html -->
<rtk-microphone-selector></rtk-microphone-selector>
```

### With Properties

```html
<!-- component.html -->
<rtk-microphone-selector
 [meeting]="meeting"
 size="md"
 [variant]="'full' | 'inline'">
</rtk-microphone-selector>
```
