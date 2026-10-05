---
description: API reference for rtk-chat-composer-ui component (Angular Library)
title: rtk-chat-composer-ui
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-composer-ui/og.png?v=70553ff20f293f15
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-chat-composer-ui

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-composer-ui/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

@deprecated . This component is deprecated, please use rtk-chat-composer-view instead.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `canSendFiles` | `boolean` | ✅ | - | Whether user can send file messages |
| `canSendTextMessage` | `boolean` | ✅ | - | Whether user can send text messages |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `prefill` | `{ suggestedReplies?: string[]; editMessage?: TextMessage; replyMessage?: TextMessage; }` | ❌ | - | prefill the composer |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-chat-composer-ui></rtk-chat-composer-ui>
```

### With Properties

```html
<!-- component.html -->
<rtk-chat-composer-ui
 [canSendFiles]="true"
 [canSendTextMessage]="true"
 size="md">
</rtk-chat-composer-ui>
```
