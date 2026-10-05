---
description: API reference for rtk-participants-audio component (Web Components (HTML) Library)
title: rtk-participants-audio
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-audio/og.png?v=df6a40db861ab214
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-participants-audio

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-participants-audio/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which plays all the audio from participants and screenshares.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `preloadedAudioElem` | `HTMLAudioElement` | ✅ | - | Pass existing audio element |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-participants-audio></rtk-participants-audio>
```

### With Properties

```html
<rtk-participants-audio>
</rtk-participants-audio>
```

```html
<script>
  const el = document.querySelector("rtk-participants-audio");

  el.meeting= meeting
</script>
```
