---
description: API reference for rtk-chat-composer-view component (Angular Library)
title: rtk-chat-composer-view
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-composer-view/og.png?v=4665cad50364e8fd
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-chat-composer-view

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-composer-view/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which renders a chat composer

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `canSendFiles` | `boolean` | ✅ | - | Whether user can send file messages |
| `canSendTextMessage` | `boolean` | ✅ | - | Whether user can send text messages |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `inputTextPlaceholder` | `string` | ✅ | - | Placeholder for text input |
| `isEditing` | `boolean` | ✅ | - | Sets composer to edit mode |
| `maxLength` | `number` | ✅ | - | Max length for text input |
| `message` | `string` | ✅ | - | Message to be pre-populated |
| `quotedMessage` | `string` | ✅ | - | Quote message to be displayed |
| `rateLimits` | `{ period: number; maxInvocations: number; }` | ✅ | - | Rate limits |
| `storageKey` | `string` | ✅ | - | Key for storing message in localStorage |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-chat-composer-view></rtk-chat-composer-view>
```

### With Properties

```html
<!-- component.html -->
<rtk-chat-composer-view
 [canSendFiles]="true"
 [canSendTextMessage]="true"
 inputTextPlaceholder="example">
</rtk-chat-composer-view>
```
