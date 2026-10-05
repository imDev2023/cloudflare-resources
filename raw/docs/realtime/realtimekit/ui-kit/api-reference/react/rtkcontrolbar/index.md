---
description: API reference for RtkControlbar component (React Library)
title: RtkControlbar
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcontrolbar/og.png?v=7f0018b9a6115cb7
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkControlbar

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcontrolbar/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Controlbar component provides you with various designs as variants.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config |
| `disableRender` | `boolean` | ✅ | - | Whether to render the default UI |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon Pack |
| `meeting` | `Meeting` | ✅ | - | Meeting |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `'solid' \| 'boxed'` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkControlbar } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkControlbar />;
}
```

### With Properties

```tsx
import { RtkControlbar } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkControlbar
      disableRender={true}
      meeting={meeting}
      size="md"
    />
  );
}
```
