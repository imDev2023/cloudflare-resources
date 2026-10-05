---
description: API reference for RtkEndedScreen component (React Library)
title: RtkEndedScreen
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkendedscreen/og.png?v=81f563531e50240c
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkEndedScreen

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkendedscreen/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A screen which shows a meeting has ended.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Global states |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | Global states |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkEndedScreen } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkEndedScreen />;
}
```

### With Properties

```tsx
import { RtkEndedScreen } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkEndedScreen
      meeting={meeting}
      size="md"
    />
  );
}
```
