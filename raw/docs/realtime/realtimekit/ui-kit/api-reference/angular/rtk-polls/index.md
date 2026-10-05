---
description: API reference for rtk-polls component (Angular Library)
title: rtk-polls
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-polls/og.png?v=1a3b13d201f8db6f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-polls

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-polls/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which lists all available plugins a user can access with the ability to enable or disable them as per their permissions.

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
<rtk-polls></rtk-polls>
```

### With Properties

```html
<!-- component.html -->
<rtk-polls
 [meeting]="meeting"
 size="md">
</rtk-polls>
```
