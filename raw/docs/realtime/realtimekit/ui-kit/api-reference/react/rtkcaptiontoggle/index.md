---
description: API reference for RtkCaptionToggle component (React Library)
title: RtkCaptionToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcaptiontoggle/og.png?v=1c286e48e7ff3fd4
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkCaptionToggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcaptiontoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `states` | `States1` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkCaptionToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkCaptionToggle />;
}
```

### With Properties

```tsx
import { RtkCaptionToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkCaptionToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
