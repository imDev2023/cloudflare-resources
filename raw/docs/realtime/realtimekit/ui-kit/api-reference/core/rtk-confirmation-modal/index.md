---
description: API reference for rtk-confirmation-modal component (Web Components (HTML) Library)
title: rtk-confirmation-modal
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-confirmation-modal/og.png?v=2ac758597b748df1
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-confirmation-modal

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-confirmation-modal/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A confirmation modal.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-confirmation-modal></rtk-confirmation-modal>
```

### With Properties

```html
<rtk-confirmation-modal>
</rtk-confirmation-modal>
```

```html
<script>
  const el = document.querySelector("rtk-confirmation-modal");

  el.meeting= meeting
</script>
```
