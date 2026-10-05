---
description: API reference for RtkTranscripts component (React Library)
title: RtkTranscripts
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktranscripts/og.png?v=53ebfc78193be13c
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkTranscripts

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktranscripts/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

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

```tsx
import { RtkTranscripts } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkTranscripts />;
}
```

### With Properties

```tsx
import { RtkTranscripts } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkTranscripts
      meeting={meeting}
    />
  );
}
```
