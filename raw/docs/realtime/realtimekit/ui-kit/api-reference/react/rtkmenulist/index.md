---
description: API reference for RtkMenuList component (React Library)
title: RtkMenuList
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmenulist/og.png?v=9291578ef51f9c47
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkMenuList

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmenulist/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A menu list component.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `menuVariant` | `'primary' \| 'secondary'` | ✅ | - | Variant |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkMenuList } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkMenuList />;
}
```

### With Properties

```tsx
import { RtkMenuList } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkMenuList
      menuVariant={'primary' | 'secondary'}
    />
  );
}
```
