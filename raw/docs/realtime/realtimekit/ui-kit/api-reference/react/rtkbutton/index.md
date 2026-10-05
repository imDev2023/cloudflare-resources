---
description: API reference for RtkButton component (React Library)
title: RtkButton
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbutton/og.png?v=1f01e255896b340a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkButton

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkbutton/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button that follows RTK Design System.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `disabled` | `boolean` | ✅ | - | Where the button is disabled or not |
| `kind` | `ButtonKind` | ✅ | - | Button type |
| `reverse` | `boolean` | ✅ | - | Whether to reverse order of children |
| `size` | `Size` | ✅ | - | Size |
| `type` | `HTMLButtonElement['type']` | ✅ | - | Button type |
| `variant` | `ButtonVariant` | ✅ | - | Button variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkButton } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkButton />;
}
```

### With Properties

```tsx
import { RtkButton } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkButton
      disabled={true}
      kind={buttonkind}
      reverse={true}
    />
  );
}
```
