---
description: API reference for RtkWaitingScreen component (React Library)
title: RtkWaitingScreen
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkwaitingscreen/og.png?v=cec1f6b517e3b05a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkWaitingScreen

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkwaitingscreen/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkWaitingScreen } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkWaitingScreen />;
}
```

### With Properties

```tsx
import { RtkWaitingScreen } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkWaitingScreen
      meeting={meeting}
    />
  );
}
```
