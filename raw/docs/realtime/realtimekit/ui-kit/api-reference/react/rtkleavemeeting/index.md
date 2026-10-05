---
description: API reference for RtkLeaveMeeting component (React Library)
title: RtkLeaveMeeting
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkleavemeeting/og.png?v=137f2448c398f78a
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkLeaveMeeting

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkleavemeeting/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which allows you to leave a meeting or end meeting for all, if you have the permission.

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
import { RtkLeaveMeeting } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkLeaveMeeting />;
}
```

### With Properties

```tsx
import { RtkLeaveMeeting } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkLeaveMeeting
      meeting={meeting}
    />
  );
}
```
