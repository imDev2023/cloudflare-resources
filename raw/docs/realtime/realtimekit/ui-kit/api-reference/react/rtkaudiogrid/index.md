---
description: API reference for RtkAudioGrid component (React Library)
title: RtkAudioGrid
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiogrid/og.png?v=17ba0c18ab00ea42
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkAudioGrid

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaudiogrid/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig1` | ✅ | - | Config |
| `hideSelf` | `boolean` | ✅ | - | Whether to hide self in the grid |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon Pack |
| `meeting` | `Meeting` | ✅ | - | Meeting |
| `size` | `Size1` | ✅ | - | Size |
| `states` | `States1` | ✅ | - | States |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkAudioGrid } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkAudioGrid />;
}
```

### With Properties

```tsx
import { RtkAudioGrid } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkAudioGrid
      config={defaultUiConfig}
      hideSelf={true}
      meeting={meeting}
    />
  );
}
```
