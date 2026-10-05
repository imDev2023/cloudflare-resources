---
description: API reference for rtk-poll-form component (Web Components (HTML) Library)
title: rtk-poll-form
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-poll-form/og.png?v=34dacf110372ecd4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-poll-form

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-poll-form/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component that lets you create a poll.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-poll-form></rtk-poll-form>
```

### With Properties

```html
<rtk-poll-form>
</rtk-poll-form>
```

```html
<script>
  const el = document.querySelector("rtk-poll-form");

  el.iconPack= defaultIconPack
</script>
```
