---
description: API reference for RtkViewerCount component (React Library)
title: RtkViewerCount
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkviewercount/og.png?v=e3e91caf97e4aedb
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkViewerCount

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkviewercount/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which shows count of total joined participants in a meeting.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ViewerCountVariant` | ✅ | - | Viewer count variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkViewerCount } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkViewerCount />;
}
```

### With Properties

```tsx
import { RtkViewerCount } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkViewerCount
      meeting={meeting}
      variant="primary"
    />
  );
}
```
