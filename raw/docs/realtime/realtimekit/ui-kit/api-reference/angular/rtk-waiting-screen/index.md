---
description: API reference for rtk-waiting-screen component (Angular Library)
title: rtk-waiting-screen
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-waiting-screen/og.png?v=bd92d31b4309b2e0
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-waiting-screen

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-waiting-screen/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-waiting-screen></rtk-waiting-screen>
```

### With Properties

```html
<!-- component.html -->
<rtk-waiting-screen
 [meeting]="meeting">
</rtk-waiting-screen>
```
