---
description: API reference for rtk-file-dropzone component (Angular Library)
title: rtk-file-dropzone
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-dropzone/og.png?v=e583f6821aadb1c5
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-file-dropzone

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-dropzone/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `hostEl` | `HTMLElement` | ✅ | - | Host element on which drop events to attach |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-file-dropzone></rtk-file-dropzone>
```

### With Properties

```html
<!-- component.html -->
<rtk-file-dropzone
 [hostEl]="htmlelement">
</rtk-file-dropzone>
```
