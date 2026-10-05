---
description: API reference for rtk-participants-viewer-list component (Angular Library)
title: rtk-participants-viewer-list
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participants-viewer-list/og.png?v=2c48ac2492ddbd1b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-participants-viewer-list

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participants-viewer-list/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config |
| `hideHeader` | `boolean` | ✅ | - | Hide Viewer Count Header |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `search` | `string` | ✅ | - | Search |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |
| `view` | `ParticipantsViewMode` | ✅ | - | View mode for participants list |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-participants-viewer-list></rtk-participants-viewer-list>
```

### With Properties

```html
<!-- component.html -->
<rtk-participants-viewer-list
 [hideHeader]="true"
 [meeting]="meeting"
 search="example">
</rtk-participants-viewer-list>
```
