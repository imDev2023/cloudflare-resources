---
description: API reference for rtk-draft-attachment-view component (Angular Library)
title: rtk-draft-attachment-view
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-draft-attachment-view/og.png?v=ec2a640cc716bc83
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-draft-attachment-view

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-draft-attachment-view/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which renders the draft attachment to send

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `attachment` | `{ type: 'image' \| 'file'; file: File; }` | ✅ | - | Attachment to display |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-draft-attachment-view></rtk-draft-attachment-view>
```

### With Properties

```html
<!-- component.html -->
<rtk-draft-attachment-view
 [attachment=]"{}">
</rtk-draft-attachment-view>
```
