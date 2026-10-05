---
description: API reference for rtk-ai-transcriptions component (Web Components (HTML) Library)
title: rtk-ai-transcriptions
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ai-transcriptions/og.png?v=43c4452961730e27
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# rtk-ai-transcriptions

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ai-transcriptions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `initialTranscriptions` | `Transcript[]` | ✅ | - | Initial transcriptions |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-ai-transcriptions></rtk-ai-transcriptions>
```

### With Properties

```html
<rtk-ai-transcriptions>
</rtk-ai-transcriptions>
```

```html
<script>
  const el = document.querySelector("rtk-ai-transcriptions");

  el.initialTranscriptions= [];
  el.meeting= meeting
</script>
```
