---
description: API reference for RtkSpotlightGrid component (React Library)
title: RtkSpotlightGrid
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspotlightgrid/og.png?v=3225ff86894c8ce5
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkSpotlightGrid

Last updated Sep 4, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspotlightgrid/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A grid component that renders two lists of participants: `pinnedParticipants` and `participants`. You can customize the layout to a `column` view, by default is `row`.

- Participants from `pinnedParticipants[]` are rendered inside a larger grid.
- Participants from `participants[]` array are rendered in a smaller grid.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `aspectRatio` | `string` | ✅ | - | Aspect Ratio of participant tile Format: `width:height` |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config |
| `gap` | `number` | ✅ | - | Gap between participant tiles |
| `gridSize` | `GridSize1` | ✅ | - | Grid size |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack |
| `layout` | `GridLayout1` | ✅ | - | Grid Layout |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `participants` | `Peer[]` | ✅ | - | Participants |
| `pinnedParticipants` | `Peer[]` | ✅ | - | Pinned Participants |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkSpotlightGrid } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkSpotlightGrid />;
}
```

### With Properties

```tsx
import { RtkSpotlightGrid } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkSpotlightGrid
      aspectRatio="example"
      gap={42}
      gridSize="md"
    />
  );
}
```
