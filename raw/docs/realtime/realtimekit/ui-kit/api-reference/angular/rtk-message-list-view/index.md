---
description: API reference for rtk-message-list-view component (Angular Library)
title: rtk-message-list-view
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-message-list-view/og.png?v=55f712ce9ad1d8f2
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-message-list-view

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-message-list-view/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which renders list of messages.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `estimateItemSize` | `number` | ✅ | - | Estimated height of an item |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `loadMore` | `(lastMessage: Message)` | ✅ | - | Function to load more messages. Messages returned from this will be prepended |
| `messages` | `Message[]` | ✅ | - | Messages to render |
| `renderer` | `(message: Message, index: number)` | ✅ | - | Render function of the message |
| `visibleItemsCount` | `number` | ✅ | - | Maximum visible messages |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-message-list-view></rtk-message-list-view>
```

### With Properties

```html
<!-- component.html -->
<rtk-message-list-view
 estimateItemSize="42"
 [loadMore]="(lastmessage: message)"
 [messages]="[]">
</rtk-message-list-view>
```
