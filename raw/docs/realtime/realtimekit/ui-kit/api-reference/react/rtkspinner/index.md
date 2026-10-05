---
description: API reference for RtkSpinner component (React Library)
title: RtkSpinner
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspinner/og.png?v=8739ee4d74485a8e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkSpinner

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkspinner/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which shows an animating spinner.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `size` | `Size1` | ✅ | - | Size |

## Usage Examples

### Basic Usage

```tsx
import { RtkSpinner } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkSpinner />;
}
```

### With Properties

```tsx
import { RtkSpinner } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkSpinner
      size="md"
    />
  );
}
```
