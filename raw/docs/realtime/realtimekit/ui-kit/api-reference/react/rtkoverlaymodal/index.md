---
description: API reference for RtkOverlayModal component (React Library)
title: RtkOverlayModal
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkoverlaymodal/og.png?v=f17372a273a64640
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkOverlayModal

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkoverlaymodal/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

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
import { RtkOverlayModal } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkOverlayModal />;
}
```

### With Properties

```tsx
import { RtkOverlayModal } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkOverlayModal
      meeting={meeting}
    />
  );
}
```
