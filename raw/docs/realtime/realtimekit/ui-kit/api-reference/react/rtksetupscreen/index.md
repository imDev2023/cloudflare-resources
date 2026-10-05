---
description: API reference for RtkSetupScreen component (React Library)
title: RtkSetupScreen
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksetupscreen/og.png?v=64ac08ff33da4268
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkSetupScreen

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtksetupscreen/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A screen shown before joining the meeting, where you can edit your display name, and media settings.

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
import { RtkSetupScreen } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkSetupScreen />;
}
```

### With Properties

```tsx
import { RtkSetupScreen } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkSetupScreen
      meeting={meeting}
      size="md"
    />
  );
}
```
