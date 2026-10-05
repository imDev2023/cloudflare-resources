---
description: API reference for RtkConfirmationModal component (React Library)
title: RtkConfirmationModal
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkconfirmationmodal/og.png?v=5ec59b0b50e10ce2
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkConfirmationModal

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkconfirmationmodal/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A confirmation modal.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkConfirmationModal } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkConfirmationModal />;
}
```

### With Properties

```tsx
import { RtkConfirmationModal } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkConfirmationModal
      meeting={meeting}
    />
  );
}
```
