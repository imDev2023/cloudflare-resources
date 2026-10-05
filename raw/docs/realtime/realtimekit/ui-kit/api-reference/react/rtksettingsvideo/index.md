---
description: API reference for RtkSettingsVideo component (React Library)
title: RtkSettingsVideo
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingsvideo/og.png?v=9df3ccedda570a34
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkSettingsVideo

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingsvideo/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which lets to manage your camera devices and your video preferences. Emits `rtkStateUpdate` event with data for toggling mirroring of self video:

```ts
{
 prefs: {
   mirrorVideo: boolean
 }
}
```

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkSettingsVideo } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkSettingsVideo />;
}
```

### With Properties

```tsx
import { RtkSettingsVideo } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkSettingsVideo
      meeting={meeting}
      size="md"
    />
  );
}
```
