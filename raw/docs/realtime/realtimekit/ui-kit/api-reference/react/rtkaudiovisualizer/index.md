---
description: API reference for RtkAudioVisualizer component (React Library)
title: RtkAudioVisualizer
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiovisualizer/og.png?v=13f4bf266aaa5158
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkAudioVisualizer

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiovisualizer/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

An audio visualizer component which visualizes a participants audio. Commonly used inside `rtk-name-tag`.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `hideMuted` | `boolean` | ✅ | - | Hide the visualizer if audio is muted |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `isScreenShare` | `boolean` | ✅ | - | Audio visualizer for screensharing, it will use screenShareTracks.audio instead of audioTrack |
| `participant` | `Peer` | ✅ | - | Participant object |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `AudioVisualizerVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkAudioVisualizer } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkAudioVisualizer />;
}
```

### With Properties

```tsx
import { RtkAudioVisualizer } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkAudioVisualizer
      hideMuted={true}
      isScreenShare={true}
      participant={participant}
    />
  );
}
```
