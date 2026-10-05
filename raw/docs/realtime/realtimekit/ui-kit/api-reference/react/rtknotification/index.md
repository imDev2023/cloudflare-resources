---
description: API reference for RtkNotification component (React Library)
title: RtkNotification
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknotification/og.png?v=9d9ade37144fb0e8
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkNotification

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtknotification/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which shows a notification. You need to remove the element after you receive the `rtkNotificationDismiss` event.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `notification` | `Notification` | ✅ | - | Message |
| `paused` | `boolean` | ✅ | - | Stops timeout when true |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkNotification } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkNotification />;
}
```

### With Properties

```tsx
import { RtkNotification } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkNotification
      notification={notification}
      paused={true}
      size="md"
    />
  );
}
```
