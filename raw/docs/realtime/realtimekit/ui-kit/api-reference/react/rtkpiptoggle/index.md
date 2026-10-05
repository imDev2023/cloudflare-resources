---
description: API reference for RtkPipToggle component (React Library)
title: RtkPipToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpiptoggle/og.png?v=f2335a332dd176ce
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkPipToggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpiptoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `states` | `States1` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkPipToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkPipToggle />;
}
```

### With Properties

```tsx
import { RtkPipToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkPipToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
