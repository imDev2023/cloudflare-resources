---
description: API reference for RtkPaginatedList component (React Library)
title: RtkPaginatedList
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpaginatedlist/og.png?v=d4feac37122d3707
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkPaginatedList

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpaginatedlist/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `autoScroll` | `boolean` | ✅ | - | auto scroll list to bottom |
| `createNodes` | `(data: unknown[])` | ✅ | - | Create nodes |
| `emptyListLabel` | `string` | ✅ | - | label to show when empty |
| `fetchData` | `(timestamp: number, size: number, reversed: boolean)` | ✅ | - | Fetch the data |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `pageSize` | `number` | ✅ | - | Page Size |
| `pagesAllowed` | `number` | ✅ | - | Number of pages allowed to be shown |
| `rerenderList` | `()` | ✅ | - | Rerender paginated list |
| `reset` | `(timestamp?: number)` | ❌ | - | Resets the paginated list to a given timestamp |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkPaginatedList } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkPaginatedList />;
}
```

### With Properties

```tsx
import { RtkPaginatedList } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkPaginatedList
      autoScroll={true}
      createNodes={[]}
      emptyListLabel="example"
    />
  );
}
```
