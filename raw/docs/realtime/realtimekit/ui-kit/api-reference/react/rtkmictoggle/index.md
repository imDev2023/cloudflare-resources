---
description: API reference for RtkMicToggle component (React Library)
title: RtkMicToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmictoggle/og.png?v=30b7996cf191a5cb
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkMicToggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmictoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles your microphone.

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
import { RtkMicToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkMicToggle />;
}
```

### With Properties

```tsx
import { RtkMicToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkMicToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
