---
description: API reference for rtk-file-picker-button component (Angular Library)
title: rtk-file-picker-button
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-picker-button/og.png?v=893bd83786d89d90
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-file-picker-button

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-picker-button/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `filter` | `string` | ✅ | - | File type filter to open file picker with |
| `icon` | `keyof IconPack1` | ✅ | - | Icon |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `label` | `string` | ✅ | - | Label for tooltip |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-file-picker-button></rtk-file-picker-button>
```

### With Properties

```html
<!-- component.html -->
<rtk-file-picker-button
 filter="example"
 [icon]="defaultIconPack"
 label="example">
</rtk-file-picker-button>
```
