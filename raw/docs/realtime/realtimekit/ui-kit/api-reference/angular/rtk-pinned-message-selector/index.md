---
description: API reference for rtk-pinned-message-selector component (Angular Library)
title: rtk-pinned-message-selector
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-pinned-message-selector/og.png?v=dcb4c53dc239a19b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-pinned-message-selector

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-pinned-message-selector/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-pinned-message-selector></rtk-pinned-message-selector>
```

### With Properties

```html
<!-- component.html -->
<rtk-pinned-message-selector
 [meeting]="meeting">
</rtk-pinned-message-selector>
```
