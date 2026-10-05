---
description: API reference for rtk-chat-selector-ui component (Angular Library)
title: rtk-chat-selector-ui
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-selector-ui/og.png?v=bb8e5225b4a243bb
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-chat-selector-ui

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-selector-ui/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `groups` | `ChatGroup[]` | ✅ | - | Participants |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `selectedGroupId` | `string` | ✅ | - | Selected participant |
| `selfUserId` | `string` | ✅ | - | Self User ID |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `unreadCounts` | `Record<string, number>` | ✅ | - | Unread counts |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-chat-selector-ui></rtk-chat-selector-ui>
```

### With Properties

```html
<!-- component.html -->
<rtk-chat-selector-ui
 [groups]="[]"
 selectedGroupId="example"
 selfUserId="example">
</rtk-chat-selector-ui>
```
