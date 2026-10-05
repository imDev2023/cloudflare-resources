---
description: API reference for RtkNetworkIndicator component (React Library)
title: RtkNetworkIndicator
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknetworkindicator/og.png?v=07b7f9077deff987
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkNetworkIndicator

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknetworkindicator/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `isScreenShare` | `boolean` | ✅ | - | Is for screenshare |
| `meeting` | `Meeting` | ✅ | - | Meeting |
| `participant` | `Peer` | ✅ | - | Participant or Self |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkNetworkIndicator } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkNetworkIndicator />;
}
```

### With Properties

```tsx
import { RtkNetworkIndicator } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkNetworkIndicator
      isScreenShare={true}
      meeting={meeting}
      participant={participant}
    />
  );
}
```
