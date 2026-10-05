---
description: API reference for RtkAiToggle component (React Library)
title: RtkAiToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaitoggle/og.png?v=5365f86bb6f8a245
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkAiToggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaitoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

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
import { RtkAiToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkAiToggle />;
}
```

### With Properties

```tsx
import { RtkAiToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkAiToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
