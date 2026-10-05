---
description: API reference for RtkMenu component (React Library)
title: RtkMenu
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmenu/og.png?v=c6af63e8de344b82
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkMenu

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmenu/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A menu component.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `offset` | `number` | ✅ | - | Offset in px |
| `placement` | `Placement` | ✅ | - | Placement of menu |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkMenu } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkMenu />;
}
```

### With Properties

```tsx
import { RtkMenu } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkMenu
      offset={42}
      placement={placement}
      size="md"
    />
  );
}
```
