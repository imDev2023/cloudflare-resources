---
description: API reference for rtk-notification component (Angular Library)
title: rtk-notification
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-notification/og.png?v=4f46c713c6303a3f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-notification

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-notification/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which shows a notification. You need to remove the element after you receive the `rtkNotificationDismiss` event.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `notification` | `Notification` | ✅ | - | Message |
| `paused` | `boolean` | ✅ | - | Stops timeout when true |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-notification></rtk-notification>
```

### With Properties

```html
<!-- component.html -->
<rtk-notification
 [notification]="notification"
 [paused]="true"
 size="md">
</rtk-notification>
```
