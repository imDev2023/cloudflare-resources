---
description: API reference for RtkDebuggerVideo component (React Library)
title: RtkDebuggerVideo
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggervideo/og.png?v=56e31e4d905dbfa0
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkDebuggerVideo

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggervideo/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `states` | `States1` | ✅ | - | States object |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkDebuggerVideo } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkDebuggerVideo />;
}
```

### With Properties

```tsx
import { RtkDebuggerVideo } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkDebuggerVideo
      meeting={meeting}
      size="md"
    />
  );
}
```
