---
description: API reference for rtk-tab-bar component (Angular Library)
title: rtk-tab-bar
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-tab-bar/og.png?v=fe2dced7c5143cb0
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-tab-bar

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-tab-bar/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `activeTab` | `Tab` | ✅ | - | Active tab |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack |
| `layout` | `GridLayout1` | ✅ | - | Grid Layout |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `tabs` | `Tab[]` | ✅ | - | Tabs |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-tab-bar></rtk-tab-bar>
```

### With Properties

```html
<!-- component.html -->
<rtk-tab-bar
 [activeTab]="tab"
 [layout]="gridlayout1"
 [meeting]="meeting">
</rtk-tab-bar>
```
