---
description: API reference for rtk-transcript component (Angular Library)
title: rtk-transcript
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-transcript/og.png?v=59a8b0491b3060dc
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-transcript

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-transcript/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which shows a transcript. You need to remove the element after you receive the `rtkTranscriptDismiss` event.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `transcript` | `Transcript & { renderedId?: string }` | ❌ | - | Message |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-transcript></rtk-transcript>
```

### With Properties

```html
<!-- component.html -->
<rtk-transcript
 [t]="rtki18n"
 transcript="example">
</rtk-transcript>
```
