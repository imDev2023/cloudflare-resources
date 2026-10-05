---
description: API reference for RtkDialog component (React Library)
title: RtkDialog
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdialog/og.png?v=b1b2cd000fd2fc10
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkDialog

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkdialog/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A dialog component.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config |
| `disableEscapeKey` | `boolean` | ✅ | - | Whether Escape key can close the modal |
| `hideCloseButton` | `boolean` | ✅ | - | Whether to show the close button |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `open` | `boolean` | ✅ | - | Whether a dialog is open or not |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkDialog } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkDialog />;
}
```

### With Properties

```tsx
import { RtkDialog } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkDialog
      disableEscapeKey={true}
      hideCloseButton={true}
      meeting={meeting}
    />
  );
}
```
