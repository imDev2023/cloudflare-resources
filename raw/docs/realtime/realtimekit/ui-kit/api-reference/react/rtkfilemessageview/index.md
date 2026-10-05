---
description: API reference for RtkFileMessageView component (React Library)
title: RtkFileMessageView
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilemessageview/og.png?v=f3d10e1865ccd385
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkFileMessageView

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkfilemessageview/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which renders a file message.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `name` | `string` | ✅ | - | Name of the file |
| `size` | `number` | ✅ | - | Size of the file |
| `url` | `string` | ✅ | - | Url of the file |

## Usage Examples

### Basic Usage

```tsx
import { RtkFileMessageView } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkFileMessageView />;
}
```

### With Properties

```tsx
import { RtkFileMessageView } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkFileMessageView
      name="example"
      size={42}
      url="example"
    />
  );
}
```
