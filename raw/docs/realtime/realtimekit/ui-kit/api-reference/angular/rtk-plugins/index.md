---
description: API reference for rtk-plugins component (Angular Library)
title: rtk-plugins
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-plugins/og.png?v=e7ee19ae85188ae5
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-plugins

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-plugins/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which lists all available plugins from their preset, and ability to enable or disable plugins.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-plugins></rtk-plugins>
```

### With Properties

```html
<!-- component.html -->
<rtk-plugins
 [meeting]="meeting"
 size="md">
</rtk-plugins>
```
