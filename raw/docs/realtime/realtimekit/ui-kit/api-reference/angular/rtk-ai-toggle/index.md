---
description: API reference for rtk-ai-toggle component (Angular Library)
title: rtk-ai-toggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-ai-toggle/og.png?v=cf6223aee8f4400d
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-ai-toggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-ai-toggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-ai-toggle></rtk-ai-toggle>
```

### With Properties

```html
<!-- component.html -->
<rtk-ai-toggle
 [meeting]="meeting"
 size="md"
 variant="button">
</rtk-ai-toggle>
```
