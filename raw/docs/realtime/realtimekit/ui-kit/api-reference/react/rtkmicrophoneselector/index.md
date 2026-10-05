---
description: API reference for RtkMicrophoneSelector component (React Library)
title: RtkMicrophoneSelector
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmicrophoneselector/og.png?v=77a1e186a7a36d61
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkMicrophoneSelector

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmicrophoneselector/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

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
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `'full' \| 'inline'` | ✅ | - | variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkMicrophoneSelector } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkMicrophoneSelector />;
}
```

### With Properties

```tsx
import { RtkMicrophoneSelector } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkMicrophoneSelector
      meeting={meeting}
      size="md"
      variant={'full' | 'inline'}
    />
  );
}
```
