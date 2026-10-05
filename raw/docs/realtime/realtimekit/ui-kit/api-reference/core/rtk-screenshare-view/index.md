---
description: API reference for rtk-screenshare-view component (Web Components (HTML) Library)
title: rtk-screenshare-view
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-screenshare-view/og.png?v=973ed3336700bbc3
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-screenshare-view

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-screenshare-view/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which plays a participant's screenshared video. It also allows for placement of other components similar to `rtk-participant-tile`. This component will not render anything if the participant hasn't start screensharing.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `hideFullScreenButton` | `boolean` | ✅ | - | Hide full screen button |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `nameTagPosition` | `\| 'bottom-left' \| 'bottom-right' \| 'bottom-center' \| 'top-left' \| 'top-right' \| 'top-center'` | ✅ | - | Position of name tag |
| `participant` | `Peer` | ✅ | - | Participant object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `'solid' \| 'gradient'` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<rtk-screenshare-view></rtk-screenshare-view>
```

### With Properties

```html
<rtk-screenshare-view>
</rtk-screenshare-view>
```

```html
<script>
  const el = document.querySelector("rtk-screenshare-view");

  el.hideFullScreenButton= true;
  el.meeting= meeting
</script>
```
