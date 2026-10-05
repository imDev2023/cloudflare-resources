---
description: API reference for RtkChatSelector component (React Library)
title: RtkChatSelector
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselector/og.png?v=cdf945533fc55fde
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkChatSelector

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchatselector/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `overrides` | `Overrides1` | ❌ | `defaultOverrides` | UI Overrides |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States1` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkChatSelector } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkChatSelector />;
}
```

### With Properties

```tsx
import { RtkChatSelector } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkChatSelector
      meeting={meeting}
      size="md"
    />
  );
}
```
