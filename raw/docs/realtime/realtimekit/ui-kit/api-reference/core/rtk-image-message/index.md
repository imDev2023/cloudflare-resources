---
description: API reference for rtk-image-message component (Web Components (HTML) Library)
title: rtk-image-message
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-image-message/og.png?v=e2cffeda75103c3b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-image-message

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-image-message/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

@deprecated `rtk-image-message` is deprecated and will be removed soon. Use `rtk-image-message-view` instead. A component which renders an image message from chat.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `isContinued` | `boolean` | ✅ | - | Whether the message is continued by same user |
| `message` | `ImageMessage` | ✅ | - | Text message object |
| `now` | `Date` | ✅ | - | Date object of now, to calculate distance between dates |
| `showBubble` | `boolean` | ✅ | - | show message in bubble |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-image-message></rtk-image-message>
```

### With Properties

```html
<rtk-image-message>
</rtk-image-message>
```

```html
<script>
  const el = document.querySelector("rtk-image-message");

  el.isContinued= true;
</script>
```
