---
description: API reference for rtk-stage component (Angular Library)
title: rtk-stage
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-stage/og.png?v=29d56ce9a2debf32
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-stage

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-stage/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component used as a stage that commonly houses the `grid` and `sidebar` components.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-stage></rtk-stage>
```

### With Properties

```html
<!-- component.html -->
<rtk-stage
 [iconPack]="defaultIconPack"
 [t]="rtki18n">
</rtk-stage>
```
