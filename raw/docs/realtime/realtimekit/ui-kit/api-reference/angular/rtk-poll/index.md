---
description: API reference for rtk-poll component (Angular Library)
title: rtk-poll
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-poll/og.png?v=dd8e3736a35521ce
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-poll

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-poll/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A poll component. Shows a poll where a user can vote.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `permissions` | `RTKPermissionsPreset` | ✅ | - | Permissions Object |
| `poll` | `Poll` | ✅ | - | Poll |
| `self` | `string` | ✅ | - | Self ID |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-poll></rtk-poll>
```

### With Properties

```html
<!-- component.html -->
<rtk-poll
 [permissions]="rtkpermissionspreset"
 [poll]="poll"
 self="example">
</rtk-poll>
```
