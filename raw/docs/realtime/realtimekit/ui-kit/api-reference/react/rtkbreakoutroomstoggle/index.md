---
description: API reference for RtkBreakoutRoomsToggle component (React Library)
title: RtkBreakoutRoomsToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroomstoggle/og.png?v=e25d5a1d0aaca522
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkBreakoutRoomsToggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroomstoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles visibility of breakout rooms. You need to pass the `meeting` object to it.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ✅ | - | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ✅ | - | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkBreakoutRoomsToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkBreakoutRoomsToggle />;
}
```

### With Properties

```tsx
import { RtkBreakoutRoomsToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkBreakoutRoomsToggle
      iconPack={defaultIconPack}
      meeting={meeting}
      size="md"
    />
  );
}
```
