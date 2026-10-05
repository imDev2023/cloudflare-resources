---
description: API reference for RtkGridPagination component (React Library)
title: RtkGridPagination
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkgridpagination/og.png?v=e5272e9f91aade2a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkGridPagination

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkgridpagination/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which allows you to change current page and view mode of active participants list. This is reflected in the `rtk-grid` component.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size Prop |
| `states` | `States` | ✅ | - | States |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `GridPaginationVariants` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkGridPagination } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkGridPagination />;
}
```

### With Properties

```tsx
import { RtkGridPagination } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkGridPagination
      meeting={meeting}
      size="md"
      variant={gridpaginationvariants}
    />
  );
}
```
