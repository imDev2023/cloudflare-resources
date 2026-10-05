---
description: API reference for rtk-ui-provider component (Angular Library)
title: rtk-ui-provider
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-ui-provider/og.png?v=dc8be1a874eb0a2e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-ui-provider

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-ui-provider/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig1` | ✅ | - | Config |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting \| null` | ❌ | `null` | Meeting |
| `mode` | `MeetingMode1` | ✅ | - | Fill type |
| `overrides` | `Overrides1` | ❌ | `defaultOverrides` | UI Kit Overrides |
| `showSetupScreen` | `boolean` | ✅ | - | Whether to show setup screen or not |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language utility |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-ui-provider></rtk-ui-provider>
```

### With Properties

```html
<!-- component.html -->
<rtk-ui-provider
 [config]="defaultUiConfig"
 [mode]="meeting"
 [showSetupScreen]="true">
</rtk-ui-provider>
```
