---
description: API reference for RtkPluginsToggle component (React Library)
title: RtkPluginsToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpluginstoggle/og.png?v=7efafa061f04e3a0
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkPluginsToggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpluginstoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles visibility of plugins. When clicked it emits a `rtkStateUpdate` event with the data:

```ts
{ activeSidebar: boolean; sidebar: 'plugins' }
```

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkPluginsToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkPluginsToggle />;
}
```

### With Properties

```tsx
import { RtkPluginsToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkPluginsToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
