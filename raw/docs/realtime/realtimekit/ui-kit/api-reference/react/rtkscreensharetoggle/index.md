---
description: API reference for RtkScreenShareToggle component (React Library)
title: RtkScreenShareToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkscreensharetoggle/og.png?v=03e5ddc07ba009fe
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkScreenShareToggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkscreensharetoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles your screenshare.

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
import { RtkScreenShareToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkScreenShareToggle />;
}
```

### With Properties

```tsx
import { RtkScreenShareToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkScreenShareToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
