---
description: API reference for RtkTooltip component (React Library)
title: RtkTooltip
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktooltip/og.png?v=b063da09c0771099
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkTooltip

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktooltip/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

Tooltip component which follows RTK Design System.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `delay` | `number` | ✅ | - | Delay before showing the tooltip |
| `disabled` | `boolean` | ✅ | - | Disabled |
| `kind` | `TooltipKind` | ✅ | - | Tooltip kind |
| `label` | `string` | ✅ | - | Tooltip label |
| `open` | `boolean` | ✅ | - | Open |
| `placement` | `Placement` | ✅ | - | Placement of menu |
| `size` | `Size` | ✅ | - | Size |
| `variant` | `TooltipVariant` | ✅ | - | Tooltip variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkTooltip } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkTooltip />;
}
```

### With Properties

```tsx
import { RtkTooltip } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkTooltip
      delay={42}
      disabled={true}
      kind={tooltipkind}
    />
  );
}
```
