---
description: API reference for RtkCameraToggle component (React Library)
title: RtkCameraToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcameratoggle/og.png?v=3665c032712ae2ae
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkCameraToggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcameratoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles your camera.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkCameraToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkCameraToggle />;
}
```

### With Properties

```tsx
import { RtkCameraToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkCameraToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
