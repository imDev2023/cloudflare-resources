---
description: API reference for RtkDebuggerToggle component (React Library)
title: RtkDebuggerToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggertoggle/og.png?v=136fac72600a4b28
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkDebuggerToggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdebuggertoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkDebuggerToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkDebuggerToggle />;
}
```

### With Properties

```tsx
import { RtkDebuggerToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkDebuggerToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
