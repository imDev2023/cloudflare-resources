---
description: API reference for rtk-network-indicator component (Web Components (HTML) Library)
title: rtk-network-indicator
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-network-indicator/og.png?v=3d441c0ca0abf70d
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-network-indicator

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-network-indicator/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `isScreenShare` | `boolean` | ✅ | - | Is for screenshare |
| `meeting` | `Meeting` | ✅ | - | Meeting |
| `participant` | `Peer` | ✅ | - | Participant or Self |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-network-indicator></rtk-network-indicator>
```

### With Properties

```html
<rtk-network-indicator>
</rtk-network-indicator>
```

```html
<script>
  const el = document.querySelector("rtk-network-indicator");

  el.isScreenShare= true;
  el.meeting= meeting
  el.participant= participant
</script>
```
