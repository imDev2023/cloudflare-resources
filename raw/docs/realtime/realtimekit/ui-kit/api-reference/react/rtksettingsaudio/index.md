---
description: API reference for RtkSettingsAudio component (React Library)
title: RtkSettingsAudio
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingsaudio/og.png?v=49cab8353221259b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkSettingsAudio

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettingsaudio/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which lets to manage your audio devices and audio preferences. Emits `rtkStateUpdate` event with data for muting notification sounds:

```ts
{
 prefs: {
   muteNotificationSounds: boolean
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
import { RtkSettingsAudio } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkSettingsAudio />;
}
```

### With Properties

```tsx
import { RtkSettingsAudio } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkSettingsAudio
      meeting={meeting}
      size="md"
    />
  );
}
```
