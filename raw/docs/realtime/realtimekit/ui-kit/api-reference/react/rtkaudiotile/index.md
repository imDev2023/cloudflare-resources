---
description: API reference for RtkAudioTile component (React Library)
title: RtkAudioTile
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiotile/og.png?v=dcf62d751397bc44
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkAudioTile

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiotile/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ✅ | - | Config |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting |
| `participant` | `Peer` | ✅ | - | Participant object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States1` | ✅ | - | States |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkAudioTile } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkAudioTile />;
}
```

### With Properties

```tsx
import { RtkAudioTile } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkAudioTile
      config={defaultUiConfig}
      meeting={meeting}
      participant={participant}
    />
  );
}
```
