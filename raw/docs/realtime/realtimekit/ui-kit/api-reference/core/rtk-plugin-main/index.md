---
description: API reference for rtk-plugin-main component (Web Components (HTML) Library)
title: rtk-plugin-main
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-plugin-main/og.png?v=b56ef20697789790
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-plugin-main

Last updated Jun 18, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-plugin-main/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which renders a plugin's UI.

The plugin's `component` (an HTMLElement) is placed into this element's light DOM and projected into the shadow DOM layout via a `<slot>`. This ensures external CSS from the consuming application continues to apply to the plugin content.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting |
| `plugin` | `RTKPlugin` | ✅ | - | Plugin |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-plugin-main></rtk-plugin-main>
```

### With Properties

```html
<rtk-plugin-main>
</rtk-plugin-main>
```

```html
<script>
  const el = document.querySelector("rtk-plugin-main");

  el.meeting= meeting
</script>
```
