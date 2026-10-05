---
description: API reference for RtkChat component (React Library)
title: RtkChat
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchat/og.png?v=2ebfb16bf4516e30
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkChat

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkchat/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Fully featured chat component with image & file upload, emoji picker and auto-scroll.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig1` | ❌ | `createDefaultConfig()` | Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `overrides` | `Overrides` | ❌ | `defaultOverrides` | UI Overrides |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkChat } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkChat />;
}
```

### With Properties

```tsx
import { RtkChat } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkChat
      meeting={meeting}
      size="md"
    />
  );
}
```
