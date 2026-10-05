---
description: API reference for RtkRecordingIndicator component (React Library)
title: RtkRecordingIndicator
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkrecordingindicator/og.png?v=eadcdc862010b323
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkRecordingIndicator

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkrecordingindicator/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which indicates the recording status of a meeting. It will not render anything if no recording is taking place.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkRecordingIndicator } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkRecordingIndicator />;
}
```

### With Properties

```tsx
import { RtkRecordingIndicator } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkRecordingIndicator
      meeting={meeting}
      size="md"
    />
  );
}
```
