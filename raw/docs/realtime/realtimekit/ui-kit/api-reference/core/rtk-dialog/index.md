---
description: API reference for rtk-dialog component (Web Components (HTML) Library)
title: rtk-dialog
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-dialog/og.png?v=d746ef60a6c81ef9
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-dialog

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-dialog/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A dialog component.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config |
| `disableEscapeKey` | `boolean` | ✅ | - | Whether Escape key can close the modal |
| `hideCloseButton` | `boolean` | ✅ | - | Whether to show the close button |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `open` | `boolean` | ✅ | - | Whether a dialog is open or not |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-dialog></rtk-dialog>
```

### With Properties

```html
<rtk-dialog>
</rtk-dialog>
```

```html
<script>
  const el = document.querySelector("rtk-dialog");

  el.disableEscapeKey= true;
  el.hideCloseButton= true;
  el.meeting= meeting
</script>
```
