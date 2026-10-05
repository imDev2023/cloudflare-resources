---
description: API reference for RtkBreakoutRoomsManager component (React Library)
title: RtkBreakoutRoomsManager
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroomsmanager/og.png?v=26e2114f8c1972cc
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkBreakoutRoomsManager

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbreakoutroomsmanager/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkBreakoutRoomsManager } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkBreakoutRoomsManager />;
}
```

### With Properties

```tsx
import { RtkBreakoutRoomsManager } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkBreakoutRoomsManager
      meeting={meeting}
    />
  );
}
```
