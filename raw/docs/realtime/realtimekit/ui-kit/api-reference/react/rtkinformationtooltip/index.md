---
description: API reference for RtkInformationTooltip component (React Library)
title: RtkInformationTooltip
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkinformationtooltip/og.png?v=46f90d3cf08dd05f
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkInformationTooltip

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkinformationtooltip/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |

## Usage Examples

### Basic Usage

```tsx
import { RtkInformationTooltip } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkInformationTooltip />;
}
```

### With Properties

```tsx
import { RtkInformationTooltip } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkInformationTooltip
      iconPack={defaultIconPack}
    />
  );
}
```
