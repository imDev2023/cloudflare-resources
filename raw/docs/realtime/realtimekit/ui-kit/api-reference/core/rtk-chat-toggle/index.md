---
description: API reference for rtk-chat-toggle component (Web Components (HTML) Library)
title: rtk-chat-toggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-toggle/og.png?v=03fec893b711e97e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-chat-toggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-toggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles visibility of chat. You need to pass the `meeting` object to it to see the unread messages count badge. When clicked it emits a `rtkStateUpdate` event with the data:

```ts
{ activeSidebar: boolean; sidebar: 'chat' }
```

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<rtk-chat-toggle></rtk-chat-toggle>
```

### With Properties

```html
<rtk-chat-toggle
 size="md"
 variant"button">
</rtk-chat-toggle>
```

```html
<script>
  const el = document.querySelector("rtk-chat-toggle");

  el.meeting= meeting
</script>
```
