---
description: API reference for rtk-transcripts component (Angular Library)
title: rtk-transcripts
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-transcripts/og.png?v=9ed4d43272ba8ea0
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-transcripts

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-transcripts/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which handles transcripts. You can configure which transcripts you want to see and which ones you want to hear. There are also certain limits which you can set as well.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-transcripts></rtk-transcripts>
```

### With Properties

```html
<!-- component.html -->
<rtk-transcripts
 [meeting]="meeting">
</rtk-transcripts>
```
