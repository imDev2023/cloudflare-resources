---
description: API reference for RtkCameraSelector component (React Library)
title: RtkCameraSelector
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcameraselector/og.png?v=7bd9f2ddf432f9bd
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkCameraSelector

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcameraselector/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

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
import { RtkCameraSelector } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkCameraSelector />;
}
```

### With Properties

```tsx
import { RtkCameraSelector } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkCameraSelector
      meeting={meeting}
      size="md"
      variant={'full' | 'inline'}
    />
  );
}
```
