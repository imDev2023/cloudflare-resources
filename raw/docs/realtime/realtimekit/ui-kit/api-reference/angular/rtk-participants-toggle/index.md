---
description: API reference for rtk-participants-toggle component (Angular Library)
title: rtk-participants-toggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participants-toggle/og.png?v=64185833c817bf01
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-participants-toggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participants-toggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles visibility of participants. When clicked it emits a `rtkStateUpdate` event with the data:

```ts
{ activeSidebar: boolean; sidebar: 'participants' }
```

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-participants-toggle></rtk-participants-toggle>
```

### With Properties

```html
<!-- component.html -->
<rtk-participants-toggle
 [meeting]="meeting"
 size="md"
 variant="button">
</rtk-participants-toggle>
```
