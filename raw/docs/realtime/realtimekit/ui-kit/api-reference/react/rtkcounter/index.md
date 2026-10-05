---
description: API reference for RtkCounter component (React Library)
title: RtkCounter
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcounter/og.png?v=1cfef5e59e75da41
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkCounter

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcounter/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A number picker with increment and decrement buttons.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `minValue` | `number` | ✅ | - | Minimum value |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `value` | `number` | ✅ | - | Initial value |

## Usage Examples

### Basic Usage

```tsx
import { RtkCounter } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkCounter />;
}
```

### With Properties

```tsx
import { RtkCounter } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkCounter
      minValue={42}
      size="md"
      value={42}
    />
  );
}
```
