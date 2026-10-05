---
description: API reference for rtk-meeting component (Web Components (HTML) Library)
title: rtk-meeting
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-meeting/og.png?v=dac4b66aeb2584a8
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-meeting

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-meeting/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A single component which renders an entire meeting UI. It loads your preset and renders the UI based on it. With this component, you don't have to handle all the states, dialogs and other smaller bits of managing the application.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `applyDesignSystem` | `boolean` | ✅ | - | Whether to apply the design system on the document root from config |
| `config` | `UIConfig` | ✅ | - | UI Config |
| `gridLayout` | `GridLayout1` | ✅ | - | Grid layout |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `leaveOnUnmount` | `boolean` | ✅ | - | Whether participant should leave when this component gets unmounted |
| `loadConfigFromPreset` | `boolean` | ✅ | - | Whether to load config from preset |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `mode` | `MeetingMode` | ✅ | - | Fill type |
| `overrides` | `Overrides` | ❌ | `defaultOverrides` | UI Kit Overrides |
| `showSetupScreen` | `boolean` | ✅ | - | Whether to show setup screen or not |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-meeting></rtk-meeting>
```

### With Properties

```html
<rtk-meeting>
</rtk-meeting>
```

```html
<script>
  const el = document.querySelector("rtk-meeting");

  el.applyDesignSystem= true;
  el.config= defaultUiConfig
</script>
```
