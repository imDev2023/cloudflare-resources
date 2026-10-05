---
description: API reference for RtkLeaveButton component (React Library)
title: RtkLeaveButton
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkleavebutton/og.png?v=9585f0f5c7a51f16
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkLeaveButton

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkleavebutton/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A button which toggles visilibility of the leave confirmation dialog.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkLeaveButton } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkLeaveButton />;
}
```

### With Properties

```tsx
import { RtkLeaveButton } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkLeaveButton
      size="md"
      variant="button"
    />
  );
}
```
