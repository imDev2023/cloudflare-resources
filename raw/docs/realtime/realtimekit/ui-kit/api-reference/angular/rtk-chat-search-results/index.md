---
description: API reference for rtk-chat-search-results component (Angular Library)
title: rtk-chat-search-results
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-search-results/og.png?v=5c03474fdd79e1c8
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-chat-search-results

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-chat-search-results/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

@deprecated `rtk-chat-search-results` is deprecated and will be removed soon. Use `rtk-chat-messages-ui-paginated` instead. -

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `channelId` | `string` | ✅ | - | Channel id |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `query` | `string` | ✅ | - | Search query |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-chat-search-results></rtk-chat-search-results>
```

### With Properties

```html
<!-- component.html -->
<rtk-chat-search-results
 channelId="example"
 [meeting]="meeting"
 query="example">
</rtk-chat-search-results>
```
