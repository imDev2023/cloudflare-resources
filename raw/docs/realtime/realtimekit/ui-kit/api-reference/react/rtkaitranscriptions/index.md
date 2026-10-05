---
description: API reference for RtkAiTranscriptions component (React Library)
title: RtkAiTranscriptions
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaitranscriptions/og.png?v=4574f6d5767e6b85
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkAiTranscriptions

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaitranscriptions/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `initialTranscriptions` | `Transcript[]` | ✅ | - | Initial transcriptions |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkAiTranscriptions } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkAiTranscriptions />;
}
```

### With Properties

```tsx
import { RtkAiTranscriptions } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkAiTranscriptions
      initialTranscriptions={[]}
      meeting={meeting}
    />
  );
}
```
