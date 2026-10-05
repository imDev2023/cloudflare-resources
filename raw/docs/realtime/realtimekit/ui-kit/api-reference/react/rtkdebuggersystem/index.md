---
description: API reference for RtkDebuggerSystem component (React Library)
title: RtkDebuggerSystem
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggersystem/og.png?v=0c7d9b2f2b5ff9e8
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkDebuggerSystem

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggersystem/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

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
import { RtkDebuggerSystem } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkDebuggerSystem />;
}
```

### With Properties

```tsx
import { RtkDebuggerSystem } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkDebuggerSystem
      meeting={meeting}
      size="md"
    />
  );
}
```
