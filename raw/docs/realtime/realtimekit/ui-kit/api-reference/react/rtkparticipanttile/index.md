---
description: API reference for RtkParticipantTile component (React Library)
title: RtkParticipantTile
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipanttile/og.png?v=bbd83562368e5ab2
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkParticipantTile

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkparticipanttile/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which plays a participants video and allows for placement of components like `rtk-name-tag`, `rtk-audio-visualizer` or any other component.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `isPreview` | `boolean` | ✅ | - | Whether tile is used for preview |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `nameTagPosition` | `\| 'bottom-left' \| 'bottom-right' \| 'bottom-center' \| 'top-left' \| 'top-right' \| 'top-center'` | ✅ | - | Position of name tag |
| `participant` | `Peer` | ✅ | - | Participant object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `'solid' \| 'gradient'` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkParticipantTile } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkParticipantTile />;
}
```

### With Properties

```tsx
import { RtkParticipantTile } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkParticipantTile
      isPreview={true}
      meeting={meeting}
      nameTagPosition={| 'bottom-left'
    | 'bottom-right'
    | 'bottom-center'
    | 'top-left'
    | 'top-right'
    | 'top-center'}
    />
  );
}
```
