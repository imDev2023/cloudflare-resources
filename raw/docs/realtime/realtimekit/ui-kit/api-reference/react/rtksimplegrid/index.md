---
description: API reference for RtkSimpleGrid component (React Library)
title: RtkSimpleGrid
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksimplegrid/og.png?v=1de93f1c06d8f0ad
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkSimpleGrid

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksimplegrid/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A grid component which renders only the participants in a simple grid.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `aspectRatio` | `string` | ✅ | - | Aspect Ratio of participant tile Format: `width:height` |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config |
| `gap` | `number` | ✅ | - | Gap between participant tiles |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `participants` | `Peer[]` | ✅ | - | Participants |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkSimpleGrid } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkSimpleGrid />;
}
```

### With Properties

```tsx
import { RtkSimpleGrid } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkSimpleGrid
      aspectRatio="example"
      gap={42}
      meeting={meeting}
    />
  );
}
```
