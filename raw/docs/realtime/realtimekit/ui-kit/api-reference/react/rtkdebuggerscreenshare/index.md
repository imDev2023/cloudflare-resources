---
description: API reference for RtkDebuggerScreenshare component (React Library)
title: RtkDebuggerScreenshare
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggerscreenshare/og.png?v=f85b77516af68fe4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkDebuggerScreenshare

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggerscreenshare/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

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
import { RtkDebuggerScreenshare } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkDebuggerScreenshare />;
}
```

### With Properties

```tsx
import { RtkDebuggerScreenshare } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkDebuggerScreenshare
      meeting={meeting}
      size="md"
    />
  );
}
```
