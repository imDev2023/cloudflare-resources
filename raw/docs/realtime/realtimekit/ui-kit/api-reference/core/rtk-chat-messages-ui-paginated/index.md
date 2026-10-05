---
description: API reference for rtk-chat-messages-ui-paginated component (Web Components (HTML) Library)
title: rtk-chat-messages-ui-paginated
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-messages-ui-paginated/og.png?v=c54664b7a043ccc5
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-chat-messages-ui-paginated

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-messages-ui-paginated/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `privateChatRecipient` | `Participant \| null` | ✅ | - | Selected recipient for private chat; when unset, messages are loaded for public chat (Everyone). |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-chat-messages-ui-paginated></rtk-chat-messages-ui-paginated>
```

### With Properties

```html
<rtk-chat-messages-ui-paginated
 size="md">
</rtk-chat-messages-ui-paginated>
```

```html
<script>
  const el = document.querySelector("rtk-chat-messages-ui-paginated");

  el.meeting= meeting
</script>
```
