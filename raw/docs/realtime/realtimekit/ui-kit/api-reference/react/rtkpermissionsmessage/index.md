---
description: API reference for RtkPermissionsMessage component (React Library)
title: RtkPermissionsMessage
image: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpermissionsmessage/og.png?v=7f9328949d4dad39
---

[Skip to content](#main-content)

> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/realtime/llms.txt  
> Use this file to discover all available pages before exploring further.

# RtkPermissionsMessage

Last updated Apr 21, 2026|Copy as Markdown| [View as Markdown](https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpermissionsmessage/index.md)| [Agent setup](https://developers.cloudflare.com/agent-setup/)

A component which shows permission related troubleshooting information.

## Properties

| Property | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon Pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkPermissionsMessage } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return <RtkPermissionsMessage />;
}
```

### With Properties

```tsx
import { RtkPermissionsMessage } from '@cloudflare/realtimekit-react-ui';

function MyComponent() {
  return (
    <RtkPermissionsMessage
      meeting={meeting}
    />
  );
}
```
