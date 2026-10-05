---
description: API reference for RtkDebugger component (React Library)
title: RtkDebugger
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebugger/og.png?v=d0e7d37c5a077afd
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkDebugger

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebugger/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A troubleshooting component to identify and fix any issues in the meeting.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkDebugger } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkDebugger />;
}
```

### With Properties

```tsx
import { RtkDebugger } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkDebugger
      meeting={meeting}
      size="md"
    />
  );
}
```
