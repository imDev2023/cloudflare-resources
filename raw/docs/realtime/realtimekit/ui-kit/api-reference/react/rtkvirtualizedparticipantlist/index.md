---
description: API reference for RtkVirtualizedParticipantList component (React Library)
title: RtkVirtualizedParticipantList
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkvirtualizedparticipantlist/og.png?v=588e9cae4ce2bbd9
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkVirtualizedParticipantList

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkvirtualizedparticipantlist/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `bufferedItemsCount` | `number` | ✅ | - | Buffer items to render before and after the visible area |
| `emptyListElement` | `HTMLElement` | ✅ | - | Element to render if list is empty |
| `itemHeight` | `number` | ✅ | - | Height of each item in pixels (assumed fixed) |
| `items` | `Peer1[]` | ✅ | - | Items to be virtualized |
| `renderItem` | `(item: Peer1, index: number)` | ✅ | - | Function to render each item |

## Usage Examples

### Basic Usage

```tsx
import { RtkVirtualizedParticipantList } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkVirtualizedParticipantList />;
}
```

### With Properties

```tsx
import { RtkVirtualizedParticipantList } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkVirtualizedParticipantList
      bufferedItemsCount={42}
      emptyListElement={htmlelement}
      itemHeight={42}
    />
  );
}
```
