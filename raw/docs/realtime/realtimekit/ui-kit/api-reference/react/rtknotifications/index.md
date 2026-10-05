---
description: API reference for RtkNotifications component (React Library)
title: RtkNotifications
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknotifications/og.png?v=81c980fc58db4a3b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkNotifications

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknotifications/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which handles notifications. You can configure which notifications you want to see and which ones you want to hear. There are also certain limits which you can set as well.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkNotifications } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkNotifications />;
}
```

### With Properties

```tsx
import { RtkNotifications } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkNotifications
      meeting={meeting}
      size="md"
    />
  );
}
```
