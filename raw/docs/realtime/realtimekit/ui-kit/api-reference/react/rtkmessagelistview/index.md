---
description: API reference for RtkMessageListView component (React Library)
title: RtkMessageListView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmessagelistview/og.png?v=f9e9e0d95ec20755
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkMessageListView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmessagelistview/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which renders list of messages.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `estimateItemSize` | `number` | ✅ | - | Estimated height of an item |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `loadMore` | `(lastMessage: Message)` | ✅ | - | Function to load more messages. Messages returned from this will be prepended |
| `messages` | `Message[]` | ✅ | - | Messages to render |
| `renderer` | `(message: Message, index: number)` | ✅ | - | Render function of the message |
| `visibleItemsCount` | `number` | ✅ | - | Maximum visible messages |

## Usage Examples

### Basic Usage

```tsx
import { RtkMessageListView } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkMessageListView />;
}
```

### With Properties

```tsx
import { RtkMessageListView } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkMessageListView
      estimateItemSize={42}
      loadMore={(lastmessage: message)}
      messages={[]}
    />
  );
}
```
