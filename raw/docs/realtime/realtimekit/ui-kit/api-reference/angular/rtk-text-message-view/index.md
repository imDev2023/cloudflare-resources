---
description: API reference for rtk-text-message-view component (Angular Library)
title: rtk-text-message-view
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-text-message-view/og.png?v=8ab1d1056630951e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-text-message-view

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-text-message-view/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which renders a text message from chat.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `isMarkdown` | `boolean` | ✅ | - | Renders text as markdown (default = true) |
| `text` | `string` | ✅ | - | Text message |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-text-message-view></rtk-text-message-view>
```

### With Properties

```html
<!-- component.html -->
<rtk-text-message-view
 [isMarkdown]="true"
 text="example">
</rtk-text-message-view>
```
