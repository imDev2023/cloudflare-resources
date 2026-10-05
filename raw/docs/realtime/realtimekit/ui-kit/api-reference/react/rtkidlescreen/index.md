---
description: API reference for RtkIdleScreen component (React Library)
title: RtkIdleScreen
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkidlescreen/og.png?v=0412da7e40a80fb5
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkIdleScreen

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkidlescreen/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A screen that handles the idle state, i.e; when you are waiting for data about the meeting, specifically the `meeting` object.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkIdleScreen } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkIdleScreen />;
}
```

### With Properties

```tsx
import { RtkIdleScreen } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkIdleScreen
      meeting={meeting}
    />
  );
}
```
