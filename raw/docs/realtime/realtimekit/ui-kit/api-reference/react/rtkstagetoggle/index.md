---
description: API reference for RtkStageToggle component (React Library)
title: RtkStageToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkstagetoggle/og.png?v=5a675b03b82791c9
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkStageToggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkstagetoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `states` | `States1` | ✅ | - | States |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkStageToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkStageToggle />;
}
```

### With Properties

```tsx
import { RtkStageToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkStageToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
