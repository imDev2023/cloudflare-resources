---
description: API reference for RtkNameTag component (React Library)
title: RtkNameTag
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknametag/og.png?v=2ea405d9650023aa
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkNameTag

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknametag/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which shows a participant's name.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `isScreenShare` | `boolean` | ✅ | - | Whether it is used in a screen share view |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `participant` | `Peer` | ✅ | - | Participant object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `RtkNameTagVariant` | ✅ | - | Name tag variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkNameTag } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkNameTag />;
}
```

### With Properties

```tsx
import { RtkNameTag } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkNameTag
      isScreenShare={true}
      meeting={meeting}
      participant={participant}
    />
  );
}
```
