---
description: API reference for rtk-markdown-view component (Angular Library)
title: rtk-markdown-view
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-markdown-view/og.png?v=9d2f0597e8cb909d
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-markdown-view

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-markdown-view/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `maxLength` | `number` | ✅ | - | max length of text to render as markdown |
| `text` | `string` | ✅ | - | raw text to render as markdown |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-markdown-view></rtk-markdown-view>
```

### With Properties

```html
<!-- component.html -->
<rtk-markdown-view
 maxLength="42"
 text="example">
</rtk-markdown-view>
```
