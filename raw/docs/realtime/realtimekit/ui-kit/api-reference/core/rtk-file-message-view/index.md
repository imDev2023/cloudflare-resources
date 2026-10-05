---
description: API reference for rtk-file-message-view component (Web Components (HTML) Library)
title: rtk-file-message-view
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-file-message-view/og.png?v=78e952c7f49cd52f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-file-message-view

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-file-message-view/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which renders a file message.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `name` | `string` | ✅ | - | Name of the file |
| `size` | `number` | ✅ | - | Size of the file |
| `url` | `string` | ✅ | - | Url of the file |

## Usage Examples

### Basic Usage

```html
<rtk-file-message-view></rtk-file-message-view>
```

### With Properties

```html
<rtk-file-message-view
 name="example"
 url="example">
</rtk-file-message-view>
```

```html
<script>
  const el = document.querySelector("rtk-file-message-view");

  el.size= 42;
</script>
```
