---
description: API reference for RtkPoll component (React Library)
title: RtkPoll
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpoll/og.png?v=54810cd33a95719e
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkPoll

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpoll/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A poll component. Shows a poll where a user can vote.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `permissions` | `RTKPermissionsPreset` | ✅ | - | Permissions Object |
| `poll` | `Poll` | ✅ | - | Poll |
| `self` | `string` | ✅ | - | Self ID |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkPoll } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkPoll />;
}
```

### With Properties

```tsx
import { RtkPoll } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkPoll
      permissions={rtkpermissionspreset}
      poll={poll}
      self="example"
    />
  );
}
```
