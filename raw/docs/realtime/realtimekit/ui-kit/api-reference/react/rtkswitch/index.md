---
description: API reference for RtkSwitch component (React Library)
title: RtkSwitch
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkswitch/og.png?v=dbfd896f18bdab8e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkSwitch

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkswitch/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A switch component which follows RTK Design System.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `checked` | `boolean` | ✅ | - | Whether the switch is enabled/checked |
| `disabled` | `boolean` | ✅ | - | Whether switch is readonly |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `readonly` | `boolean` | ✅ | - | Whether switch is readonly |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkSwitch } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkSwitch />;
}
```

### With Properties

```tsx
import { RtkSwitch } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkSwitch
      checked={true}
      disabled={true}
      readonly={true}
    />
  );
}
```
