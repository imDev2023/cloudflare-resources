---
description: API reference for RtkIcon component (React Library)
title: RtkIcon
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkicon/og.png?v=659e98e99411a51b
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkIcon

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkicon/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

An icon component which accepts an svg string and renders it.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `icon` | `string` | ✅ | - | Icon |
| `size` | `Size1` | ✅ | - | Size |
| `variant` | `IconVariant` | ✅ | - | Icon variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkIcon } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkIcon />;
}
```

### With Properties

```tsx
import { RtkIcon } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkIcon
      icon="example"
      size="md"
      variant="primary"
    />
  );
}
```
