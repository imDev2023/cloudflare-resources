---
description: API reference for RtkSettings component (React Library)
title: RtkSettings
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettings/og.png?v=655bb2b8ef09f945
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkSettings

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksettings/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A settings component to see and change your audio/video devices as well as see your connection quality.

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
import { RtkSettings } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkSettings />;
}
```

### With Properties

```tsx
import { RtkSettings } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkSettings
      meeting={meeting}
      size="md"
    />
  );
}
```
