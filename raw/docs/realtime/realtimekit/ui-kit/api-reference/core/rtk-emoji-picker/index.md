---
description: API reference for rtk-emoji-picker component (Web Components (HTML) Library)
title: rtk-emoji-picker
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-emoji-picker/og.png?v=9d3756a7bc117c92
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-emoji-picker

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-emoji-picker/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A very simple emoji picker component.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `focusWhenOpened` | `boolean` | ✅ | - | Controls whether or not to focus on mount |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-emoji-picker></rtk-emoji-picker>
```

### With Properties

```html
<rtk-emoji-picker>
</rtk-emoji-picker>
```

```html
<script>
  const el = document.querySelector("rtk-emoji-picker");

  el.focusWhenOpened= true;
</script>
```
