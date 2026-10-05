---
description: API reference for rtk-overlay-modal component (Angular Library)
title: rtk-overlay-modal
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-overlay-modal/og.png?v=42128bba09e5418c
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-overlay-modal

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-overlay-modal/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

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
<!-- component.html -->
<rtk-overlay-modal></rtk-overlay-modal>
```

### With Properties

```html
<!-- component.html -->
<rtk-overlay-modal
 [meeting]="meeting">
</rtk-overlay-modal>
```
