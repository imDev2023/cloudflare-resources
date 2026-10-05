---
description: API reference for RtkLivestreamToggle component (React Library)
title: RtkLivestreamToggle
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamtoggle/og.png?v=599d6868b74efaf3
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkLivestreamToggle

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtklivestreamtoggle/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size1` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkLivestreamToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkLivestreamToggle />;
}
```

### With Properties

```tsx
import { RtkLivestreamToggle } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkLivestreamToggle
      meeting={meeting}
      size="md"
      variant="button"
    />
  );
}
```
