---
description: API reference for rtk-join-stage component (Angular Library)
title: rtk-join-stage
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-join-stage/og.png?v=3db5efdf91dbefa9
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-join-stage

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-join-stage/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config |
| `dataConfig` | `ModalDataConfig` | ✅ | - | Content Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-join-stage></rtk-join-stage>
```

### With Properties

```html
<!-- component.html -->
<rtk-join-stage
 [dataConfig]="modaldataconfig"
 [meeting]="meeting"
 size="md">
</rtk-join-stage>
```
