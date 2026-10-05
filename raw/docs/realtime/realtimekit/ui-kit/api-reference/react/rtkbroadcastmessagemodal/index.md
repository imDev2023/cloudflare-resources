---
description: API reference for RtkBroadcastMessageModal component (React Library)
title: RtkBroadcastMessageModal
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbroadcastmessagemodal/og.png?v=e496efff87eac19f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkBroadcastMessageModal

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbroadcastmessagemodal/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `states` | `States1` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkBroadcastMessageModal } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkBroadcastMessageModal />;
}
```

### With Properties

```tsx
import { RtkBroadcastMessageModal } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkBroadcastMessageModal
      meeting={meeting}
    />
  );
}
```
