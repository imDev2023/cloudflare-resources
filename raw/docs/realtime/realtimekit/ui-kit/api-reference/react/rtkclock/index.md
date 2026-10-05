---
description: API reference for RtkClock component (React Library)
title: RtkClock
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkclock/og.png?v=ce627aae9380acca
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkClock

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkclock/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Shows the time elapsed in a meeting.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |

## Usage Examples

### Basic Usage

```tsx
import { RtkClock } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkClock />;
}
```

### With Properties

```tsx
import { RtkClock } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkClock
      meeting={meeting}
      size="md"
    />
  );
}
```
