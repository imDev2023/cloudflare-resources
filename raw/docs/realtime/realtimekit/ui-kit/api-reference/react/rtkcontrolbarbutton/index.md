---
description: API reference for RtkControlbarButton component (React Library)
title: RtkControlbarButton
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcontrolbarbutton/og.png?v=28f06e1419a23ebd
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkControlbarButton

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkcontrolbarbutton/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A skeleton component used for composing custom controlbar buttons.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `brandIcon` | `boolean` | ✅ | - | Whether icon requires brand color |
| `disabled` | `boolean` | ✅ | - | Whether button is disabled |
| `icon` | `string` | ✅ | - | Icon |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `isLoading` | `boolean` | ✅ | - | Loading state Ignores current icon and shows a spinner if true |
| `label` | `string` | ✅ | - | Label of button |
| `showWarning` | `boolean` | ✅ | - | Whether to show warning icon |
| `size` | `Size` | ✅ | - | Size |
| `variant` | `ControlBarVariant1` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkControlbarButton } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkControlbarButton />;
}
```

### With Properties

```tsx
import { RtkControlbarButton } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkControlbarButton
      brandIcon={true}
      disabled={true}
      icon="example"
    />
  );
}
```
